"""
Script which imports data from USDA's National Nutrient Database for Standard Reference
"""
from core.srlegacy import food
from core.srlegacy import nutrition
from core.srlegacy import weight
from core.srlegacy import correct_weights

PATH_TO_FOOD = "FOOD_DES.txt"
PATH_TO_WEIGHT = "WEIGHT.txt"
PATH_TO_NUTRITION = "NUT_DATA.txt"
PATH_TO_DEF_DATA = "NUTR_DEF.txt"


food.main(PATH_TO_FOOD)
weight.main(PATH_TO_WEIGHT)
nutrition.main(PATH_TO_NUTRITION, PATH_TO_DEF_DATA)
correct_weights.correct()