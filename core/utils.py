import re
import time
from urllib.parse import urlparse

import textblob.en.inflect
import textblob.translate
from nltk.stem import WordNetLemmatizer

DEFAULT_MEASUREMENT = "serving"
DEFAULT_MEASUREMENT_VARIATIONS = {
    'piece', 'fruit', 'bit', 'section', 'slice', 'chunk', 
    'segment', 'lump', 'hunk', 'wedge', 'slab', 'knob', 
    'block', 'cake', 'bar', 'tablet', 'brick', 'cube', 'stick', 
    'length; offcut', 'sample', 'particle', 'fragment', 'flake', 
    'sliver', 'splinter', 'wafer', 'chip', 'crumb', 'grain', 
    'speck', 'scrap', 'remnant', 'shred', 'shard', 'snippet', 
    'mite', 'mouthful', 'morsel'
}

# stop words taken from https://www.ranks.nl/stopwords
# units and measures e.g. can, g, l, ml, etc.. are not included (removed from list)
stop_words = {
'a','able','about','above','abst','accordance',
'according','accordingly','across','act','actually',
'added','adj','affected','affecting','affects','after',
'afterwards','again','against','ah','all','almost',
'alone','along','already','also','although','always',
'am','among','amongst','an','and','announce','another',
'any','anybody','anyhow','anymore','anyone','anything',
'anyway','anyways','anywhere','apparently','approximately',
'are','aren','arent','arise','around','as','aside',
'ask','asking','at','auth','available','away','awfully',
'b','back','be','became','because','become','becomes',
'becoming','been','before','beforehand','begin','beginning',
'beginnings','begins','behind','being','believe','below',
'beside','besides','between','beyond','biol','both','brief',
'briefly','but','by','ca','came', 'cannot',
"can't",'cause','causes','certain','certainly','co','com',
'come','comes','contain','containing','contains','could','couldnt',
'd','date','did',"didn't",'different','do','does',"doesn't",
'doing','done',"don't",'down','downwards','due','during','e',
'each','ed','edu','effect','eg','eight','eighty','either',
'else','elsewhere','end','ending','enough','especially','et',
'et-al','etc','even','ever','every','everybody','everyone',
'everything','everywhere','ex','except','f','far','few','ff',
'fifth','first','five','fix','followed','following','follows',
'for','former','formerly','forth','found','four','from','further',
'furthermore','gave','get','gets','getting','give','given',
'gives','giving','go','goes','gone','got','gotten','h','had',
'happens','hardly','has',"hasn't",'have',"haven't",'having','he',
'hed','hence','her','here','hereafter','hereby','herein','heres',
'hereupon','hers','herself','hes','hi','hid','him','himself','his',
'hither','home','how','howbeit','however','hundred','i','id','ie',
'if',"i'll",'im','immediate','immediately','importance','important',
'in','inc','indeed','index','information','instead','into','invention',
'inward','is',"isn't",'it','itd',"it'll",'its','itself',"i've",
'j','just','k','keep','keeps','kept', 'km','know','known',
'knows','largely','last','lately','later','latter','latterly',
'least','less','lest','let','lets','like','liked','likely','line',
'little',"'ll",'look','looking','looks','ltd', 'made','mainly',
'make','makes','many','may','maybe','me','mean','means','meantime',
'meanwhile','merely','might','million','miss', 'more','moreover',
'most','mostly','mr','mrs','much','mug','must','my','myself','n','na',
'name','namely','nay','nd','near','nearly','necessarily','necessary',
'need','needs','neither','never','nevertheless','new','next','nine',
'ninety','no','nobody','non','none','nonetheless','noone','nor',
'normally','nos','not','noted','nothing','now','nowhere','o','obtain',
'obtained','obviously','of','off','often','oh','ok','okay','old',
'omitted','on','once','one','ones','only','onto','or','ord','other',
'others','otherwise','ought','our','ours','ourselves','out','outside',
'over','overall','owing','own','page','pages','part','particular',
'particularly','past','per','perhaps','placed','please','plus','poorly',
'possible','possibly','potentially','pp','predominantly','present','previously',
'primarily','probably','promptly','proud','provides','put','que','quickly',
'quite','qv','r','ran','rather','rd','re','readily','really','recent',
'recently','ref','refs','regarding','regardless','regards','related',
'relatively','research','respectively','resulted','resulting','results',
'right','run','s','said','same','saw','say','saying','says','sec','section',
'see','seeing','seem','seemed','seeming','seems','seen','self','selves','sent',
'seven','several','shall','she','shed',"she'll",'shes','should',"shouldn't",
'show','showed','shown','showns','shows','significant','significantly',
'similar','similarly','since','six','slightly','so','some','somebody','somehow',
'someone','somethan','something','sometime','sometimes','somewhat','somewhere',
'soon','sorry','specifically','specified','specify','specifying','still','stop',
'strongly','sub','substantially','successfully','such','sufficiently','suggest',
'sup','sure\tt','take','taken','taking','tell','tends','th','than','thank',
'thanks','thanx','that',"that'll",'thats',"that've",'the','their','theirs','them',
'themselves','then','thence','there','thereafter','thereby','thered','therefore',
'therein',"there'll",'thereof','therere','theres','thereto','thereupon',
"there've",'these','they','theyd',"they'll",'theyre',"they've",
'think','this','those','thou','though','thoughh','thousand','throug',
'through','throughout','thru','thus','til','tip','to','together','too','took',
'toward','towards','tried','tries','truly','try','trying',
'ts','twice','two','u','un','under','unfortunately','unless','unlike','unlikely',
'until','unto','up','upon','ups','us','use','used','useful','usefully','usefulness',
'uses','using','usually','v','value','various',"'ve",'very','via','viz','vol',
'vols','vs','w','want','wants','was','wasnt','way','we','wed','welcome',"we'll",
'went','were','werent',"we've",'what','whatever',"what'll",'whats','when','whence',
'whenever','where','whereafter','whereas','whereby','wherein','wheres','whereupon',
'wherever','whether','which','while','whim','whither','who','whod','whoever','whole',
"who'll",'whom','whomever','whos','whose','why','widely','willing','wish','with',
'within','without','wont','words','world','would','wouldnt','www','x','y',
'yes','yet','you','youd',"you'll",'your','youre','yours','yourself','yourselves',
"you've",'z','zero'
}

