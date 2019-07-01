from difflib import get_close_matches

from django.core.cache import cache
from django.db.models import Q

from core import utils
from core.models import Food, FoodWeight


class ParseIngredientError(Exception):
    """Exception raised when parsing ingredient fails."""

    def __init__(self, to_parse, message):
        self.to_parse = to_parse
        self.message = message


def match_food(string: str, n: int = 5) -> list:
    """Finds most matching Food from database to a string.

    Very basic (but so far most effective) function to match a string to a Food object.
    It grants points by:
        3 points for every matching word in Food's name
        1 points for every matching word in Food's description
        3 points if string is equal to Food's common name
    Then sorts the results by:
        1. Scored points (More is better)
        2. Length of long description (Less is better)
    
    Args:
        string: A string to be matched with Food.
        n: Number of objects to return (default is 5)
    Returns:
        List of tuples: (Food, points) with points > 0.
    """
    if not string:
        return []

    POINTS_PER_NAME = 3
    POINTS_ON_COMMON_NAME = 3
    POINTS_PER_DESCRIPTION = 1

    string = string.casefold()
    string_split = set(string.split())

    # Optimize query by adding filters
    filters = Q()
    for w in string_split:
        filters = filters | Q(name__icontains=w) | Q(common_name__icontains=w)
    food_list = Food.objects.filter(filters)

    result = []
    for food in food_list:
        points = sum(
            [
                POINTS_PER_NAME
                for word in food.name.casefold().split()
                if word in string_split
            ]
        )
        if food.common_name and food.common_name.casefold() == string:
            points += POINTS_ON_COMMON_NAME
        if points > 0:
            if food.description:
                points += sum(
                    [
                        POINTS_PER_DESCRIPTION
                        for word in food.description.casefold().split()
                        if word in string_split
                    ]
                )
            result.append((food, points))
    if not result:
        return result
    return sorted(
        result,
        key=lambda tup: (tup[1], -len(tup[0].name), -len(tup[0].description)),
        reverse=True,
    )[:n]


def match_one_weight(food: Food, measurement: str) -> FoodWeight:
    """Finds best matching weight (FoodWeight object) to a measurement.

    Most of Food objects have common Weight entries, so this function uses difflib.get_close_matches()
    to find the most matching to the ingredient unit.
    If there's no match, returns last Weight in the list.

    Args:
        food: Food which weights are searched.
        measurement: Measurement to be searched.
    Returns:
        Best matching FoodWeight
    Raises:
        AttributeError if Food doesn't have Weight entries.
    """
    if not food.weight.exists():
        raise AttributeError(f"{food} has no weights.")
    weights = food.weight.all()
    matches = get_close_matches(measurement, [w.desc for w in weights], cutoff=0.5)
    if matches:
        return weights.filter(desc=matches[0])[0]
    # If couldn't match default measurement then try it's varations
    if measurement == utils.DEFAULT_MEASUREMENT:
        for def_measurement in utils.DEFAULT_MEASUREMENT_VARIATIONS:
            for weight in weights:
                if def_measurement == utils.singularize(weight.desc):
                    matches.append(weight.desc)
    if matches:
        return weights.filter(desc=matches[0])[0]
    else:
        return food.weight.last()


def match_one_food(string: str) -> Food:
    """Wrapper for match_food(). Returns only one Food object.

    Args:
        string: A string to be matched with Food.
    Returns:
        Food object.
    """
    res = match_food(string, n=1)
    return res[0][0] if res else None


def parse_ingredient(string: str) -> dict:
    """Parses string and returns unit, amount, measurement and name of ingredient

    Args:
        string: A string to be parsed.
    Returns:
        Dictionary:
            'amount': float
            'unit': str (may be empty)
            'measurement': str (may be empty) 
            'name': str
            'raw': str
    Raises:
        ValueError: When string is empty.
    """
    return naive_parse_ingredient(string)


