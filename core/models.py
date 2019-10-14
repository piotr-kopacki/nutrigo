from django.db import models


class Food(models.Model):
    """
    Model for Food object (from 'FOOD_DES' table).

    :name         - 100-character name of product, should be concise
                    (no adjectives etc.). It's the main field that will be
                    used when matching ingredients from recipes to products from db.
    :raw_name     - Original long description of product from USDA's database
    :description  - 200-character description of food item
                    (e.g if it's raw or cooked, skin only, etc.)
    :common_name  - Other names commonly used to describe a food,
                    including local or regional names, such as “soda” or
                    “pop” for “carbonated beverages”. May also be used to declare
                    default product for a category.
    :n_factor     - Factor for converting nitrogen to protein amounts
    :pro_factor   - Factor for calculating calories from protein amounts
    :fat_factor   - Factor for calculating calories from fat levels
    :cho_factor   - Factor for calculating calories from carbohydrate values
    """

    name = models.CharField(max_length=100, null=True, blank=True)
    raw_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=False, default="")
    common_name = models.CharField(max_length=100, null=True, blank=True)
    n_factor = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pro_factor = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    fat_factor = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    cho_factor = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )

    def __str__(self):  # pragma: no cover
        if self.description:
            return f"#{self.id} {self.name} [{self.description}]"
        return f"#{self.id} {self.name}"


class FoodWeight(models.Model):
    """
    FoodWeight model contains the weights in grams of several common measures for each food item.

    :food        - Food object
    :amount      - Unit modifier (for example, 1 in “1 cup”)
    :desc        - Description (for example, “cup, diced,” or “1-inch pieces”)
    :value       - Weight in grams
    :deviation   - Standard deviation
    """

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="weight")
    amount = models.DecimalField(max_digits=6, decimal_places=3)
    desc = models.CharField(max_length=84)
    value = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self):  # pragma: no cover
        return f"{self.desc} of {self.food}"


class FoodNutrition(models.Model):
    """
    FoodNutrition model contains the nutrient values of Food.

    :food    - Food object
    :desc    - Name of nutrient/food component
    :value   - Amount in 100 g, edible portion
    :units   - Units of measure (e.g., mg, g, and μg)
    :tagname - International Network of Food Data Systems tagname
    """

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="nutrition")
    desc = models.CharField(max_length=60)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    units = models.CharField(max_length=7)
    tagname = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):  # pragma: no cover
        return f"{self.tagname} of {self.food}"