units = {
    'tsp': ('tsp', 'teaspoon'),
    'tbsp': ('tbsp', 'tablespoon', 'tbl', 'tb', 't'),
    'ounce': ('ounce', 'fl oz', 'oz'),
    'gill': ('gill',),
    'cup': ('cup', 'c'),
    'pint': ('pint', 'p', 'pt', 'fl pt'),
    'quart': ('quart', 'q', 'qt', 'fl qt'), 
    'gallon': ('gallon', 'gal'),
    'ml': ('ml', 'milliliter', 'millilitre', 'cc', 'mL'),
    'l': ('l', 'liter', 'litre', 'L'),
    'dl': ('dl', 'deciliter', 'decilitre', 'dL'),
    'lb': ('lb', 'pound'),
    'mg': ('mg', 'milligram', 'milligramme'),
    'g': ('g', 'gram', 'gramme'),
    'kg': ('kg', 'kilogram', 'kilogramme'),
    'mm': ('mm', 'millimeter', 'millimetre'),
    'cm': ('cm', 'centimeter', 'centimetre'),
    'm': ('m', 'meter', 'metre'),
    'inch': ('inch',),
}

# Approximate conversion from some units to grams
unit_to_grams = {
    'tsp': 5,
    'tbsp': 15,
    'ounce': 28,
    'gill': 120,
    'cup': 240,
    'pint': 570,
    'quart': 1000, 
    'gallon': 3800,
    'ml': 1,
    'l': 1000,
    'dl': 100,
    'lb': 450,
    'mg': 0.001,
    'g': 1,
    'kg': 1000,
}