def naive_parse_ingredient(string: str) -> dict:
    """Parses string and returns unit, amount, measurement and name of ingredient

    It is a very basic and naive implementation of parsing a string (ingredient).
    Based on simple checks if string starts with an amount or with a unit, etc.
    Ideally would be implemented with CRF (e.g. using PyStruct).

    Usage example:
    >>> parse_ingredient("1 onion")
    {'amount': 1.0, 'unit': '', 'measurement': 'serving', 'name': 'onion', 'raw': '1 onion'}

    >>> parse_ingredient("150 grams of chicken breasts (boneless and skinless)")
    {'amount': 150.0, 'unit': 'g', 'measurement': '', 'name': 'chicken breast boneless skinless', 'raw': '150 grams of chicken breasts (boneless and skinless)'}

    Args:
        string: A string to be parsed.
    Returns:
        Dictionary:
            'amount': float
            'unit': str (may be empty)
            'measurement': str (may be empty)
            'name': str
            'raw': str
    Raises:
        ParseIngredientError: When string is empty.
    """
    if not string:
        raise ParseIngredientError(string, "String cannot be empty.")
    raw = string
    string = utils.strip_special_chars(string)
    string = utils.separate_letters_from_numbers(string)
    string = utils.remove_or_ingredients(string)
    string = utils.strip_stop_words(string)
    string = utils.convert_range_to_one_amount(string)
    if not string:  # Re-check in case of invalid strings like "$$" etc.
        raise ParseIngredientError(raw, "String is not valid.")
    string_split = string.split()

    amount = 0
    unit = ""
    measurement = ""
    name = ""
    if (
        len(string_split) > 1
        and string_split[0].isnumeric()
        and utils.is_decimal_amount(string_split[1])
    ):
        # 1.0 - Case when 1st and 2nd words are amount (2nd is decimal) e.g. '1 1/2 ...'
        amount = list(map(int, string_split[1].split("/")))
        amount = amount[0] / amount[1]
        amount = amount + int(string_split[0])
        if len(string_split) > 2 and utils.is_measure_or_unit(string_split[2]):
            # 1.1 - Case when 1st and 2nd word is a decimal amount, 3nd word is a unit and the rest is name
            if utils.is_measurement(string_split[2]):
                measurement = string_split[2]
            else:
                unit = utils.get_unit(string_split[2])
            name = utils.singularize(" ".join(string_split[3:]))
        else:
            # 1.2 - Case when 1st and 2nd word is an amount and the rest is name
            measurement = utils.DEFAULT_MEASUREMENT
            name = utils.singularize(" ".join(string_split[2:]))
    elif utils.is_decimal_amount(string_split[0]):
        # 2.0 - Case when 1st word is a decimal amount e.g. '1/2 ...'
        amount = list(map(int, string_split[0].split("/")))
        amount = amount[0] / amount[1]
        if len(string_split) > 1 and utils.is_measure_or_unit(string_split[1]):
            # 2.1 - Case when 1st word is a decimal amount, 2nd word is a unit and the rest is name
            if utils.is_measurement(string_split[1]):
                measurement = string_split[1]
            else:
                unit = utils.get_unit(string_split[1])
            name = utils.singularize(" ".join(string_split[2:]))
        else:
            # 2.2 - Case when 1st word is a decimal amount and the rest is name
            measurement = utils.DEFAULT_MEASUREMENT
            name = utils.singularize(" ".join(string_split[1:]))
    elif string_split[0].isnumeric():
        # 3.0 - Case when 1st word is numeric and the rest is not numeric
        if len(string_split) > 1 and utils.is_measure_or_unit(string_split[1]):
            # 3.1 - Case when 1st word is an amount, 2nd word is a unit and the rest is name
            amount = int(string_split[0])
            if utils.is_measurement(string_split[1]):
                measurement = string_split[1]
            else:
                unit = utils.get_unit(string_split[1])
            name = utils.singularize(" ".join(string_split[2:]))
        else:
            # 3.2 - Case when 1st word is an amount and the rest is name
            amount = int(string_split[0])
            measurement = utils.DEFAULT_MEASUREMENT
            name = utils.singularize(" ".join(string_split[1:]))
    else:
        # 4.0 - Case when 1st word is not an amount
        if utils.is_measure_or_unit(string_split[0]):
            # 4.1 - Case when 1st word is a unit and the rest is name
            amount = 1
            if utils.is_measurement(string_split[0]):
                measurement = string_split[0]
            else:
                unit = utils.get_unit(string_split[0])
            name = utils.singularize(" ".join(string_split[1:]))
        else:
            # 4.2 - Case when whole string is a name
            amount = 1
            measurement = utils.DEFAULT_MEASUREMENT
            name = utils.singularize(" ".join(string_split[0:]))
    return {
        "amount": float(amount),
        "unit": unit,
        "measurement": measurement,
        "name": name,
        "raw": raw,
    }
