import pytest
import textblob

from core import utils


class TestUtils:
    def test_strip_stop_words(self):
        assert utils.strip_stop_words(" ".join(utils.stop_words)) == ""
        assert utils.strip_stop_words(
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
        assert utils.strip_special_chars(r"!@#$%^&*()_+-=[];\,./'{}|:<>?") == "-/'"
        assert utils.strip_special_chars(
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
            utils.strip_special_chars("1/2 chickens leg (boneless and skinless)")
            == "1/2 chickens leg boneless and skinless"
        )

    def test_trim_whitespaces(self):
        assert utils.trim_whitespaces("hello     friend") == "hello friend"
        assert (
            utils.trim_whitespaces("     hello     old       friend             ")
            == "hello old friend"
        )
        assert utils.trim_whitespaces("a b c d") == "a b c d"

    def test_translate(self):
        assert utils.translate("kurczak") == "chicken"
        with pytest.raises(textblob.exceptions.NotTranslated):
            utils.translate("kurczak", "en")

    def test_translate_many(self):
        assert utils.translate_many(['kurczak', 'cebula'], "pl") == ['chicken', 'onion']

    def test_convert_range_to_one_amount(self):
        assert utils.convert_range_to_one_amount('100 - 200 g of chicken breast') == "200 g of chicken breast"
    

    def test_singularize(self):
        for unit in utils.all_units:
            if unit[-1] != "s":
                assert utils.singularize(unit) == unit
        for measure in utils.measurements:
            assert utils.singularize(measure) == measure
        assert utils.singularize("chickens") == "chicken"
        assert utils.singularize("leaves") == "leaf"
        assert utils.singularize("flour") == "flour"
        assert utils.singularize("pasta") == "pasta"

    def test_unit_uniqueness(self):
        assert len(utils.all_units) == len(
            [unit for tup in utils.units.values() for unit in tup]
        )

    def test_is_unit(self):
        for unit in utils.all_units:
            assert utils.is_unit(unit)

    def test_is_measurement(self):
        for measure in utils.measurements:
            assert utils.is_measurement(measure)

    def test_is_measure_or_unit(self):
        for measure in utils.measurements:
            assert utils.is_measure_or_unit(measure)
        for unit in utils.all_units:
            assert utils.is_measure_or_unit(unit)

    def test_is_decimal_amount(self):
        assert utils.is_decimal_amount("1/1")
        assert utils.is_decimal_amount("1/2")
        assert utils.is_decimal_amount("1/16")
        assert not utils.is_decimal_amount("1/s")
        assert not utils.is_decimal_amount("s/s")
        assert not utils.is_decimal_amount("/s")
        assert not utils.is_decimal_amount("s/")
        assert not utils.is_decimal_amount("/")
        assert not utils.is_decimal_amount("1/")
        assert not utils.is_decimal_amount("/1")

    def test_get_unit(self):
        for k, v in utils.units.items():
            for u in v:
                assert utils.get_unit(u) == k

    def test_units_and_measures_not_in_stop_words(self):
        for m in utils.measurements:
            assert m not in utils.stop_words
        for u in utils.all_units:
            assert u not in utils.stop_words
    
    def test_separate_letters_and_numbers(self):
        assert utils.separate_letters_from_numbers("1kg of chicken") == "1 kg of chicken"
        assert utils.separate_letters_from_numbers("abc1234abc") == "abc 1234 abc"
        assert utils.separate_letters_from_numbers("1234 1234abc") == "1234 1234 abc"
        assert utils.separate_letters_from_numbers("1 1/2") == "1 1/2"
        assert utils.separate_letters_from_numbers("1.2") == "1.2"
        assert utils.separate_letters_from_numbers("1/2 1.2 1") == "1/2 1.2 1"
        assert utils.separate_letters_from_numbers("25%") == "25%"
        assert utils.separate_letters_from_numbers("1/2 cup of 3.25% milk") == "1/2 cup of 3.25% milk"
    
    def test_get_domain_from_url(self):
        assert utils.get_domain_from_url("https://www.example.com/example/example.html") == "example.com"
        assert utils.get_domain_from_url("http://example.com/example/example.html") == "example.com"
        assert utils.get_domain_from_url("http://example.com/") == "example.com"
    
    def test_remove_or_ingredients(self):
        assert utils.remove_or_ingredients("1/2 small eggplant or a few mushrooms or half a small zucchini or half a pepper") == "1/2 small eggplant"
        assert utils.remove_or_ingredients("a small corn") == "a small corn"
    
    def test_split_and_ingredients(self):
        assert utils.split_and_ingredients(['salt and pepper', 'water']) == ['salt', 'pepper', 'water']
        assert utils.split_and_ingredients(['grand banana']) == ['grand banana']
        assert utils.split_and_ingredients(['2 and a half glasses of milk']) == ['2 and a half glasses of milk']
        assert utils.split_and_ingredients(['2 and 1/2 glasses of milk']) == ['2 and 1/2 glasses of milk']