measurements = {
    'piece', 'stick', 'batch', 'bed', 'bite', 'bowl',
    'bowlful', 'can', 'consumption', 'crumb', 'chunk', 'dash', 
    'dice', 'dollop', 'jar', 'lump', 'morsel', 'mouthful', 'nibble',
    'pat', 'pinch', 'plate', 'plateful', 'portion', 'punnet', 'ration', 'rind',
    'round', 'scrap', 'serving', 'slab', 'slice', 'tidbit',
    'titbit', 'topping', 'mm', 'cm', 'm', 'inch', "small", "big", "large"
}

all_units = {unit for tup in units.values() for unit in tup}

stop_words_re = "|".join(stop_words)
stop_words_re = r"(?<!\S)(" + stop_words_re + r")(?!\S)"

wnl = WordNetLemmatizer()
wnl.lemmatize("", "n")  # Call with dummy data to make nltk load WordNet on start


def trim_whitespaces(string: str) -> str:
    """Replaces all multiple whitespaces with one and calls default strip function on a result
    
    Example:
    >>> trim_whitespaces('hello     friend')
    hello friend
    >>> trim_whitespaces('     hello     old       friend             ')
    hello old friend

    Args:
        string: A string to be trimmed.
    Returns:
        Trimmed string.
    """
    return re.sub(r"\s+", " ", string).strip()


def strip_special_chars(string: str) -> str:
    # TODO: convert words with hyphen into separate words
    """Removes all special characters except forward slash from a word. Also removes " 's " from word.
    
    Example:
    >>> strip_special_chars("1/2 chicken's leg (boneless and skinless)")
    1/2 chickens leg boneless and skinless

    Args:
        string: A string to be stripped.
    Returns:
        Stripped string.
    """
    return trim_whitespaces(
        re.sub(r"([^a-zA-Z\s0-9/'-]+?)", "", string).replace("'s", "")
    )


def strip_stop_words(string: str) -> str:
    """Removes all stop words from a string.
    
    Args:
        string: A string to be stripped.
    Returns:
        Stripped string.
    """
    return trim_whitespaces(re.sub(stop_words_re, "", f" {string} "))


def translate(string: str, from_lang: str = None) -> str:
    """Translates a string into English.

    Uses textblob Translator object which calls Google Translate API to translate text.
    
    Args:
        string: A string to be translated
        from_lang: Optionally can be set to language that the string is translated from (e.g. 'fr')
    Returns:
        Translated string.
    """
    translator = textblob.translate.Translator()
    if from_lang:
        return translator.translate(string, from_lang=from_lang, to_lang="en")
    return translator.translate(string, to_lang="en")


def translate_many(ingredients: list, from_lang: str = None) -> list:
    """Translates list of ingredients into English.

    Args:
        ingredients: List of ingredients to be translated
        from_lang: Optionally can be set to language that the ingredients are translated from (e.g. 'fr')
    Returns:
        List of translated ingredients.
    """
    ret = translate("\n".join(ingredients), from_lang=from_lang)
    return ret.split("\n")


def singularize(string: str) -> str:
    """Singularizes words in string.

    Uses singularize method from textblob module.
    
    Args:
        string: A string to be singularized
    Returns:
        Singularized string.
    """
    ret = [
        textblob.en.inflect.singularize(word) if not is_singular(word) else word
        for word in string.split()
    ]
    return " ".join(ret)


def is_singular(string: str) -> str:
    """Checks if word is singular.

    Args:
        string: A string to be checked
    Returns:
        True if word is singular otherwise returns False
    """
    return wnl.lemmatize(string, "n") == string


def convert_range_to_one_amount(string: str) -> str:
    """Converts a range of amount to one (biggest).

    Example
    >>> convert_range_to_one_amount('100 - 200 g of chicken breast')
    200 g of chicken breast

    Args:
        string: String which may contain such range.
    Returns:
        String with converted range (if found)
    """
    return re.sub(r"\d+\s{0,1}-\s{0,1}(\d+)", r"\1", string)


def get_unit(string: str) -> str:
    """Returns matching unit to a string
    Args:
        string: String to be matched to a unit
    Returns:
        Unit.
    """
    string = singularize(string)
    ret = [k for k, v in units.items() if string in v]
    return ret[0]


