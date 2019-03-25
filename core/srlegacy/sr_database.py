"""
Script which imports data from USDA's National Nutrient Database for Standard Reference
"""
import food
import nutrition
import weight

PATH_TO_FOOD = "FOOD_DES.txt"
PATH_TO_WEIGHT = "WEIGHT.txt"
PATH_TO_NUTRITION = "NUT_DATA.txt"
PATH_TO_DEF_DATA = "NUTR_DEF.txt"


food.main(PATH_TO_FOOD_DES)
weight.main(PATH_TO_WEIGHT)
nutrition.main(PATH_TO_NUTRITION, PATH_TO_DEF_DATA)