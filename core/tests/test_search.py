import pytest

from core import models, search, utils


@pytest.mark.django_db
class TestSearch:
    def test_match_one_weight(self):
        food = models.Food.objects.create(desc_long="Chicken", desc_short="Chicken")
        sample_weight1 = models.FoodWeight.objects.create(
            food=food, seq=1, amount=1, desc="pinch", weight=1
        )
        sample_weight2 = models.FoodWeight.objects.create(
            food=food, seq=1, amount=1, desc="piece", weight=1
        )
        # Chicken has no 'serving' weight so it should return last weight in the list
        assert search.match_one_weight(food, "serving") == food.weight.last()
        # Food with no weights should raise an Exception when matching weights
        food_with_no_weights = models.Food.objects.create(
            desc_long="Null", desc_short="Null"
        )
        with pytest.raises(AttributeError):
            search.match_one_weight(food_with_no_weights, "serving")
        assert search.match_one_weight(food, "pinch") == sample_weight1

    def test_match_one_food(self):
        models.Food.objects.create(desc_long="Chicken", desc_short="Chicken")
        assert isinstance(search.match_one_food("chicken"), models.Food)
        assert search.match_one_food("yyyaaazzzttt") == []

    def test_common_name_prevalence(self):
        food1 = models.Food.objects.create(desc_long="Salt", desc_short="Salt")
        food2 = models.Food.objects.create(
            desc_long="Salt", desc_short="Salt", common_name="Salt"
        )
        food3 = models.Food.objects.create(
            desc_long="Salt, spice", desc_short="Salt, spice"
        )
        assert search.match_one_food("Salt").id == food2.id
        food1 = models.Food.objects.create(
            desc_long="Chilli Pepper", desc_short="Pepper", common_name="Pepper, Chilli"
        )
        food2 = models.Food.objects.create(
            desc_long="Chilli Pepper", desc_short="Pepper", common_name="Pepper"
        )
        match = search.match_food("Chilli")
        assert match[0][0].id == food1.id
        assert match[0][1] > match[1][1]

    def test_match_food(self):
        models.Food.objects.create(desc_long="Chicken", desc_short="Chicken")
        res = search.match_food("chicken")
        assert isinstance(res, list)
        assert isinstance(res[0], tuple)
        assert isinstance(res[0][0], models.Food)
        assert isinstance(res[0][1], int)
        assert search.match_food("yyyaaazzzttt") == []
        with pytest.raises(ValueError):
            assert search.match_food("")

    def test_parse_ingredient(self):
        assert search.parse_ingredient("chicken") == {
            "amount": 1,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "chicken",
        }
        assert search.parse_ingredient("1 chicken breast") == {
            "amount": 1,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "chicken breast",
        }
        assert search.parse_ingredient("slice of bread") == {
            "amount": 1,
            "unit": "",
            "measurement": "slice",
            "name": "bread",
        }
        assert search.parse_ingredient("1 1/2 cup of water") == {
            "amount": 1.5,
            "unit": "cup",
            "measurement": "",
            "name": "water",
        }
        assert search.parse_ingredient("1/2 cup of water") == {
            "amount": 0.5,
            "unit": "cup",
            "measurement": "",
            "name": "water",
        }
        assert search.parse_ingredient("4 (1/2 pound) beef cube steaks") == {
            "amount": 4.5,
            "unit": "lb",
            "measurement": "",
            "name": "beef cube steak",
        }
        assert search.parse_ingredient(
            "3 cups vegetable shortening for deep frying"
        ) == {
            "amount": 3,
            "unit": "cup",
            "measurement": "",
            "name": "vegetable shortening deep frying",
        }
        assert search.parse_ingredient("1/4 cup all-purpose flour") == {
            "amount": 0.25,
            "unit": "cup",
            "measurement": "",
            "name": "all-purpose flour",
        }
        assert search.parse_ingredient("1 1/2 tablespoons Worcestershire sauce") == {
            "amount": 1.5,
            "unit": "tbsp",
            "measurement": "",
            "name": "Worcestershire sauce",
        }
        assert search.parse_ingredient("1 1/2 slice of onion") == {
            "amount": 1.5,
            "unit": "",
            "measurement": "slice",
            "name": "onion",
        }
        assert search.parse_ingredient("1/2 slice of onion") == {
            "amount": 0.5,
            "unit": "",
            "measurement": "slice",
            "name": "onion",
        }
        assert search.parse_ingredient("slice of ham") == {
            "amount": 1,
            "unit": "",
            "measurement": "slice",
            "name": "ham",
        }
        assert search.parse_ingredient("g of ham") == {
            "amount": 1,
            "unit": "g",
            "measurement": "",
            "name": "ham",
        }
        assert search.parse_ingredient(
            "1 dash hot pepper sauce (such as Frank's RedHot®), or to taste"
        ) == {
            "amount": 1,
            "unit": "",
            "measurement": "dash",
            "name": "hot pepper sauce Frank RedHot",
        }
        assert search.parse_ingredient("1 1/2 apples") == {
            "amount": 1.5,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "apple",
        }
        assert search.parse_ingredient("1/2 red onion") == {
            "amount": 0.5,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "red onion",
        }
        assert search.parse_ingredient("1kg of chicken breasts") == {
            "amount": 1,
            "unit": "kg",
            "measurement": "",
            "name": "chicken breast",
        }
        with pytest.raises(ValueError):
            search.parse_ingredient("")
