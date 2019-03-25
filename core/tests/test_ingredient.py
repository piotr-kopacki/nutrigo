import pytest

from core import models, ingredient


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
        water = models.Food.objects.create(desc_long="Water", desc_short="Water")
        models.FoodWeight.objects.create(
            food=water, seq=1, amount=1, desc="ml", weight=1
        )
        for n in nutrients:
            models.FoodNutrition.objects.create(
                food=water, desc=n, value=0.0, units="mg", tagname=n
            )
        ing = ingredient.Ingredient(water.desc_long)
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
        food = models.Food.objects.create(desc_long="Chicken", desc_short="Chicken")
        sample_weight = models.FoodWeight.objects.create(
            food=food, seq=1, amount=1, desc="Pinch", weight=1
        )
        food = ingredient.Ingredient(food.desc_long)
        assert food.energy is None

    def test_parsing_non_existent_ingredient(self):
        with pytest.raises(ingredient.IngredientError):
            assert ingredient.Ingredient("xyz")

    def test_assign_weight(self):
        models.Food.objects.create(
            desc_long="Chicken breast", desc_short="Chicken breast"
        )
        ing = ingredient.Ingredient("1 g of chicken breast")
        assert ing.weight == 1

    def test_raise_when_no_weight(self):
        food = models.Food.objects.create(
            desc_long="Chicken breast", desc_short="Chicken breast"
        )
        with pytest.raises(ingredient.IngredientError):
            ingredient.Ingredient(
                "Chicken breast"
            )  # Unit wasn't specified and Chicken doesn't have any weight objects so it should raise IngredientError
    
    def test_calculate_total_nutrition(self):
        food = models.Food.objects.create(desc_long="Chicken", desc_short="CHICKN")
        food2 = models.Food.objects.create(desc_long="Apple", desc_short="APPL")
        models.FoodNutrition.objects.create(food=food, desc="Energy (kcal)", value=20, units='kcal', tagname="ENERC_KCAL")
        models.FoodNutrition.objects.create(food=food, desc="Proteins", value=5, units='g', tagname="PROCNT")
        models.FoodNutrition.objects.create(food=food2, desc="Energy (kcal)", value=10.1, units='kcal', tagname="ENERC_KCAL")
        ings = [
            ingredient.Ingredient("100 g chicken"),
            ingredient.Ingredient("100 g apple")
        ]
        total_nutrition = ingredient.calculate_total_nutrition(ings)
        assert total_nutrition['ENERGY'][0] == 30.1
        assert total_nutrition['PROTEIN'][0] == 5
        assert total_nutrition['FAT'][0] == 0.0
        assert total_nutrition['CARB'][0] == 0.0
