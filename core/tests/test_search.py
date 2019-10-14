import pytest

from core import models, search, utils


@pytest.mark.django_db
class TestSearch:
    def test_match_one_weight(self):
        food = models.Food.objects.create(name="Chicken")
        sample_weight1 = models.FoodWeight.objects.create(
            food=food, amount=1, desc="pinch", value=1
        )
        models.FoodWeight.objects.create(food=food, amount=1, desc="piece", value=1)
        # Chicken has no 'serving' weight so it should return last weight in the list
        assert search.match_one_weight(food, "serving") == food.weight.last()
        # Food with no weights should raise an Exception when matching weights
        food_with_no_weights = models.Food.objects.create(name="Null")
        with pytest.raises(AttributeError):
            search.match_one_weight(food_with_no_weights, "serving")
        assert search.match_one_weight(food, "pinch") == sample_weight1

    def test_match_one_weight_returns_last_if_no_match(self):
        """Ensure that if match_one_weight can't match a weight it returns last in the list"""
        f = models.Food.objects.create(name="Chicken")
        models.FoodWeight.objects.create(food=f, amount=1, desc="pinch", value=1)
        w2 = models.FoodWeight.objects.create(food=f, amount=1, desc="cup", value=1)
        assert search.match_one_weight(f, "teaspoon").id == w2.id

    def test_match_one_food(self):
        food = models.Food.objects.create(name="Chicken")
        assert search.match_one_food("chicken").id == food.id
        assert search.match_one_food("") is None

    def test_common_name_prevalence(self):
        models.Food.objects.create(name="Salt")
        food2 = models.Food.objects.create(name="Salt", common_name="Salt")
        assert search.match_one_food("Salt").id == food2.id

    def test_match_food(self):
        models.Food.objects.create(name="Chicken")
        res = search.match_food("chicken")
        assert isinstance(res, list)
        assert isinstance(res[0], tuple)
        assert isinstance(res[0][0], models.Food)
        assert isinstance(res[0][1], int)
        assert search.match_food("") == []

    def test_match_food_with_description(self):
        """Ensure that foods description is taken into account when matching"""
        models.Food.objects.create(name="Pepper", description="red")
        f2 = models.Food.objects.create(name="Pepper", description="green")
        assert search.match_food("green pepper")[0][0].id == f2.id

    def test_parse_ingredient_handles_bad_input(self):
        """Ensure that parse_ingredient raises ValueError when given bad input (like '$$')"""
        with pytest.raises(search.ParseIngredientError):
            assert search.parse_ingredient("$$")

    def test_parse_ingredient(self):
        assert search.parse_ingredient("chicken") == {
            "amount": 1,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "chicken",
            "raw": "chicken",
        }
        assert search.parse_ingredient("1 chicken breast") == {
            "amount": 1,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "chicken breast",
            "raw": "1 chicken breast",
        }
        assert search.parse_ingredient("slice of bread") == {
            "amount": 1,
            "unit": "",
            "measurement": "slice",
            "name": "bread",
            "raw": "slice of bread",
        }
        assert search.parse_ingredient("1 1/2 cup of water") == {
            "amount": 1.5,
            "unit": "cup",
            "measurement": "",
            "name": "water",
            "raw": "1 1/2 cup of water",
        }
        assert search.parse_ingredient("1/2 cup of water") == {
            "amount": 0.5,
            "unit": "cup",
            "measurement": "",
            "name": "water",
            "raw": "1/2 cup of water",
        }
        assert search.parse_ingredient("4 (1/2 pound) beef cube steaks") == {
            "amount": 4.5,
            "unit": "lb",
            "measurement": "",
            "name": "beef cube steak",
            "raw": "4 (1/2 pound) beef cube steaks",
        }
        assert search.parse_ingredient(
            "3 cups vegetable shortening for deep frying"
        ) == {
            "amount": 3,
            "unit": "cup",
            "measurement": "",
            "name": "vegetable shortening deep frying",
            "raw": "3 cups vegetable shortening for deep frying",
        }
        assert search.parse_ingredient("1/4 cup all-purpose flour") == {
            "amount": 0.25,
            "unit": "cup",
            "measurement": "",
            "name": "all-purpose flour",
            "raw": "1/4 cup all-purpose flour",
        }
        assert search.parse_ingredient("1 1/2 tablespoons Worcestershire sauce") == {
            "amount": 1.5,
            "unit": "tbsp",
            "measurement": "",
            "name": "Worcestershire sauce",
            "raw": "1 1/2 tablespoons Worcestershire sauce",
        }
        assert search.parse_ingredient("1 1/2 slice of onion") == {
            "amount": 1.5,
            "unit": "",
            "measurement": "slice",
            "name": "onion",
            "raw": "1 1/2 slice of onion",
        }
        assert search.parse_ingredient("1/2 slice of onion") == {
            "amount": 0.5,
            "unit": "",
            "measurement": "slice",
            "name": "onion",
            "raw": "1/2 slice of onion",
        }
        assert search.parse_ingredient("slice of ham") == {
            "amount": 1,
            "unit": "",
            "measurement": "slice",
            "name": "ham",
            "raw": "slice of ham",
        }
        assert search.parse_ingredient("g of ham") == {
            "amount": 1,
            "unit": "g",
            "measurement": "",
            "name": "ham",
            "raw": "g of ham",
        }
        assert search.parse_ingredient(
            "1 dash hot pepper sauce (such as Frank's RedHot®), or to taste"
        ) == {
            "amount": 1,
            "unit": "",
            "measurement": "dash",
            "name": "hot pepper sauce Frank RedHot",
            "raw": "1 dash hot pepper sauce (such as Frank's RedHot®), or to taste",
        }
        assert search.parse_ingredient("1 1/2 apples") == {
            "amount": 1.5,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "apple",
            "raw": "1 1/2 apples",
        }
        assert search.parse_ingredient("1/2 red onion") == {
            "amount": 0.5,
            "unit": "",
            "measurement": utils.DEFAULT_MEASUREMENT,
            "name": "red onion",
            "raw": "1/2 red onion",
        }
        assert search.parse_ingredient("1kg of chicken breasts") == {
            "amount": 1,
            "unit": "kg",
            "measurement": "",
            "name": "chicken breast",
            "raw": "1kg of chicken breasts",
        }
        with pytest.raises(search.ParseIngredientError):
            search.parse_ingredient("")
