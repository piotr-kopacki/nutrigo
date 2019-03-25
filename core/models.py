from django.db import models


class Food(models.Model):
    """
    Model for Food object (from 'FOOD_DES' table).

    :desc_long    - 200-character description of food item
    :desc_short   - 60-character abbreviated description of food item
    :common_name  - Other names commonly used to describe a food,
                    including local or regional names, such as “soda” or
                    “pop” for “carbonated beverages”
    :manufac_name - The company that manufactured the product, when appropriate
    :refuse_perc  - Percentage of refuse by weight (refuse is inedible parts of a food item)
    :sci_name     - Scientific name of the food item for the least
                    processed form of the food (usually raw), if applicable
    :n_factor     - Factor for converting nitrogen to protein amounts
    :pro_factor   - Factor for calculating calories from protein amounts
    :fat_factor   - Factor for calculating calories from fat levels
    :cho_factor   - Factor for calculating calories from carbohydrate values
    """

    desc_long = models.CharField(max_length=200)
    desc_short = models.CharField(max_length=60)
    common_name = models.CharField(max_length=100, null=True, blank=True)
    manufac_name = models.CharField(max_length=65, null=True, blank=True)
    refuse_perc = models.IntegerField(null=True, blank=True)
    sci_name = models.CharField(max_length=65, null=True, blank=True)
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

    def __str__(self): # pragma: no cover
        return f"#{self.id} {self.desc_long}"


class FoodWeight(models.Model):
    """
    FoodWeight model contains the weights in grams of several common measures for each food item.

    :food        - Food object
    :seq         - Sequence number
    :amount      - Unit modifier (for example, 1 in “1 cup”)
    :desc        - Description (for example, “cup, diced,” or “1-inch pieces”)
    :weight      - Weight in grams
    :data_points - Number of data points
    :deviation   - Standard deviation
    """

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="weight")
    seq = models.IntegerField()
    amount = models.DecimalField(max_digits=6, decimal_places=3)
    desc = models.CharField(max_length=84)
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    data_points = models.IntegerField(null=True, blank=True)
    deviation = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=True
    )

    def __str__(self): # pragma: no cover
        return f"{self.desc} of {self.food}"


class FoodNutrition(models.Model):
    """
    FoodNutrition model contains the nutrient values of Food.
    
    :food    - Food object
    :desc    - Name of nutrient/food component
    :value   - Amount in 100 g, edible portion
    :units   - Units of measure (e.g., mg, g, and μg)
    :min_val - Minimum value
    :max_val - Maximum value
    :tagname - International Network of Food Data Systems tagname
    """

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="nutrition")
    desc = models.CharField(max_length=60)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    units = models.CharField(max_length=7)
    min_val = models.DecimalField(
        max_digits=10, decimal_places=3, null=True, blank=True
    )
    max_val = models.DecimalField(
        max_digits=10, decimal_places=3, null=True, blank=True
    )
    tagname = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self): # pragma: no cover
        return f"{self.tagname} of {self.food}"

