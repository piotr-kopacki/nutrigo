import re
import time
from urllib.parse import urlparse

import textblob.en.inflect
import textblob.translate
from nltk.stem import WordNetLemmatizer

from core.stop_words import stop_words

DEFAULT_MEASUREMENT = "serving"
DEFAULT_MEASUREMENT_VARIATIONS = {
    "piece",
    "fruit",
    "bit",
    "section",
    "slice",
    "chunk",
    "segment",
    "lump",
    "hunk",
    "wedge",
    "slab",
    "knob",
    "block",
    "cake",
    "bar",
    "tablet",
    "brick",
    "cube",
    "stick",
    "length; offcut",
    "sample",
    "particle",
    "fragment",
    "flake",
    "sliver",
    "splinter",
    "wafer",
    "chip",
    "crumb",
    "grain",
    "speck",
    "scrap",
    "remnant",
    "shred",
    "shard",
    "snippet",
    "mite",
    "mouthful",
    "morsel",
}

units = {
    "tsp": ("tsp", "teaspoon"),
    "tbsp": ("tbsp", "tablespoon", "tbl", "tb", "t"),
    "ounce": ("ounce", "fl oz", "oz"),
    "gill": ("gill",),
    "cup": ("cup", "c"),
    "pint": ("pint", "p", "pt", "fl pt"),
    "quart": ("quart", "q", "qt", "fl qt"),
    "gallon": ("gallon", "gal"),
    "ml": ("ml", "milliliter", "millilitre", "cc", "mL"),
    "l": ("l", "liter", "litre", "L"),
    "dl": ("dl", "deciliter", "decilitre", "dL"),
    "lb": ("lb", "pound"),
    "mg": ("mg", "milligram", "milligramme"),
    "g": ("g", "gram", "gramme"),
    "kg": ("kg", "kilogram", "kilogramme"),
    "mm": ("mm", "millimeter", "millimetre"),
    "cm": ("cm", "centimeter", "centimetre"),
    "m": ("m", "meter", "metre"),
    "inch": ("inch",),
}

nutrient_units = {
    "ENERGY": "kcal",
    "FAT": "g",
    "PROTEIN": "g",
    "CARB": "g",
    "FAT_KCAL": "kcal",
    "PROTEIN_KCAL": "kcal",
    "CARB_KCAL": "kcal",
    "FAT_SAT": "g",
    "FAT_POLY": "g",
    "FAT_MONO": "g",
    "SUGAR": "g",
    "CHOLE": "mg",
    "SODIUM": "mg",
    "POTAS": "mg",
    "FIBER": "g",
}

nutrient_to_tagname = {
    "ENERGY": "ENERC_KCAL",
    "FAT": "FAT",
    "PROTEIN": "PROCNT",
    "CARB": "CHOCDF",
    "FAT_SAT": "FASAT",
    "FAT_POLY": "FAPU",
    "FAT_MONO": "FAMS",
    "SUGAR": "SUGAR",
    "CHOLE": "CHOLE",
    "SODIUM": "NA",
    "POTAS": "K",
    "FIBER": "FIBTG",
}

# Approximate conversion from some units to grams
unit_to_grams = {
    "tsp": 5,
    "tbsp": 15,
    "ounce": 28,
    "gill": 120,
    "cup": 240,
    "pint": 570,
    "quart": 1000,
    "gallon": 3800,
    "ml": 1,
    "l": 1000,
    "dl": 100,
    "lb": 450,
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
}

measurements = {
    "piece",
    "stick",
    "batch",
    "bed",
    "bite",
    "bowl",
    "bowlful",
    "can",
    "consumption",
    "crumb",
    "chunk",
    "dash",
    "dice",
    "dollop",
    "jar",
    "lump",
    "morsel",
    "mouthful",
    "nibble",
    "pat",
    "pinch",
    "plate",
    "plateful",
    "portion",
    "punnet",
    "ration",
    "rind",
    "round",
    "scrap",
    "serving",
    "slab",
    "slice",
    "tidbit",
    "titbit",
    "topping",
    "mm",
    "cm",
    "m",
    "inch",
    "small",
    "big",
    "large",
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


def strip_special_chars(string: str, whitelist: list = ["%", "/", "\\-", "'"]) -> str:
    # TODO: convert words with hyphen into separate words
    """Removes all special characters except chars from whitelist from a word. Also removes " 's " from word.

    Example:
    >>> strip_special_chars("1/2 chicken's leg (boneless and skinless)")
    1/2 chickens leg boneless and skinless

    Args:
        string: A string to be stripped.
    Returns:
        Stripped string.
    """
    # In case whitelist was a None
    if not whitelist:
        whitelist = []
    return trim_whitespaces(
        re.sub(r"([^a-zA-Z\s0-9{}]+?)".format("".join(whitelist)), "", string).replace(
            "'s", ""
        )
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
    if "/" not in string or len(string.split("/")) != 2:
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
