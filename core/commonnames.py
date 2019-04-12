"""
Food objects have a common_name field which is mostly null in USDA Database so to improve matching results this file
contains more common names for various ingredients.

Usage:
    >>> manage.py collectcommonnames
"""

common_names = {
    # ID    # Common name
    # Dairies and eggs
    1123:   'Egg',
    1125:   'Yolk',
    1173:   'White',
    1145:   'Butter',
    1211:   'Milk',
    # Meats
    5011:   'Chicken',
    5048:   'Chicken back',
    5057:   'Chicken breast',
    6194:   'Chicken broth',
    5066:   'Chicken drumstick',
    5075:   'Chicken leg',
    5084:   'Chicken neck',
    5091:   'Chicken thigh',
    5100:   'Chicken wing',
    13047:  'Beef',
    5305:   'Turkey',
    7059:   'Sausage',
    # Cereal grains and pasta
    20481:  'Flour',
    20444:  'Rice',
    # Spices
    2047:   'Salt',
    2030:   'Pepper',  
    # Fruits and juices
    9037:   'Avocado',
    9150:   'Lemon',
    9266:   'Pineapple',
    9316:   'Strawberry',
    16257:  'Blueberry',
    9302:   'Raspberry',
    9078:   'Cranberry',
    # Vegetables and Vegetable Products
    11282:  'Onion',
    11503:  'Water Spinach',
    43406:  'Yeast',
    # Legumes and Legume Products
    16087:  'Peanut',
    12155:  'Walnut',
    # Beverages
    14555:  'Water',
    # Baked Products
    18064:  'Bread',
    18363:  'Tortilla',
    # Fats and Oils
    4025:   'Mayonnaise',
}
