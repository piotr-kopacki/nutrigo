import pytest
import textblob

from core.utils import (
    all_units,
    convert_range_to_one_amount,
    get_domain_from_url,
    get_unit,
    is_decimal_amount,
    is_measure_or_unit,
    is_measurement,
    is_singular,
    is_unit,
    measurements,
    remove_or_ingredients,
    separate_letters_from_numbers,
    singularize,
    split_and_ingredients,
    stop_words,
    strip_special_chars,
    strip_stop_words,
    translate,
    translate_many,
    trim_whitespaces,
    units,
)


class TestUtils:
    def test_strip_stop_words(self):
        assert strip_stop_words(" ".join(stop_words)) == ""
        assert strip_stop_words(
            "4 boiled eggs 1/2 broccoli 1 small onion 4 plasters of dried ham "
            "or bacon 50 g cheese 1 teaspoon of mustard 2 raw eggs 1 tablespoon "
            "breadcrumbs + to be coated frying fat (eg 3 tablespoons of clarified "
            "butter, coconut oil, olive oil)"
        ) == (
            "4 boiled eggs 1/2 broccoli 1 small onion 4 plasters dried ham bacon "
            "50 g cheese 1 teaspoon mustard 2 raw eggs 1 tablespoon breadcrumbs "
            "+ coated frying fat (eg 3 tablespoons clarified butter, coconut oil, olive oil)"
        )

    def test_strip_special_chars(self):
        assert strip_special_chars(r"!@#$%^&*()_+-=[];\,./'{}|:<>?") == "%-/'"
        assert strip_special_chars(
            "4 boiled eggs 1/2 broccoli 1 small onion 4 plasters of dried ham or "
            "bacon 50 g cheese 1 teaspoon of mustard 2 raw eggs 1 tablespoon "
            "breadcrumbs + to be coated frying fat (eg 3 tablespoons of clarified "
            "butter, coconut oil, olive oil)"
        ) == (
            "4 boiled eggs 1/2 broccoli 1 small onion 4 plasters of dried ham or "
            "bacon 50 g cheese 1 teaspoon of mustard 2 raw eggs 1 tablespoon breadcrumbs "
            "to be coated frying fat eg 3 tablespoons of clarified butter coconut oil olive oil"
        )

        assert (
            strip_special_chars("1/2 chickens leg (boneless and skinless)")
            == "1/2 chickens leg boneless and skinless"
        )
        assert strip_special_chars(r"!@#$%^&*()_+-=[];\,./'{}|:<>?", []) == ""

    def test_trim_whitespaces(self):
        assert trim_whitespaces("hello     friend") == "hello friend"
        assert (
            trim_whitespaces("     hello     old       friend             ")
            == "hello old friend"
        )
        assert trim_whitespaces("a b c d") == "a b c d"

    def test_translate(self):
        assert translate("kurczak") == "chicken"
        with pytest.raises(textblob.exceptions.NotTranslated):
            translate("kurczak", "en")

    def test_translate_many(self):
        assert translate_many(["kurczak", "cebula"], "pl") == ["chicken", "onion"]

    def test_convert_range_to_one_amount(self):
        assert (
            convert_range_to_one_amount("100 - 200 g of chicken breast")
            == "200 g of chicken breast"
        )

    def test_singularize(self):
        for unit in all_units:
            if unit[-1] != "s":
                assert singularize(unit) == unit
        for measure in measurements:
            assert singularize(measure) == measure
        assert singularize("chickens") == "chicken"
        assert singularize("leaves") == "leaf"
        assert singularize("flour") == "flour"
        assert singularize("pasta") == "pasta"

    def test_unit_uniqueness(self):
        assert len(all_units) == len([unit for tup in units.values() for unit in tup])

    def test_is_unit(self):
        for unit in all_units:
            assert is_unit(unit)

    def test_is_measurement(self):
        for measure in measurements:
            assert is_measurement(measure)

    def test_is_measure_or_unit(self):
        for measure in measurements:
            assert is_measure_or_unit(measure)
        for unit in all_units:
            assert is_measure_or_unit(unit)

    def test_is_decimal_amount(self):
        assert is_decimal_amount("1/1")
        assert is_decimal_amount("1/2")
        assert is_decimal_amount("1/16")
        assert not is_decimal_amount("1/s")
        assert not is_decimal_amount("s/s")
        assert not is_decimal_amount("/s")
        assert not is_decimal_amount("s/")
        assert not is_decimal_amount("/")
        assert not is_decimal_amount("1/")
        assert not is_decimal_amount("/1")

    def test_get_unit(self):
        for k, v in units.items():
            for u in v:
                assert get_unit(u) == k

    def test_units_and_measures_not_in_stop_words(self):
        for m in measurements:
            assert m not in stop_words
        for u in all_units:
            assert u not in stop_words

    def test_separate_letters_and_numbers(self):
        assert separate_letters_from_numbers("1kg of chicken") == "1 kg of chicken"
        assert separate_letters_from_numbers("abc1234abc") == "abc 1234 abc"
        assert separate_letters_from_numbers("1234 1234abc") == "1234 1234 abc"
        assert separate_letters_from_numbers("1 1/2") == "1 1/2"
        assert separate_letters_from_numbers("1.2") == "1.2"
        assert separate_letters_from_numbers("1/2 1.2 1") == "1/2 1.2 1"
        assert separate_letters_from_numbers("25%") == "25%"
        assert (
            separate_letters_from_numbers("1/2 cup of 3.25% milk")
            == "1/2 cup of 3.25% milk"
        )

    def test_get_domain_from_url(self):
        assert (
            get_domain_from_url("https://www.example.com/example/example.html")
            == "example.com"
        )
        assert (
            get_domain_from_url("http://example.com/example/example.html")
            == "example.com"
        )
        assert get_domain_from_url("http://example.com/") == "example.com"

    def test_remove_or_ingredients(self):
        assert (
            remove_or_ingredients(
                "1/2 small eggplant or a few mushrooms or half a small zucchini or half a pepper"
            )
            == "1/2 small eggplant"
        )
        assert remove_or_ingredients("a small corn") == "a small corn"

    def test_split_and_ingredients(self):
        assert split_and_ingredients(["salt and pepper", "water"]) == [
            "salt",
            "pepper",
            "water",
        ]
        assert split_and_ingredients(["grand banana"]) == ["grand banana"]
        assert split_and_ingredients(["2 and a half glasses of milk"]) == [
            "2 and a half glasses of milk"
        ]
        assert split_and_ingredients(["2 and 1/2 glasses of milk"]) == [
            "2 and 1/2 glasses of milk"
        ]
        assert split_and_ingredients(["1 egg,,,,"]) == ["1 egg,,,,"]
