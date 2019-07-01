import pytest

from core import ingredient, models


@pytest.mark.django_db
class TestIngredient:
    def test_sample_water(self):
        nutrients = [
            "ENERC_KCAL",
            "PROCNT",
            "FAT",
            "FASAT",
            "FAPU",
            "FAMS",
            "CHOCDF",
            "SUGAR",
            "CHOLE",
            "NA",
            "K",
            "FIBTG",
        ]
        water = models.Food.objects.create(name="Water")
        models.FoodWeight.objects.create(food=water, amount=1, desc="ml", value=1)
        for n in nutrients:
            models.FoodNutrition.objects.create(
                food=water, desc=n, value=0.0, units="mg", tagname=n
            )
        ing = ingredient.Ingredient(water.name)
        assert ing.matched_food.id == water.id
        assert ing.energy == 0.0
        assert ing.protein == 0.0
        assert ing.fat == 0.0
        assert ing.fat_sat == 0.0
        assert ing.fat_poly == 0.0
        assert ing.fat_mono == 0.0
        assert ing.carb == 0.0
        assert ing.sugar == 0.0
        assert ing.chol == 0.0
        assert ing.fiber == 0.0
        assert ing.potas == 0.0
        assert ing.sodium == 0.0

    def test_food_with_no_nutrients(self):
        food = models.Food.objects.create(name="Chicken")
        models.FoodWeight.objects.create(food=food, amount=1, desc="Pinch", value=1)
        food = ingredient.Ingredient(food.name)
        assert food.energy is None

    def test_parsing_non_existent_ingredient(self):
        with pytest.raises(ingredient.IngredientError):
            assert ingredient.Ingredient("xyz")

    def test_assign_weight(self):
        models.Food.objects.create(name="Chicken breast")
        ing = ingredient.Ingredient("1 g of chicken breast")
        assert ing.weight == 1

    def test_raise_when_no_weight(self):
        models.Food.objects.create(name="Chicken breast")
        with pytest.raises(ingredient.IngredientError):
            ingredient.Ingredient(
                "Chicken breast"
            )  # Unit wasn't specified and Chicken doesn't have any weight objects so it should raise IngredientError

    def test_total_nutrition(self):
        food = models.Food.objects.create(name="Chicken")
        food2 = models.Food.objects.create(name="Apple")
        models.FoodNutrition.objects.create(
            food=food,
            desc="Energy (kcal)",
            value=20,
            units="kcal",
            tagname="ENERC_KCAL",
        )
        models.FoodNutrition.objects.create(
            food=food, desc="Proteins", value=5, units="g", tagname="PROCNT"
        )
        models.FoodNutrition.objects.create(
            food=food2,
            desc="Energy (kcal)",
            value=10.1,
            units="kcal",
            tagname="ENERC_KCAL",
        )
        ings = ingredient.IngredientList(["100 g chicken", "100 g apple"])
        total_nutrition = ings.total_nutrition()
        assert total_nutrition["ENERGY"][0] == 30.1
        assert total_nutrition["PROTEIN"][0] == 5
        assert total_nutrition["FAT"][0] == 0.0
        assert total_nutrition["CARB"][0] == 0.0

    def test_serving_nutrition(self):
        chicken = models.Food.objects.create(name="Chicken")
        models.FoodNutrition.objects.create(
            food=chicken,
            desc="Energy (kcal)",
            value=20,
            units="kcal",
            tagname="ENERC_KCAL",
        )
        ings = ingredient.IngredientList(["100 g chicken"])
        serving_nutrition = ings.total_nutrition(2)
        assert (
            serving_nutrition["ENERGY"][1]
            == float(chicken.nutrition.first().value) / 2.0
        )


@pytest.mark.django_db
class TestIngredientList:
    def test_add_to_bad_when_ParseIngredientError(self):
        """Ensure IngredientList handles ParseIngredientError by adding input to bad list"""
        ings = ingredient.IngredientList(["$$"])
        assert ings.bad[0] == "$$"
        assert len(ings.bad) == 1