def is_unit(string: str) -> bool:
    """Checks if string is a unit (e.g. gram, g, litre, etc..)
    Args:
        string: string to be checked.
    Returns:
        True if string is a unit, False otherwise.
    """
    string = singularize(string)
    return string in all_units


def is_measurement(string: str) -> bool:
    """Checks if string is a measurement (e.g. slice, piece, etc..)

    Args:
        string: string to be checked.
    Returns:
        True if string is a measurement, False otherwise.
    """
    return singularize(string) in measurements


def is_measure_or_unit(string: str) -> bool:
    """Checks if string is a measurement or a unit

    Args:
        string: string to be checked.
    Returns:
        True if string is a measurement or a unit, False otherwise.
    """
    return is_measurement(string) or is_unit(string)


def is_decimal_amount(string: str) -> bool:
    """Checks if string is a decimal amount (e.g. 1/2, 1/4, etc..)

    Args:
        string: string to be checked.
    Returns:
        True if string is a decimal amount, False otherwise.
    """
    if not "/" in string or len(string.split("/")) != 2:
        return False
    string_split = string.split("/")
    return string_split[0].isnumeric() and string_split[1].isnumeric()


def remove_or_ingredients(string: str) -> str:
    """Removes any 'or' ingredients.

    Example:
    >>> 1/2 small eggplant or a few mushrooms or half a small zucchini or half a pepper
    1/2 small eggplant
    """
    or_index = string.find(" or ")
    if or_index != -1:
        return string[:or_index]
    return string


def separate_letters_from_numbers(string: str) -> str:
    """Sperates letters and numbers in a string.

    Sperates letters and numbers in a string so cases like '1kg of chicken breast' are still valid for parser.
    Leaves untouched:
    - numbers separated by a '/' or '.'
    - percentages e.g 32% (beware that if a percentage number is provided with a space, it will be joined together)
    
    Example:
    >>> split_by_letters_and_numbers("abc1234abc 124-124")
    abc 1234 abc 124 - 124
    >>> split_by_letters_and_numbers("1/2 kg of onions")
    1/2 kg of onions

    Args:
        string: string containing letters and numbers.
    Returns:
        String with separated letters and numbers.
    """
    res = trim_whitespaces(" ".join(re.split(r"(\d+)", string)))
    res = re.sub(r"(\d+)(?:\s)(\/|\.)(?:\s)(\d+)", r"\1\2\3", res)
    res = re.sub(r"(\d+)(?:\s)(%)", r"\1\2", res)
    return res


def split_and_ingredients(ingredient_list: list) -> list:
    """Ingredients separated by 'and' are split into multiple ingredients.

    Example:
    >>> split_and_ingredients(['salt and pepper', 'water'])
    ['salt', 'pepper', 'water']

    Args:
        ingredient_list: list of ingredients
    Returns:
        Corrected list of ingredients
    """
    ret = []
    for ing in ingredient_list:
        if " and " in ing:
            and_index = ing.index(" and ")
            # Skip when 'and' suggests decimal amount e.g. '1 and half tbsp of sugar'
            if (
                ing[and_index - 1].isnumeric()
                or is_decimal_amount(ing[and_index - 1])
                or ing[and_index + 1].isnumeric()
                or is_decimal_amount(ing[and_index + 1])
            ):
                ret.append(ing)
            else:
                ret.extend(ing.split(" and "))
        else:
            ret.append(ing)
    return ret


def get_domain_from_url(string: str) -> str:
    """Parses domain from url.

    Example:
    >>> get_domain_from_url("https://www.example.com/example/example.html")
    example.com

    Args:
        string: url to be parsed
    Returns:
        Parsed domain
    """
    return urlparse(string).netloc.replace("www.", "")


def time_func(f):
    """Simple decorator to time functions"""

    def wrap(*args, **kwargs):  # pragma: no cover
        old = time.time()
        ret = f(*args, **kwargs)
        now = time.time()
        print("{:s} function took {:.3f} ms".format(f.__name__, (now - old) * 1000.0))
        return ret

    return wrap  # pragma: no cover

