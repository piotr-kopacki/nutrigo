"""
To get better results when matching ingredients to products in database we need to
change the naming convention for products. This module is used to rename products in database.

Legend:
id: [name, description, common_name] # raw_name
* Description and common name may be null.
* Name must be singular
* Description may contain multiple words separated by a whitespace

Usage:
    >>> manage.py collectnames
"""

names = {
    1001: ['Butter', 'salted'], # Butter, salted
    1002: ['Butter', 'whipped'], # Butter, whipped, with salt
    1003: [], # Butter oil, anhydrous
    1004: ['Blue cheese'], # Cheese, blue
    1005: ['Brick cheese'], # Cheese, brick
    1006: ['Brie cheese'], # Cheese, brie
    1007: ['Camembert cheese'], # Cheese, camembert
    1008: ['Caraway cheese'], # Cheese, caraway
    1009: ['Cheddar cheese'], # Cheese, cheddar (Includes foods for USDA's Food Distribution Program)
    1010: ['Cheshire cheese'], # Cheese, cheshire
    1011: ['Colby cheese'], # Cheese, colby
    1012: ['Cottage cheese', "creamed"], # Cheese, cottage, creamed, large or small curd
    1013: [], # Cheese, cottage, creamed, with fruit
    1014: ['Cottage cheese', "nonfat uncreamed dry"], # Cheese, cottage, nonfat, uncreamed, dry, large or small curd
    1015: [], # Cheese, cottage, lowfat, 2% milkfat
    1016: [], # Cheese, cottage, lowfat, 1% milkfat
    1017: ['Cream cheese'], # Cheese, cream
    1018: ['Edam cheese'], # Cheese, edam
    1019: ['Feta cheese'], # Cheese, feta
    1020: ['Fontina cheese'], # Cheese, fontina
    1021: ['Gjetost cheese'], # Cheese, gjetost
    1022: ['Gouda cheese', '', 'Cheese'], # Cheese, gouda
    1023: ['Gruyere cheese'], # Cheese, gruyere
    1024: ['Limburger cheese'], # Cheese, limburger
    1025: ['Monterey cheese'], # Cheese, monterey
    1026: ['Mozzarella cheese'], # Cheese, mozzarella, whole milk
    1027: [], # Cheese, mozzarella, whole milk, low moisture
    1028: [], # Cheese, mozzarella, part skim milk
    1029: [], # Cheese, mozzarella, low moisture, part-skim
    1030: ['Muenster cheese'], # Cheese, muenster
    1031: ['Neufchatel cheese'], # Cheese, neufchatel
    1032: ['Parmesan cheese', 'grated'], # Cheese, parmesan, grated
    1033: ['Parmesan cheese'], # Cheese, parmesan, hard
    1034: ['Port Salut cheese'], # Cheese, port de salut
    1035: ['Provolone cheese'], # Cheese, provolone
    1036: ['Ricotta cheese'], # Cheese, ricotta, whole milk
    1037: [], # Cheese, ricotta, part skim milk
    1038: ['Romano cheese'], # Cheese, romano
    1039: ['Roquefort cheese'], # Cheese, roquefort
    1040: ['Swiss cheese'], # Cheese, swiss
    1041: ['Tilsit cheese'], # Cheese, tilsit
    1042: [], # Cheese, pasteurized process, American, fortified with vitamin D
    1043: [], # Cheese, pasteurized process, pimento
    1044: [], # Cheese, pasteurized process, swiss
    1045: [], # Cheese food, cold pack, American
    1046: [], # Cheese food, pasteurized process, American, vitamin D fortified
    1047: [], # Cheese food, pasteurized process, swiss
    1048: [], # Cheese spread, pasteurized process, American
    1049: ['Fluid cream'], # Cream, fluid, half and half
    1050: [], # Cream, fluid, light (coffee cream or table cream)
    1052: [], # Cream, fluid, light whipping
    1053: [], # Cream, fluid, heavy whipping
    1054: ['Whipped cream', '', 'Cream topping'], # Cream, whipped, cream topping, pressurized
    1055: [], # Cream, sour, reduced fat, cultured
    1056: ['Sour cream'], # Cream, sour, cultured
    1057: [], # Eggnog
    1058: [], # Sour dressing, non-butterfat, cultured, filled cream-type
    1059: [], # Milk, filled, fluid, with blend of hydrogenated vegetable oils
    1060: [], # Milk, filled, fluid, with lauric acid oil
    1061: [], # Cheese, American, nonfat or fat free
    1064: [], # Yogurt, Greek, 2% fat, apricot, CHOBANI
    1065: [], # Yogurt, Greek, 2%fat, coconut blend, CHOBANI
    1067: [], # Cream substitute, liquid, with hydrogenated vegetable oil and soy protein
    1068: [], # Cream substitute, liquid, with lauric acid oil and sodium caseinate
    1069: [], # Cream substitute, powdered
    1070: [], # Dessert topping, powdered
    1071: [], # Dessert topping, powdered, 1.5 ounce prepared with 1/2 cup milk
    1072: [], # Dessert topping, pressurized
    1073: [], # Dessert topping, semi solid, frozen
    1074: [], # Sour cream, imitation, cultured
    1076: [], # Milk substitutes, fluid, with lauric acid oil
    1077: [], # Milk, whole, 3.25% milkfat, with added vitamin D
    1078: [], # Milk, producer, fluid, 3.7% milkfat
    1079: [], # Milk, reduced fat, fluid, 2% milkfat, with added vitamin A and vitamin D
    1080: [], # Milk, reduced fat, fluid, 2% milkfat, with added nonfat milk solids and vitamin A and vitamin D
    1081: [], # Milk, reduced fat, fluid, 2% milkfat, protein fortified, with added vitamin A and vitamin D
    1082: [], # Milk, lowfat, fluid, 1% milkfat, with added vitamin A and vitamin D
    1083: [], # Milk, lowfat, fluid, 1% milkfat, with added nonfat milk solids, vitamin A and vitamin D
    1084: [], # Milk, lowfat, fluid, 1% milkfat, protein fortified, with added vitamin A and vitamin D
    1085: [], # Milk, nonfat, fluid, with added vitamin A and vitamin D (fat free or skim)
    1086: [], # Milk, nonfat, fluid, with added nonfat milk solids, vitamin A and vitamin D (fat free or skim)
    1087: [], # Milk, nonfat, fluid, protein fortified, with added vitamin A and vitamin D (fat free and skim)
    1088: [], # Milk, buttermilk, fluid, cultured, lowfat
    1089: [], # Milk, low sodium, fluid
    1090: [], # Milk, dry, whole, with added vitamin D
    1091: [], # Milk, dry, nonfat, regular, without added vitamin A and vitamin D
    1092: [], # Milk, dry, nonfat, instant, with added vitamin A and vitamin D
    1093: [], # Milk, dry, nonfat, calcium reduced
    1094: [], # Milk, buttermilk, dried
    1095: [], # Milk, canned, condensed, sweetened
    1096: [], # Milk, canned, evaporated, with added vitamin D and without added vitamin A
    1097: [], # Milk, canned, evaporated, nonfat, with added vitamin A and vitamin D
    1102: [], # Milk, chocolate, fluid, commercial, whole, with added vitamin A and vitamin D
    1103: [], # Milk, chocolate, fluid, commercial, reduced fat, with added vitamin A and vitamin D
    1104: [], # Milk, chocolate, lowfat, with added vitamin A and vitamin D
    1105: [], # Milk, chocolate beverage, hot cocoa, homemade
    1106: [], # Milk, goat, fluid, with added vitamin D
    1107: [], # Milk, human, mature, fluid
    1108: [], # Milk, indian buffalo, fluid
    1109: [], # Milk, sheep, fluid
    1110: [], # Milk shakes, thick chocolate
    1111: [], # Milk shakes, thick vanilla
    1112: ['Whey', 'acid fluid'], # Whey, acid, fluid
    1113: ['Whey', 'acid dried'], # Whey, acid, dried
    1114: ['Whey', 'sweet fluid'], # Whey, sweet, fluid
    1115: ['Whey', 'sweet dried'], # Whey, sweet, dried
    1116: ['Yogurt'], # Yogurt, plain, whole milk
    1117: ['Yogurt', 'low fat'], # Yogurt, plain, low fat
    1118: [], # Yogurt, plain, skim milk
    1119: ['Vanilla yogurt', 'low fat'], # Yogurt, vanilla, low fat.
    1120: [], # Yogurt, fruit, low fat,9 g protein/8 oz
    1121: [], # Yogurt, fruit, low fat, 10 grams protein per 8 ounce
    1122: [], # Yogurt, fruit, low fat, 11g protein/8 oz
    1123: ['Egg', '', 'Egg'], # Egg, whole, raw, fresh
    1124: ['Egg white', '', 'White'], # Egg, white, raw, fresh
    1125: ['Egg yolk', '', 'Yolk'], # Egg, yolk, raw, fresh
    1126: [], # Egg, yolk, raw, frozen, pasteurized
    1127: [], # Egg, yolk, raw, frozen, sugared, pasteurized
    1128: [], # Egg, whole, cooked, fried
    1129: [], # Egg, whole, cooked, hard-boiled
    1130: [], # Egg, whole, cooked, omelet
    1131: [], # Egg, whole, cooked, poached
    1132: [], # Egg, whole, cooked, scrambled
    1133: [], # Egg, whole, dried
    1134: [], # Egg, whole, dried, stabilized, glucose reduced
    1135: [], # Egg, white, dried, flakes, stabilized, glucose reduced
    1136: [], # Egg, white, dried, powder, stabilized, glucose reduced
    1137: [], # Egg, yolk, dried
    1138: [], # Egg, duck, whole, fresh, raw
    1139: [], # Egg, goose, whole, fresh, raw
    1140: [], # Egg, quail, whole, fresh, raw
    1141: [], # Egg, turkey, whole, fresh, raw
    1144: [], # Egg substitute, powder
    1145: ['Butter'], # Butter, without salt
    1146: [], # Cheese, parmesan, shredded
    1151: [], # Milk, nonfat, fluid, without added vitamin A and vitamin D (fat free or skim)
    1152: [], # Milk, reduced fat, fluid, 2% milkfat, with added nonfat milk solids, without added vitamin A
    1153: [], # Milk, canned, evaporated, with added vitamin A
    1154: [], # Milk, dry, nonfat, regular, with added vitamin A and vitamin D
    1155: [], # Milk, dry, nonfat, instant, without added vitamin A and vitamin D
    1156: ['Goat cheese'], # Cheese, goat, hard type
    1157: [], # Cheese, goat, semisoft type
    1158: [], # Yogurt, Greek, 2% fat, key lime blend, CHOBANI
    1159: [], # Cheese, goat, soft type
    1160: [], # Egg, yolk, raw, frozen, salted, pasteurized
    1161: [], # Cheese substitute, mozzarella
    1162: [], # Yogurt, Greek, 2% fat, mango, CHOBANI
    1164: [], # Cheese sauce, prepared from recipe
    1165: [], # Cheese, mexican, queso anejo
    1166: [], # Cheese, mexican, queso asadero
    1167: [], # Cheese, mexican, queso chihuahua
    1168: [], # Cheese, low fat, cheddar or colby
    1169: [], # Cheese, low-sodium, cheddar or colby
    1171: [], # Egg, whole, raw, frozen, pasteurized (Includes foods for USDA's Food Distribution Program)
    1172: [], # Egg, white, raw, frozen, pasteurized
    1173: [], # Egg, white, dried
    1174: ['Milk', '2% fat'], # Milk, reduced fat, fluid, 2% milkfat, without added vitamin A and vitamin D
    1175: ['Milk', '1% fat'], # Milk, fluid, 1% fat, without added vitamin A and vitamin D
    1178: [], # Sour cream, reduced fat
    1179: [], # Sour cream, light
    1180: [], # Sour cream, fat free
    1184: [], # Yogurt, vanilla or lemon flavor, nonfat milk, sweetened with low-calorie sweetener
    1185: [], # Parmesan cheese topping, fat free
    1186: [], # Cheese, cream, fat free
    1187: [], # Yogurt, chocolate, nonfat milk
    1188: [], # KRAFT CHEEZ WHIZ Pasteurized Process Cheese Sauce
    1189: [], # KRAFT CHEEZ WHIZ LIGHT Pasteurized Process Cheese Product
    1190: [], # KRAFT FREE Singles American Nonfat Pasteurized Process Cheese Product
    1191: [], # KRAFT VELVEETA Pasteurized Process Cheese Spread
    1192: [], # KRAFT VELVEETA LIGHT Reduced Fat Pasteurized Process Cheese Product
    1193: [], # KRAFT BREAKSTONE'S Reduced Fat Sour Cream
    1194: [], # KRAFT BREAKSTONE'S FREE Fat Free Sour Cream
    1199: [], # Cream, half and half, fat free
    1200: [], # Reddi Wip Fat Free Whipped Topping
    1202: [], # Milk, chocolate, fluid, commercial, reduced fat, with added calcium
    1203: [], # Yogurt, fruit, lowfat, with low calorie sweetener
    1204: [], # Cheese, parmesan, dry grated, reduced fat
    1205: [], # Cream substitute, flavored, liquid
    1206: [], # Cream substitute, flavored, powdered
    1208: [], # Cheese, provolone, reduced fat
    1209: [], # Cheese, Mexican, blend, reduced fat
    1211: ['Milk', '3.25% fat', 'Milk'], # Milk, whole, 3.25% milkfat, without added vitamin A and vitamin D
    1212: ['Dry milk'], # Milk, dry, whole, without added vitamin D
    1215: [], # Cheese product, pasteurized process, American, reduced fat, fortified with vitamin D
    1216: [], # Yogurt, fruit, low fat, 9 grams protein per 8 ounce, fortified with vitamin D
    1217: [], # Yogurt, fruit, low fat, 10 grams protein per 8 ounce, fortified with vitamin D
    1218: [], # Yogurt, fruit variety, nonfat, fortified with vitamin D
    1219: [], # Yogurt, fruit, lowfat, with low calorie sweetener, fortified with vitamin D
    1220: [], # Yogurt, vanilla, low fat, fortified with vitamin D
    1221: [], # Yogurt, vanilla or lemon flavor, nonfat milk, sweetened with low-calorie sweetener, fortified with vitamin D
    1222: [], # Yogurt, chocolate, nonfat milk, fortified with vitamin D
    1223: [], # Protein supplement, milk based, Muscle Milk, powder
    1224: [], # Protein supplement, milk based, Muscle Milk Light, powder
    1225: [], # Dulce de Leche
    1226: [], # Egg substitute, liquid or frozen, fat free
    1227: [], # Cheese, dry white, queso seco
    1228: [], # Cheese, fresh, queso fresco
    1229: [], # Cheese, white, queso blanco
    1230: [], # Milk, buttermilk, fluid, whole
    1231: [], # Yogurt, vanilla flavor, lowfat milk, sweetened with low calorie sweetener
    1235: [], # Yogurt, frozen, flavors not chocolate, nonfat milk, with low-calorie sweetener
    1236: [], # Ice cream, soft serve, chocolate
    1237: [], # Ice cream, bar or stick, chocolate covered
    1238: [], # Ice cream sandwich
    1239: [], # Ice cream cookie sandwich
    1240: [], # Ice cream cone, chocolate covered, with nuts, flavors other than chocolate
    1241: [], # Ice cream sandwich, made with light ice cream, vanilla
    1242: [], # Ice cream sandwich, vanilla, light, no sugar added
    1243: [], # Fat free ice cream, no sugar added, flavors other than chocolate
    1244: [], # Milk dessert bar, frozen, made from lowfat milk
    1249: [], # Yogurt, Greek, 2% fat,mixed berry blend, CHOBANI
    1250: [], # Nutritional supplement for people with diabetes, liquid
    1251: [], # Cheese, Mexican blend
    1252: [], # Cheese product, pasteurized process, American, vitamin D fortified
    1253: [], # Cheese, pasteurized process, American, without added vitamin D
    1254: [], # Cheese food, pasteurized process, American, without added vitamin D
    1255: [], # Egg, whole, raw, frozen, salted, pasteurized
    1256: [], # Yogurt, Greek, plain, nonfat (Includes foods for USDA's Food Distribution Program)
    1258: [], # Egg, white, dried, stabilized, glucose reduced
    1259: [], # Cheese spread, American or Cheddar cheese base, reduced fat
    1260: [], # Cheese, cheddar, reduced fat (Includes foods for USDA's Food Distribution Program)
    1263: [], # Ice cream, light, soft serve, chocolate
    1264: [], # Ice cream bar, stick or nugget, with crunch coating
    1265: [], # Cheese, cheddar, nonfat or fat free
    1266: [], # Cheese, Swiss, nonfat or fat free
    1267: [], # Cheese, mexican, queso cotija
    1270: [], # Cheese, cheddar, sharp, sliced
    1271: [], # Cheese, mozzarella, low moisture, part-skim, shredded
    1275: [], # Yogurt, Greek, nonfat, vanilla, CHOBANI
    1276: [], # Yogurt, Greek, strawberry, DANNON OIKOS
    1278: [], # Yogurt, Greek, nonfat, vanilla, DANNON OIKOS
    1280: [], # Yogurt, Greek, nonfat, strawberry, DANNON OIKOS
    1284: [], # Yogurt, Greek, strawberry, lowfat
    1285: [], # Yogurt, Greek, strawberry, nonfat
    1286: [], # Yogurt, Greek, vanilla, nonfat
    1287: ['Greek yogurt', 'low fat'], # Yogurt, Greek, plain, lowfat
    1289: ['Kefir'], # Kefir, lowfat, plain, LIFEWAY
    1290: ['Strawberry kefir'], # Kefir, lowfat, strawberry, LIFEWAY
    1291: [], # Milk, evaporated, 2% fat, with added vitamin A and vitamin D
    1292: [], # Milk, chocolate, fat free, with added vitamin A and vitamin D
    1293: ['Greek yogurt'], # Yogurt, Greek, plain, whole milk
    1294: [], # Yogurt, Greek, fruit, whole milk
    1295: [], # Yogurt, vanilla, non-fat
    1297: [], # Yogurt, Greek, vanilla, lowfat
    1298: [], # Yogurt, frozen, flavors other than chocolate, lowfat
    1300: [], # Ice cream bar, covered with chocolate and nuts
    1301: [], # Ice cream sundae cone
    1302: [], # Light ice cream, Creamsicle
    1303: [], # Cream, half and half, lowfat
    1304: [], # Yogurt, Greek, 2% fat, pineapple, CHOBANI
    1305: [], # Milk, chocolate, lowfat, reduced sugar
    1306: [], # Ice cream, lowfat, no sugar added, cone, added peanuts and chocolate sauce
    1307: [], # Yogurt, Greek, 2% fat, strawberry banana, CHOBANI
    1308: [], # Yogurt, Greek, whole, plain, CHOBANI
    1312: [], # Yogurt, Greek, nonfat, lemon blend, CHOBANI
    1313: [], # Yogurt, Greek, nonfat, peach, CHOBANI
    1314: [], # Yogurt, Greek, nonfat, plain, CHOBANI
    1316: [], # Yogurt, Greek, nonfat, raspberry, CHOBANI
    1319: [], # Yogurt, Greek, nonfat, Fruit on Bottom, Pomegranate, CHOBANI
    1320: [], # Yogurt, Greek, Blueberry, CHOBANI
    1321: [], # Yogurt, Greek, nonfat, Fruit on Bottom, Strawberry, CHOBANI
    1322: [], # Yogurt, Greek, nonfat, Fruit on Bottom, Blackberry, CHOBANI
    1323: ['Clarified butter', '', 'Ghee'], # Butter, Clarified butter (ghee)
    2001: ['Allspice', 'ground'], # Spices, allspice, ground
    2002: ['Anise seed'], # Spices, anise seed
    2003: ['Basil', 'dried'], # Spices, basil, dried
    2004: ['Bay leaf'], # Spices, bay leaf
    2005: ['Caraway seed'], # Spices, caraway seed
    2006: ['Cardamom'], # Spices, cardamom
    2007: ['Celery seed'], # Spices, celery seed
    2008: ['Chervil', 'dried'], # Spices, chervil, dried
    2009: ['Chili powder'], # Spices, chili powder
    2010: ['Cinnamon', 'ground'], # Spices, cinnamon, ground
    2011: ['Cloves', 'ground'], # Spices, cloves, ground
    2012: ['Coriander leaf', 'dried'], # Spices, coriander leaf, dried
    2013: ['Coriander seed'], # Spices, coriander seed
    2014: ['Cumin seed'], # Spices, cumin seed
    2015: ['Curry powder'], # Spices, curry powder
    2016: ['Dill seed'], # Spices, dill seed
    2017: ['Dill weed', 'dried'], # Spices, dill weed, dried
    2018: ['Fennel seed'], # Spices, fennel seed
    2019: ['Fenugreek seed'], # Spices, fenugreek seed
    2020: ['Garlic powder'], # Spices, garlic powder
    2021: ['Ginger', 'ground'], # Spices, ginger, ground
    2022: ['Mace', 'ground'], # Spices, mace, ground
    2023: ['Marjoram', 'dried'], # Spices, marjoram, dried
    2024: ['Mustard seed', 'ground'], # Spices, mustard seed, ground
    2025: ['Nutmeg', 'ground'], # Spices, nutmeg, ground
    2026: ['Onion powder'], # Spices, onion powder
    2027: ['Oregano', 'dried'], # Spices, oregano, dried
    2028: ['Paprika', 'dried'], # Spices, paprika
    2029: ['Parsley', 'dried'], # Spices, parsley, dried
    2030: ['Black pepper', '', "Pepper"], # Spices, pepper, black
    2031: ['Cayenne pepper'], # Spices, pepper, red or cayenne
    2032: ['White pepper'], # Spices, pepper, white
    2033: ['Poppy seed'], # Spices, poppy seed
    2034: ['Poultry seasoning'], # Spices, poultry seasoning
    2035: ['Pumpkin pie spice'], # Spices, pumpkin pie spice
    2036: ['Rosemary', 'dried'], # Spices, rosemary, dried
    2037: ['Saffron'], # Spices, saffron
    2038: ['Sage', 'ground'], # Spices, sage, ground
    2039: ['Savory', 'ground'], # Spices, savory, ground
    2041: ['Tarragon', 'dried'], # Spices, tarragon, dried
    2042: ['Thyme', 'dried'], # Spices, thyme, dried
    2043: ['Turmeric', 'ground'], # Spices, turmeric, ground
    2044: ['Basil', 'fresh'], # Basil, fresh
    2045: ['Dill weed', 'fresh'], # Dill weed, fresh
    2046: ['Mustard'], # Mustard, prepared, yellow
    2047: ['Salt'], # Salt, table
    2048: ['Cider vinegar'], # Vinegar, cider
    2049: ['Thyme', 'fresh'], # Thyme, fresh
    2050: ['Vanilla extract'], # Vanilla extract
    2051: [], # Vanilla extract, imitation, alcohol
    2052: [], # Vanilla extract, imitation, no alcohol
    2053: [], # Vinegar, distilled
    2054: ['Capers'], # Capers, canned
    2055: ['Horseradish'], # Horseradish, prepared
    2063: ['Rosemary', 'fresh'], # Rosemary, fresh
    2064: ['Peppermint', 'fresh'], # Peppermint, fresh
    2065: ['Spearmint', 'fresh', 'Mint'], # Spearmint, fresh
    2066: ['Spearmint', 'dried'], # Spearmint, dried
    2068: ['Red wine vinegar'], # Vinegar, red wine
    2069: ['Balsamic vinegar'], # Vinegar, balsamic
    2074: [], # Seasoning mix, dry, sazon, coriander & annatto
    2075: [], # Seasoning mix, dry, taco, original
    2076: [], # Seasoning mix, dry, chili, original
    3000: [], # Clif Z bar
    3001: [], # Babyfood, juice treats, fruit medley, toddler
    3002: [], # Babyfood, meat, beef, strained
    3003: [], # Babyfood, meat, beef, junior
    3005: [], # Babyfood, meat, veal, strained
    3007: [], # Babyfood, meat, pork, strained
    3008: [], # Babyfood, meat, ham, strained
    3009: [], # Babyfood, meat, ham, junior
    3010: [], # Babyfood, meat, lamb, strained
    3011: [], # Babyfood, meat, lamb, junior
    3012: [], # Babyfood, meat, chicken, strained
    3013: [], # Babyfood, meat, chicken, junior
    3014: [], # Babyfood, meat, chicken sticks, junior
    3015: [], # Babyfood, meat, turkey, strained
    3016: [], # Babyfood, meat, turkey, junior
    3017: [], # Babyfood, meat, turkey sticks, junior
    3019: [], # Babyfood, snack, GERBER GRADUATE FRUIT  STRIPS, Real Fruit Bars
    3021: [], # Babyfood, meat, meat sticks, junior
    3022: [], # Babyfood, GERBER, 2nd Foods, apple, carrot and squash, organic
    3023: [], # Babyfood, finger snacks, GERBER, GRADUATES, PUFFS, apple and cinnamon
    3024: [], # Babyfood, water, bottled, GERBER, without added fluoride
    3025: [], # Babyfood, GERBER, 3rd Foods, apple, mango and kiwi
    3026: [], # Babyfood, tropical fruit medley
    3041: [], # Babyfood, dinner, vegetables and dumplings and beef, strained
    3042: [], # Babyfood, dinner, vegetables and dumplings and beef, junior
    3043: [], # Babyfood, dinner, beef lasagna, toddler
    3044: [], # Babyfood, dinner, macaroni and tomato and beef, strained
    3045: [], # Babyfood, dinner, macaroni and tomato and beef, junior
    3046: [], # Babyfood, ravioli, cheese filled, with tomato sauce
    3047: [], # Babyfood, dinner, beef noodle, strained
    3048: [], # Babyfood, macaroni and cheese, toddler
    3049: [], # Babyfood, dinner, beef and rice, toddler
    3050: [], # Babyfood, dinner, spaghetti and tomato and meat, junior
    3051: [], # Babyfood, dinner, spaghetti and tomato and meat, toddler
    3053: [], # Babyfood, dinner, vegetables and beef, strained
    3054: [], # Babyfood, dinner, vegetables and beef, junior
    3055: [], # Babyfood, dinner, beef with vegetables
    3067: [], # Babyfood, dinner, vegetables and lamb, junior
    3068: [], # Babyfood, dinner, chicken noodle, strained
    3069: [], # Babyfood, dinner, chicken noodle, junior
    3070: [], # Babyfood, dinner, chicken soup, strained
    3072: [], # Babyfood, dinner, chicken stew, toddler
    3073: [], # Babyfood, dinner, vegetables chicken, strained
    3075: [], # Babyfood, dinner, vegetables, noodles and chicken, strained
    3076: [], # Babyfood, dinner, vegetables, noodles and chicken, junior
    3077: [], # Babyfood, dinner, pasta with vegetables
    3079: [], # Babyfood, dinner, vegetables and noodles and turkey, strained
    3081: [], # Babyfood, dinner, vegetables and noodles and turkey, junior
    3082: [], # Babyfood, dinner, turkey and rice, strained
    3083: [], # Babyfood, dinner, turkey and rice, junior
    3084: [], # Babyfood, dinner, vegetables and turkey, strained
    3085: [], # Babyfood, dinner, vegetables and turkey, junior
    3089: [], # Babyfood, dinner, macaroni and cheese, strained
    3090: [], # Babyfood, dinner, macaroni and cheese, junior
    3091: [], # Babyfood, vegetables, green beans, strained
    3092: [], # Babyfood, vegetables, green beans, junior
    3093: [], # Babyfood, green beans, dices, toddler
    3096: [], # Babyfood, vegetable, green beans and potatoes
    3098: [], # Babyfood, vegetables, beets, strained
    3099: [], # Babyfood, vegetables, carrots, strained
    3100: [], # Babyfood, vegetables, carrots, junior
    3104: [], # Babyfood, vegetables, squash, strained
    3105: [], # Babyfood, vegetables, squash, junior
    3108: [], # Babyfood, vegetables, sweet potatoes strained
    3109: [], # Babyfood, vegetables, sweet potatoes, junior
    3112: [], # Babyfood, potatoes, toddler
    3113: [], # Babyfood, cereal, Oatmeal, dry, GERBER, SINGLE GRAIN, fortified
    3114: [], # Babyfood, vegetable, butternut squash and corn
    3115: [], # Babyfood, apples, dices, toddler
    3116: [], # Babyfood, fruit, applesauce, strained
    3117: [], # Babyfood, fruit, applesauce, junior
    3118: [], # Babyfood, fruit, apricot with tapioca, strained
    3119: [], # Babyfood, vegetables, corn, creamed, strained
    3120: [], # Babyfood, vegetables, corn, creamed, junior
    3121: [], # Babyfood, vegetables, peas, strained
    3122: [], # Babyfood, peas, dices, toddler
    3127: [], # Babyfood, vegetables, spinach, creamed, strained
    3128: [], # Babyfood, fruit, apricot with tapioca, junior
    3129: [], # Babyfood, fruit, bananas with tapioca, strained
    3130: [], # Babyfood, fruit, peaches, strained
    3131: [], # Babyfood, fruit, peaches, junior
    3132: [], # Babyfood, fruit, pears, strained
    3133: [], # Babyfood, fruit, pears, junior
    3134: [], # Babyfood, fruit, plums with tapioca, without ascorbic acid, strained
    3135: [], # Babyfood, fruit, plums with tapioca, without ascorbic acid, junior
    3136: [], # Babyfood, fruit, prunes with tapioca, without ascorbic acid, strained
    3137: [], # Babyfood, fruit, prunes with tapioca, without ascorbic acid, junior
    3139: [], # Babyfood, prunes, without vitamin c, strained
    3140: [], # Babyfood, fruit dessert, mango with tapioca
    3141: [], # Babyfood, pears, dices, toddler
    3142: [], # Babyfood, fruit, applesauce and apricots, strained
    3143: [], # Babyfood, fruit, applesauce and apricots, junior
    3144: [], # Babyfood, fruit, applesauce and cherries, strained
    3145: [], # Babyfood, fruit, applesauce and cherries, junior
    3147: [], # Babyfood, fruit, applesauce with banana, junior
    3150: [], # Babyfood, fruit, applesauce and pineapple, strained
    3151: [], # Babyfood, fruit, applesauce and pineapple, junior
    3152: [], # Babyfood, fruit, apple and raspberry, strained
    3153: [], # Babyfood, fruit, apple and raspberry, junior
    3154: [], # Babyfood, fruit and vegetable, apple and sweet potato
    3156: [], # Babyfood, fruit, bananas and pineapple with tapioca, junior
    3157: [], # Babyfood, fruit, bananas and pineapple with tapioca, strained
    3158: [], # Babyfood, fruit, pears and pineapple, strained
    3159: [], # Babyfood, fruit, pears and pineapple, junior
    3160: [], # Babyfood, fruit, guava and papaya with tapioca, strained
    3161: [], # Babyfood, peaches, dices, toddler
    3162: [], # Babyfood, fruit, papaya and applesauce with tapioca, strained
    3163: [], # Babyfood, fruit, bananas with apples and pears, strained
    3164: [], # Babyfood, fruit, apple and blueberry, strained
    3165: [], # Babyfood, fruit, apple and blueberry, junior
    3166: [], # Babyfood, juice, apple
    3167: [], # Babyfood, apple-banana juice
    3168: [], # Babyfood, juice, apple and peach
    3171: [], # Babyfood, juice, apple and prune
    3172: [], # Babyfood, juice, orange
    3173: [], # Babyfood, juice, orange and apple
    3174: [], # Babyfood, juice, orange and apple and banana
    3175: [], # Babyfood, juice, orange and apricot
    3176: [], # Babyfood, juice, orange and banana
    3177: [], # Babyfood, juice, orange and pineapple
    3178: [], # Babyfood, juice, prune and orange
    3179: [], # Babyfood, juice, mixed fruit
    3181: [], # Babyfood, cereal, barley, dry fortified
    3184: [], # Babyfood, cereal, whole wheat, with apples, dry fortified
    3185: [], # Babyfood, cereal, mixed, dry fortified
    3186: [], # Babyfood, cereal, mixed, with bananas, dry
    3187: [], # Babyfood, cereal, mixed, with applesauce and bananas, strained
    3188: [], # Babyfood, cereal, mixed, with applesauce and bananas, junior, fortified
    3189: [], # Babyfood, cereal, oatmeal, dry fortified
    3190: [], # Babyfood, cereal, oatmeal, with bananas, dry
    3191: [], # Babyfood, cereal, oatmeal, with applesauce and bananas, strained
    3192: [], # Babyfood, cereal, oatmeal, with applesauce and bananas, junior, fortified
    3193: [], # Babyfood, cereal, oatmeal, with honey, dry
    3194: [], # Babyfood, cereal, rice, dry fortified
    3195: [], # Babyfood, cereal, rice, with applesauce and bananas, strained
    3197: [], # Babyfood, cereal, with egg yolks, strained
    3198: [], # Babyfood, cereal, with egg yolks, junior
    3199: [], # Babyfood, cereal, with eggs, strained
    3201: [], # Babyfood, cereal, egg yolks and bacon, junior
    3205: [], # Babyfood, oatmeal cereal with fruit, dry, instant, toddler fortified
    3206: [], # Babyfood, cookie, baby, fruit
    3209: [], # Babyfood, crackers, vegetable
    3211: [], # Babyfood, cereal, high protein, with apple and orange, dry
    3212: [], # Babyfood, cereal, rice, with bananas, dry
    3213: [], # Babyfood, cookies
    3214: [], # Babyfood, cookies, arrowroot
    3215: [], # Babyfood, pretzels
    3216: [], # Babyfood, GERBER, GRADUATES Lil Biscuits Vanilla Wheat
    3217: [], # Zwieback
    3220: [], # Babyfood, dessert, dutch apple, strained
    3221: [], # Babyfood, dessert, dutch apple, junior
    3222: [], # Babyfood, cherry cobbler, junior
    3224: [], # Babyfood, dessert, cherry vanilla pudding, strained
    3225: [], # Babyfood, dessert, cherry vanilla pudding, junior
    3226: [], # Babyfood, dessert, fruit pudding, orange, strained
    3227: [], # Babyfood, dessert, peach cobbler, strained
    3228: [], # Babyfood, dessert, peach cobbler, junior
    3229: [], # Babyfood, dessert, peach melba, strained
    3230: [], # Babyfood, dessert, peach melba, junior
    3233: [], # Babyfood, dessert, fruit pudding, pineapple, strained
    3235: [], # Babyfood, dessert, fruit dessert, without ascorbic acid, strained
    3236: [], # Babyfood, dessert, fruit dessert, without ascorbic acid, junior
    3238: [], # Babyfood, dessert, tropical fruit, junior
    3245: [], # Babyfood, dessert, custard pudding, vanilla, strained
    3246: [], # Babyfood, dessert, custard pudding, vanilla, junior
    3265: [], # Babyfood, juice, apple and grape
    3267: [], # Babyfood, juice, fruit punch, with calcium
    3269: [], # Babyfood, juice, apple, with calcium
    3274: [], # Babyfood, dinner, vegetables and chicken, junior
    3278: [], # Babyfood, dinner, mixed vegetable, strained
    3279: [], # Babyfood, dinner, mixed vegetable, junior
    3280: [], # Babyfood, fruit, bananas with tapioca, junior
    3282: [], # Babyfood, vegetables, mix vegetables junior
    3283: [], # Babyfood, vegetables, garden vegetable, strained
    3286: [], # Babyfood, vegetables, mix vegetables strained
    3287: [], # Babyfood, dinner, beef noodle, junior
    3289: [], # Babyfood, apples with ham, strained
    3290: [], # Babyfood, carrots and beef, strained
    3293: [], # Babyfood, plums, bananas and rice, strained
    3296: [], # Babyfood, dinner, turkey, rice, and vegetables, toddler
    3297: [], # Babyfood, dinner, apples and chicken, strained
    3298: [], # Babyfood, dinner, broccoli and chicken, junior
    3301: [], # Babyfood, beverage, GERBER, GRADUATES, FRUIT SPLASHERS
    3302: [], # Babyfood, snack, GERBER, GRADUATES, YOGURT MELTS
    3303: [], # Babyfood, dinner, sweet potatoes and chicken, strained
    3376: [], # Infant formula, MEAD JOHNSON, Enfamil 24, ready to feed, with ARA and DHA
    3381: [], # Infant formula, MEAD JOHNSON, Enfamil Enspire Powder, with ARA and DHA, not reconstituted
    3382: [], # Infant formula, MEAD JOHNSON, Enfamil Premature High Protein 24 Calories, ready to feed, with ARA and DHA
    3384: [], # Infant formula, MEAD JOHNSON, Enfamil Premature 30 Calories, ready to feed, with ARA and DHA
    3385: [], # Infant formula, MEAD JOHNSON, Enfamil for Supplementing, powder, with ARA and DHA, not reconstituted
    3386: [], # Infant formula, MEAD JOHNSON, Enfamil Reguline Powder, with ARA and DHA, not reconstituted
    3387: [], # Infant formula, MEAD JOHNSON, Enfamil Reguline, ready to feed, with ARA and DHA
    3388: [], # Infant formula, MEAD JOHNSON, Gentlease, ready to feed, with ARA and DHA
    3389: [], # Toddler formula, MEAD JOHNSON, Nutramigen Toddler with LGG Powder, with ARA and DHA, not reconstituted
    3390: [], # Infant formula, MEAD JOHNSON, Pregestimil 20 Calories, ready to feed, with ARA and DHA
    3391: [], # Infant formula, MEAD JOHNSON, Pregestimil 24 Calories, ready to feed, with ARA and DHA
    3392: [], # Toddler drink, MEAD JOHNSON, PurAmino Toddler Powder, with ARA and DHA, not reconstituted
    3393: [], # Infant formula, MEAD JOHNSON, Enfamil for Supplementing, ready to feed, with ARA and DHA
    3681: [], # Babyfood, cereal, barley, prepared with whole milk
    3682: [], # Babyfood, cereal, high protein, prepared with whole milk
    3685: [], # Babyfood, cereal, mixed, prepared with whole milk
    3686: [], # Babyfood, cereal, mixed, with bananas, prepared with whole milk
    3689: [], # Babyfood, cereal, oatmeal, prepared with whole milk
    3690: [], # Babyfood, cereal, oatmeal, with bananas, prepared with whole milk
    3693: [], # Babyfood, cereal, oatmeal, with honey, prepared with whole milk
    3694: [], # Babyfood, cereal, rice, prepared with whole milk
    3696: [], # Babyfood, cereal, rice, with honey, prepared with whole milk
    3704: [], # Babyfood, cereal, mixed, with honey, prepared with whole milk
    3711: [], # Babyfood, cereal, high protein, with apple and orange, prepared with whole milk
    3712: [], # Babyfood, cereal, rice, with bananas, prepared with whole milk
    3801: [], # Infant formula, NESTLE, GOOD START SUPREME, with iron, liquid concentrate, not reconstituted
    3802: [], # Infant formula, NESTLE, GOOD START SUPREME, with iron, powder
    3805: [], # Infant formula, MEAD JOHNSON, ENFAMIL, with iron, powder
    3808: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Infant, with iron, powder, with ARA and DHA
    3812: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Infant, with iron, liquid concentrate, with ARA and DHA, reconstituted
    3815: [], # Infant formula, MEAD JOHNSON, ENFAMIL LIPIL, with iron, ready-to-feed, with ARA and DHA
    3818: [], # Infant formula, MEAD JOHNSON, ENFAMIL, LIPIL, low iron, liquid concentrate, with ARA and DHA
    3821: [], # Infant formula, MEAD JOHNSON, PREGESTIMIL, with iron, powder, with ARA and DHA, not reconstituted
    3822: [], # Infant formula, MEAD JOHNSON, PREGESTIMIL, with iron, with ARA and DHA, prepared from powder
    3823: [], # Infant formula, MEAD JOHNSON, PROSOBEE, with iron, ready-to-feed
    3825: [], # Infant formula, MEAD JOHNSON, ENFAMIL, LIPIL, low iron, ready to feed, with ARA and DHA
    3832: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Infant, ready-to-feed, with ARA and DHA
    3837: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, PM 60/40, powder not reconstituted
    3838: [], # Infant formula, MEAD JOHNSON, ENFAMIL, NUTRAMIGEN WITH LGG, with iron, powder, not reconstituted, with ARA and DHA
    3841: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, with iron, ready-to-feed
    3842: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, with iron, liquid concentrate
    3843: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, with iron, powder, not reconstituted
    3844: [], # Infant formula, MEAD JOHNSON, ENFAMIL, NUTRAMIGEN, with iron, liquid concentrate not reconstituted, with ARA and DHA
    3845: [], # Infant formula, MEAD JOHNSON, ENFAMIL, NUTRAMIGEN, with iron, ready-to-feed, with ARA and DHA
    3846: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ALIMENTUM, with iron, ready-to-feed
    3849: [], # Infant formula, MEAD JOHNSON, ENFAMIL, ENFACARE, with iron, powder, with ARA and DHA
    3851: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, with iron, liquid concentrate, not reconstituted
    3852: [], # Infant formula, MEAD JOHNSON, ENFAMIL, PROSOBEE, with iron, powder, not reconstituted, with ARA and DHA
    3853: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, with iron, powder, not reconstituted
    3854: [], # Infant formula, MEAD JOHNSON, ENFAMIL, PROSOBEE, liquid concentrate, reconstituted, with ARA and DHA
    3857: [], # Infant formula, MEAD JOHNSON, PROSOBEE, with iron, ready to feed, with ARA and DHA
    3859: [], # Infant formula, NESTLE, GOOD START SOY, with DHA and ARA, ready-to-feed
    3860: [], # Child formula, ABBOTT NUTRITION, PEDIASURE, ready-to-feed
    3861: [], # Infant formula, MEAD JOHNSON, NEXT STEP, PROSOBEE LIPIL, powder, with ARA and DHA
    3864: [], # Infant formula, MEAD JOHNSON, NEXT STEP, PROSOBEE, LIPIL, ready to feed, with ARA and DHA
    3867: [], # Infant formula, NESTLE, GOOD START SOY, with ARA and DHA, powder
    3870: [], # Child formula, ABBOTT NUTRITION, PEDIASURE, ready-to-feed, with iron and fiber
    3928: [], # Infant formula, NESTLE, GOOD START ESSENTIALS SOY, with iron, powder
    3929: [], # Infant formula, MEAD JOHNSON, NEXT STEP PROSOBEE, powder, not reconstituted
    3930: [], # Infant formula, MEAD JOHNSON,NEXT STEP PROSOBEE, prepared from powder
    3934: [], # Babyfood, corn and sweet potatoes, strained
    3935: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ALIMENTUM, ADVANCE, ready-to-feed, with ARA and DHA
    3936: [], # Infant formula, PBM PRODUCTS, store brand, ready-to-feed
    3937: [], # Infant formula, PBM PRODUCTS, store brand, liquid concentrate, not reconstituted
    3938: [], # Infant formula, PBM PRODUCTS, store brand, powder
    3939: [], # Infant formula, PBM PRODUCTS, store brand, soy, ready-to-feed
    3940: [], # Infant formula, PBM PRODUCTS, store brand, soy, liquid concentrate, not reconstituted
    3941: [], # Infant formula, PBM PRODUCTS, store brand, soy, powder
    3942: [], # Infant formula, MEAD JOHNSON, ENFAMIL, AR, ready-to-feed, with ARA and DHA
    3943: [], # Infant formula, MEAD JOHNSON, ENFAMIL, AR, powder, with ARA and DHA
    3944: [], # Infant formula, ABBOTT NUTRITION, SIMILAC NEOSURE, ready-to-feed, with ARA and DHA
    3945: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, NEOSURE, powder, with ARA and DHA
    3946: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, SENSITIVE (LACTOSE FREE) ready-to-feed, with ARA and DHA
    3947: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, SENSITIVE, (LACTOSE FREE), liquid concentrate, with ARA and DHA
    3948: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, SENSITIVE, (LACTOSE FREE), powder, with ARA and DHA
    3949: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ADVANCE, with iron, ready-to-feed
    3950: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ADVANCE, with iron, powder, not reconstituted
    3951: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ADVANCE, with iron, liquid concentrate, not reconstituted
    3952: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, ADVANCE with iron, liquid concentrate
    3953: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, ADVANCE with iron, ready-to-feed
    3954: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, ISOMIL, ADVANCE with iron, powder, not reconstituted
    3955: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, ENFACARE, ready-to-feed, with ARA and DHA
    3956: [], # Babyfood, yogurt, whole milk, with fruit, multigrain cereal and added DHA fortified
    3957: [], # Infant formula, ABBOTT NUTRITION, ALIMENTUM ADVANCE, with iron, powder, not reconstituted, with DHA and ARA
    3959: [], # Babyfood, mashed cheddar potatoes and broccoli, toddlers
    3960: [], # Infant formula, NESTLE, GOOD START SUPREME, with iron, DHA and ARA, ready-to-feed
    3961: [], # Infant formula, NESTLE, GOOD START SUPREME, with iron, DHA and ARA, prepared from liquid concentrate
    3963: [], # Infant Formula, MEAD JOHNSON, ENFAMIL GENTLEASE, with iron, prepared from powder
    3964: [], # Babyfood, fortified cereal bar, fruit filling
    3965: [], # Babyfood, yogurt, whole milk, with fruit, multigrain cereal and added iron fortified
    3966: [], # Infant formula, NESTLE, GOOD START SOY, with DHA and ARA, liquid concentrate
    3967: [], # Toddler formula, MEAD JOHNSON, ENFAGROW, Toddler Transitions, with ARA and DHA, powder
    3968: [], # Toddler formula, MEAD JOHNSON, ENFAGROW PREMIUM (formerly ENFAMIL, LIPIL, NEXT STEP), ready-to-feed
    3980: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, GENTLEASE, with ARA and DHA powder not reconstituted
    3982: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Enfagrow, Soy, Toddler ready-to-feed
    3983: [], # Infant formula, MEAD JOHNSON, ENFAMIL, NUTRAMIGEN AA, ready-to-feed
    3984: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Premature, with iron, 20 calories, ready-to-feed
    3985: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Premature, with iron, 24 calories, ready-to-feed
    3986: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Newborn, with DHA and ARA, ready-to-feed
    3987: [], # Infant formula, GERBER, GOOD START 2 Soy, with iron, ready-to-feed
    3988: [], # Infant formula, GERBER, GOOD START, PROTECT PLUS, ready-to-feed
    3989: [], # Infant Formula, GERBER GOOD START 2, GENTLE PLUS, ready-to-feed
    3990: [], # Infant formula, GERBER, GOOD START 2, PROTECT PLUS, ready-to-feed
    3991: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, GO AND GROW, ready-to-feed, with ARA and DHA
    3992: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, Expert Care, Diarrhea, ready- to- feed with ARA and DHA
    3993: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, For Spit Up, ready-to-feed, with ARA and DHA
    3994: [], # Babyfood, fruit, banana and strawberry, junior
    3995: [], # Babyfood, banana with mixed berries, strained
    3996: [], # Babyfood, Multigrain whole grain cereal, dry fortified
    3997: [], # Babyfood, Baby MUM MUM Rice Biscuits
    3998: [], # Babyfood, Snack, GERBER, GRADUATES, LIL CRUNCHIES, baked whole grain corn snack
    3999: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, For Spit Up, powder, with ARA and DHA
    4001: ['Beef tallow'], # Fat, beef tallow
    4002: ['Lard'], # Lard
    4011: [], # Salad dressing, KRAFT Mayo Light Mayonnaise
    4013: [], # Salad dressing, KRAFT Mayo Fat Free Mayonnaise Dressing
    4014: [], # Salad dressing, KRAFT MIRACLE WHIP FREE Nonfat Dressing
    4015: [], # Salad dressing, russian dressing
    4016: [], # Salad dressing, sesame seed dressing, regular
    4017: [], # Salad dressing, thousand island, commercial, regular
    4018: [], # Salad dressing, mayonnaise type, regular, with salt
    4020: [], # Salad dressing, french dressing, reduced fat
    4021: [], # Salad dressing, italian dressing, commercial, reduced fat
    4022: [], # Salad dressing, russian dressing, low calorie
    4023: [], # Salad dressing, thousand island dressing, reduced fat
    4025: [], # Salad dressing, mayonnaise, regular
    4026: [], # Salad dressing, mayonnaise, soybean and safflower oil, with salt
    4027: [], # Salad dressing, mayonnaise, imitation, soybean
    4028: [], # Salad dressing, mayonnaise, imitation, milk cream
    4029: [], # Salad dressing, mayonnaise, imitation, soybean without cholesterol
    4030: [], # Sandwich spread, with chopped pickle, regular, unspecified oils
    4031: [], # Shortening, household, soybean (partially hydrogenated)-cottonseed (partially hydrogenated)
    4034: [], # Oil, soybean, salad or cooking, (partially hydrogenated)
    4037: ['Rice bran oil'], # Oil, rice bran
    4038: ['Wheat germ oil'], # Oil, wheat germ
    4042: ['Peanut oil'], # Oil, peanut, salad or cooking
    4044: ['Soybean oil'], # Oil, soybean, salad or cooking
    4047: ['Coconut oil'], # Oil, coconut
    4053: ['Olive oil'], # Oil, olive, salad or cooking
    4055: ['Palm oil'], # Oil, palm
    4058: ['Sesame oil'], # Oil, sesame, salad or cooking
    4060: ['Sunflower oil', '', 'Vegetable oil'], # Oil, sunflower, linoleic (less than 60%)
    4073: [], # Margarine, regular, hard, soybean (hydrogenated)
    4114: [], # Salad dressing, italian dressing, commercial, regular
    4120: [], # Salad dressing, french dressing, commercial, regular
    4128: [], # Margarine,spread, 35-39% fat, tub
    4133: [], # Salad dressing, french, home recipe
    4135: [], # Salad dressing, home recipe, vinegar and oil
    4141: [], # Salad dressing, french dressing, commercial, regular, without salt
    4142: [], # Salad dressing, french dressing, reduced fat, without salt
    4143: [], # Salad dressing, italian dressing, commercial, regular, without salt
    4144: [], # Salad dressing, italian dressing, reduced fat, without salt
    4145: [], # Salad dressing, mayonnaise, soybean oil, without salt
    4146: [], # Salad dressing, french, cottonseed, oil, home recipe
    4367: [], # Salad dressing, french dressing, fat-free
    4501: [], # Oil, cocoa butter
    4502: [], # Oil, cottonseed, salad or cooking
    4506: [], # Oil, sunflower, linoleic, (approx. 65%)
    4510: [], # Oil, safflower, salad or cooking, linoleic, (over 70%)
    4511: [], # Oil, safflower, salad or cooking, high oleic (primary safflower oil of commerce)
    4513: [], # Vegetable oil, palm kernel
    4514: [], # Oil, poppyseed
    4515: [], # Oil, tomatoseed
    4516: [], # Oil, teaseed
    4517: [], # Oil, grapeseed
    4518: [], # Oil, corn, industrial and retail, all purpose salad or cooking
    4528: ['Walnut oil'], # Oil, walnut
    4529: [], # Oil, almond
    4530: [], # Oil, apricot kernel
    4531: [], # Oil, soybean lecithin
    4532: [], # Oil, hazelnut
    4534: [], # Oil, babassu
    4536: [], # Oil, sheanut
    4539: [], # Salad dressing, blue or roquefort cheese dressing, commercial, regular
    4541: [], # Oil, cupu assu
    4542: [], # Fat, chicken
    4543: [], # Oil, soybean, salad or cooking, (partially hydrogenated) and cottonseed
    4544: [], # Shortening, household, lard and vegetable oil
    4545: [], # Oil, sunflower, linoleic, (partially hydrogenated)
    4546: [], # Shortening bread, soybean (hydrogenated) and cottonseed
    4548: [], # Shortening cake mix, soybean (hydrogenated) and cottonseed (hydrogenated)
    4549: [], # Shortening industrial, lard and vegetable oil
    4550: [], # Shortening frying (heavy duty), beef tallow and cottonseed
    4551: [], # Shortening confectionery, coconut (hydrogenated) and or palm kernel (hydrogenated)
    4554: [], # Shortening industrial, soybean (hydrogenated) and cottonseed
    4556: [], # Shortening frying (heavy duty), palm (hydrogenated)
    4559: [], # Shortening household soybean (hydrogenated) and palm
    4560: [], # Shortening frying (heavy duty), soybean (hydrogenated), linoleic (less than 1%)
    4570: [], # Shortening, confectionery, fractionated palm
    4572: [], # Oil, nutmeg butter
    4573: [], # Oil, ucuhuba butter
    4575: ['Turkey fat'], # Fat, turkey
    4576: ['Goose fat'], # Fat, goose
    4581: ['Avocado oil'], # Oil, avocado
    4582: [], # Oil, canola
    4583: [], # Oil, mustard
    4584: [], # Oil, sunflower, high oleic (70% and over)
    4585: [], # Margarine-like, margarine-butter blend, soybean oil and butter
    4586: [], # Shortening, special purpose for cakes and frostings, soybean (hydrogenated)
    4587: [], # Shortening, special purpose for baking, soybean (hydrogenated) palm and cottonseed
    4588: [], # Oil, oat
    4589: [], # Fish oil, cod liver
    4590: [], # Fish oil, herring
    4591: [], # Fish oil, menhaden
    4592: [], # Fish oil, menhaden, fully hydrogenated
    4593: [], # Fish oil, salmon
    4594: [], # Fish oil, sardine
    4595: [], # Shortening, multipurpose, soybean (hydrogenated) and palm (hydrogenated)
    4600: [], # Margarine-like, vegetable oil-butter spread, tub, with salt
    4601: [], # Butter, light, stick, with salt
    4602: [], # Butter, light, stick, without salt
    4609: [], # Animal fat, bacon grease
    4610: [], # Margarine, regular, 80% fat, composite, stick, with salt
    4611: [], # Margarine, regular, 80% fat, composite, tub, with salt
    4612: [], # Margarine-like, vegetable oil spread, 60% fat, stick, with salt
    4613: [], # Margarine-like, vegetable oil spread, 60% fat, tub, with salt
    4614: [], # Margarine-like, vegetable oil spread, 60% fat, stick/tub/bottle, with salt
    4615: [], # Shortening, vegetable, household, composite
    4617: ['Margarine'], # Margarine, regular, 80% fat, composite, stick, without salt
    4618: [], # Margarine, regular, 80% fat, composite, tub, without salt
    4620: [], # Margarine-like, vegetable oil spread, 60% fat, stick/tub/bottle, without salt
    4624: [], # Margarine-like, vegetable oil spread, fat free, liquid, with salt
    4626: [], # Margarine-like spread with yogurt, 70% fat, stick, with salt
    4627: [], # Margarine-like spread with yogurt, approximately 40% fat, tub, with salt
    4628: [], # Margarine, 80% fat, stick, includes regular and hydrogenated corn and soybean oils
    4629: [], # Margarine, margarine-type vegetable oil spread, 70% fat, soybean and partially hydrogenated soybean, stick
    4630: [], # Margarine Spread, 40-49% fat, tub
    4631: [], # Margarine-like, vegetable oil spread, fat-free, tub
    4633: [], # Margarine-like, vegetable oil spread, 20% fat, with salt
    4634: [], # Margarine-like, vegetable oil spread, 20% fat, without salt
    4635: [], # Salad dressing, thousand island dressing, fat-free
    4636: [], # Salad dressing, italian dressing, fat-free
    4638: [], # Salad dressing, ranch dressing, fat-free
    4639: [], # Salad dressing, ranch dressing, regular
    4640: [], # Salad dressing, ranch dressing, reduced fat
    4641: [], # Salad dressing, mayonnaise, light
    4642: [], # Oil, industrial, mid-oleic, sunflower
    4643: [], # Oil, industrial, canola with antifoaming agent, principal uses salads, woks and light frying
    4644: [], # Oil, industrial, canola for salads, woks and light frying
    4645: [], # Oil, industrial, canola (partially hydrogenated) oil for deep fat frying
    4646: [], # Oil, industrial, coconut, principal uses candy coatings, oil sprays, roasting nuts
    4648: [], # Oil, industrial, soy (partially hydrogenated), principal uses popcorn and flavoring vegetables
    4649: [], # Shortening, industrial, soy (partially hydrogenated), pourable liquid fry shortening
    4650: [], # Oil, industrial, soy, refined, for woks and light frying
    4651: [], # Oil, industrial, soy (partially hydrogenated), multiuse for non-dairy butter flavor
    4652: [], # Oil, industrial, soy ( partially hydrogenated), all purpose
    4653: [], # Oil, industrial, soy (partially hydrogenated ) and soy (winterized), pourable clear fry
    4654: [], # Oil, industrial, soy (partially hydrogenated)  and cottonseed, principal use as a tortilla shortening
    4655: [], # Margarine-like shortening, industrial, soy (partially hydrogenated), cottonseed, and soy, principal use flaky pastries
    4656: [], # Oil, industrial, palm kernel, confection fat, uses similar to high quality cocoa butter
    4657: [], # Oil, industrial, palm kernel (hydrogenated), confection fat, uses similar to 95 degree hard butter
    4658: [], # Oil, industrial, palm kernel (hydrogenated), confection fat, intermediate grade product
    4659: [], # Oil, industrial, coconut, confection fat, typical basis for ice cream coatings
    4660: [], # Oil, industrial, palm kernel (hydrogenated) , used for whipped toppings, non-dairy
    4661: [], # Oil, industrial, coconut (hydrogenated), used for whipped toppings and coffee whiteners
    4662: [], # Oil, industrial, palm and palm kernel, filling fat (non-hydrogenated)
    4663: [], # Oil, industrial, palm kernel (hydrogenated), filling fat
    4664: [], # Oil, industrial, soy (partially hydrogenated ), palm, principal uses icings and fillings
    4665: [], # Margarine, industrial, non-dairy, cottonseed, soy oil (partially hydrogenated ), for flaky pastries
    4666: [], # Shortening, industrial, soy (partially hydrogenated ) and corn for frying
    4667: [], # Shortening, industrial, soy (partially hydrogenated ) for baking and confections
    4668: [], # Margarine, industrial, soy and partially hydrogenated soy oil, use for baking, sauces and candy
    4669: [], # Oil, vegetable, soybean, refined
    4673: [], # Margarine-like spread, SMART BALANCE Regular Buttery Spread with flax oil
    4674: [], # Margarine-like spread, SMART BALANCE Light Buttery Spread
    4675: [], # Margarine-like spread, SMART BEAT Super Light without saturated fat
    4676: [], # Margarine-like spread, SMART BEAT Smart Squeeze
    4677: [], # Margarine-like spread, SMART BALANCE Omega Plus Spread (with plant sterols & fish oil)
    4678: [], # Oil, vegetable, Natreon canola, high stability, non trans, high oleic (70%)
    4679: [], # Oil, PAM cooking spray, original
    4683: [], # Margarine, margarine-like vegetable oil spread, 67-70% fat, tub
    4684: [], # Margarine, 80% fat, tub, CANOLA HARVEST Soft Spread (canola, palm and palm kernel oils)
    4685: [], # Oil, cooking and salad, ENOVA, 80% diglycerides
    4686: [], # Salad dressing, honey mustard dressing, reduced calorie
    4687: [], # Margarine-like spread, BENECOL Light Spread
    4688: [], # Salad dressing, spray-style dressing, assorted flavors
    4689: [], # Salad Dressing, mayonnaise, light, SMART BALANCE, Omega Plus light
    4690: [], # Margarine-like, vegetable oil spread, approximately 37% fat, unspecified oils, with salt, with added vitamin D
    4691: [], # Margarine, regular, 80% fat, composite, stick, with salt, with added vitamin D
    4692: [], # Margarine, regular, 80% fat, composite, tub, with salt, with added vitamin D
    4693: [], # Margarine-like, vegetable oil spread, 60% fat, stick, with salt, with added vitamin D
    4694: [], # Margarine-like, vegetable oil spread, 60% fat, tub, with salt, with added vitamin D
    4695: [], # Margarine-like vegetable-oil spread, stick/tub/bottle, 60% fat, with added vitamin D
    4696: [], # Margarine, regular, 80% fat, composite, stick, without salt, with added vitamin D
    4697: [], # Margarine-like, vegetable oil spread, 60% fat, stick/tub/bottle, without salt, with added vitamin D
    4698: [], # Oil, industrial, canola, high oleic
    4699: [], # Oil, industrial, soy, low linolenic
    4700: [], # Oil, industrial, soy, ultra low linolenic
    4701: [], # Oil, industrial, soy, fully hydrogenated
    4702: [], # Oil, industrial, cottonseed, fully hydrogenated
    4703: [], # Salad dressing, honey mustard, regular
    4704: [], # Salad dressing, poppyseed, creamy
    4705: [], # Salad dressing, caesar, fat-free
    4706: [], # Dressing, honey mustard, fat-free
    4707: [], # Oil, flaxseed, contains added sliced flaxseed
    4708: ['Mayonnaise'], # Mayonnaise, reduced fat, with olive oil
    4709: [], # Salad dressing, mayonnaise-type, light
    5000: [], # Chicken, broiler, rotisserie, BBQ, breast, meat only
    5001: [], # Chicken, broilers or fryers, meat and skin and giblets and neck, raw
    5002: [], # Chicken, broilers or fryers, meat and skin and giblets and neck, cooked, fried, batter
    5003: [], # Chicken, broilers or fryers, meat and skin and giblets and neck, cooked, fried, flour
    5004: [], # Chicken, broilers or fryers, meat and skin and giblets and neck, roasted
    5005: [], # Chicken, broilers or fryers, meat and skin and giblets and neck, stewed
    5006: ['Chicken', 'whole'], # Chicken, broilers or fryers, meat and skin, raw
    5007: [], # Chicken, broilers or fryers, meat and skin, cooked, fried, batter
    5008: [], # Chicken, broilers or fryers, meat and skin, cooked, fried, flour
    5009: [], # Chicken, broilers or fryers, meat and skin, cooked, roasted
    5010: [], # Chicken, broilers or fryers, meat and skin, cooked, stewed
    5011: ['Chicken', 'skinless'], # Chicken, broilers or fryers, meat only, raw
    5012: [], # Chicken, broilers or fryers, meat only, cooked, fried
    5013: [], # Chicken, broilers or fryers, meat only, cooked, roasted
    5014: [], # Chicken, broilers or fryers, meat only, cooked, stewed
    5015: ['Chicken skin'], # Chicken, broilers or fryers, skin only, raw
    5016: [], # Chicken, broilers or fryers, skin only, cooked, fried, batter
    5017: [], # Chicken, broilers or fryers, skin only, cooked, fried, flour
    5018: [], # Chicken, broilers or fryers, skin only, cooked, roasted
    5019: [], # Chicken, broilers or fryers, skin only, cooked, stewed
    5020: ['Chicken giblet'], # Chicken, broilers or fryers, giblets, raw
    5021: [], # Chicken, broilers or fryers, giblets, cooked, fried
    5022: [], # Chicken, broilers or fryers, giblets, cooked, simmered
    5023: [], # Chicken, gizzard, all classes, raw
    5024: [], # Chicken, gizzard, all classes, cooked, simmered
    5025: ['Chicken heart'], # Chicken, heart, all classes, raw
    5026: [], # Chicken, heart, all classes, cooked, simmered
    5027: ['Chicken liver'], # Chicken, liver, all classes, raw
    5028: [], # Chicken, liver, all classes, cooked, simmered
    5029: [], # Chicken, broilers or fryers, light meat, meat and skin, raw
    5030: [], # Chicken, broilers or fryers, light meat, meat and skin, cooked, fried, batter
    5031: [], # Chicken, broilers or fryers, light meat, meat and skin, cooked, fried, flour
    5032: [], # Chicken, broilers or fryers, light meat, meat and skin, cooked, roasted
    5033: [], # Chicken, broilers or fryers, light meat, meat and skin, cooked, stewed
    5034: [], # Chicken, broilers or fryers, dark meat, meat and skin, raw
    5035: [], # Chicken, broilers or fryers, dark meat, meat and skin, cooked, fried, batter
    5036: [], # Chicken, broilers or fryers, dark meat, meat and skin, cooked, fried, flour
    5037: [], # Chicken, broilers or fryers, dark meat, meat and skin, cooked, roasted
    5038: [], # Chicken, broilers or fryers, dark meat, meat and skin, cooked, stewed
    5039: [], # Chicken, broilers or fryers, light meat, meat only, raw
    5040: [], # Chicken, broilers or fryers, light meat, meat only, cooked, fried
    5041: [], # Chicken, broilers or fryers, light meat, meat only, cooked, roasted
    5042: [], # Chicken, broilers or fryers, light meat, meat only, cooked, stewed
    5043: [], # Chicken, broilers or fryers, dark meat, meat only, raw
    5044: [], # Chicken, broilers or fryers, dark meat, meat only, cooked, fried
    5045: [], # Chicken, broilers or fryers, dark meat, meat only, cooked, roasted
    5046: [], # Chicken, broilers or fryers, dark meat, meat only, cooked, stewed
    5047: [], # Chicken, broilers or fryers, separable fat, raw
    5048: ['Chicken back'], # Chicken, broilers or fryers, back, meat and skin, raw
    5049: [], # Chicken, broilers or fryers, back, meat and skin, cooked, fried, batter
    5050: [], # Chicken, broilers or fryers, back, meat and skin, cooked, fried, flour
    5051: [], # Chicken, broilers or fryers, back, meat and skin, cooked, roasted
    5052: [], # Chicken, broilers or fryers, back, meat and skin, cooked, stewed
    5053: ['Chicken back', 'skinless'], # Chicken, broilers or fryers, back, meat only, raw
    5054: [], # Chicken, broilers or fryers, back, meat only, cooked, fried
    5055: [], # Chicken, broilers or fryers, back, meat only, cooked, roasted
    5056: [], # Chicken, broilers or fryers, back, meat only, cooked, stewed
    5057: ['Chicken breast'], # Chicken, broilers or fryers, breast, meat and skin, raw
    5058: [], # Chicken, broilers or fryers, breast, meat and skin, cooked, fried, batter
    5059: [], # Chicken, broilers or fryers, breast, meat and skin, cooked, fried, flour
    5060: [], # Chicken, broilers or fryers, breast, meat and skin, cooked, roasted
    5061: [], # Chicken, broilers or fryers, breast, meat and skin, cooked, stewed
    5062: ['Chicken breast', 'skinless'], # Chicken, broiler or fryers, breast, skinless, boneless, meat only, raw
    5063: [], # Chicken, broilers or fryers, breast, meat only, cooked, fried
    5064: [], # Chicken, broilers or fryers, breast, meat only, cooked, roasted
    5065: [], # Chicken, broilers or fryers, breast, meat only, cooked, stewed
    5066: ['Chicken drumstick'], # Chicken, broilers or fryers, drumstick, meat and skin, raw
    5067: [], # Chicken, broilers or fryers, drumstick, meat and skin, cooked, fried, batter
    5068: [], # Chicken, broilers or fryers, drumstick, meat and skin, cooked, fried, flour
    5069: [], # Chicken, broilers or fryers, drumstick, meat and skin, cooked, roasted
    5070: [], # Chicken, broilers or fryers, drumstick, meat and skin, cooked, stewed
    5071: [], # Chicken, broilers or fryers, dark meat, drumstick, meat only, raw
    5072: [], # Chicken, broilers or fryers, drumstick, meat only, cooked, fried
    5073: [], # Chicken, broilers or fryers, dark meat, drumstick, meat only, cooked, roasted
    5074: [], # Chicken, broilers or fryers, drumstick, meat only, cooked, stewed
    5075: ['Chicken leg'], # Chicken, broilers or fryers, leg, meat and skin, raw
    5076: [], # Chicken, broilers or fryers, leg, meat and skin, cooked, fried, batter
    5077: [], # Chicken, broilers or fryers, leg, meat and skin, cooked, fried, flour
    5078: [], # Chicken, broilers or fryers, leg, meat and skin, cooked, roasted
    5079: [], # Chicken, broilers or fryers, leg, meat and skin, cooked, stewed
    5080: ['Chicken leg', 'skinless'], # Chicken, broilers or fryers, leg, meat only, raw
    5081: [], # Chicken, broilers or fryers, leg, meat only, cooked, fried
    5082: [], # Chicken, broilers or fryers, leg, meat only, cooked, roasted
    5083: [], # Chicken, broilers or fryers, leg, meat only, cooked, stewed
    5084: ['Chicken neck'], # Chicken, broilers or fryers, neck, meat and skin, raw
    5085: [], # Chicken, broilers or fryers, neck, meat and skin, cooked, fried, batter
    5086: [], # Chicken, broilers or fryers, neck, meat and skin, cooked, fried, flour
    5087: [], # Chicken, broilers or fryers, neck, meat and skin, cooked simmered
    5088: ['Chicken neck', 'skinless'], # Chicken, broilers or fryers, neck, meat only, raw
    5089: [], # Chicken, broilers or fryers, neck, meat only, cooked, fried
    5090: [], # Chicken, broilers or fryers, neck, meat only, cooked, simmered
    5091: ['Chicken thigh'], # Chicken, broilers or fryers, thigh, meat and skin, raw
    5092: [], # Chicken, broilers or fryers, thigh, meat and skin, cooked, fried, batter
    5093: [], # Chicken, broilers or fryers, thigh, meat and skin, cooked, fried, flour
    5094: [], # Chicken, broilers or fryers, thigh, meat and skin, cooked, roasted
    5095: [], # Chicken, broilers or fryers, thigh, meat and skin, cooked, stewed
    5096: ['Chicken thigh', 'skinless'], # Chicken, broilers or fryers, dark meat, thigh, meat only, raw
    5097: [], # Chicken, broilers or fryers, thigh, meat only, cooked, fried
    5098: [], # Chicken, broilers or fryers, thigh, meat only, cooked, roasted
    5099: [], # Chicken, broilers or fryers, thigh, meat only, cooked, stewed
    5100: ['Chicken wing'], # Chicken, broilers or fryers, wing, meat and skin, raw
    5101: [], # Chicken, broilers or fryers, wing, meat and skin, cooked, fried, batter
    5102: [], # Chicken, broilers or fryers, wing, meat and skin, cooked, fried, flour
    5103: [], # Chicken, broilers or fryers, wing, meat and skin, cooked, roasted
    5104: [], # Chicken, broilers or fryers, wing, meat and skin, cooked, stewed
    5105: ['Chicken wing', 'skinless'], # Chicken, broilers or fryers, wing, meat only, raw
    5106: [], # Chicken, broilers or fryers, wing, meat only, cooked, fried
    5107: [], # Chicken, broilers or fryers, wing, meat only, cooked, roasted
    5108: [], # Chicken, broilers or fryers, wing, meat only, cooked, stewed
    5109: [], # Chicken, roasting, meat and skin and giblets and neck, raw
    5110: [], # Chicken, roasting, meat and skin and giblets and neck, cooked, roasted
    5111: [], # Canada Goose, breast meat only, skinless, raw
    5112: [], # Chicken, roasting, meat and skin, cooked, roasted
    5113: [], # Chicken, roasting, meat only, raw
    5114: [], # Chicken, roasting, meat only, cooked, roasted
    5115: [], # Chicken, roasting, giblets, raw
    5116: [], # Chicken, roasting, giblets, cooked, simmered
    5117: [], # Chicken, roasting, light meat, meat only, raw
    5118: [], # Chicken, roasting, light meat, meat only, cooked, roasted
    5119: [], # Chicken, roasting, dark meat, meat only, raw
    5120: [], # Chicken, roasting, dark meat, meat only, cooked, roasted
    5121: [], # Chicken, stewing, meat and skin, and giblets and neck, raw
    5122: [], # Chicken, stewing, meat and skin, and giblets and neck, cooked, stewed
    5123: [], # Chicken, stewing, meat and skin, raw
    5124: [], # Chicken, stewing, meat and skin, cooked, stewed
    5125: [], # Chicken, stewing, meat only, raw
    5126: [], # Chicken, stewing, meat only, cooked, stewed
    5127: [], # Chicken, stewing, giblets, raw
    5128: [], # Chicken, stewing, giblets, cooked, simmered
    5129: [], # Chicken, stewing, light meat, meat only, raw
    5130: [], # Chicken, stewing, light meat, meat only, cooked, stewed
    5131: [], # Chicken, stewing, dark meat, meat only, raw
    5132: [], # Chicken, stewing, dark meat, meat only, cooked, stewed
    5133: [], # Chicken, capons, meat and skin and giblets and neck, raw
    5134: [], # Chicken, capons, meat and skin and giblets and neck, cooked, roasted
    5135: [], # Chicken, capons, meat and skin, raw
    5136: [], # Chicken, capons, meat and skin, cooked, roasted
    5137: [], # Chicken, capons, giblets, raw
    5138: [], # Chicken, capons, giblets, cooked, simmered
    5139: ['Duck', 'whole'], # Duck, domesticated, meat and skin, raw
    5140: [], # Duck, domesticated, meat and skin, cooked, roasted
    5141: ['Duck', 'skinless'], # Duck, domesticated, meat only, raw
    5142: [], # Duck, domesticated, meat only, cooked, roasted
    5143: ['Duck liver'], # Duck, domesticated, liver, raw
    5144: [], # Duck, wild, meat and skin, raw
    5145: ['Duck breast'], # Duck, wild, breast, meat only, raw
    5146: ['Goose', 'whole'], # Goose, domesticated, meat and skin, raw
    5147: [], # Goose, domesticated, meat and skin, cooked, roasted
    5148: ['Goose', 'skinless'], # Goose, domesticated, meat only, raw
    5149: [], # Goose, domesticated, meat only, cooked, roasted
    5150: ['Goose liver'], # Goose, liver, raw
    5151: ['Guinea hen', 'whole'], # Guinea hen, meat and skin, raw
    5152: ['Guinea hen', 'skinless'], # Guinea hen, meat only, raw
    5153: ['Pheasant', 'whole'], # Pheasant, raw, meat and skin
    5154: ['Pheasant', 'skinless'], # Pheasant, raw, meat only
    5155: [], # Pheasant, breast, meat only, raw
    5156: [], # Pheasant, leg, meat only, raw
    5157: ['Quail', 'whole'], # Quail, meat and skin, raw
    5158: ['Quail', 'skinless'], # Quail, meat only, raw
    5159: ['Quail breast'], # Quail, breast, meat only, raw
    5160: ['Squab', 'whole', 'Pigeon'], # Squab, (pigeon), meat and skin, raw
    5161: ['Squab', 'skinless', 'Pigeon'], # Squab, (pigeon), meat only, raw
    5162: [], # Squab, (pigeon), light meat without skin, raw
    5165: ['Turkey', 'whole'], # Turkey, whole, meat and skin, raw
    5166: [], # Turkey, whole, meat and skin, cooked, roasted
    5167: ['Turkey', 'skinless'], # Turkey, whole, meat only, raw
    5168: [], # Turkey, whole, meat only, cooked, roasted
    5169: ['Turkey skin'], # Turkey, whole, skin (light and dark), raw
    5170: [], # Turkey, whole, skin (light and dark), roasted
    5171: ['Turkey giblets'], # Turkey, whole, giblets, raw
    5172: [], # Turkey, whole, giblets, cooked, simmered
    5173: [], # Turkey, gizzard, all classes, raw
    5174: [], # Turkey, all classes, gizzard, cooked, simmered
    5175: ['Turkey heart'], # Turkey, all classes, heart, raw
    5176: [], # Turkey, all classes, heart, cooked, simmered
    5177: ['Turkey liver'], # Turkey, all classes, liver, raw
    5178: [], # Turkey, all classes, liver, cooked, simmered
    5179: ['Turkey neck'], # Turkey, whole, neck, meat only, raw
    5180: [], # Turkey, whole, neck, meat only, cooked, simmered
    5181: [], # Turkey, whole, light meat, meat and skin, raw
    5182: [], # Turkey, whole, light meat, meat and skin, cooked, roasted
    5183: [], # Turkey, dark meat, meat and skin, raw
    5184: [], # Turkey, whole, dark meat, meat and skin, cooked, roasted
    5185: [], # Turkey, whole, light meat, raw
    5186: [], # Turkey, all classes, light meat, cooked, roasted
    5187: [], # Turkey, whole, dark meat, meat only, raw
    5188: [], # Turkey, whole, dark meat, cooked, roasted
    5190: [], # Turkey, all classes, back, meat and skin, cooked, roasted
    5191: ['Turkey breast'], # Turkey, all classes, breast, meat and skin, raw
    5192: [], # Turkey, all classes, breast, meat and skin, cooked, roasted
    5193: ['Turkey leg'], # Turkey, all classes, leg, meat and skin, raw
    5194: [], # Turkey, all classes, leg, meat and skin, cooked, roasted
    5195: ['Turkey wing'], # Turkey, all classes, wing, meat and skin, raw
    5196: [], # Turkey, all classes, wing, meat and skin, cooked, roasted
    5200: [], # Turkey, fryer-roasters, meat and skin, cooked, roasted
    5215: ['Turkey back'], # Turkey, whole, back, meat only, raw
    5216: [], # Turkey, whole, back, meat only, cooked, roasted
    5219: [], # Turkey, whole, breast, meat only, raw
    5220: [], # Turkey, whole, breast, meat only, cooked, roasted
    5227: [], # Turkey, whole, wing, meat only, raw
    5228: [], # Turkey, whole, wing, meat only, cooked, roasted
    5236: [], # Turkey, young hen, skin only, cooked, roasted
    5277: [], # Chicken, canned, meat only, with broth
    5282: [], # Pate de foie gras, canned (goose liver pate), smoked
    5284: [], # Turkey, canned, meat only, with broth
    5285: [], # Turkey, diced, light and dark meat, seasoned
    5286: [], # Turkey and gravy, frozen
    5293: [], # Turkey breast, pre-basted, meat and skin, cooked, roasted
    5294: [], # Turkey thigh, pre-basted, meat and skin, cooked, roasted
    5295: [], # Turkey roast, boneless, frozen, seasoned, light and dark meat, raw
    5300: [], # Turkey sticks, breaded, battered, fried
    5301: [], # Poultry, mechanically deboned, from backs and necks with skin, raw
    5302: [], # Poultry, mechanically deboned, from backs and necks without skin, raw
    5303: [], # Poultry, mechanically deboned, from mature hens, raw
    5304: [], # Turkey, mechanically deboned, from turkey frames, raw
    5305: [], # Turkey, Ground, raw
    5306: [], # Turkey, Ground, cooked
    5307: [], # Chicken, cornish game hens, meat and skin, raw
    5308: [], # Chicken, cornish game hens, meat and skin, cooked, roasted
    5309: [], # Chicken, cornish game hens, meat only, raw
    5310: [], # Chicken, cornish game hens, meat only, cooked, roasted
    5311: [], # Chicken, canned, no broth
    5312: [], # Chicken, wing, frozen, glazed, barbecue flavored
    5313: [], # Chicken, wing, frozen, glazed, barbecue flavored, heated (microwave)
    5314: [], # Chicken, broilers or fryers, breast, skinless, boneless, meat only, with added solution, raw
    5315: [], # Duck, young duckling, domesticated, White Pekin, breast, meat and skin, boneless, cooked, roasted
    5316: [], # Duck, young duckling, domesticated, White Pekin, breast, meat only, boneless, cooked without skin, broiled
    5317: [], # Duck, young duckling, domesticated, White Pekin, leg, meat and skin, bone in, cooked, roasted
    5318: [], # Duck, young duckling, domesticated, White Pekin, leg, meat only, bone in, cooked without skin, braised
    5319: [], # Chicken, broiler, rotisserie, BBQ, drumstick, meat only
    5320: [], # Chicken, wing, frozen, glazed, barbecue flavored, heated (conventional oven)
    5323: [], # Chicken patty, frozen, uncooked
    5324: [], # Chicken patty, frozen, cooked
    5326: [], # Chicken breast tenders, breaded, cooked, microwaved
    5327: [], # Chicken breast tenders, breaded, uncooked
    5332: ['Chicken', 'ground'], # Chicken, ground, raw
    5333: [], # Chicken, ground, crumbles, cooked, pan-browned
    5334: [], # Chicken, broiler, rotisserie, BBQ, thigh, meat only
    5335: [], # Chicken, feet, boiled
    5339: [], # Chicken, broiler, rotisserie, BBQ, wing, meat only
    5341: [], # Chicken, broilers or fryers, rotisserie, original seasoning, back, meat only, cooked
    5342: [], # Chicken, broilers or fryers, rotisserie, original seasoning, breast, meat only, cooked
    5343: [], # Chicken, broilers or fryers, drumstick, rotisserie, original seasoning, meat only, cooked
    5344: [], # Chicken, broilers or fryers, rotisserie, original seasoning, skin only, cooked
    5345: [], # Chicken, broilers or fryers, rotisserie, original seasoning, thigh, meat only, cooked
    5346: [], # Chicken, broilers or fryers, rotisserie, original seasoning, wing, meat only, cooked
    5347: [], # Chicken, broilers or fryers, rotisserie, original seasoning, back, meat and skin, cooked
    5348: [], # Chicken, broilers or fryers, rotisserie, original seasoning, breast, meat and skin, cooked
    5349: [], # Chicken, broilers or fryers,  rotisserie, original seasoning, drumstick, meat and skin, cooked
    5351: [], # Chicken, broilers or fryers, rotisserie, original seasoning, thigh, meat and skin, cooked
    5352: [], # Chicken, broilers or fryers, rotisserie, original seasoning, wing, meat and skin, cooked
    5356: [], # Chicken, broiler, rotisserie, BBQ, skin
    5357: [], # Chicken, broiler, rotisserie, BBQ, back, meat and skin
    5358: [], # Chicken, broiler, rotisserie, BBQ, breast, meat and skin
    5359: [], # Chicken, broiler, rotisserie, BBQ, drumstick, meat and skin
    5361: [], # Chicken, broiler, rotisserie, BBQ, thigh, meat and skin
    5362: [], # Chicken, broiler, rotisserie, BBQ, wing, meat and skin
    5363: [], # Ruffed Grouse, breast meat, skinless, raw
    5621: ['Emu', 'ground'], # Emu, ground, raw
    5622: [], # Emu, ground, cooked, pan-broiled
    5623: ['Emu fan fillet'], # Emu, fan fillet, raw
    5624: [], # Emu, fan fillet, cooked, broiled
    5625: ['Emu flat fillet'], # Emu, flat fillet, raw
    5626: ['Emu full rump'], # Emu, full rump, raw
    5627: [], # Emu, full rump, cooked, broiled
    5628: ['Emu inside drum'], # Emu, inside drum, raw
    5629: [], # Emu, inside drums, cooked, broiled
    5630: ['Emu outside drum'], # Emu, outside drum, raw
    5631: ['Emu oyster'], # Emu, oyster, raw
    5632: [], # Emu, top loin, cooked, broiled
    5641: ['Ostrich', 'ground'], # Ostrich, ground, raw
    5642: [], # Ostrich, ground, cooked, pan-broiled
    5643: ['Ostrich fan'], # Ostrich, fan, raw
    5644: ['Ostrich inside leg'], # Ostrich, inside leg, raw
    5645: [], # Ostrich, inside leg, cooked
    5646: ['Ostrich inside strip'], # Ostrich, inside strip, raw
    5647: [], # Ostrich, inside strip, cooked
    5648: ['Ostrich outside leg'], # Ostrich, outside leg, raw
    5649: [], # Ostrich, outside strip, raw
    5650: [], # Ostrich, outside strip, cooked
    5651: ['Ostrich oyster'], # Ostrich, oyster, raw
    5652: [], # Ostrich, oyster, cooked
    5653: ['Ostrich round'], # Ostrich, round, raw
    5654: ['Ostrich tenderloin'], # Ostrich, tenderloin, raw
    5655: [], # Ostrich, tip trimmed, raw
    5656: [], # Ostrich, tip trimmed, cooked
    5657: ['Ostrich top loin'], # Ostrich, top loin, raw
    5658: [], # Ostrich, top loin, cooked
    5661: [], # Chicken, liver, all classes, cooked, pan-fried
    5662: [], # Turkey, ground, fat free, raw
    5663: [], # Turkey, ground, fat free, pan-broiled crumbles
    5664: [], # Turkey, ground, fat free, patties, broiled
    5665: [], # Turkey, ground, 93% lean, 7% fat, raw
    5666: [], # Turkey, ground, 93% lean, 7% fat, pan-broiled crumbles
    5667: [], # Turkey, ground, 93% lean, 7% fat, patties, broiled
    5668: [], # Turkey, ground, 85% lean, 15% fat, raw
    5669: [], # Turkey, ground, 85% lean, 15% fat, pan-broiled crumbles
    5670: [], # Turkey, ground, 85% lean, 15% fat, patties, broiled
    5671: [], # Chicken, broilers or fryers, dark meat, drumstick, meat only, cooked, braised
    5672: [], # Chicken, broilers or fryers, dark meat, thigh, meat only, cooked, braised
    5673: [], # Chicken, skin (drumsticks and thighs), cooked, braised
    5674: [], # Chicken, skin (drumsticks and thighs), raw
    5675: [], # Chicken, skin (drumsticks and thighs), cooked, roasted
    5676: [], # Chicken, broilers or fryers, dark meat, drumstick, meat and skin, cooked, braised
    5677: [], # Chicken, broilers or fryers, dark meat, thigh, meat and skin, cooked, braised
    5678: [], # Chicken, dark meat, drumstick, meat only, with added solution, raw
    5679: [], # Chicken, dark meat, drumstick, meat only, with added solution, cooked, roasted
    5680: [], # Chicken, dark meat, drumstick, meat only, with added solution, cooked, braised
    5681: [], # Chicken, dark meat, thigh, meat only, with added solution, cooked, braised
    5682: [], # Chicken, dark meat, thigh, meat only, with added solution, raw
    5683: [], # Chicken, dark meat, thigh, meat only, with added solution, cooked, roasted
    5684: [], # Chicken, skin (drumsticks and thighs), with added solution, cooked, braised
    5685: [], # Chicken, skin (drumsticks and thighs), with added solution, raw
    5686: [], # Chicken, skin (drumsticks and thighs), with added solution, cooked, roasted
    5687: [], # Chicken, dark meat, drumstick, meat and skin, with added solution, cooked, braised
    5688: [], # Chicken, dark meat, drumstick, meat and skin, with added solution, raw
    5689: [], # Chicken, dark meat, drumstick, meat and skin, with added solution, cooked, roasted
    5690: [], # Chicken, dark meat, thigh, meat and skin, with added solution, cooked, braised
    5691: [], # Chicken, dark meat, thigh, meat and skin, with added solution, raw
    5692: [], # Chicken, dark meat, thigh, meat and skin, with added solution, cooked, roasted
    5693: [], # Chicken, broiler, rotisserie, BBQ, back meat only
    5694: [], # Turkey, dark meat from whole, meat only, with added solution, raw
    5695: [], # Turkey, dark meat, meat only, with added solution, cooked, roasted
    5696: [], # Turkey from whole, light meat, meat only, with added solution, raw
    5697: [], # Turkey from whole, light meat, meat only, with added solution, cooked, roasted
    5698: [], # Turkey, skin from whole (light and dark), with added solution, raw
    5699: [], # Turkey, skin from whole, (light and dark), with added solution, roasted
    5700: [], # Turkey, dark meat from whole, meat and skin, with added solution, raw
    5701: [], # Turkey, dark meat from whole, meat and skin, with added solution, cooked, roasted
    5702: [], # Turkey from whole, light meat, meat and skin, with added solution, raw
    5703: [], # Turkey from whole, light meat, meat and skin, with added solution, cooked, roasted
    5704: [], # Turkey, whole, meat only, with added solution, raw
    5705: [], # Turkey, whole, meat only, with added solution, roasted
    5706: [], # Turkey, whole, meat and skin, with added solution, raw
    5707: [], # Turkey, whole, meat and skin, with added solution, roasted
    5708: [], # Turkey, retail parts, breast, meat only, with added solution, raw
    5709: [], # Turkey, retail parts, breast, meat only, with added solution, cooked, roasted
    5710: [], # Turkey, retail parts, breast, meat only, raw
    5711: [], # Turkey, retail parts, breast, meat only, cooked, roasted
    5712: [], # Turkey, retail parts, wing, meat only, raw
    5713: [], # Turkey, retail parts, wing, meat only, cooked, roasted
    5714: [], # Turkey, skin, from retail parts, from dark meat, raw
    5715: [], # Turkey, skin, from retail parts, from dark meat, cooked, roasted
    5716: [], # Turkey, retail parts, drumstick, meat only, raw
    5717: [], # Turkey, retail parts, thigh, meat only, raw
    5718: [], # Turkey, breast, from whole bird, meat only, with added solution, roasted
    5719: [], # Turkey, back, from whole bird, meat only, with added solution, raw
    5720: [], # Turkey, back, from whole bird, meat only, with added solution, roasted
    5721: [], # Turkey, breast, from whole bird, meat only, with added solution, raw
    5722: [], # Turkey, retail parts, thigh, meat only, cooked, roasted
    5723: [], # Turkey, retail parts, drumstick, meat only, cooked, roasted
    5724: [], # Turkey, drumstick, from whole bird, meat only, with added solution, raw
    5725: [], # Turkey, drumstick, from whole bird, meat only, with added solution, roasted
    5726: [], # Turkey, thigh, from whole bird, meat only, with added solution, raw
    5727: [], # Turkey, retail parts, breast, meat and skin, with added solution, raw
    5728: [], # Turkey, thigh, from whole bird, meat only, with added solution, roasted
    5729: [], # Turkey, wing, from whole bird, meat only, with added solution, raw
    5730: [], # Turkey, wing, from whole bird, meat only, with added solution, roasted
    5732: [], # Turkey, retail parts, breast, meat and skin, raw
    5733: [], # Turkey, retail parts, breast, meat and skin, cooked, roasted
    5734: [], # Turkey, retail parts, wing, meat and skin, raw
    5735: [], # Turkey, retail parts, wing, meat and skin, cooked, roasted
    5736: [], # Turkey, retail parts, drumstick, meat and skin, raw
    5737: [], # Turkey, retail parts, drumstick, meat and skin, cooked, roasted
    5738: ['Turkey drumstick'], # Turkey, drumstick, from whole bird, meat only, raw
    5739: [], # Turkey, drumstick, from whole bird, meat only, roasted
    5740: [], # Turkey, thigh, from whole bird, meat only, raw
    5741: [], # Turkey, thigh, from whole bird, meat only, roasted
    5742: [], # Turkey, retail parts, thigh, meat and skin, raw
    5743: [], # Turkey, retail parts, thigh, meat and skin, cooked, roasted
    5744: [], # Turkey, back, from whole bird, meat and skin, with added solution, raw
    5745: [], # Turkey, back, from whole bird, meat and skin, with added solution, roasted
    5746: [], # Chicken, broiler or fryers, breast, skinless, boneless, meat only, cooked, braised
    5747: [], # Chicken, broiler or fryers, breast, skinless, boneless, meat only, cooked, grilled
    5748: [], # Chicken, broiler or fryers, breast, skinless, boneless, meat only, with added solution, cooked, braised
    5749: [], # Chicken, broiler or fryers, breast, skinless, boneless, meat only, with added solution, cooked, grilled
    6001: [], # Soup, cream of asparagus, canned, condensed
    6002: [], # Soup, black bean, canned, condensed
    6004: [], # Soup, bean with pork, canned, condensed
    6006: [], # Soup, bean with frankfurters, canned, condensed
    6007: [], # Soup, bean with ham, canned, chunky, ready-to-serve
    6008: ['Beef broth'], # Soup, beef broth or bouillon canned, ready-to-serve
    6009: [], # Soup, beef noodle, canned, condensed
    6010: [], # Soup, cream of celery, canned, condensed
    6011: [], # Soup, cheese, canned, condensed
    6013: [], # Soup, chicken broth, canned, condensed
    6015: [], # Soup, chicken, canned, chunky, ready-to-serve
    6016: [], # Soup, cream of chicken, canned, condensed
    6017: [], # Soup, chicken gumbo, canned, condensed
    6018: [], # Soup, chunky chicken noodle, canned, ready-to-serve
    6019: [], # Soup, chicken noodle, canned, condensed
    6022: [], # Soup, chicken rice, canned, chunky, ready-to-serve
    6023: [], # Soup, chicken with rice, canned, condensed
    6024: [], # Soup, chicken and vegetable, canned, ready-to-serve
    6025: [], # Soup, chicken vegetable, canned, condensed
    6026: [], # Soup, chili beef, canned, condensed
    6027: [], # Soup, clam chowder, manhattan style, canned, chunky, ready-to-serve
    6028: [], # Soup, clam chowder, manhattan, canned, condensed
    6030: [], # Soup, clam chowder, new england, canned, condensed
    6032: [], # Soup, beef broth bouillon and consomme, canned, condensed
    6037: [], # Soup, lentil with ham, canned, ready-to-serve
    6039: [], # Soup, minestrone, canned, chunky, ready-to-serve
    6040: [], # Soup, minestrone, canned, condensed
    6042: [], # Soup, mushroom barley, canned, condensed
    6043: [], # Soup, cream of mushroom, canned, condensed
    6044: [], # Soup, mushroom with beef stock, canned, condensed
    6045: [], # Soup, onion, canned, condensed
    6046: [], # Soup, cream of onion, canned, condensed
    6048: [], # Soup, oyster stew, canned, condensed
    6049: [], # Soup, pea, green, canned, condensed
    6050: [], # Soup, pea, split with ham, canned, chunky, ready-to-serve
    6051: [], # Soup, pea, split with ham, canned, condensed
    6053: [], # Soup, cream of potato, canned, condensed
    6056: [], # Soup, cream of shrimp, canned, condensed
    6061: [], # Soup, tomato beef with noodle, canned, condensed
    6062: [], # CAMPBELL'S, Chicken Noodle Soup, condensed
    6063: [], # Soup, tomato rice, canned, condensed
    6064: [], # Soup, turkey, chunky, canned, ready-to-serve
    6067: [], # Soup, chunky vegetable, canned, ready-to-serve
    6068: [], # Soup, vegetarian vegetable, canned, condensed
    6070: [], # Soup, chunky beef, canned, ready-to-serve
    6071: [], # Soup, vegetable beef, canned, condensed
    6072: [], # Soup, vegetable with beef broth, canned, condensed
    6075: [], # Soup, beef broth or bouillon, powder, dry
    6076: ['Beef broth cube'], # Soup, beef broth, cubed, dry
    6080: [], # Soup, chicken broth or bouillon, dry
    6081: ['Chicken broth cube'], # Soup, chicken broth cubes, dry
    6094: [], # Soup, onion, dry, mix
    6101: [], # Soup, cream of vegetable, dry, powder
    6112: [], # Sauce, teriyaki, ready-to-serve
    6114: [], # Gravy, au jus, canned
    6115: [], # Gravy, au jus, dry
    6116: ['Beef gravy'], # Gravy, beef, canned, ready-to-serve
    6118: ['Brown gravy'], # Gravy, brown, dry
    6119: ['Chicken gravy'], # Gravy, chicken, canned or bottled, ready-to-serve
    6120: ['Chicken gravy', 'dry'], # Gravy, chicken, dry
    6121: [], # Gravy, mushroom, canned
    6122: [], # Gravy, mushroom, dry, powder
    6123: [], # Gravy, onion, dry, mix
    6124: [], # Gravy, pork, dry, powder
    6125: [], # Gravy, turkey, canned, ready-to-serve
    6126: [], # Gravy, turkey, dry
    6127: [], # Gravy, unspecified type, dry
    6128: [], # Soup, chicken noodle, dry, mix
    6142: [], # Sauce, sofrito, prepared from recipe
    6147: [], # Soup, beef mushroom, canned, condensed
    6149: [], # Soup, chicken mushroom, canned, condensed
    6150: ['Barbecue sauce', '', 'BBQ Sauce'], # Sauce, barbecue
    6151: ['Plum sauce'], # Sauce, plum, ready-to-serve
    6152: ['Pizza sauce'], # Sauce, pizza, canned, ready-to-serve
    6158: [], # Soup, tomato bisque, canned, condensed
    6159: [], # Soup, tomato, canned, condensed
    6164: ['Salsa sauce'], # Sauce, salsa, ready-to-serve
    6166: [], # Sauce, homemade, white, medium
    6167: [], # Sauce, homemade, white, thick
    6168: [], # Sauce, ready-to-serve, pepper or hot
    6169: ['Tabasco sauce'], # Sauce, ready-to-serve, pepper, TABASCO
    6170: ["Beef stock"], # Soup, stock, beef, home-prepared
    6172: ["Chicken stock"], # Soup, stock, chicken, home-prepared
    6174: ["Fish stock"], # Soup, stock, fish, home-prepared
    6175: ['Hoisin sauce'], # Sauce, hoisin, ready-to-serve
    6176: ['Oyster sauce'], # Sauce, oyster, ready-to-serve
    6177: [], # Soup, minestrone, canned, reduced sodium, ready-to-serve
    6179: ['Fish sauce'], # Sauce, fish, ready-to-serve
    6180: [], # Soup, shark fin, restaurant-prepared
    6182: [], # Soup, cream of mushroom, canned, condensed, reduced sodium
    6183: [], # Soup, chicken broth, less/reduced sodium, ready to serve
    6188: [], # Soup, beef broth, less/reduced sodium, ready to serve
    6189: ['Teriyaki sauce'], # Sauce, teriyaki, ready-to-serve, reduced sodium
    6190: [], # Soup, bean & ham, canned, reduced sodium, prepared with water or ready-to-serve
    6192: [], # Split pea soup, canned, reduced sodium, prepared with water or ready-to serve
    6193: [], # Split pea with ham soup, canned, reduced sodium, prepared with water or ready-to-serve
    6194: ['Chicken broth'], # Soup, chicken broth, ready-to-serve
    6201: [], # Soup, cream of asparagus, canned, prepared with equal volume milk
    6208: [], # Soup, chicken vegetable with potato and cheese, chunky, ready-to-serve
    6210: [], # Soup, cream of celery, canned, prepared with equal volume milk
    6211: [], # Soup, cheese, canned, prepared with equal volume milk
    6216: [], # Soup, cream of chicken, canned, prepared with equal volume milk
    6217: [], # Soup, vegetable, canned, low sodium, condensed
    6230: [], # Soup, clam chowder, new england, canned, prepared with equal volume low fat (2%) milk
    6243: [], # Soup, cream of mushroom, canned, prepared with equal volume low fat (2%) milk
    6246: [], # Soup, cream of onion, canned, prepared with equal volume milk
    6248: [], # Soup, oyster stew, canned, prepared with equal volume milk
    6249: [], # Soup, pea, green, canned, prepared with equal volume milk
    6253: [], # Soup, cream of potato, canned, prepared with equal volume milk
    6256: [], # Soup, cream of shrimp, canned, prepared with equal volume low fat (2%) milk
    6264: [], # Sauce, white, thin, prepared-from-recipe, with butter
    6285: ['Sweet and sour sauce'], # Sauce, sweet and sour, prepared-from-recipe
    6307: [], # Sauce, barbecue, KRAFT, original
    6314: [], # Soup, HEALTHY CHOICE Chicken Noodle Soup, canned
    6315: [], # Soup, HEALTHY CHOICE Chicken and Rice Soup, canned
    6316: [], # Soup, HEALTHY CHOICE Garden Vegetable Soup, canned
    6338: [], # CAMPBELL'S, Cream of Mushroom Soup, condensed
    6358: [], # Soup, tomato bisque, canned, prepared with equal volume milk
    6359: [], # Soup, tomato, canned, prepared with equal volume low fat (2%) milk
    6377: [], # CAMPBELL'S, Tomato Soup, condensed
    6395: [], # CAMPBELL'S CHUNKY, Classic Chicken Noodle Soup
    6401: [], # Soup, cream of asparagus, canned, prepared with equal volume water
    6402: [], # Soup, black bean, canned, prepared with equal volume water
    6404: [], # Soup, bean with pork, canned, prepared with equal volume water
    6406: [], # Soup, bean with frankfurters, canned, prepared with equal volume water
    6409: [], # Soup, beef noodle, canned, prepared with equal volume water
    6410: [], # Soup, cream of celery, canned, prepared with equal volume water
    6411: [], # Soup, cheese, canned, prepared with equal volume water
    6413: [], # Soup, chicken broth, canned, prepared with equal volume water
    6415: [], # CAMPBELL'S CHUNKY, Hearty Beef Barley Soup
    6416: [], # Soup, cream of chicken, canned, prepared with equal volume water
    6417: [], # Soup, chicken gumbo, canned, prepared with equal volume water
    6419: [], # Soup, chicken noodle, canned, prepared with equal volume water
    6423: [], # Soup, chicken with rice, canned, prepared with equal volume water
    6426: [], # Soup, chili beef, canned, prepared with equal volume water
    6428: [], # Soup, clam chowder, manhattan, canned, prepared with equal volume water
    6430: [], # Soup, clam chowder, new england, canned, prepared with equal volume water
    6431: [], # CAMPBELL'S CHUNKY, New England Clam Chowder
    6432: [], # Soup, beef broth, bouillon, consomme, prepared with equal volume water
    6434: [], # CAMPBELL'S CHUNKY, Old Fashioned Vegetable Beef Soup
    6440: [], # Soup, minestrone, canned, prepared with equal volume water
    6442: [], # Soup, mushroom barley, canned, prepared with equal volume water
    6443: [], # Soup, cream of mushroom, canned, prepared with equal volume water
    6444: [], # Soup, mushroom with beef stock, canned, prepared with equal volume water
    6446: [], # Soup, cream of onion, canned, prepared with equal volume water
    6448: [], # Soup, oyster stew, canned, prepared with equal volume water
    6449: [], # Soup, pea, green, canned, prepared with equal volume water
    6451: [], # Soup, pea, split with ham, canned, prepared with equal volume water
    6453: [], # Soup, cream of potato, canned, prepared with equal volume water
    6456: [], # Soup, cream of shrimp, canned, prepared with equal volume water
    6461: [], # Soup, tomato beef with noodle, canned, prepared with equal volume water
    6463: [], # Soup, tomato rice, canned, prepared with equal volume water
    6465: [], # Soup, turkey noodle, canned, prepared with equal volume water
    6466: [], # Soup, turkey vegetable, canned, prepared with equal volume water
    6468: [], # Soup, vegetarian vegetable, canned, prepared with equal volume water
    6471: [], # Soup, vegetable beef, canned, prepared with equal volume water
    6472: [], # Soup, vegetable with beef broth, canned, prepared with equal volume water
    6475: [], # Soup, beef broth or bouillon, powder, prepared with water
    6476: [], # Soup, beef broth, cubed, prepared with water
    6480: [], # Soup, chicken broth or bouillon, dry, prepared with water
    6481: [], # Soup, chicken broth cubes, dry, prepared with water
    6483: [], # Soup, cream of chicken, dry, mix, prepared with water
    6494: [], # Soup, onion, dry, mix, prepared with water
    6498: [], # Soup, tomato, dry, mix, prepared with water
    6528: [], # Soup, chicken noodle, dry, mix, prepared with water
    6547: [], # Soup, beef mushroom, canned, prepared with equal volume water
    6549: [], # Soup, chicken mushroom, canned, prepared with equal volume water
    6558: [], # Soup, tomato bisque, canned, prepared with equal volume water
    6559: [], # Soup, tomato, canned, prepared with equal volume water, commercial
    6583: [], # Soup, ramen noodle, any flavor, dry
    6584: [], # Soup, broccoli cheese, canned, condensed, commercial
    6611: [], # Soup, SWANSON, beef broth, lower sodium
    6615: [], # Soup, SWANSON, vegetable broth
    6618: [], # Sauce, peanut, made from coconut, water, sugar, peanuts
    6619: [], # SMART SOUP, Santa Fe Corn Chowder
    6620: [], # SMART SOUP, French Lentil
    6621: [], # SMART SOUP, Greek Minestrone
    6622: [], # SMART SOUP, Indian Bean Masala
    6623: [], # SMART SOUP, Moroccan Chick Pea
    6624: [], # SMART SOUP, Thai Coconut Curry
    6625: [], # SMART SOUP, Vietnamese Carrot Lemongrass
    6626: ['Pesto sauce'], # Sauce, pesto, ready-to-serve, refrigerated
    6627: [], # Sauce, pesto, ready-to-serve, shelf stable
    6628: [], # Sauce, pesto, BUITONI, pesto with basil, ready-to-serve, refrigerated
    6629: [], # Sauce, pesto, CLASSICO, basil pesto, ready-to-serve
    6630: [], # Sauce, pesto, MEZZETTA, NAPA VALLEY BISTRO, basil pesto, ready-to-serve
    6631: ['Sriracha sauce'], # Sauce, hot chile, sriracha
    6632: [], # Sauce, hot chile, sriracha, CHA! BY TEXAS PETE
    6633: [], # Sauce, hot chile, sriracha, TUONG OT SRIRACHA
    6700: ['Vegetable broth'], # Soup, vegetable broth, ready to serve
    6720: [], # Sauce, cheese sauce mix, dry
    6725: [], # Soup, chicken corn chowder, chunky, ready-to-serve, single brand
    6731: [], # Soup, bean with bacon, condensed, single brand
    6742: [], # Soup, vegetable beef, microwavable, ready-to-serve, single brand
    6749: [], # Soup, beef and vegetables, canned, ready-to-serve
    6930: ['Cheese sauce'], # Sauce, cheese, ready-to-serve
    6931: ['Spaghetti sauce'], # Sauce, pasta, spaghetti/marinara, ready-to-serve
    6955: [], # Soup, cream of chicken, canned, condensed, reduced sodium
    6956: [], # Soup, tomato, canned, condensed, reduced sodium
    6957: [], # Gravy, brown instant, dry
    6958: [], # Gravy, instant beef, dry
    6959: [], # Gravy, instant turkey, dry
    6960: [], # Sauce, alfredo mix, dry
    6961: [], # Sauce, peppers, hot, chili, mature red, canned
    6962: [], # Sauce, chili, peppers, hot, immature green, canned
    6963: ['Fish broth'], # Fish broth
    6964: [], # Soup, tomato, low sodium, with water
    6965: [], # Soup, pea, low sodium, prepared with equal volume water
    6966: [], # Soup, chicken noodle, low sodium, canned, prepared with equal volume water
    6967: [], # Soup, vegetable soup, condensed, low sodium, prepared with equal volume water
    6968: [], # Soup, cream of mushroom, low sodium, ready-to-serve, canned
    6969: [], # Potato soup, instant, dry mix
    6970: [], # Soup, chicken broth, low sodium, canned
    6971: ['Worcestershire sauce'], # Sauce, worcestershire
    6972: ['Tomato chili sauce'], # Sauce, tomato chili sauce, bottled, with salt
    6974: [], # Soup, vegetable chicken, canned, prepared with water, low sodium
    6976: [], # Sauce, pasta, spaghetti/marinara, ready-to-serve, low sodium
    6977: [], # Gravy, meat or poultry, low sodium, prepared
    6978: [], # Soup, beef and mushroom, low sodium, chunk style
    6980: [], # Soup, beef stroganoff, canned, chunky style, ready-to-serve
    6981: [], # Soup, bouillon cubes and granules, low sodium, dry
    6982: [], # Soup, ramen noodle, beef flavor, dry
    6983: [], # Soup, ramen noodle, chicken flavor, dry
    6985: [], # Gravy, HEINZ Home Style, savory beef
    6999: [], # Gravy, CAMPBELL'S, chicken
    7001: ['Barbecue pork loaf'], # Barbecue loaf, pork, beef
    7002: ['Beerwurst sausage', '', 'Beer salami'], # Beerwurst, beer salami, pork and beef
    7003: [], # Beerwurst, beer salami, pork
    7004: ['Berliner sausage'], # Sausage, Berliner, pork, beef
    7005: ['Blood sausage'], # Blood sausage
    7006: ['Bockwurst sausage'], # Bockwurst, pork, veal, raw
    7007: ['Bologna sausage', 'beef'], # Bologna, beef
    7008: ['Bologna sausage', 'beef pork'], # Bologna, beef and pork
    7010: ['Bologna sausage', 'pork'], # Bologna, pork
    7011: ['Bologna sausage', 'turkey'], # Bologna, turkey
    7013: ['Bratwurst sausage'], # Bratwurst, pork, cooked
    7014: [], # Braunschweiger (a liver sausage), pork
    7015: [], # Bratwurst, pork, beef, link
    7016: [], # Cheesefurter, cheese smokie, pork, beef
    7018: [], # Chicken spread
    7019: ['Chorizo sausage'], # Sausage, pork, chorizo, link or ground, raw
    7020: [], # Corned beef loaf, jellied
    7021: [], # Dutch brand loaf, chicken, pork and beef
    7022: ['Frankfurter sausage', 'beef'], # Frankfurter, beef, unheated
    7024: ['Frankfurter sausage', 'chicken'], # Frankfurter, chicken
    7025: ['Frankfurter sausage', 'turkey'], # Frankfurter, turkey
    7026: ['Ham', 'chopped canned'], # Ham, chopped, canned
    7027: ['Ham'], # Ham, chopped, not canned
    7028: [], # Ham, sliced, pre-packaged, deli meat (96%fat free, water added)
    7029: ['Ham', 'sliced'], # Ham, sliced, regular (approximately 11% fat)
    7030: ['Ham', 'minced'], # Ham, minced
    7031: [], # Ham salad spread
    7032: [], # Ham and cheese loaf or roll
    7033: [], # Ham and cheese spread
    7034: [], # Headcheese, pork
    7036: ['Italian sausage'], # Sausage, Italian, pork, mild, raw
    7038: ['Knackwurst sausage'], # Knackwurst, knockwurst, pork, beef
    7039: [], # Lebanon bologna, beef
    7040: [], # Liver cheese, pork
    7041: ['Liver sausage', 'pork', 'Liverwurst'], # Liver sausage, liverwurst, pork
    7043: [], # Roast beef, deli style, prepackaged, sliced
    7045: [], # Luncheon meat, pork, canned
    7046: [], # Turkey breast, low salt, prepackaged or deli, luncheon meat
    7050: ['Mortadella', 'beef pork'], # Mortadella, beef, pork
    7051: [], # Olive loaf, pork
    7052: [], # Pastrami, turkey
    7053: ['Chicken liver pate'], # Pate, chicken liver, canned
    7054: ['Goose liver pate'], # Pate, goose liver, smoked, canned
    7055: ['Liver pate'], # Pate, liver, not specified, canned
    7056: [], # Peppered loaf, pork, beef
    7057: ['Pepperoni'], # Pepperoni, beef and pork, sliced
    7058: [], # Pickle and pimiento loaf, pork
    7059: ['Polish sausage'], # Polish sausage, pork
    7060: ['Luxury loaf'], # Luxury loaf, pork
    7061: [], # Mother's loaf, pork
    7062: [], # Picnic loaf, pork, beef
    7063: ['Pork sausage'], # Pork sausage, link/patty, unprepared
    7064: [], # Pork sausage, link/patty, cooked, pan-fried
    7065: [], # Sausage, pork and beef, fresh, cooked
    7066: [], # Sausage, turkey, reduced fat, brown and serve, cooked
    7067: [], # Poultry salad sandwich spread
    7068: ['Salami', 'cooked beef'], # Salami, cooked, beef
    7069: ['Salami', 'cooked pork'], # Salami, cooked, beef and pork
    7070: ['Salami', 'turkey'], # Salami, cooked, turkey
    7071: ['Salami', 'dry hard'], # Salami, dry or hard, pork
    7072: [], # Salami, dry or hard, pork, beef
    7073: [], # Sandwich spread, pork, beef
    7074: [], # Sausage, smoked link sausage, pork
    7075: ['Smoked link sausage'], # Sausage, smoked link sausage, pork and beef
    7077: [], # Sausage, smoked link sausage, pork and beef (nonfat dry milk added)
    7078: [], # Thuringer, cervelat, summer sausage, beef, pork
    7081: [], # Turkey breast, sliced, prepackaged
    7083: [], # Sausage, Vienna, canned, chicken, beef, pork
    7088: [], # Honey roll sausage, beef
    7089: [], # Sausage, Italian, pork, mild, cooked, pan-fried
    7090: ['Luncheon sausage'], # Luncheon sausage, pork and beef
    7091: [], # Sausage, New england brand, pork, beef
    7201: [], # Oscar Mayer, Bologna (beef)
    7207: [], # Oscar Mayer, Braunschweiger Liver Sausage (sliced)
    7209: [], # Oscar Mayer, Chicken Breast (honey glazed)
    7212: [], # Oscar Mayer, Ham (chopped with natural juice)
    7230: [], # Oscar Mayer, Salami (hard)
    7236: [], # Oscar Mayer, Smokies Sausage Little Cheese (pork, turkey)
    7241: [], # Oscar Mayer, Wieners (beef franks)
    7254: ['Turkey bacon'], # Bacon, turkey, unprepared
    7278: [], # Hormel Pillow Pak Sliced Turkey Pepperoni
    7900: [], # Sausage, turkey, pork, and beef, low fat, smoked
    7905: [], # Frankfurter, beef, pork, and turkey, fat free
    7906: [], # Luncheon meat, pork, ham, and chicken, minced, canned, reduced sodium, added ascorbic acid, includes SPAM, 25% less sodium
    7908: [], # Luncheon meat, pork with ham, minced, canned, includes Spam (Hormel)
    7909: [], # Luncheon meat, pork and chicken, minced, canned, includes Spam Lite
    7910: [], # Bratwurst, veal, cooked
    7911: [], # Liverwurst spread
    7912: [], # Roast beef spread
    7913: [], # Salami, pork, beef, less sodium
    7914: [], # Sausage, Italian, sweet, links
    7915: [], # Sausage, Polish, beef with chicken, hot
    7916: [], # Sausage, Polish, pork and beef, smoked
    7917: [], # Sausage, pork and beef, with cheddar cheese, smoked
    7918: [], # Sausage, summer, pork and beef, sticks, with cheddar cheese
    7919: [], # Sausage, turkey, breakfast links, mild, raw
    7920: [], # Swisswurst, pork and beef, with swiss cheese, smoked
    7921: [], # Bacon and beef sticks
    7922: [], # Bratwurst, beef and pork, smoked
    7923: [], # Bratwurst, chicken, cooked
    7924: [], # Bratwurst, pork, beef and turkey, lite, smoked
    7925: [], # Pastrami, beef, 98% fat-free
    7926: ['Salami'], # Salami, Italian, pork
    7927: [], # Sausage, Italian, turkey, smoked
    7928: [], # Sausage, chicken, beef, pork, skinless, smoked
    7929: [], # Sausage, turkey, hot, smoked
    7930: [], # Yachtwurst, with pistachio nuts, cooked
    7931: [], # Beerwurst, pork and beef
    7932: [], # Chicken breast, fat-free, mesquite flavor, sliced
    7933: [], # Chicken breast, oven-roasted, fat-free, sliced
    7934: ['Kielbasa'], # Kielbasa, Polish, turkey and beef, smoked
    7935: [], # Chicken breast, roll, oven-roasted
    7936: [], # Bologna, pork and turkey, lite
    7937: [], # Bologna, pork, turkey and beef
    7938: [], # Ham, honey, smoked, cooked
    7939: [], # Frankfurter, pork
    7940: [], # Macaroni and cheese loaf, chicken, pork and beef
    7941: [], # Salami, Italian, pork and beef, dry, sliced, 50% less sodium
    7942: [], # Pate, truffle flavor
    7943: [], # Turkey, breast, smoked, lemon pepper flavor, 97% fat-free
    7944: [], # Turkey, white, rotisserie, deli cut
    7945: [], # Frankfurter, beef, heated
    7949: [], # Frankfurter, meat, heated
    7950: [], # Frankfurter, meat
    7951: [], # Scrapple, pork
    7952: [], # Bologna, chicken, turkey, pork
    7953: [], # Pork sausage, link/patty, fully cooked, microwaved
    7954: [], # Sausage, breakfast sausage, beef, pre-cooked, unprepared
    7955: [], # Sausage, turkey, fresh, raw
    7956: [], # Sausage, beef, fresh, cooked
    7957: [], # Sausage, pork and turkey, pre-cooked
    7958: [], # Sausage, turkey, fresh, cooked
    7959: [], # Bologna, chicken, pork, beef
    7960: [], # Bologna, chicken, pork
    7961: [], # Chicken breast, deli, rotisserie seasoned, sliced, prepackaged
    7962: [], # Frankfurter, meat and poultry, unheated
    7963: [], # Frankfurter, meat and poultry, cooked, boiled
    7964: [], # Frankfurter, meat and poultry, cooked, grilled
    7965: [], # Pork sausage, link/patty, reduced fat, unprepared
    7966: [], # Pork sausage, link/patty, reduced fat, cooked, pan-fried
    7967: [], # Pork sausage, link/patty, fully cooked, unheated
    7968: [], # Kielbasa, fully cooked, grilled
    7969: [], # Kielbasa, fully cooked, pan-fried
    7970: [], # Kielbasa, fully cooked, unheated
    7971: [], # Bologna, meat and poultry
    7972: [], # Meatballs, frozen, Italian style
    7973: [], # Bacon, turkey, microwaved
    7974: [], # Bacon, turkey, low sodium
    7976: [], # Sausage, chicken or turkey, Italian style,  lower sodium
    7977: [], # Ham, smoked, extra lean, low sodium
    7978: [], # Pork sausage, reduced sodium, cooked
    7979: [], # Sausage, pork, turkey, and beef, reduced sodium
    8002: [], # Cereals ready-to-eat, POST, ALPHA-BITS
    8010: [], # Cereals ready-to-eat, QUAKER, CAP'N CRUNCH
    8011: [], # Cereals ready-to-eat, QUAKER, CAP'N CRUNCH with CRUNCHBERRIES
    8012: [], # Cereals ready-to-eat, QUAKER, CAP'N CRUNCH'S PEANUT BUTTER CRUNCH
    8013: [], # Cereals ready-to-eat, GENERAL MILLS, CHEERIOS
    8015: [], # Cereals ready-to-eat, POST, COCOA PEBBLES
    8018: [], # Cereals ready-to-eat, QUAKER, QUAKER CRUNCHY BRAN
    8025: [], # Cereals ready-to-eat, RALSTON CRISP RICE
    8029: [], # Cereals ready-to-eat, POST Bran Flakes
    8034: [], # Cereals ready-to-eat, POST, FRUITY PEBBLES
    8037: ['Granola cereal'], # Cereals ready-to-eat, granola, homemade
    8038: [], # Cereals ready-to-eat, POST, GRAPE-NUTS Cereal
    8039: [], # Cereals ready-to-eat, POST, GRAPE-NUTS Flakes
    8046: ['Honeycomb cereal'], # Cereals ready-to-eat, POST, Honeycomb Cereal
    8047: [], # Cereals ready-to-eat, QUAKER, KING VITAMAN
    8049: [], # Cereals ready-to-eat, QUAKER, QUAKER OAT LIFE, plain
    8054: [], # Cereals ready-to-eat, QUAKER, 100% Natural Granola, Oats, Wheat and Honey
    8059: [], # Cereals ready-to-eat, QUAKER, SWEET CRUNCH/QUISP
    8061: [], # Cereals ready-to-eat, POST Raisin Bran Cereal
    8066: [], # Cereals ready-to-eat, QUAKER, QUAKER Puffed Rice
    8073: [], # Cereals ready-to-eat, POST, GOLDEN CRISP
    8074: [], # Cereals ready-to-eat, RALSTON TASTEEOS
    8081: [], # Cereals ready-to-eat, POST, Honey Nut Shredded Wheat
    8083: [], # Cereals ready-to-eat, MALT-O-MEAL, CORN BURSTS
    8084: ['Wheat germ cereal'], # Cereals ready-to-eat, wheat germ, toasted, plain
    8085: [], # Cereals ready-to-eat, SUN COUNTRY, KRETSCHMER Honey Crunch Wheat Germ
    8090: [], # Cereals, corn grits, white, regular and quick, enriched, dry
    8091: [], # Cereals, corn grits, white, regular and quick, enriched, cooked with water, without salt
    8092: [], # Cereals, QUAKER, corn grits, instant, plain, dry
    8093: [], # Cereals, QUAKER, corn grits, instant, plain, prepared (microwaved or boiling water added), without salt
    8094: [], # Cereals, QUAKER, corn grits, instant, cheddar cheese flavor, dry
    8096: [], # Cereals, QUAKER, Instant Grits, Country Bacon flavor, dry
    8100: [], # Cereals, CREAM OF RICE, dry
    8102: [], # Cereals, CREAM OF WHEAT, regular, 10 minute cooking, dry
    8103: [], # Cereals, CREAM OF WHEAT, regular (10 minute), cooked with water, without salt
    8104: [], # Cereals, farina, enriched, assorted brands including CREAM OF WHEAT, quick (1-3 minutes), dry
    8105: [], # Cereals, farina, enriched, assorted brands including CREAM OF WHEAT, quick (1-3 minutes), cooked with water, without salt
    8106: [], # Cereals, CREAM OF WHEAT, instant, dry
    8107: [], # Cereals, CREAM OF WHEAT, instant, prepared with water, without salt
    8116: [], # Cereals, MALT-O-MEAL, original, plain, dry
    8120: ['Oat cereal'], # Cereals, oats, regular and quick, not fortified, dry
    8121: [], # Cereals, oats, regular and quick, unenriched, cooked with water (includes boiling and microwaving), without salt
    8122: [], # Cereals, oats, instant, fortified, plain, dry
    8123: [], # Cereals, oats, instant, fortified, plain, prepared with water (boiling water added or microwaved)
    8124: [], # Cereals, QUAKER, Instant Oatmeal, apples and cinnamon, dry
    8128: [], # Cereals, oats, instant, fortified, with cinnamon and spice, dry
    8129: [], # Cereals, oats, instant, fortified, with cinnamon and spice, prepared with water
    8130: [], # Cereals, QUAKER, Instant Oatmeal, maple and brown sugar, dry
    8133: [], # Cereals, oats, instant, fortified, with raisins and spice, prepared with water
    8138: [], # Cereals ready-to-eat, MALT-O-MEAL, MARSHMALLOW MATEYS
    8142: [], # Cereals, WHEATENA, dry
    8143: [], # Cereals, WHEATENA, cooked with water
    8144: [], # Cereals, whole wheat hot natural cereal, dry
    8145: [], # Cereals, whole wheat hot natural cereal, cooked with water, without salt
    8146: [], # Cereals ready-to-eat, QUAKER, QUAKER Puffed Wheat
    8147: [], # Cereals ready-to-eat, POST, Shredded Wheat, original big biscuit
    8148: [], # Cereals ready-to-eat, POST, Shredded Wheat, original spoon-size
    8156: [], # Cereals ready-to-eat, rice, puffed, fortified
    8157: [], # Cereals ready-to-eat, wheat, puffed, fortified
    8160: [], # Cereals, corn grits, yellow, regular and quick, unenriched, dry
    8161: [], # Cereals, corn grits, white, regular and quick, enriched, cooked with water, with salt
    8164: [], # Cereals, corn grits, yellow, regular and quick, enriched, cooked with water, without salt
    8165: [], # Cereals, corn grits, yellow, regular, quick, enriched, cooked with water, with salt
    8168: [], # Cereals, CREAM OF RICE, cooked with water, with salt
    8169: [], # Cereals, CREAM OF WHEAT, regular (10 minute), cooked with water, with salt
    8172: [], # Cereals, farina, unenriched, dry
    8173: [], # Cereals, farina, enriched, cooked with water, with salt
    8177: [], # Cereals, MALT-O-MEAL, chocolate, dry
    8180: [], # Cereals, oats, regular and quick and instant, unenriched, cooked with water (includes boiling and microwaving), with salt
    8182: [], # Cereals, WHEATENA, cooked with water, with salt
    8183: [], # Cereals, whole wheat hot natural cereal, cooked with water, with salt
    8191: [], # Cereals ready-to-eat, POST, Shredded Wheat, lightly frosted, spoon-size
    8192: [], # Cereals ready-to-eat, POST SELECTS Blueberry Morning
    8200: [], # Cereals, QUAKER, QUAKER MultiGrain Oatmeal, dry
    8204: [], # Cereals ready-to-eat, chocolate-flavored frosted puffed corn
    8206: [], # Cereals ready-to-eat, MALT-O-MEAL, COCO-ROOS
    8210: [], # Cereals ready-to-eat, QUAKER, QUAKER OAT CINNAMON LIFE
    8211: [], # Cereals ready-to-eat, QUAKER, HONEY GRAHAM OH!S
    8214: [], # Cereals ready-to-eat, QUAKER, Oatmeal Squares
    8215: [], # Cereals ready-to-eat, QUAKER, Oatmeal Squares, cinnamon
    8216: [], # Cereals ready-to-eat, QUAKER, Toasted Multigrain Crisps
    8218: [], # Cereals ready-to-eat, QUAKER, QUAKER 100% Natural Granola with Oats, Wheat, Honey, and Raisins
    8220: [], # Cereals ready-to-eat, QUAKER, Low Fat 100% Natural Granola with Raisins
    8221: [], # Cereals, QUAKER, Instant Grits, Butter flavor, dry
    8225: [], # Cereals, QUAKER, Instant Oatmeal, fruit and cream variety, dry
    8228: [], # Cereals, QUAKER, Instant Oatmeal, raisins, dates and walnuts, dry
    8231: [], # Cereals, QUAKER, Oat Bran, QUAKER/MOTHER'S Oat Bran, dry
    8236: [], # Cereals, QUAKER, Oat Bran, QUAKER/MOTHER'S Oat Bran, prepared with water, no salt
    8240: [], # Cereals, Oat Bran, QUAKER, QUAKER/MOTHER'S Oat Bran, prepared with water, salt
    8249: [], # Cereals, QUAKER, QUAKER MultiGrain Oatmeal, prepared with water, no salt
    8252: [], # Cereals, QUAKER, QUAKER MultiGrain Oatmeal, prepared with water, salt
    8290: [], # Cereals ready-to-eat, HEALTH VALLEY, FIBER 7 Flakes
    8305: [], # Cereals ready-to-eat, Post, Waffle Crisp
    8314: [], # Cereals, QUAKER, hominy grits, white, quick, dry
    8316: [], # Cereals, QUAKER, hominy grits, white, regular, dry
    8346: [], # Cereals ready-to-eat, MALT-O-MEAL, COLOSSAL CRUNCH
    8347: [], # Cereals ready-to-eat, MALT-O-MEAL, BERRY COLOSSAL CRUNCH
    8348: [], # Cereals ready-to-eat, MALT-O-MEAL, Crispy Rice
    8349: [], # Cereals ready-to-eat, MALT-O-MEAL, TOOTIE FRUITIES
    8351: [], # Cereals ready-to-eat, QUAKER, MOTHER'S PEANUT BUTTER BUMPERS Cereal
    8352: [], # Cereals ready-to-eat, QUAKER, MOTHER'S Toasted Oat Bran cereal
    8353: [], # Cereals ready-to-eat, QUAKER, MOTHER'S Cinnamon Oat Crunch
    8354: [], # Cereals ready-to-eat, QUAKER, MOTHER'S GRAHAM BUMPERS
    8355: [], # Cereals ready-to-eat, QUAKER, MOTHER'S COCOA BUMPERS
    8363: [], # Cereals ready-to-eat, SUN COUNTRY, KRETSCHMER Toasted Wheat Bran
    8365: [], # Cereals ready-to-eat, QUAKER, Shredded Wheat, bagged cereal
    8366: [], # Cereals ready-to-eat, SUN COUNTRY, KRETSCHMER Wheat Germ, Regular
    8402: [], # Cereals, QUAKER, Quick Oats, Dry
    8409: [], # Cereals ready-to-eat, MALT-O-MEAL, Frosted Flakes
    8410: [], # Cereals, QUAKER, Instant Oatmeal, Cinnamon-Spice, dry
    8411: [], # Cereals, QUAKER, Instant Oatmeal, DINOSAUR EGGS, Brown Sugar, dry
    8417: [], # Cereals, QUAKER, Instant Oatmeal, Banana Bread, dry
    8435: [], # Cereals ready-to-eat, UNCLE SAM CEREAL
    8436: [], # Cereals, QUAKER, Instant Oatmeal, Raisin and Spice, dry
    8444: [], # Cereals, QUAKER, Instant Grits, Redeye Gravy & Country Ham flavor, dry
    8449: [], # Cereals, QUAKER, Instant Grits Product with American Cheese Flavor, dry
    8450: [], # Cereals, QUAKER, Instant Grits, Ham 'n' Cheese flavor, dry
    8451: [], # Cereals, QUAKER, Quick Oats with Iron, Dry
    8452: [], # Cereals, QUAKER, Whole Wheat Natural Cereal, dry
    8476: [], # Cereals ready-to-eat, MALT-O-MEAL, Honey BUZZERS
    8478: [], # Cereals ready-to-eat, MALT-O-MEAL, GOLDEN PUFFS
    8481: [], # Cereals ready-to-eat, MALT-O-MEAL, HONEY GRAHAM SQUARES
    8484: [], # Cereals ready-to-eat, MALT-O-MEAL, Raisin Bran Cereal
    8487: [], # Cereals ready-to-eat, MALT-O-MEAL, Blueberry MUFFIN TOPS Cereal
    8488: [], # Cereals, MALT-O-MEAL, Farina Hot Wheat Cereal, dry
    8489: [], # Cereals, MALT-O-MEAL, Maple & Brown Sugar Hot Wheat Cereal, dry
    8491: [], # Cereals ready-to-eat, MOM'S BEST, Honey Nut TOASTY O'S
    8493: [], # Cereals ready-to-eat, MALT-O-MEAL, Apple ZINGS
    8494: [], # Cereals ready-to-eat, MALT-O-MEAL, CINNAMON TOASTERS
    8495: [], # Cereals ready-to-eat, MALT-O-MEAL, Cocoa DYNO-BITES
    8500: [], # Cereals ready-to-eat, MALT-O-MEAL, Frosted Mini SPOONERS
    8501: [], # Cereals ready-to-eat, MALT-O-MEAL, Fruity DYNO-BITES
    8504: [], # Cereals ready-to-eat, RALSTON Enriched Wheat Bran flakes
    8505: [], # Cereals ready-to-eat, RALSTON Corn Biscuits
    8506: ['Corn flakes cereal'], # Cereals ready-to-eat, RALSTON Corn Flakes
    8507: [], # Cereals ready-to-eat, RALSTON Crispy Hexagons
    8510: [], # Milk and cereal bar
    8511: [], # Cereals, MALT-O-MEAL, original, plain, prepared with water, without salt
    8512: [], # Cereals, MALT-O-MEAL, chocolate, prepared with water, without salt
    8544: [], # Cereals ready-to-eat, POST GREAT GRAINS Cranberry Almond Crunch
    8546: [], # Rice and Wheat cereal bar
    8549: [], # Cereals ready-to-eat, QUAKER, QUAKER Honey Graham LIFE Cereal
    8550: [], # Cereals ready-to-eat, QUAKER, Christmas Crunch
    8554: [], # Cereals ready-to-eat, POST SELECTS Maple Pecan Crunch
    8571: [], # Cereals ready-to-eat, NATURE'S PATH, Organic FLAX PLUS, Pumpkin Granola
    8573: [], # Cereals, CREAM OF WHEAT, 2 1/2 minute cook time, dry
    8574: [], # Cereals, CREAM OF WHEAT, 2 1/2 minute cook time, cooked with water, stove-top, without salt
    8575: [], # Cereals, CREAM OF WHEAT, 2 1/2 minute cook time, cooked with water, microwaved, without salt
    8576: [], # Cereals, CREAM OF WHEAT, 1 minute cook time, dry
    8577: [], # Cereals, CREAM OF WHEAT, 1 minute cook time, cooked with water, stove-top, without salt
    8578: [], # Cereals, CREAM OF WHEAT, 1 minute cook time, cooked with water, microwaved, without salt
    8580: [], # Incaparina, dry mix (corn and soy flours), unprepared
    8625: [], # Cereals ready-to-eat, QUAKER, CAP'N CRUNCH'S Halloween Crunch
    8627: [], # Cereals ready-to-eat, QUAKER, Natural Granola Apple Cranberry Almond
    8628: [], # Cereals ready-to-eat, QUAKER, Maple Brown Sugar LIFE Cereal
    8629: [], # Cereals ready-to-eat, QUAKER, Cap'n Crunch's OOPS! All Berries Cereal
    8632: [], # Cereals ready-to-eat, QUAKER Oatmeal Squares, Golden Maple
    8633: [], # Cereals ready-to-eat, POST, HONEY BUNCHES OF OATS with vanilla bunches
    8639: [], # Cereals, QUAKER, Instant Oatmeal, Cinnamon Spice, reduced sugar
    8640: [], # Cereals, QUAKER, Instant Oatmeal Organic, Regular
    8641: [], # Cereals, QUAKER, Instant Oatmeal, fruit and cream, variety of flavors, reduced sugar
    8642: [], # Cereals, QUAKER, Instant Oatmeal, Apple and Cinnamon, reduced sugar
    8655: [], # Cereals ready-to-eat, POST, HONEY BUNCHES OF OATS, pecan bunches
    8656: [], # Cereals ready-to-eat, NATURE'S PATH, Organic FLAX PLUS flakes
    8657: [], # Cereals ready-to-eat, BARBARA'S PUFFINS, original
    8662: [], # Cereals ready-to-eat, POST, HONEY BUNCHES OF OATS, with real strawberries
    8665: [], # Cereals ready-to-eat, POST HONEY BUNCHES OF OATS with cinnamon bunches
    8672: [], # Cereals ready-to-eat, MALT-O-MEAL, CHOCOLATE MARSHMALLOW MATEYS
    8673: [], # Cereals, ready-to-eat, MALT-O-MEAL, Blueberry Mini SPOONERS
    8674: [], # Cereals ready-to-eat, MALT-O-MEAL, OAT BLENDERS with honey
    8675: [], # Cereals ready-to-eat, MALT-O-MEAL, OAT BLENDERS with honey & almonds
    8676: [], # Cereals ready-to-eat, MALT-O-MEAL, Honey Nut SCOOTERS
    8680: [], # Cereals, oats, instant, fortified, maple and brown sugar, dry
    8685: [], # Cereals ready-to-eat, QUAKER WHOLE HEARTS oat cereal
    8686: [], # Cereals, QUAKER, Weight Control Instant Oatmeal, maple and brown sugar
    8687: [], # Cereals, QUAKER, Weight Control Instant Oatmeal, banana bread
    8688: [], # Cereals, QUAKER, Instant Oatmeal, Cinnamon Swirl, high fiber
    8689: [], # Cereals, QUAKER, oatmeal, REAL MEDLEYS, blueberry hazelnut, dry
    8690: [], # Cereals, QUAKER, oatmeal, REAL MEDLEYS, apple walnut, dry
    8691: [], # Cereals, QUAKER, oatmeal, REAL MEDLEYS, summer berry, dry
    8692: [], # Cereals, QUAKER, oatmeal, REAL MEDLEYS, peach almond, dry
    8693: [], # Cereals, QUAKER, oatmeal, REAL MEDLEYS, cherry pistachio, dry
    8694: [], # Cereals, QUAKER, Instant Oatmeal, weight control, cinnamon
    8709: [], # Cereals ready-to-eat, MOM'S BEST, Sweetened WHEAT-FULS
    9001: ['Acerola', '', 'West indian cherry'], # Acerola, (west indian cherry), raw
    9002: ['Acerola juice'], # Acerola juice, raw
    9003: ['Apple'], # Apples, raw, with skin (Includes foods for USDA's Food Distribution Program)
    9004: ['Apple peeled'], # Apples, raw, without skin
    9005: [], # Apples, raw, without skin, cooked, boiled
    9006: [], # Apples, raw, without skin, cooked, microwave
    9008: [], # Apples, canned, sweetened, sliced, drained, heated
    9009: [], # Apples, dehydrated (low moisture), sulfured, uncooked
    9010: [], # Apples, dehydrated (low moisture), sulfured, stewed
    9011: [], # Apples, dried, sulfured, uncooked
    9012: [], # Apples, dried, sulfured, stewed, without added sugar
    9013: [], # Apples, dried, sulfured, stewed, with added sugar
    9014: [], # Apples, frozen, unsweetened, unheated (Includes foods for USDA's Food Distribution Program)
    9015: [], # Apples, frozen, unsweetened, heated (Includes foods for USDA's Food Distribution Program)
    9016: ['Apple juice'], # Apple juice, canned or bottled, unsweetened, without added ascorbic acid
    9017: [], # Apple juice, frozen concentrate, unsweetened, undiluted, without added ascorbic acid
    9018: [], # Apple juice, frozen concentrate, unsweetened, diluted with 3 volume water without added ascorbic acid
    9019: [], # Applesauce, canned, unsweetened, without added ascorbic acid (Includes foods for USDA's Food Distribution Program)
    9020: ['Applesauce'], # Applesauce, canned, sweetened, without salt
    9021: ['Apricot'], # Apricots, raw
    9022: ['Canned apricot'], # Apricots, canned, water pack, with skin, solids and liquids
    9023: ['Canned apricot', 'peeled'], # Apricots, canned, water pack, without skin, solids and liquids
    9024: [], # Apricots, canned, juice pack, with skin, solids and liquids
    9025: [], # Apricots, canned, extra light syrup pack, with skin, solids and liquids (Includes foods for USDA's Food Distribution Program)
    9026: [], # Apricots, canned, light syrup pack, with skin, solids and liquids
    9027: [], # Apricots, canned, heavy syrup pack, with skin, solids and liquids
    9028: [], # Apricots, canned, heavy syrup pack, without skin, solids and liquids
    9029: [], # Apricots, canned, extra heavy syrup pack, without skin, solids and liquids
    9030: [], # Apricots, dehydrated (low-moisture), sulfured, uncooked
    9031: [], # Apricots, dehydrated (low-moisture), sulfured, stewed
    9032: [], # Apricots, dried, sulfured, uncooked
    9033: [], # Apricots, dried, sulfured, stewed, without added sugar
    9034: [], # Apricots, dried, sulfured, stewed, with added sugar
    9035: ['Apricot', 'frozen'], # Apricots, frozen, sweetened
    9036: [], # Apricot nectar, canned, with added ascorbic acid
    9037: ['Avocado'], # Avocados, raw, all commercial varieties
    9038: [], # Avocados, raw, California
    9039: [], # Avocados, raw, Florida
    9040: ['Banana'], # Bananas, raw
    9041: [], # Bananas, dehydrated, or banana powder
    9042: ['Blackberry'], # Blackberries, raw
    9043: ['Blackberry juice'], # Blackberry juice, canned
    9044: [], # Cherries, tart, dried, sweetened (Includes foods for USDA's Food Distribution Program)
    9046: [], # Blackberries, canned, heavy syrup, solids and liquids
    9048: ['Blackberry', 'frozen'], # Blackberries, frozen, unsweetened
    9050: ['Blueberry'], # Blueberries, raw
    9052: [], # Blueberries, canned, heavy syrup, solids and liquids
    9053: [], # Blueberries, wild, frozen (Includes foods for USDA's Food Distribution Program)
    9054: ['Blueberry', 'frozen'], # Blueberries, frozen, unsweetened (Includes foods for USDA's Food Distribution Program)
    9055: [], # Blueberries, frozen, sweetened
    9056: [], # Boysenberries, canned, heavy syrup
    9057: ['Boysenberries', 'frozen'], # Boysenberries, frozen, unsweetened
    9059: ['Breadfruit'], # Breadfruit, raw
    9060: ['Carambola', '', 'starfruit'], # Carambola, (starfruit), raw
    9061: ['Carissa', '', 'natal-plum'], # Carissa, (natal-plum), raw
    9062: ['Cherimoya'], # Cherimoya, raw
    9063: ['Cherry', 'sour red'], # Cherries, sour, red, raw
    9064: ['Cherry', 'sour red canned'], # Cherries, sour, red, canned, water pack, solids and liquids
    9065: [], # Cherries, sour, red, canned, light syrup pack, solids and liquids
    9066: [], # Cherries, sour, red, canned, heavy syrup pack, solids and liquids
    9067: [], # Cherries, sour, red, canned, extra heavy syrup pack, solids and liquids
    9068: ['Cherry', 'sour red frozen'], # Cherries, sour, red, frozen, unsweetened (Includes foods for USDA's Food Distribution Program)
    9070: ['Cherry', 'sweet'], # Cherries, sweet, raw
    9071: ['Cherry', 'sweet canned'], # Cherries, sweet, canned, water pack, solids and liquids
    9072: [], # Cherries, sweet, canned, juice pack, solids and liquids
    9073: [], # Cherries, sweet, canned, light syrup pack, solids and liquids
    9074: [], # Cherries, sweet, canned, pitted, heavy syrup pack, solids and liquids
    9075: [], # Cherries, sweet, canned, extra heavy syrup pack, solids and liquids
    9077: ['Crabapple'], # Crabapples, raw
    9078: ['Cranberry'], # Cranberries, raw
    9079: ['Cranberry', 'dried sweetened'], # Cranberries, dried, sweetened (Includes foods for USDA's Food Distribution Program)
    9081: ['Cranberry sauce'], # Cranberry sauce, canned, sweetened
    9082: [], # Cranberry-orange relish, canned
    9083: ['Currant', 'european black'], # Currants, european black, raw
    9084: ['Currant', 'red white'], # Currants, red and white, raw
    9085: ['Currant', 'zante dried'], # Currants, zante, dried
    9086: ['Custard-apple', '', "Bullock's-heart"], # Custard-apple, (bullock's-heart), raw
    9087: ['Date', '', 'Deglet noor'], # Dates, deglet noor
    9088: ['Elderberry'], # Elderberries, raw
    9089: ['Fig'], # Figs, raw
    9090: ['Fig', 'canned'], # Figs, canned, water pack, solids and liquids
    9091: [], # Figs, canned, light syrup pack, solids and liquids
    9092: [], # Figs, canned, heavy syrup pack, solids and liquids
    9093: [], # Figs, canned, extra heavy syrup pack, solids and liquids
    9094: ['Fig', 'dried'], # Figs, dried, uncooked
    9095: [], # Figs, dried, stewed
    9096: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, water pack, solids and liquids
    9097: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, juice pack, solids and liquids
    9098: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, extra light syrup, solids and liquids
    9099: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, light syrup, solids and liquids
    9100: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, heavy syrup, solids and liquids
    9101: [], # Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, extra heavy syrup, solids and liquids
    9102: [], # Fruit salad, (peach and pear and apricot and pineapple and cherry), canned, water pack, solids and liquids
    9103: [], # Fruit salad, (peach and pear and apricot and pineapple and cherry), canned, juice pack, solids and liquids
    9104: [], # Fruit salad, (peach and pear and apricot and pineapple and cherry), canned, light syrup, solids and liquids
    9106: [], # Fruit salad, (peach and pear and apricot and pineapple and cherry), canned, extra heavy syrup, solids and liquids
    9107: ['Gooseberry'], # Gooseberries, raw
    9109: ['Gooseberry', 'canned'], # Gooseberries, canned, light syrup pack, solids and liquids
    9110: ['Goji berry', 'dried'], # Goji berries, dried
    9111: ['Grapefruit', 'pink red white'], # Grapefruit, raw, pink and red and white, all areas
    9112: [], # Grapefruit, raw, pink and red, all areas
    9113: [], # Grapefruit, raw, pink and red, California and Arizona
    9114: [], # Grapefruit, raw, pink and red, Florida
    9116: [], # Grapefruit, raw, white, all areas
    9117: [], # Grapefruit, raw, white, California
    9118: [], # Grapefruit, raw, white, Florida
    9119: [], # Grapefruit, sections, canned, water pack, solids and liquids
    9120: [], # Grapefruit, sections, canned, juice pack, solids and liquids
    9121: [], # Grapefruit, sections, canned, light syrup pack, solids and liquids
    9123: ['Grapefruit juice', 'white canned bottled unsweetened'], # Grapefruit juice, white, canned or bottled, unsweetened
    9124: ['Grapefruit juice', 'white canned sweetened'], # Grapefruit juice, white, canned, sweetened
    9125: [], # Grapefruit juice, white, frozen concentrate, unsweetened, undiluted
    9126: [], # Grapefruit juice, white, frozen concentrate, unsweetened, diluted with 3 volume water
    9127: ['Grapefruit juice', 'red pink'], # Grapefruit juice, pink or red, with added calcium
    9128: ['Grapefruit juice', 'white'], # Grapefruit juice, white, raw
    9129: ['Grape', 'muscadine'], # Grapes, muscadine, raw
    9130: [], # Grape juice, canned or bottled, unsweetened, with added ascorbic acid
    9131: ['Grape', 'american'], # Grapes, american type (slip skin), raw
    9132: [], # Grapes, red or green (European type, such as Thompson seedless), raw
    9133: [], # Grapes, canned, thompson seedless, water pack, solids and liquids
    9134: [], # Grapes, canned, thompson seedless, heavy syrup pack, solids and liquids
    9135: ['Grape juice', 'canned bottled unsweetened'], # Grape juice, canned or bottled, unsweetened, without added ascorbic acid
    9138: ['Groundcherry', '', 'Poha'], # Groundcherries, (cape-gooseberries or poha), raw
    9139: ['Guavas', 'common'], # Guavas, common, raw
    9140: ['Guabas', 'strawberry'], # Guavas, strawberry, raw
    9143: ['Guava sauce'], # Guava sauce, cooked
    9144: ['Jackfruit'], # Jackfruit, raw
    9145: ['Java-plum', '', 'Jambolan'], # Java-plum, (jambolan), raw
    9146: ['Jujube'], # Jujube, raw
    9147: [], # Jujube, Chinese, fresh, dried
    9148: ['Kiwifruit', 'green', 'Kiwi'], # Kiwifruit, green, raw
    9149: ['Kumquat'], # Kumquats, raw
    9150: ['Lemon'], # Lemons, raw, without peel
    9152: ['Lemon juice'], # Lemon juice, raw
    9153: [], # Lemon juice from concentrate, canned or bottled
    9156: ['Lemon peel'], # Lemon peel, raw
    9159: ['Lime'], # Limes, raw
    9160: ['Lime juice'], # Lime juice, raw
    9161: [], # Lime juice, canned or bottled, unsweetened
    9163: ['Blueberry', 'dried sweetened'], # Blueberries, dried, sweetened
    9164: ['Lychee', '', 'Litchi'], # Litchis, raw
    9165: ['Lychee', 'dried', 'Litchi'], # Litchis, dried
    9167: ['Loganberry', 'frozen'], # Loganberries, frozen
    9172: ['Longan'], # Longans, raw
    9173: ['Longan', 'dried'], # Longans, dried
    9174: ['Loquat'], # Loquats, raw
    9175: ['Mammy-apple', '', 'Mamey'], # Mammy-apple, (mamey), raw
    9176: ['Mango'], # Mangos, raw
    9177: ['Mangosteen', 'canned'], # Mangosteen, canned, syrup pack
    9178: ['Mango', 'dried sweetend'], # Mango, dried, sweetened
    9181: ['Melon', 'cantaloupe'], # Melons, cantaloupe, raw
    9183: ['Melon', 'casaba'], # Melons, casaba, raw
    9184: ['Melon', 'honeydew'], # Melons, honeydew, raw
    9185: ['Melon ball', 'frozen'], # Melon balls, frozen
    9190: ['Mulberry'], # Mulberries, raw
    9191: ['Nectarine'], # Nectarines, raw
    9192: ['Oheloberry'], # Oheloberries, raw
    9193: ['Ripe olive', 'canned small-extra large'], # Olives, ripe, canned (small-extra large)
    9194: ['Ripe olive', 'canned jumbo-super colossal'], # Olives, ripe, canned (jumbo-super colossal)
    9195: ['Olive', 'pickled canned bottled green'], # Olives, pickled, canned or bottled, green
    9200: ['Orange'], # Oranges, raw, all commercial varieties
    9201: [], # Oranges, raw, California, valencias
    9202: [], # Oranges, raw, navels (Includes foods for USDA's Food Distribution Program)
    9203: [], # Oranges, raw, Florida
    9205: [], # Oranges, raw, with peel
    9206: ['Orange juice'], # Orange juice, raw (Includes foods for USDA's Food Distribution Program)
    9207: ['Orange juice', 'canned unsweetened'], # Orange juice, canned, unsweetened
    9209: [], # Orange juice, chilled, includes from concentrate
    9210: [], # Orange juice, chilled, includes from concentrate, with added calcium and vitamin D
    9211: [], # Orange juice, chilled, includes from concentrate, with added calcium
    9212: [], # Orange juice, frozen concentrate, unsweetened, diluted with 3 volume water, with added calcium
    9213: [], # Orange juice, frozen concentrate, unsweetened, undiluted, with added calcium
    9214: [], # Orange juice, frozen concentrate, unsweetened, undiluted
    9215: [], # Orange juice, frozen concentrate, unsweetened, diluted with 3 volume water
    9216: ['Orange peel'], # Orange peel, raw
    9217: [], # Orange-grapefruit juice, canned or bottled, unsweetened
    9218: ['Tangerine', '', 'Mandarin orange'], # Tangerines, (mandarin oranges), raw
    9219: ['Tangerine', 'canned juice', 'Mandarin orange'], # Tangerines, (mandarin oranges), canned, juice pack
    9220: ['Tangerine', 'light syrup pack', 'Mandarin orange'], # Tangerines, (mandarin oranges), canned, light syrup pack
    9221: ['Tangerine juice'], # Tangerine juice, raw
    9226: ['Papaya'], # Papayas, raw
    9228: ['Papaya', 'canned heavy syrup drained'], # Papaya, canned, heavy syrup, drained
    9229: ['Papaya nectar', 'canned'], # Papaya nectar, canned
    9231: ['Passion-fruit', 'purple', 'Granadilla'], # Passion-fruit, (granadilla), purple, raw
    9232: ['Passion-fruit juice', 'purple'], # Passion-fruit juice, purple, raw
    9233: ['Passion-fruit juice', 'yellow'], # Passion-fruit juice, yellow, raw
    9236: ['Peach', 'yellow'], # Peaches, yellow, raw
    9237: ['Peach', 'canned water pack'], # Peaches, canned, water pack, solids and liquids
    9238: [], # Peaches, canned, juice pack, solids and liquids
    9239: ['Peach', 'canned extra light syrup'], # Peaches, canned, extra light syrup, solids and liquids (Includes foods for USDA's Food Distribution Program)
    9240: [], # Peaches, canned, light syrup pack, solids and liquids
    9241: [], # Peaches, canned, heavy syrup pack, solids and liquids
    9242: [], # Peaches, canned, extra heavy syrup pack, solids and liquids
    9243: [], # Peaches, spiced, canned, heavy syrup pack, solids and liquids
    9244: [], # Peaches, dehydrated (low-moisture), sulfured, uncooked
    9245: [], # Peaches, dehydrated (low-moisture), sulfured, stewed
    9246: ['Peach', 'dried sulfured uncooked'], # Peaches, dried, sulfured, uncooked
    9247: [], # Peaches, dried, sulfured, stewed, without added sugar
    9248: [], # Peaches, dried, sulfured, stewed, with added sugar
    9250: ['Peach', 'frozen'], # Peaches, frozen, sliced, sweetened
    9251: [], # Peach nectar, canned, with sucralose, without added ascorbic acid
    9252: ['Pear'], # Pears, raw
    9253: ['Pear', 'canned water pack'], # Pears, canned, water pack, solids and liquids
    9254: ['Pear', 'canned juice pack'], # Pears, canned, juice pack, solids and liquids
    9255: ['Pear', 'extra light syrup pack'], # Pears, canned, extra light syrup pack, solids and liquids (Includes foods for USDA's Food Distribution Program)
    9256: [], # Pears, canned, light syrup pack, solids and liquids
    9257: [], # Pears, canned, heavy syrup pack, solids and liquids
    9258: [], # Pears, canned, extra heavy syrup pack, solids and liquids
    9259: ['Pear', 'dried sulfured uncooked'], # Pears, dried, sulfured, uncooked
    9260: [], # Pears, dried, sulfured, stewed, without added sugar
    9261: [], # Pears, dried, sulfured, stewed, with added sugar
    9262: ['Pear nectar', 'canned'], # Pear nectar, canned, without added ascorbic acid
    9263: ['Persimmons', 'japanese'], # Persimmons, japanese, raw
    9264: ['Persimmons', 'japanese dried'], # Persimmons, japanese, dried
    9265: ['Persimmons', 'native'], # Persimmons, native, raw
    9266: ['Pineapple'], # Pineapple, raw, all varieties
    9267: ['Pineapple', 'canned water pack'], # Pineapple, canned, water pack, solids and liquids
    9268: ['Pomegranate'], # Pineapple, canned, juice pack, solids and liquids
    9269: [], # Pineapple, canned, light syrup pack, solids and liquids
    9270: [], # Pineapple, canned, heavy syrup pack, solids and liquids
    9271: [], # Pineapple, canned, extra heavy syrup pack, solids and liquids
    9272: ['Pineapple', 'frozen chunk sweetened'], # Pineapple, frozen, chunks, sweetened
    9273: ['Pineapple juice', 'canned bottled unsweetened'], # Pineapple juice, canned or bottled, unsweetened, without added ascorbic acid
    9274: [], # Pineapple juice, frozen concentrate, unsweetened, undiluted
    9275: [], # Pineapple juice, frozen concentrate, unsweetened, diluted with 3 volume water
    9276: ['Pitanga', '', 'Surinam-cherry'], # Pitanga, (surinam-cherry), raw
    9277: ['Plantain', 'yellow'], # Plantains, yellow, raw
    9278: ['Plantain', 'yellow baked'], # Plantains, yellow, baked
    9279: ['Plum'], # Plums, raw
    9281: ['Plum', 'canned water pack'], # Plums, canned, purple, water pack, solids and liquids
    9282: ['Plum', 'canned juice pack'], # Plums, canned, purple, juice pack, solids and liquids
    9283: [], # Plums, canned, purple, light syrup pack, solids and liquids
    9284: [], # Plums, canned, purple, heavy syrup pack, solids and liquids
    9285: [], # Plums, canned, purple, extra heavy syrup pack, solids and liquids
    9286: [], # Pomegranates, raw
    9287: [], # Prickly pears, raw
    9288: ['Prune', 'canned heavy syrup pack'], # Prunes, canned, heavy syrup pack, solids and liquids
    9289: ['Prune', 'dehydrated uncooked low-moisture'], # Prunes, dehydrated (low-moisture), uncooked
    9290: [], # Prunes, dehydrated (low-moisture), stewed
    9291: ['Plum', 'dried uncooked'], # Plums, dried (prunes), uncooked
    9292: [], # Plums, dried (prunes), stewed, without added sugar
    9293: [], # Plums, dried (prunes), stewed, with added sugar
    9294: ['Prune juice', 'canned'], # Prune juice, canned
    9295: ['Pummelo'], # Pummelo, raw
    9296: ['Quince'], # Quinces, raw
    9297: ['Raisin', 'golden seedless'], # Raisins, golden, seedless
    9298: ['Raisin', 'dark seedless'], # Raisins, dark, seedless (Includes foods for USDA's Food Distribution Program)
    9299: ['Raisin', 'seeded'], # Raisins, seeded
    9301: ['Rambutan', 'canned syrup pack'], # Rambutan, canned, syrup pack
    9302: ['Raspberry'], # Raspberries, raw
    9304: ['Raspberry', 'canned syrup'], # Raspberries, canned, red, heavy syrup pack, solids and liquids
    9306: ['Raspberry', 'frozen sweetened'], # Raspberries, frozen, red, sweetened
    9307: ['Rhubarb'], # Rhubarb, raw
    9309: ['Rhubarb', 'frozen uncooked'], # Rhubarb, frozen, uncooked
    9310: ['Rhubarb', 'frozen cooked with sugar'], # Rhubarb, frozen, cooked, with sugar
    9311: ['Roselle', '', 'Gravola'], # Roselle, raw
    9312: ['Rose-apples'], # Rose-apples, raw
    9313: ['Sapodilla'], # Sapodilla, raw
    9314: ['Sapote', '', 'Mamey'], # Sapote, mamey, raw
    9315: ['Soursop'], # Soursop, raw
    9316: ['Strawberry'], # Strawberries, raw
    9317: ['Strawberry', 'canned heavy syrup'], # Strawberries, canned, heavy syrup pack, solids and liquids
    9318: ['Strawberry', 'frozen unsweetened'], # Strawberries, frozen, unsweetened (Includes foods for USDA's Food Distribution Program)
    9320: ['Strawberry', 'frozen sweetened'], # Strawberries, frozen, sweetened, sliced
    9321: ['Sugar-apple', '', 'Sweetsop'], # Sugar-apples, (sweetsop), raw
    9322: ['Tamarind'], # Tamarinds, raw
    9325: [], # Fruit salad, (pineapple and papaya and banana and guava), tropical, canned, heavy syrup, solids and liquids
    9326: ['Watermelon'], # Watermelon, raw
    9328: ['Maraschino cherry', 'canned drained'], # Maraschino cherries, canned, drained
    9334: ['Feijoa'], # Feijoa, raw
    9340: ['Pear', 'asian'], # Pears, asian, raw
    9351: [], # Fruit cocktail, canned, heavy syrup, drained
    9352: [], # Blueberries, canned, light syrup, drained
    9353: [], # Blueberries, wild, canned, heavy syrup, drained
    9354: [], # Pineapple, canned, juice pack, drained
    9357: [], # Apricots, canned, heavy syrup, drained
    9362: [], # Cherries, sour, canned, water pack, drained
    9367: [], # Cherries, sweet, canned, pitted, heavy syrup, drained
    9370: [], # Peaches, canned, heavy syrup, drained
    9374: [], # Pears, canned, heavy syrup, drained
    9379: [], # Plums, canned, heavy syrup, drained
    9383: [], # Tangerines, (mandarin oranges), canned, juice pack, drained
    9400: [], # Apple juice, canned or bottled, unsweetened, with added ascorbic acid
    9401: [], # Applesauce, canned, unsweetened, with added ascorbic acid
    9402: [], # Applesauce, canned, sweetened, with salt
    9404: ['Grapefruit juice', 'ping'], # Grapefruit juice, pink, raw
    9407: [], # Peach nectar, canned, with added ascorbic acid
    9408: [], # Pear nectar, canned, with added ascorbic acid
    9409: ['Pineapple juice', 'canned bottled unsweetened enriched'], # Pineapple juice, canned or bottled, unsweetened, with added ascorbic acid
    9410: [], # Apple juice, frozen concentrate, unsweetened, undiluted, with added ascorbic acid
    9411: [], # Apple juice, frozen concentrate, unsweetened, diluted with 3 volume water, with added ascorbic acid
    9412: [], # Pears, raw, bartlett (Includes foods for USDA's Food Distribution Program)
    9413: [], # Pears, raw, red anjou
    9414: [], # Pears, raw, bosc (Includes foods for USDA's Food Distribution Program)
    9415: [], # Pears, raw, green anjou (Includes foods for USDA's Food Distribution Program)
    9416: ['Grapefruit juice', 'white bottled unsweetened'], # Grapefruit juice, white, bottled, unsweetened, OCEAN SPRAY
    9420: [], # Jackfruit, canned, syrup pack
    9421: ['Medjool date'], # Dates, medjool
    9422: ['Durian', 'raw frozen'], # Durian, raw or frozen
    9423: ['Prune puree'], # Prune puree
    9426: ['Candied fruit'], # Candied fruit
    9427: ['Abiyuch'], # Abiyuch, raw
    9428: ['Rowal'], # Rowal, raw
    9429: ['Pineapple'], # Pineapple, raw, traditional varieties
    9430: [], # Pineapple, raw, extra sweet variety
    9433: ['Clementine'], # Clementines, raw
    9434: ['Guanabana nectar', 'canned'], # Guanabana nectar, canned
    9435: ['Guava nectar', 'canned'], # Guava nectar, canned, with added ascorbic acid
    9436: ['Mango nectar', 'canned'], # Mango nectar, canned
    9437: ['Tamarind nectar', 'canned'], # Tamarind nectar, canned
    9442: ['Pomegranate juice', 'bottled'], # Pomegranate juice, bottled
    9443: [], # Juice, apple and grape blend, with added ascorbic acid
    9444: [], # Juice, apple, grape and pear blend, with added ascorbic acid and calcium
    9446: ['Plantain', 'green fried'], # Plantains, green, fried
    9447: ['Plantain', 'yellow fried'], # Plantains, yellow, fried, Latino restaurant
    9448: [], # Nance, canned, syrup, drained
    9449: [], # Nance, frozen, unsweetened
    9450: ['Naranjilla pulp', 'frozen unsweetened'], # Naranjilla (lulo) pulp, frozen, unsweetened
    9451: ['Horned melon', '', 'Kiwano'], # Horned melon (Kiwano)
    9452: [], # Orange Pineapple Juice Blend
    9500: ['Apple', 'red delicious'], # Apples, raw, red delicious, with skin (Includes foods for USDA's Food Distribution Program)
    9501: ['Apple', 'golden delicious'], # Apples, raw, golden delicious, with skin
    9502: ['Apple', 'granny smith'], # Apples, raw, granny smith, with skin (Includes foods for USDA's Food Distribution Program)
    9503: ['Apple', 'gala'], # Apples, raw, gala, with skin (Includes foods for USDA's Food Distribution Program)
    9504: ['Apple', 'fuji'], # Apples, raw, fuji, with skin (Includes foods for USDA's Food Distribution Program)
    9506: [], # Orange juice, chilled, includes from concentrate, with added calcium and vitamins A, D, E
    9507: [], # Fruit juice smoothie, NAKED JUICE, MIGHTY MANGO
    9508: [], # Fruit juice smoothie, NAKED JUICE, GREEN MACHINE
    9510: [], # Pineapple juice, canned, not from concentrate, unsweetened, with added vitamins A, C and E
    9511: [], # Fruit juice smoothie, NAKED JUICE, BLUE MACHINE
    9512: [], # Grape juice, canned or bottled, unsweetened, with added ascorbic acid and calcium
    9513: [], # Fruit juice smoothie, ODWALLA, ORIGINAL SUPERFOOD
    9514: [], # Fruit juice smoothie, BOLTHOUSE FARMS, BERRY BOOST
    9515: [], # Fruit juice smoothie, BOLTHOUSE FARMS, GREEN GOODNESS
    9516: [], # Fruit juice smoothie, BOLTHOUSE FARMS, strawberry banana
    9517: [], # Apple juice, canned or bottled, unsweetened, with added ascorbic acid, calcium, and potassium
    9518: ['Raspberry', 'frozen unsweetened'], # Raspberries, frozen, red, unsweetened
    9519: [], # Guava nectar, with sucralose, canned
    9520: [], # Kiwifruit, ZESPRI SunGold, raw
    9522: [], # Cranberry juice blend, 100% juice, bottled, with added vitamin C and calcium
    9523: [], # Lemon juice from concentrate, bottled, CONCORD
    9524: [], # Lemon juice from concentrate, bottled, REAL LEMON
    9525: [], # Cranberry sauce, whole, canned, OCEAN SPRAY
    9526: [], # Cranberry sauce, jellied, canned, OCEAN SPRAY
    9528: [], # Ruby Red grapefruit juice blend (grapefruit, grape, apple), OCEAN SPRAY, bottled, with added vitamin C
    9530: [], # Fruit juice smoothie, ODWALLA, strawberry banana
    9531: [], # Fruit juice smoothie, NAKED JUICE, strawberry banana
    9542: ['Plantain', 'green raw'], # Plantains, green, raw
    9543: ['Plantain', 'green boiled'], # Plantains, green, boiled
    9544: ['Baobab powder'], # Baobab powder
    9546: [], # Cherry juice, tart
    9552: [], # Raspberries, puree, seedless
    9553: [], # Raspberries, puree, with seeds
    9554: [], # Raspberry juice concentrate
    10000: [], # Pork, fresh, composite of separable fat, with added solution, cooked
    10001: ['Pork carcass'], # Pork, fresh, carcass, separable lean and fat, raw
    10002: [], # Pork, fresh, composite of trimmed retail cuts (leg, loin, shoulder), separable lean only, raw
    10003: [], # Pork, fresh, composite of trimmed leg, loin, shoulder, and spareribs, (includes cuts to be cured), separable lean and fat, raw
    10004: ['Pork backfat'], # Pork, fresh, backfat, raw
    10005: ['Pork belly'], # Pork, fresh, belly, raw
    10006: [], # Pork, fresh, separable fat, raw
    10007: [], # Pork, fresh, separable fat, cooked
    10008: ['Pork leg', '', 'Pork ham'], # Pork, fresh, leg (ham), whole, separable lean and fat, raw
    10009: [], # Pork, fresh, leg (ham), whole, separable lean and fat, cooked, roasted
    10010: [], # Pork, fresh, leg (ham), whole, separable lean only, raw
    10011: [], # Pork, fresh, leg (ham), whole, separable lean only, cooked, roasted
    10012: [], # Pork, fresh, leg (ham), rump half, separable lean and fat, raw
    10013: [], # Pork, fresh, leg (ham), rump half, separable lean and fat, cooked, roasted
    10014: [], # Pork, fresh, leg (ham), rump half, separable lean only, raw (Includes foods for USDA's Food Distribution Program)
    10015: [], # Pork, fresh, leg (ham), rump half, separable lean only, cooked, roasted
    10016: [], # Pork, fresh, leg (ham), shank half, separable lean and fat, raw
    10017: [], # Pork, fresh, leg (ham), shank half, separable lean and fat, cooked, roasted
    10018: [], # Pork, fresh, leg (ham), shank half, separable lean only, raw
    10019: [], # Pork, fresh, leg (ham), shank half, separable lean only, cooked, roasted
    10020: ['Pork loin', 'whole'], # Pork, fresh, loin, whole, separable lean and fat, raw
    10021: [], # Pork, fresh, loin, whole, separable lean and fat, cooked, braised
    10022: [], # Pork, fresh, loin, whole, separable lean and fat, cooked, broiled
    10023: [], # Pork, fresh, loin, whole, separable lean and fat, cooked, roasted
    10024: [], # Pork, fresh, loin, whole, separable lean only, raw
    10025: [], # Pork, fresh, loin, whole, separable lean only, cooked, braised
    10026: [], # Pork, fresh, loin, whole, separable lean only, cooked, broiled
    10027: [], # Pork, fresh, loin, whole, separable lean only, cooked, roasted
    10028: ['Pork loin', 'blade bone-in'], # Pork, fresh, loin, blade (chops or roasts), bone-in, separable lean and fat, raw
    10029: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean and fat, cooked, braised
    10030: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean and fat, cooked, broiled
    10031: [], # Pork, fresh, loin, blade (roasts), bone-in, separable lean and fat, cooked, roasted
    10032: [], # Pork, fresh, loin, blade (chops or roasts), bone-in, separable lean only, raw
    10033: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean only, cooked, braised
    10034: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean only, cooked, broiled
    10035: [], # Pork, fresh, loin, blade (roasts), bone-in, separable lean only, cooked, roasted
    10036: ['Pork loin', 'center chop bone-in'], # Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, raw
    10037: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, cooked, braised
    10038: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, cooked, broiled
    10039: [], # Pork, fresh, loin, center loin (roasts), bone-in, separable lean and fat, cooked, roasted
    10040: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean only, raw
    10041: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean only, cooked, braised
    10042: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean only, cooked, broiled
    10043: [], # Pork, fresh, loin, center loin (roasts), bone-in, separable lean only, cooked, roasted
    10044: ['Pork loin', 'center rib bone-in'], # Pork, fresh, loin, center rib (chops or roasts), bone-in, separable lean and fat, raw
    10045: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean and fat, cooked, braised
    10046: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean and fat, cooked, broiled
    10047: [], # Pork, fresh, loin, center rib (roasts), bone-in, separable lean and fat, cooked, roasted
    10048: [], # Pork, fresh, loin, center rib (chops or roasts), bone-in, separable lean only, raw
    10049: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean only, cooked, braised
    10050: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean only, cooked, broiled
    10051: [], # Pork, fresh, loin, center rib (roasts), bone-in, separable lean only, cooked, roasted
    10052: ['Pork loin', 'sirloin bone-in'], # Pork, fresh, loin, sirloin (chops or roasts), bone-in, separable lean and fat, raw
    10053: [], # Pork, fresh, loin, sirloin (chops), bone-in, separable lean and fat, cooked, braised
    10054: [], # Pork, fresh, loin, sirloin (chops), bone-in, separable lean and fat, cooked, broiled
    10055: [], # Pork, fresh, loin, sirloin (roasts), bone-in, separable lean and fat, cooked, roasted
    10056: [], # Pork, fresh, loin, sirloin (chops or roasts), bone-in, separable lean only, raw
    10057: [], # Pork, fresh, loin, sirloin (chops), bone-in, separable lean only, cooked, braised
    10058: [], # Pork, fresh, loin, sirloin (chops), bone-in, separable lean only, cooked, broiled
    10059: [], # Pork, fresh, loin, sirloin (roasts), bone-in, separable lean only, cooked, roasted
    10060: [], # Pork, fresh, loin, tenderloin, separable lean only, raw
    10061: [], # Pork, fresh, loin, tenderloin, separable lean only, cooked, roasted
    10062: ['Pork loin', 'top chop boneless'], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, raw
    10063: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, cooked, braised
    10064: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, cooked, broiled
    10065: [], # Pork, fresh, loin, top loin (roasts), boneless, separable lean and fat, cooked, roasted
    10066: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, raw
    10067: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, cooked, braised
    10068: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, cooked, broiled
    10069: [], # Pork, fresh, loin, top loin (roasts), boneless, separable lean only, cooked, roasted
    10070: ['Pork shoulder', 'whole'], # Pork, fresh, shoulder, whole, separable lean and fat, raw
    10071: [], # Pork, fresh, shoulder, whole, separable lean and fat, cooked, roasted
    10072: [], # Pork, fresh, shoulder, whole, separable lean only, raw
    10073: [], # Pork, fresh, shoulder, whole, separable lean only, cooked, roasted
    10074: ['Pork shoulder', 'arm picnic'], # Pork, fresh, shoulder, arm picnic, separable lean and fat, raw
    10075: [], # Pork, fresh, shoulder, arm picnic, separable lean and fat, cooked, braised
    10076: [], # Pork, fresh, shoulder, arm picnic, separable lean and fat, cooked, roasted
    10077: [], # Pork, fresh, shoulder, arm picnic, separable lean only, raw
    10078: [], # Pork, fresh, shoulder, arm picnic, separable lean only, cooked, braised
    10079: [], # Pork, fresh, shoulder, arm picnic, separable lean only, cooked, roasted
    10080: ['Pork shoulder', 'blade steak', 'Boston butt'], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean and fat, raw
    10081: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean and fat, cooked, braised
    10082: [], # Pork, fresh, shoulder, blade, boston (steaks), separable lean and fat, cooked, broiled
    10083: [], # Pork, fresh, shoulder, blade, boston (roasts), separable lean and fat, cooked, roasted
    10084: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean only, raw
    10085: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean only, cooked, braised
    10086: [], # Pork, fresh, shoulder, blade, boston (steaks), separable lean only, cooked, broiled
    10087: [], # Pork, fresh, shoulder, blade, boston (roasts), separable lean only, cooked, roasted
    10088: ['Pork sparerib'], # Pork, fresh, spareribs, separable lean and fat, raw
    10089: [], # Pork, fresh, spareribs, separable lean and fat, cooked, braised
    10093: [], # Pork, fresh, composite of trimmed retail cuts (leg, loin, and shoulder), separable lean only, cooked
    10094: ['Pork loin', 'center chop boneless'], # Pork, fresh, loin, center loin (chops), boneless, separable lean only, raw
    10096: ['Pork brain'], # Pork, fresh, variety meats and by-products, brain, raw
    10097: [], # Pork, fresh, variety meats and by-products, brain, cooked, braised
    10098: ['Pork chitterling'], # Pork, fresh, variety meats and by-products, chitterlings, raw
    10099: [], # Pork, fresh, variety meats and by-products, chitterlings, cooked, simmered
    10100: ['Pork ear', 'frozen'], # Pork, fresh, variety meats and by-products, ears, frozen, raw
    10101: [], # Pork, fresh, variety meats and by-products, ears, frozen, cooked, simmered
    10102: ['Pork foot'], # Pork, fresh, variety meats and by-products, feet, raw
    10103: ['Pork heart'], # Pork, fresh, variety meats and by-products, heart, raw
    10104: [], # Pork, fresh, variety meats and by-products, heart, cooked, braised
    10105: ['Pork jowl'], # Pork, fresh, variety meats and by-products, jowl, raw
    10106: ['Pork kidney'], # Pork, fresh, variety meats and by-products, kidneys, raw
    10107: [], # Pork, fresh, variety meats and by-products, kidneys, cooked, braised
    10109: ['Pork leaf fat'], # Pork, fresh, variety meats and by-products, leaf fat, raw
    10110: ['Pork liver'], # Pork, fresh, variety meats and by-products, liver, raw
    10111: [], # Pork, fresh, variety meats and by-products, liver, cooked, braised
    10112: ['Pork lung'], # Pork, fresh, variety meats and by-products, lungs, raw
    10113: [], # Pork, fresh, variety meats and by-products, lungs, cooked, braised
    10114: [], # Pork, fresh, variety meats and by-products, mechanically separated, raw
    10115: ['Pork pancreas'], # Pork, fresh, variety meats and by-products, pancreas, raw
    10116: [], # Pork, fresh, variety meats and by-products, pancreas, cooked, braised
    10117: ['Pork spleen'], # Pork, fresh, variety meats and by-products, spleen, raw
    10118: [], # Pork, fresh, variety meats and by-products, spleen, cooked, braised
    10119: ['Pork stomach'], # Pork, fresh, variety meats and by-products, stomach, raw
    10120: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean only, cooked, pan-fried
    10121: ['Pork tongue'], # Pork, fresh, variety meats and by-products, tongue, raw
    10122: [], # Pork, fresh, variety meats and by-products, tongue, cooked, braised
    10123: ['Pork bacon', 'cured', 'Bacon'], # Pork, cured, bacon, unprepared
    10128: [], # Pork, cured, breakfast strips, raw or unheated
    10130: ['Canadian bacon'], # Canadian bacon, unprepared
    10132: [], # Pork, cured, feet, pickled
    10134: [], # Pork, cured, ham, boneless, extra lean (approximately 5% fat), roasted
    10136: [], # Pork, cured, ham, boneless, regular (approximately 11% fat), roasted
    10137: [], # Pork, cured, ham, extra lean (approximately 4% fat), canned, unheated
    10138: [], # Pork, cured, ham, extra lean (approximately 4% fat), canned, roasted
    10140: [], # Pork, cured, ham, regular (approximately 13% fat), canned, roasted
    10141: [], # Pork, cured, ham, center slice, country-style, separable lean only, raw
    10142: [], # Pork, cured, ham, center slice, separable lean and fat, unheated
    10146: [], # Pork, cured, ham, patties, unheated
    10149: [], # Pork, cured, ham, steak, boneless, extra lean, unheated
    10150: [], # Pork, cured, ham, whole, separable lean and fat, unheated
    10152: [], # Pork, cured, ham, whole, separable lean only, unheated
    10153: [], # Pork, cured, ham, whole, separable lean only, roasted
    10163: [], # Pork, fresh, loin, center loin (chops), boneless, separable lean only, cooked, pan-broiled
    10164: [], # Pork, fresh, loin, center loin (chops), boneless, separable lean and fat, raw
    10165: [], # Pork, cured, salt pork, raw
    10166: [], # Pork, cured, separable fat (from ham and arm picnic), unheated
    10167: [], # Pork, cured, separable fat (from ham and arm picnic), roasted
    10168: [], # Pork, cured, shoulder, arm picnic, separable lean and fat, roasted
    10169: [], # Pork, cured, shoulder, arm picnic, separable lean only, roasted
    10170: [], # Pork, cured, shoulder, blade roll, separable lean and fat, unheated
    10171: [], # Pork, cured, shoulder, blade roll, separable lean and fat, roasted
    10173: [], # Pork, fresh, variety meats and by-products, feet, cooked, simmered
    10174: [], # Pork, fresh, variety meats and by-products, tail, raw
    10175: [], # Pork, fresh, variety meats and by-products, tail, cooked, simmered
    10176: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean only, cooked, pan-fried
    10177: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean only, cooked, pan-fried
    10178: [], # Pork, fresh, loin, blade (chops), bone-in, separable lean and fat, cooked, pan-fried
    10179: [], # Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, cooked, pan-fried
    10180: [], # Pork, fresh, loin, center rib (chops), bone-in, separable lean and fat, cooked, pan-fried
    10181: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, cooked, pan-fried
    10182: [], # Pork, cured, ham, boneless, extra lean and regular, unheated
    10183: [], # Pork, cured, ham, boneless, extra lean and regular, roasted
    10184: [], # Pork, cured, ham, extra lean and regular, canned, unheated
    10185: [], # Pork, cured, ham, extra lean and regular, canned, roasted
    10186: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, cooked, pan-fried
    10187: [], # Pork, fresh, composite of trimmed retail cuts (leg, loin, shoulder, and spareribs), separable lean and fat, raw
    10188: [], # Pork, fresh, composite of trimmed retail cuts (leg, loin, shoulder, and spareribs), separable lean and fat, cooked
    10189: [], # Pork, fresh, loin, center loin (chops), boneless, separable lean and fat, cooked, pan-broiled
    10192: ['Pork backrib'], # Pork, fresh, backribs, separable lean and fat, raw
    10193: [], # Pork, fresh, backribs, separable lean and fat, cooked, roasted
    10194: ['Pork loin', 'center rib boneless'], # Pork, fresh, loin, center rib (chops or roasts), boneless, separable lean and fat, raw
    10195: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean and fat, cooked, braised
    10196: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean and fat, cooked, broiled
    10197: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean and fat, cooked, pan-fried
    10198: [], # Pork, fresh, loin, center rib (roasts), boneless, separable lean and fat, cooked, roasted
    10199: [], # Pork, fresh, loin, center rib (chops or roasts), boneless, separable lean only, raw
    10200: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean only, cooked, braised
    10201: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean only, cooked, broiled
    10202: [], # Pork, fresh, loin, center rib (chops), boneless, separable lean only, cooked, pan-fried
    10203: [], # Pork, fresh, loin, center rib (roasts), boneless, separable lean only, cooked, roasted
    10204: ['Pork loin', 'country-style rib'], # Pork, fresh, loin, country-style ribs, separable lean and fat, raw
    10205: [], # Pork, fresh, loin, country-style ribs, separable lean and fat, cooked, braised
    10206: [], # Pork, fresh, loin, country-style ribs, separable lean and fat, bone-in, cooked, roasted
    10207: [], # Pork, fresh, loin, country-style ribs, separable lean only, raw
    10208: [], # Pork, fresh, loin, country-style ribs, separable lean only, cooked, braised
    10209: [], # Pork, fresh, loin, country-style ribs, separable lean only, bone-in, cooked, roasted
    10210: ['Pork loin', 'sirloin boneless'], # Pork, fresh, loin, sirloin (chops or roasts), boneless, separable lean and fat, raw
    10211: [], # Pork, fresh, loin, sirloin (chops), boneless, separable lean and fat, cooked, braised
    10212: [], # Pork, fresh, loin, sirloin (chops), boneless, separable lean and fat, cooked, broiled
    10213: [], # Pork, fresh, loin, sirloin (roasts), boneless, separable lean and fat, cooked, roasted
    10214: [], # Pork, fresh, loin, sirloin (chops or roasts), boneless, separable lean only, raw
    10215: [], # Pork, fresh, loin, sirloin (chops), boneless, separable lean only, cooked, braised
    10216: [], # Pork, fresh, loin, sirloin (chops), boneless, separable lean only, cooked, broiled
    10217: [], # Pork, fresh, loin, sirloin (roasts), boneless, separable lean only, cooked, roasted
    10218: ['Pork loin', 'tenderloin'], # Pork, fresh, loin, tenderloin, separable lean and fat, raw
    10219: ['Pork', 'ground'], # Pork, fresh, ground, raw
    10220: [], # Pork, fresh, ground, cooked
    10221: [], # Pork, fresh, loin, tenderloin, separable lean and fat, cooked, broiled
    10222: [], # Pork, fresh, loin, tenderloin, separable lean and fat, cooked, roasted
    10223: [], # Pork, fresh, loin, tenderloin, separable lean only, cooked, broiled
    10224: [], # Pork, fresh, loin, top loin (roasts), boneless, separable lean and fat, raw
    10225: [], # Pork, fresh, loin, top loin (roasts), boneless, separable lean only, raw
    10226: [], # Pork, fresh, composite of trimmed retail cuts (loin and shoulder blade), separable lean and fat, raw
    10227: [], # Pork, fresh, composite of trimmed retail cuts (loin and shoulder blade), separable lean and fat, cooked
    10228: [], # Pork, fresh, composite of trimmed retail cuts (loin and shoulder blade), separable lean only, raw
    10229: [], # Pork, fresh, composite of trimmed retail cuts (loin and shoulder blade), separable lean only, cooked
    10851: [], # HORMEL, Cure 81 Ham
    10852: [], # HORMEL ALWAYS TENDER, Pork Tenderloin, Teriyaki-Flavored
    10853: [], # HORMEL ALWAYS TENDER, Pork Tenderloin, Peppercorn-Flavored
    10854: [], # HORMEL ALWAYS TENDER, Pork Loin Filets, Lemon Garlic-Flavored
    10855: [], # HORMEL ALWAYS TENDER, Center Cut Chops, Fresh Pork
    10856: [], # HORMEL ALWAYS TENDER, Boneless Pork Loin, Fresh Pork
    10857: [], # HORMEL Canadian Style Bacon
    10858: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, with added solution, cooked, pan-broiled
    10859: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, with added solution, cooked, pan-broiled
    10860: [], # Pork, cured, bacon, cooked, baked
    10861: [], # Pork, cured, bacon, cooked, microwaved
    10862: [], # Pork, cured, bacon, pre-sliced, cooked, pan-fried
    10863: [], # Pork, fresh, variety meats and by-products, stomach, cooked, simmered
    10864: [], # Pork, bacon, rendered fat, cooked
    10865: [], # Pork, cured, ham -- water added, rump, bone-in, separable lean only, heated, roasted
    10866: [], # Pork, cured, ham -- water added, rump, bone-in, separable lean only, unheated
    10867: [], # Pork, cured, ham -- water added, shank, bone-in, separable lean only, heated, roasted
    10868: [], # Pork, cured, ham -- water added, slice, bone-in, separable lean only, heated, pan-broil
    10869: [], # Pork, cured, ham and water product, slice, bone-in, separable lean only, heated, pan-broil
    10870: [], # Pork, cured, ham and water product, slice, boneless, separable lean only, heated, pan-broil
    10871: [], # Pork, cured, ham and water product, whole, boneless, separable lean only, heated, roasted
    10872: [], # Pork, cured, ham and water product, whole, boneless, separable lean only, unheated
    10873: [], # Pork, cured, ham with natural juices, rump, bone-in, separable lean only, heated, roasted
    10874: [], # Pork, cured, ham with natural juices, shank, bone-in, separable lean only, heated, roasted
    10875: [], # Pork, cured, ham with natural juices, slice, bone-in, separable lean only, heated, pan-broil
    10876: [], # Pork, cured, ham with natural juices, spiral slice, meat only, boneless, separable lean only, heated, roasted
    10877: [], # Pork, cured, ham and water product, rump, bone-in, separable lean only, heated, roasted
    10878: [], # Pork, cured, ham -- water added, slice, boneless, separable lean only, heated, pan-broil
    10879: [], # Pork, cured, ham -- water added, whole, boneless, separable lean only, heated, roasted
    10880: [], # Pork, cured, ham -- water added, whole, boneless, separable lean only, unheated
    10881: [], # Pork, cured, ham and water product, shank, bone-in, separable lean only, heated, roasted
    10882: [], # Pork, cured, ham with natural juices, slice, boneless, separable lean only, heated, pan-broil
    10883: [], # Pork, cured, ham with natural juices, whole, boneless, separable lean only, heated, roasted
    10884: [], # Pork, cured, ham with natural juices, whole, boneless, separable lean only, unheated
    10885: [], # Pork, cured, ham -- water added, shank, bone-in, separable lean only, unheated
    10886: [], # Pork, cured, ham -- water added, slice, bone-in, separable lean only, unheated
    10887: [], # Pork, cured, ham and water product, rump, bone-in, separable lean only, unheated
    10888: [], # Pork, cured, ham and water product, slice, bone-in, separable lean only, unheated
    10889: [], # Pork, cured, ham and water product, shank, bone-in, unheated, separable lean only
    10890: [], # Pork, cured, ham with natural juices, rump, bone-in, separable lean only, unheated
    10891: [], # Pork, cured, ham with natural juices, shank, bone-in, separable lean only, unheated
    10892: [], # Pork, cured, ham with natural juices, slice, bone-in, separable lean only, unheated
    10893: [], # Pork, cured, ham with natural juices, spiral slice, boneless, separable lean only, unheated
    10894: [], # Pork, cured, ham, separable fat, boneless, heated
    10895: [], # Pork, cured, ham, separable fat, boneless, unheated
    10898: [], # Pork, pickled pork hocks
    10899: [], # Pork, cured, ham, slice, bone-in, separable lean only, heated, pan-broil
    10900: [], # Pork, cured, ham with natural juices, whole, boneless, separable lean and fat, unheated
    10901: [], # Pork, cured, ham with natural juices, spiral slice, boneless, separable lean and fat, unheated
    10902: [], # Pork, cured, ham with natural juices, slice, bone-in, separable lean and fat, unheated
    10903: [], # Pork, cured, ham with natural juices, shank, bone-in, separable lean and fat, unheated
    10904: [], # Pork, cured, ham with natural juices, rump, bone-in, separable lean and fat, unheated
    10905: [], # Pork, cured, ham and water product, whole, boneless, separable lean and fat, unheated
    10906: [], # Pork, cured, ham and water product, slice, bone-in, separable lean and fat, unheated
    10907: [], # Pork, cured, ham and water product, shank, bone-in, separable lean and fat, unheated
    10908: [], # Pork, cured, ham and water product, rump, bone-in, separable lean and fat, unheated
    10909: [], # Pork, cured, ham -- water added, whole, boneless, separable lean and fat, unheated
    10910: [], # Pork, cured, ham -- water added, slice, bone-in, separable lean and fat, unheated
    10911: [], # Pork, cured, ham -- water added, shank, bone-in, separable lean and fat, unheated
    10912: [], # Pork, cured, ham -- water added, rump, bone-in, separable lean and fat, unheated
    10913: [], # Pork, cured, ham -- water added, rump, bone-in, separable lean and fat, heated, roasted
    10914: [], # Pork, cured, ham -- water added, shank, bone-in, separable lean and fat, heated, roasted
    10915: [], # Pork, cured, ham -- water added, slice, bone-in, separable lean and fat, heated, pan-broil
    10916: [], # Pork, cured, ham -- water added, slice, boneless, separable lean and fat, heated, pan-broil
    10917: [], # Pork, cured, ham -- water added, whole, boneless, separable lean and fat, heated, roasted
    10918: [], # Pork, cured, ham and water product, rump, bone-in, separable lean and fat, heated, roasted
    10919: [], # Pork, cured, ham and water product, shank, bone-in, separable lean and fat, heated, roasted
    10920: [], # Pork, cured, ham and water product, slice, bone-in, separable lean and fat, heated, pan-broil
    10921: [], # Pork, cured, ham and water product, slice, boneless, separable lean and fat, heated, pan-broil
    10922: [], # Pork, cured, ham and water product, whole, boneless, separable lean and fat, heated, roasted
    10923: [], # Pork, cured, ham with natural juices, rump, bone-in, separable lean and fat, heated, roasted
    10924: [], # Pork, cured, ham with natural juices, shank, bone-in, separable lean and fat, heated, roasted
    10925: [], # Pork, cured, ham with natural juices, slice, bone-in, separable lean and fat, heated, pan-broil
    10926: [], # Pork, cured, ham with natural juices, slice, boneless, separable lean and fat, heated, pan-broil
    10927: [], # Pork, cured, ham with natural juices, spiral slice, boneless, separable lean and fat, heated, roasted
    10928: [], # Pork, cured, ham with natural juices, whole, boneless, separable lean and fat, heated, roasted
    10929: [], # Pork, cured, ham, rump, bone-in, separable lean and fat, heated, roasted
    10931: [], # Pork, cured, ham, rump, bone-in, separable lean only, heated, roasted
    10932: [], # Pork, cured, ham, rump, bone-in, separable lean only, unheated
    10933: [], # Pork, cured, ham, shank, bone-in, separable lean only, heated, roasted
    10934: [], # Pork, cured, ham, shank, bone-in, separable lean only, unheated
    10935: [], # Pork, cured, ham, shank, bone-in, separable lean and fat, heated, roasted
    10936: [], # Pork, cured, ham, shank, bone-in, separable lean and fat, unheated
    10937: [], # Pork, cured, ham, slice, bone-in, separable lean and fat, heated, pan-broil
    10938: [], # Pork, cured, ham, slice, bone-in, separable lean only, unheated
    10939: [], # Pork, cured, ham, slice, bone-in, separable lean and fat, unheated
    10940: [], # Pork, fresh, spareribs, separable lean and fat, cooked, roasted
    10942: [], # Pork, fresh, composite of separable fat, with added solution, raw
    10943: [], # Pork, fresh, loin, tenderloin, separable lean only, with added solution, cooked, roasted
    10944: [], # Pork, fresh, enhanced, loin, tenderloin, separable lean only, raw
    10945: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean only, with added solution cooked, braised
    10946: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean only, with added solution, raw
    10947: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, with added solution, cooked, broiled
    10948: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean only, with added solution, raw
    10949: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, with added solution, raw
    10950: [], # Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, with added solution, cooked, broiled
    10951: [], # Pork, fresh, loin, tenderloin, separable lean and fat, with added solution, raw
    10952: [], # Pork, fresh, loin, tenderloin, separable lean and fat, with added solution, cooked, roasted
    10953: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean and fat,with added solution, raw
    10954: [], # Pork, fresh, shoulder, (Boston butt), blade (steaks), separable lean and fat, with added solution, cooked, braised
    10955: [], # Pork, cured, ham, rump, bone-in, separable lean and fat, unheated
    10956: [], # Pork, loin, leg cap steak, boneless, separable lean and fat, cooked, broiled
    10957: [], # Pork, Leg Cap Steak, boneless, separable lean and fat, raw
    10958: ['Pork shoulder breast', 'boneless'], # Pork, Shoulder breast, boneless, separable lean and fat, raw
    10959: [], # Pork, Shoulder breast, boneless, separable lean and fat, cooked, broiled
    10960: [], # Pork, shoulder, petite tender, boneless, separable lean and fat, cooked, broiled
    10961: ['Pork shoulder petite tender'], # Pork, Shoulder petite tender, boneless, separable lean and fat, raw
    10962: [], # Pork, Leg sirloin tip roast, boneless, separable lean and fat, cooked, braised
    10963: [], # Pork, Leg sirloin tip roast, boneless, separable lean and fat, raw
    10972: [], # Pork, ground, 84% lean / 16% fat, raw
    10973: [], # Pork, ground, 96% lean / 4% fat, raw
    10974: [], # Pork, ground, 72% lean / 28% fat, cooked, crumbles
    10975: [], # Pork, ground, 84% lean / 16% fat, cooked, crumbles
    10976: [], # Pork, ground, 96% lean / 4% fat, cooked, crumbles
    10977: [], # Pork, ground, 72% lean / 28% fat, cooked, pan-broiled
    10978: [], # Pork, ground, 84% lean / 16% fat, cooked, pan-broiled
    10979: [], # Pork, ground, 96% lean / 4% fat, cooked, pan-broiled
    10980: [], # Pork loin, fresh, backribs, bone-in, raw, lean only
    10981: [], # Pork loin, fresh, backribs, bone-in, cooked-roasted, lean only
    10982: [], # Pork, fresh, loin, blade (chops or roasts), boneless, separable lean only, raw
    10983: [], # Pork, fresh, loin, blade (roasts), boneless, separable lean only, cooked, roasted
    10984: [], # Pork, fresh, loin, blade (chops), boneless, separable lean only, boneless, cooked, broiled
    10985: [], # Pork, fresh, loin, country-style ribs, separable lean only, boneless, cooked, broiled
    10986: [], # Pork, fresh, loin, country-style ribs, separable lean only, bone-in, cooked, broiled
    10987: [], # Pork, fresh, loin, country-style ribs, separable lean only, boneless, cooked, roasted
    10988: [], # Pork, fresh, blade, (chops), boneless, separable lean and fat, cooked, broiled
    10989: ['Pork loin', 'blade boneless'], # Pork, fresh, loin, blade (chops or roasts), boneless, separable lean and fat only, raw
    10990: [], # Pork, fresh, loin, blade (roasts), boneless, separable lean and fat, cooked, roasted
    10991: [], # Pork, fresh, loin, country-style ribs, separable lean and fat, boneless, cooked, broiled
    10992: [], # Pork, fresh, loin, country-style ribs, separable lean and fat, bone-in, cooked, broiled
    10993: [], # Pork, fresh, loin, country-style ribs, separable lean and fat, boneless, cooked, roasted
    10994: [], # Bacon, pre-sliced, reduced/low sodium, unprepared
    10998: [], # Canadian bacon, cooked, pan-fried
    11001: ['Alfalfa seed', 'sprouted'], # Alfalfa seeds, sprouted, raw
    11003: ['Amaranth leaf'], # Amaranth leaves, raw
    11004: [], # Amaranth leaves, cooked, boiled, drained, without salt
    11005: ['Arrowhead'], # Arrowhead, raw
    11006: [], # Arrowhead, cooked, boiled, drained, without salt
    11007: ['Artichoke'], # Artichokes, (globe or french), raw
    11008: [], # Artichokes, (globe or french), cooked, boiled, drained, without salt
    11009: [], # Artichokes, (globe or french), frozen, unprepared
    11010: [], # Artichokes, (globe or french), frozen, cooked, boiled, drained, without salt
    11011: ['Asparagus'], # Asparagus, raw
    11012: [], # Asparagus, cooked, boiled, drained
    11013: [], # Asparagus, canned, regular pack, solids and liquids
    11015: [], # Asparagus, canned, drained solids
    11018: [], # Asparagus, frozen, unprepared
    11019: [], # Asparagus, frozen, cooked, boiled, drained, without salt
    11022: ['Balsam-pear', 'leafy tip', 'Bitter gourd'], # Balsam-pear (bitter gourd), leafy tips, raw
    11023: [], # Balsam-pear (bitter gourd), leafy tips, cooked, boiled, drained, without salt
    11024: ['Balsam-pear', 'pod', 'Bitter gourd'], # Balsam-pear (bitter gourd), pods, raw
    11025: [], # Balsam-pear (bitter gourd), pods, cooked, boiled, drained, without salt
    11026: ['Bamboo shoot'], # Bamboo shoots, raw
    11027: [], # Bamboo shoots, cooked, boiled, drained, without salt
    11028: [], # Bamboo shoots, canned, drained solids
    11029: ['Kidney bean', 'mature seed'], # Beans, kidney, mature seeds, sprouted, raw
    11030: [], # Beans, kidney, mature seeds, sprouted, cooked, boiled, drained, without salt
    11031: ['Lima bean', 'immature seed'], # Lima beans, immature seeds, raw
    11032: [], # Lima beans, immature seeds, cooked, boiled, drained, without salt
    11033: [], # Lima beans, immature seeds, canned, regular pack, solids and liquids
    11037: [], # Lima beans, immature seeds, frozen, fordhook, unprepared
    11038: [], # Lima beans, immature seeds, frozen, fordhook, cooked, boiled, drained, without salt
    11039: [], # Lima beans, immature seeds, frozen, baby, unprepared
    11040: [], # Lima beans, immature seeds, frozen, baby, cooked, boiled, drained, without salt
    11043: ['Mung bean', 'sprouted'], # Mung beans, mature seeds, sprouted, raw
    11044: [], # Mung beans, mature seeds, sprouted, cooked, boiled, drained, without salt
    11045: [], # Mung beans, mature seeds, sprouted, cooked, stir-fried
    11046: ['Navy bean', 'sprouted'], # Beans, navy, mature seeds, sprouted, raw
    11047: [], # Beans, navy, mature seeds, sprouted, cooked, boiled, drained, without salt
    11048: [], # Beans, pinto, immature seeds, frozen, unprepared
    11049: [], # Beans, pinto, immature seeds, frozen, cooked, boiled, drained, without salt
    11050: [], # Beans, shellie, canned, solids and liquids
    11052: ['Snap bean', 'green'], # Beans, snap, green, raw
    11053: [], # Beans, snap, green, cooked, boiled, drained, without salt
    11054: [], # Beans, snap, green, canned, regular pack, solids and liquids
    11056: [], # Beans, snap, green, canned, regular pack, drained solids
    11058: [], # Beans, snap, canned, all styles, seasoned, solids and liquids
    11060: [], # Beans, snap, green, frozen, all styles, unprepared (Includes foods for USDA's Food Distribution Program)
    11061: [], # Beans, snap, green, frozen, cooked, boiled, drained without salt
    11062: [], # Beans, snap, green, frozen, all styles, microwaved
    11063: [], # Beans, snap, green, microwaved
    11080: ['Beet'], # Beets, raw
    11081: [], # Beets, cooked, boiled, drained
    11082: [], # Beets, canned, regular pack, solids and liquids
    11084: [], # Beets, canned, drained solids
    11086: ['Beet green'], # Beet greens, raw
    11087: [], # Beet greens, cooked, boiled, drained, without salt
    11088: ['Broadbean', 'immature seed'], # Broadbeans, immature seeds, raw
    11089: [], # Broadbeans, immature seeds, cooked, boiled, drained, without salt
    11090: ['Broccoli'], # Broccoli, raw
    11091: [], # Broccoli, cooked, boiled, drained, without salt
    11092: ['Broccoli', 'frozen chopped unprepared'], # Broccoli, frozen, chopped, unprepared
    11093: [], # Broccoli, frozen, chopped, cooked, boiled, drained, without salt
    11094: [], # Broccoli, frozen, spears, unprepared (Includes foods for USDA's Food Distribution Program)
    11095: [], # Broccoli, frozen, spears, cooked, boiled, drained, without salt
    11096: ['Broccoli raab'], # Broccoli raab, raw
    11097: [], # Broccoli raab, cooked
    11098: ['Brussels sprout'], # Brussels sprouts, raw
    11099: [], # Brussels sprouts, cooked, boiled, drained, without salt
    11100: ['Brussels sprout', 'frozen'], # Brussels sprouts, frozen, unprepared
    11101: [], # Brussels sprouts, frozen, cooked, boiled, drained, without salt
    11104: ['Burdock root'], # Burdock root, raw
    11105: [], # Burdock root, cooked, boiled, drained, without salt
    11106: ['Butterbur', '', 'Fuki'], # Butterbur, (fuki), raw
    11107: [], # Butterbur, cooked, boiled, drained, without salt
    11108: [], # Butterbur, canned
    11109: ['Cabbage'], # Cabbage, raw
    11110: [], # Cabbage, cooked, boiled, drained, without salt
    11112: ['Red cabbage'], # Cabbage, red, raw
    11113: [], # Cabbage, red, cooked, boiled, drained, without salt
    11114: ['Savoy cabbage'], # Cabbage, savoy, raw
    11115: [], # Cabbage, savoy, cooked, boiled, drained, without salt
    11116: ['Chinese cabbage', '', 'Pak-choi'], # Cabbage, chinese (pak-choi), raw
    11117: [], # Cabbage, chinese (pak-choi), cooked, boiled, drained, without salt
    11118: ['Kimchi cabbage'], # Cabbage, kimchi
    11119: ['Chinese cabbage', '', 'Pe-tsai'], # Cabbage, chinese (pe-tsai), raw
    11120: [], # Cabbage, chinese (pe-tsai), cooked, boiled, drained, without salt
    11122: ['Cardoon'], # Cardoon, raw
    11123: [], # Cardoon, cooked, boiled, drained, without salt
    11124: ['Carrot'], # Carrots, raw
    11125: [], # Carrots, cooked, boiled, drained, without salt
    11126: [], # Carrots, canned, regular pack, solids and liquids
    11128: [], # Carrots, canned, regular pack, drained solids
    11130: ['Carrot', 'frozen unprepared'], # Carrots, frozen, unprepared (Includes foods for USDA's Food Distribution Program)
    11131: [], # Carrots, frozen, cooked, boiled, drained, without salt
    11134: ['Cassava'], # Cassava, raw
    11135: ['Cauliflower'], # Cauliflower, raw
    11136: [], # Cauliflower, cooked, boiled, drained, without salt
    11137: ['Cauliflower', 'frozen unprepared'], # Cauliflower, frozen, unprepared
    11138: [], # Cauliflower, frozen, cooked, boiled, drained, without salt
    11141: ['Celeriac'], # Celeriac, raw
    11142: [], # Celeriac, cooked, boiled, drained, without salt
    11143: ['Celery'], # Celery, raw
    11144: [], # Celery, cooked, boiled, drained, without salt
    11145: ['Celtuce'], # Celtuce, raw
    11147: ['Chard', 'swiss'], # Chard, swiss, raw
    11148: [], # Chard, swiss, cooked, boiled, drained, without salt
    11149: ['Chayote', 'fruit'], # Chayote, fruit, raw
    11150: [], # Chayote, fruit, cooked, boiled, drained, without salt
    11151: ['Chicory', 'witloof'], # Chicory, witloof, raw
    11152: ['Chicory green'], # Chicory greens, raw
    11154: ['Chicory root'], # Chicory roots, raw
    11156: ['Chive'], # Chives, raw
    11157: ['Chrysanthemum', 'garland'], # Chrysanthemum, garland, raw
    11158: [], # Chrysanthemum, garland, cooked, boiled, drained, without salt
    11161: ['Collard'], # Collards, raw
    11162: [], # Collards, cooked, boiled, drained, without salt
    11163: [], # Collards, frozen, chopped, unprepared
    11164: [], # Collards, frozen, chopped, cooked, boiled, drained, without salt
    11165: ['Coriander leaf'], # Coriander (cilantro) leaves, raw
    11167: ['Corn', 'sweet yellow'], # Corn, sweet, yellow, raw
    11168: [], # Corn, sweet, yellow, cooked, boiled, drained, without salt
    11170: [], # Corn, sweet, yellow, canned, brine pack, regular pack, solids and liquids
    11172: [], # Corn, sweet, yellow, canned, whole kernel, drained solids
    11174: [], # Corn, sweet, yellow, canned, cream style, regular pack
    11176: [], # Corn, sweet, yellow, canned, vacuum pack, regular pack
    11177: [], # Corn, sweet, yellow, canned, drained solids, rinsed with tap water
    11178: [], # Corn, sweet, yellow, frozen, kernels cut off cob, unprepared (Includes foods for USDA's Food Distribution Program)
    11179: [], # Corn, sweet, yellow, frozen, kernels cut off cob, boiled, drained, without salt
    11180: [], # Corn, sweet, yellow, frozen, kernels on cob, unprepared
    11181: [], # Corn, sweet, yellow, frozen, kernels on cob, cooked, boiled, drained, without salt
    11182: [], # Corn, yellow, whole kernel, frozen, microwaved
    11184: [], # Corn with red and green peppers, canned, solids and liquids
    11190: ['Cornsalad'], # Cornsalad, raw
    11191: ['Cowpea', 'immature seed', 'Blackeye'], # Cowpeas (blackeyes), immature seeds, raw
    11192: [], # Cowpeas (blackeyes), immature seeds, cooked, boiled, drained, without salt
    11195: [], # Cowpeas (blackeyes), immature seeds, frozen, unprepared
    11196: [], # Cowpeas (blackeyes), immature seeds, frozen, cooked, boiled, drained, without salt
    11197: ['Cowpea', 'young pod seed'], # Cowpeas, young pods with seeds, raw
    11198: [], # Cowpeas, young pods with seeds, cooked, boiled, drained, without salt
    11199: ['Yardlong bean'], # Yardlong bean, raw
    11200: [], # Yardlong bean, cooked, boiled, drained, without salt
    11201: ['Cowpea', 'leafy tip'], # Cowpeas, leafy tips, raw
    11202: [], # Cowpeas, leafy tips, cooked, boiled, drained, without salt
    11203: ['Cress', 'garden'], # Cress, garden, raw
    11204: [], # Cress, garden, cooked, boiled, drained, without salt
    11205: ['Cucumber'], # Cucumber, with peel, raw
    11206: ['Cucumber', 'peeled'], # Cucumber, peeled, raw
    11207: ['Dandelion green'], # Dandelion greens, raw
    11208: [], # Dandelion greens, cooked, boiled, drained, without salt
    11209: ['Eggplant'], # Eggplant, raw
    11210: [], # Eggplant, cooked, boiled, drained, without salt
    11211: ['Edamame', 'frozen unprepared'], # Edamame, frozen, unprepared
    11212: ['Edamame', 'frozen prepared'], # Edamame, frozen, prepared
    11213: ['Endive'], # Endive, raw
    11214: [], # Escarole, cooked, boiled, drained, no salt added
    11215: ['Garlic'], # Garlic, raw
    11216: ['Ginger root'], # Ginger root, raw
    11218: ['Gourd', 'white-flowered', 'Calabash'], # Gourd, white-flowered (calabash), raw
    11219: [], # Gourd, white-flowered (calabash), cooked, boiled, drained, without salt
    11220: ['Gourd', 'dishcloth', 'Towelgourd'], # Gourd, dishcloth (towelgourd), raw
    11221: [], # Gourd, dishcloth (towelgourd), cooked, boiled, drained, without salt
    11222: ['Drumstick leaf'], # Drumstick leaves, raw
    11223: [], # Drumstick leaves, cooked, boiled, drained, without salt
    11224: ['Hyacinth bean', '', 'Lablab'], # Hyacinth-beans, immature seeds, raw
    11225: [], # Hyacinth-beans, immature seeds, cooked, boiled, drained, without salt
    11226: ['Jerusalem artichoke'], # Jerusalem-artichokes, raw
    11228: ['Jew ear', '', 'Pepeao'], # Jew's ear, (pepeao), raw
    11230: ['Pepeao', 'dried', 'Pepeao'], # Pepeao, dried
    11231: ['Jute', 'potherb'], # Jute, potherb, raw
    11232: [], # Jute, potherb, cooked, boiled, drained, without salt
    11233: ['Kale'], # Kale, raw
    11234: [], # Kale, cooked, boiled, drained, without salt
    11235: [], # Kale, frozen, unprepared
    11236: [], # Kale, frozen, cooked, boiled, drained, without salt
    11237: [], # Kanpyo, (dried gourd strips)
    11238: ['Shiitake mushroom'], # Mushrooms, shiitake, raw
    11239: ['Chanterelle mushroom'], # Mushrooms, Chanterelle, raw
    11240: ['Morel mushroom'], # Mushrooms, morel, raw
    11241: ['Kohlrabi'], # Kohlrabi, raw
    11242: [], # Kohlrabi, cooked, boiled, drained, without salt
    11243: [], # Mushrooms, portabella, grilled
    11244: ['Lambsquarter'], # Lambsquarters, raw
    11245: [], # Lambsquarters, cooked, boiled, drained, without salt
    11246: ['Leek'], # Leeks, (bulb and lower leaf-portion), raw
    11247: [], # Leeks, (bulb and lower leaf-portion), cooked, boiled, drained, without salt
    11248: ['Lentil', 'sprouted'], # Lentils, sprouted, raw
    11249: [], # Lentils, sprouted, cooked, stir-fried, without salt
    11250: ['Lettuce', 'butterhead'], # Lettuce, butterhead (includes boston and bibb types), raw
    11251: ['Lettuce', 'cos romaine'], # Lettuce, cos or romaine, raw
    11252: ['Lettuce', 'iceberg'], # Lettuce, iceberg (includes crisphead types), raw
    11253: ['Lettuce', 'green leaf'], # Lettuce, green leaf, raw
    11254: ['Lotus root'], # Lotus root, raw
    11255: [], # Lotus root, cooked, boiled, drained, without salt
    11257: ['Lettuce red'], # Lettuce, red leaf, raw
    11258: ['Mountain yam', 'hawaii'], # Mountain yam, hawaii, raw
    11259: [], # Mountain yam, hawaii, cooked, steamed, without salt
    11260: ['Mushroom', 'white'], # Mushrooms, white, raw
    11261: [], # Mushrooms, white, cooked, boiled, drained, without salt
    11263: [], # Mushrooms, white, stir-fried
    11264: [], # Mushrooms, canned, drained solids
    11265: ['Mushroom', 'portabella'], # Mushrooms, portabella, raw
    11266: ['Mushroom', 'brown italian crimini'], # Mushrooms, brown, italian, or crimini, raw
    11267: [], # Mushrooms, shiitake, stir-fried
    11268: [], # Mushrooms, shiitake, dried
    11269: [], # Mushrooms, shiitake, cooked, without salt
    11270: ['Mustard green'], # Mustard greens, raw
    11271: [], # Mustard greens, cooked, boiled, drained, without salt
    11272: [], # Mustard greens, frozen, unprepared
    11273: [], # Mustard greens, frozen, cooked, boiled, drained, without salt
    11274: ['Mustard spinach'], # Mustard spinach, (tendergreen), raw
    11275: [], # Mustard spinach, (tendergreen), cooked, boiled, drained, without salt
    11276: ['Spinach', 'New Zealand'], # New Zealand spinach, raw
    11277: [], # New Zealand spinach, cooked, boiled, drained, without salt
    11278: ['Okra'], # Okra, raw
    11279: [], # Okra, cooked, boiled, drained, without salt
    11280: [], # Okra, frozen, unprepared
    11281: [], # Okra, frozen, cooked, boiled, drained, without salt
    11282: ['Onion'], # Onions, raw
    11283: [], # Onions, cooked, boiled, drained, without salt
    11284: [], # Onions, dehydrated flakes
    11285: [], # Onions, canned, solids and liquids
    11286: ['Onion', 'yellow sauteed'], # Onions, yellow, sauteed
    11287: [], # Onions, frozen, chopped, unprepared
    11288: [], # Onions, frozen, chopped, cooked, boiled, drained, without salt
    11289: [], # Onions, frozen, whole, unprepared
    11290: [], # Onions, frozen, whole, cooked, boiled, drained, without salt
    11291: ["Scallion onion"], # Onions, spring or scallions (includes tops and bulb), raw
    11292: [], # Onions, young green, tops only
    11293: ['Welsh onion'], # Onions, welsh, raw
    11294: ['Sweet onion'], # Onions, sweet, raw
    11295: [], # Onion rings, breaded, par fried, frozen, unprepared
    11296: [], # Onion rings, breaded, par fried, frozen, prepared, heated in oven
    11297: ['Parsley'], # Parsley, fresh
    11298: ['Parsnip'], # Parsnips, raw
    11299: [], # Parsnips, cooked, boiled, drained, without salt
    11300: ['Pea'], # Peas, edible-podded, raw
    11301: [], # Peas, edible-podded, boiled, drained, without salt
    11302: [], # Peas, edible-podded, frozen, unprepared
    11303: [], # Peas, edible-podded, frozen, cooked, boiled, drained, without salt
    11304: ['Pea', 'green'], # Peas, green, raw
    11305: [], # Peas, green, cooked, boiled, drained, without salt
    11306: [], # Peas, green, canned, regular pack, solids and liquids
    11308: [], # Peas, green (includes baby and lesuer types), canned, drained solids, unprepared
    11310: [], # Peas, green, canned, seasoned, solids and liquids
    11311: [], # Peas, green, canned, drained solids, rinsed in tap water
    11312: [], # Peas, green, frozen, unprepared (Includes foods for USDA's Food Distribution Program)
    11313: [], # Peas, green, frozen, cooked, boiled, drained, without salt
    11316: [], # Peas, mature seeds, sprouted, raw
    11317: [], # Peas, mature seeds, sprouted, cooked, boiled, drained, without salt
    11318: [], # Peas and carrots, canned, regular pack, solids and liquids
    11322: [], # Peas and carrots, frozen, unprepared
    11323: [], # Peas and carrots, frozen, cooked, boiled, drained, without salt
    11324: [], # Peas and onions, canned, solids and liquids
    11326: [], # Peas and onions, frozen, unprepared
    11327: [], # Peas and onions, frozen, cooked, boiled, drained, without salt
    11329: [], # Peppers, hot chili, green, canned, pods, excluding seeds, solids and liquids
    11333: ['Green pepper', 'sweet'], # Peppers, sweet, green, raw
    11334: [], # Peppers, sweet, green, cooked, boiled, drained, without salt
    11335: [], # Peppers, sweet, green, canned, solids and liquids
    11337: [], # Peppers, sweet, green, frozen, chopped, unprepared
    11338: [], # Peppers, sweet, green, frozen, chopped, boiled, drained, without salt
    11339: [], # Peppers, sweet, green, sauteed
    11344: ['Pigeon pea'], # Pigeonpeas, immature seeds, raw
    11345: [], # Pigeonpeas, immature seeds, cooked, boiled, drained, without salt
    11349: ['Poi'], # Poi
    11350: ['Pokeberry shoot', '', 'Poke'], # Pokeberry shoots, (poke), raw
    11351: [], # Pokeberry shoots, (poke), cooked, boiled, drained, without salt
    11352: ['Potato'], # Potatoes, flesh and skin, raw
    11353: ['Potato', 'russet'], # Potatoes, russet, flesh and skin, raw (Includes foods for USDA's Food Distribution Program)
    11354: ['Potato', 'white'], # Potatoes, white, flesh and skin, raw
    11355: ['Potato', 'red'], # Potatoes, red, flesh and skin, raw
    11356: [], # Potatoes, Russet, flesh and skin, baked
    11357: [], # Potatoes, white, flesh and skin, baked
    11358: [], # Potatoes, red, flesh and skin, baked
    11359: [], # Potatoes, french fried, crinkle or regular cut, salt added in processing, frozen, as purchased
    11360: [], # Potatoes, french fried, crinkle or regular cut, salt added in processing, frozen, oven-heated
    11361: [], # Potatoes, roasted, salt added in processing, frozen, unprepared
    11362: [], # Potatoes, raw, skin
    11363: [], # Potatoes, baked, flesh, without salt
    11364: [], # Potatoes, baked, skin, without salt
    11365: [], # Potatoes, boiled, cooked in skin, flesh, without salt
    11366: [], # Potatoes, boiled, cooked in skin, skin, without salt
    11367: [], # Potatoes, boiled, cooked without skin, flesh, without salt
    11368: [], # Potatoes, microwaved, cooked in skin, flesh, without salt
    11369: [], # Potatoes, microwaved, cooked in skin, skin, without salt
    11370: [], # Potatoes, hash brown, home-prepared
    11371: [], # Potatoes, mashed, home-prepared, whole milk and margarine added
    11372: [], # Potatoes, scalloped, home-prepared with butter
    11373: [], # Potatoes, au gratin, home-prepared from recipe using butter
    11374: [], # Potatoes, canned, solids and liquids
    11376: [], # Potatoes, canned, drained solids
    11378: [], # Potatoes, mashed, dehydrated, flakes without milk, dry form
    11379: [], # Potatoes, mashed, dehydrated, prepared from flakes without milk, whole milk and butter added
    11380: [], # Potatoes, mashed, dehydrated, granules without milk, dry form
    11381: [], # Potatoes, mashed, dehydrated, prepared from granules without milk, whole milk and butter added
    11382: [], # Potatoes, mashed, dehydrated, granules with milk, dry form
    11383: [], # Potatoes, mashed, dehydrated, prepared from granules with milk, water and margarine added
    11384: [], # Potatoes, au gratin, dry mix, unprepared
    11385: [], # Potatoes, au gratin, dry mix, prepared with water, whole milk and butter
    11386: [], # Potatoes, scalloped, dry mix, unprepared
    11387: [], # Potatoes, scalloped, dry mix, prepared with water, whole milk and butter
    11390: [], # Potatoes, hash brown, frozen, plain, unprepared
    11391: [], # Potatoes, hash brown, frozen, plain, prepared, pan fried in canola oil
    11392: [], # Potatoes, hash brown, frozen, with butter sauce, unprepared
    11393: [], # Potatoes, hash brown, frozen, with butter sauce, prepared
    11394: [], # Potatoes, french fried, shoestring, salt added in processing, frozen, as purchased
    11395: [], # Potatoes, french fried, shoestring, salt added in processing, frozen, oven-heated
    11396: [], # Potatoes, o'brien, frozen, unprepared
    11397: [], # Potatoes, o'brien, frozen, prepared
    11398: [], # Potato puffs, frozen, unprepared
    11399: [], # Potato puffs, frozen, oven-heated
    11401: [], # Potatoes, frozen, whole, cooked, boiled, drained, without salt
    11402: [], # Potatoes, french fried, all types, salt added in processing, frozen, unprepared
    11403: [], # Potatoes, french fried, all types, salt added in processing, frozen, home-prepared, oven heated
    11406: [], # Potatoes, french fried, cottage-cut, salt not added in processing, frozen, as purchased
    11407: [], # Potatoes, french fried, cottage-cut, salt not added in processing, frozen, oven-heated
    11408: [], # Potatoes, frozen, french fried, par fried, extruded, unprepared
    11409: [], # Potatoes, frozen, french fried, par fried, extruded, prepared, heated in oven, without salt
    11410: [], # Potato wedges, frozen (Includes foods for USDA's Food Distribution Program)
    11411: [], # Potatoes, french fried, steak fries, salt added in processing, frozen, as purchased
    11412: [], # Potatoes, french fried, steak fries, salt added in processing, frozen, oven-heated
    11413: [], # Potato flour
    11414: [], # Potato salad, home-prepared
    11416: ['Pumpkin flower'], # Pumpkin flowers, raw
    11417: [], # Pumpkin flowers, cooked, boiled, drained, without salt
    11418: ['Pumpkin leaf'], # Pumpkin leaves, raw
    11419: [], # Pumpkin leaves, cooked, boiled, drained, without salt
    11422: ['Pumpkin'], # Pumpkin, raw
    11423: [], # Pumpkin, cooked, boiled, drained, without salt
    11424: [], # Pumpkin, canned, without salt
    11426: [], # Pumpkin pie mix, canned
    11427: ['Purslane'], # Purslane, raw
    11428: [], # Purslane, cooked, boiled, drained, without salt
    11429: ['Radish'], # Radishes, raw
    11430: ['Radish', 'oriental'], # Radishes, oriental, raw
    11431: [], # Radishes, oriental, cooked, boiled, drained, without salt
    11432: [], # Radishes, oriental, dried
    11435: ['Rutabaga'], # Rutabagas, raw
    11436: [], # Rutabagas, cooked, boiled, drained, without salt
    11437: ['Salsify', '', 'Vegetable oyster'], # Salsify, (vegetable oyster), raw
    11438: [], # Salsify, cooked, boiled, drained, without salt
    11439: [], # Sauerkraut, canned, solids and liquids
    11442: ['Seaweed', 'agar'], # Seaweed, agar, raw
    11444: ['Seaweed', 'irishmoss'], # Seaweed, irishmoss, raw
    11445: ['Seaweed', 'kelp'], # Seaweed, kelp, raw
    11446: ['Seaweed', 'laver'], # Seaweed, laver, raw
    11447: ['Sesbania flower'], # Sesbania flower, raw
    11448: [], # Sesbania flower, cooked, steamed, without salt
    11450: ['Soybean', 'green'], # Soybeans, green, raw
    11451: [], # Soybeans, green, cooked, boiled, drained, without salt
    11452: [], # Soybeans, mature seeds, sprouted, raw
    11453: [], # Soybeans, mature seeds, sprouted, cooked, steamed
    11454: [], # Soybeans, mature seeds, sprouted, cooked, stir-fried
    11457: ['Spinach'], # Spinach, raw
    11458: [], # Spinach, cooked, boiled, drained, without salt
    11459: [], # Spinach, canned, regular pack, solids and liquids
    11461: [], # Spinach, canned, regular pack, drained solids
    11463: ['Spinach', 'frozen'], # Spinach, frozen, chopped or leaf, unprepared (Includes foods for USDA's Food Distribution Program)
    11464: [], # Spinach, frozen, chopped or leaf, cooked, boiled, drained, without salt
    11467: ['Squash', 'summer crookneck straightneck'], # Squash, summer, crookneck and straightneck, raw
    11468: [], # Squash, summer, crookneck and straightneck, cooked, boiled, drained, without salt
    11471: [], # Squash, summer, crookneck and straightneck, canned, drained, solid, without salt
    11473: [], # Squash, summer, crookneck and straightneck, frozen, unprepared
    11474: [], # Squash, summer, crookneck and straightneck, frozen, cooked, boiled, drained, without salt
    11475: ['Squash', 'summer scallop'], # Squash, summer, scallop, raw
    11476: [], # Squash, summer, scallop, cooked, boiled, drained, without salt
    11477: ['Squash', 'summer zucchini'], # Squash, summer, zucchini, includes skin, raw
    11478: [], # Squash, summer, zucchini, includes skin, cooked, boiled, drained, without salt
    11479: [], # Squash, summer, zucchini, includes skin, frozen, unprepared
    11480: [], # Squash, summer, zucchini, includes skin, frozen, cooked, boiled, drained, without salt
    11481: [], # Squash, summer, zucchini, italian style, canned
    11482: ['Squash', 'winter acorn'], # Squash, winter, acorn, raw
    11483: [], # Squash, winter, acorn, cooked, baked, without salt
    11484: [], # Squash, winter, acorn, cooked, boiled, mashed, without salt
    11485: ['Squash', 'winter butternut'], # Squash, winter, butternut, raw
    11486: [], # Squash, winter, butternut, cooked, baked, without salt
    11487: [], # Squash, winter, butternut, frozen, unprepared
    11488: [], # Squash, winter, butternut, frozen, cooked, boiled, without salt
    11489: ['Squash', 'winter hubbard'], # Squash, winter, hubbard, raw
    11490: [], # Squash, winter, hubbard, baked, without salt
    11491: [], # Squash, winter, hubbard, cooked, boiled, mashed, without salt
    11492: ['Squash', 'winter spaghetti'], # Squash, winter, spaghetti, raw
    11493: [], # Squash, winter, spaghetti, cooked, boiled, drained, or baked, without salt
    11495: ['Succotash'], # Succotash, (corn and limas), raw
    11496: [], # Succotash, (corn and limas), cooked, boiled, drained, without salt
    11497: [], # Succotash, (corn and limas), canned, with cream style corn
    11499: [], # Succotash, (corn and limas), canned, with whole kernel corn, solids and liquids
    11501: [], # Succotash, (corn and limas), frozen, unprepared
    11502: [], # Succotash, (corn and limas), frozen, cooked, boiled, drained, without salt
    11503: ['Water convolvulus'], # Water convolvulus,raw
    11504: [], # Water convolvulus, cooked, boiled, drained, without salt
    11505: ['Sweet potato leaf'], # Sweet potato leaves, raw
    11506: [], # Sweet potato leaves, cooked, steamed, without salt
    11507: ['Sweet potato'], # Sweet potato, raw, unprepared (Includes foods for USDA's Food Distribution Program)
    11508: [], # Sweet potato, cooked, baked in skin, flesh, without salt
    11510: [], # Sweet potato, cooked, boiled, without skin
    11512: [], # Sweet potato, canned, vacuum pack
    11514: [], # Sweet potato, canned, mashed
    11516: [], # Sweet potato, frozen, unprepared (Includes foods for USDA's Food Distribution Program)
    11517: [], # Sweet potato, frozen, cooked, baked, without salt
    11518: ['Taro'], # Taro, raw
    11519: [], # Taro, cooked, without salt
    11520: ['Taro leaf'], # Taro leaves, raw
    11521: [], # Taro leaves, cooked, steamed, without salt
    11522: ['Taro shoot'], # Taro shoots, raw
    11523: [], # Taro shoots, cooked, without salt
    11525: ['Taro tahitian'], # Taro, tahitian, raw
    11526: [], # Taro, tahitian, cooked, without salt
    11527: ['Tomato', 'green'], # Tomatoes, green, raw
    11529: ['Tomato', 'red ripe'], # Tomatoes, red, ripe, raw, year round average
    11530: [], # Tomatoes, red, ripe, cooked
    11531: [], # Tomatoes, red, ripe, canned, packed in tomato juice
    11533: [], # Tomatoes, red, ripe, canned, stewed
    11537: [], # Tomatoes, red, ripe, canned, with green chilies
    11540: ["Tomato juice", "canned"], # Tomato juice, canned, with salt added
    11546: ["Tomato paste", "canned"], # Tomato products, canned, paste, without salt added (Includes foods for USDA's Food Distribution Program)
    11547: ["Tomato puree", "canned"], # Tomato products, canned, puree, without salt added
    11548: ["Tomato powder"], # Tomato powder
    11549: ["Tomato sauce", "canned"], # Tomato products, canned, sauce
    11551: [], # Tomato products, canned, sauce, with mushrooms
    11553: [], # Tomato products, canned, sauce, with onions
    11555: [], # Tomato products, canned, sauce, with herbs and cheese
    11557: [], # Tomato products, canned, sauce, with onions, green peppers, and celery
    11559: [], # Tomato products, canned, sauce, with tomato tidbits
    11563: [], # Tree fern, cooked, without salt
    11564: ['Turnip'], # Turnips, raw
    11565: [], # Turnips, cooked, boiled, drained, without salt
    11566: [], # Turnips, frozen, unprepared
    11567: [], # Turnips, frozen, cooked, boiled, drained, without salt
    11568: ['Turnip green'], # Turnip greens, raw
    11569: [], # Turnip greens, cooked, boiled, drained, without salt
    11570: [], # Turnip greens, canned, solids and liquids
    11574: [], # Turnip greens, frozen, unprepared
    11575: [], # Turnip greens, frozen, cooked, boiled, drained, without salt
    11576: [], # Turnip greens and turnips, frozen, unprepared
    11577: [], # Turnip greens and turnips, frozen, cooked, boiled, drained, without salt
    11578: [], # Vegetable juice cocktail, canned
    11579: [], # Vegetables, mixed, canned, solids and liquids
    11581: [], # Vegetables, mixed, canned, drained solids
    11583: [], # Vegetables, mixed, frozen, unprepared
    11584: [], # Vegetables, mixed, frozen, cooked, boiled, drained, without salt
    11585: [], # Vegetable juice cocktail, low sodium, canned
    11587: ['Vinespinach', '', 'Basella'], # Vinespinach, (basella), raw
    11588: [], # Waterchestnuts, chinese, (matai), raw
    11590: [], # Waterchestnuts, chinese, canned, solids and liquids
    11591: ['Watercress'], # Watercress, raw
    11593: ['Waxgourd'], # Waxgourd, (chinese preserving melon), raw
    11594: [], # Waxgourd, (chinese preserving melon), cooked, boiled, drained, without salt
    11595: ['Winged bean'], # Winged beans, immature seeds, raw
    11596: [], # Winged beans, immature seeds, cooked, boiled, drained, without salt
    11597: ['Winged bean leaf'], # Winged bean leaves, raw
    11599: ['Winged bean tuber'], # Winged bean tuber, raw
    11601: ['Yam'], # Yam, raw
    11602: [], # Yam, cooked, boiled, drained, or baked, without salt
    11603: ['Yambean'], # Yambean (jicama), raw
    11604: [], # Yambean (jicama), cooked, boiled, drained, without salt
    11605: [], # Beets, harvard, canned, solids and liquids
    11609: [], # Beets, pickled, canned, solids and liquids
    11613: ['Borage'], # Borage, raw
    11614: [], # Borage, cooked, boiled, drained, without salt
    11615: [], # Chives, freeze-dried
    11616: ['Dock'], # Dock, raw
    11617: [], # Dock, cooked, boiled, drained, without salt
    11618: [], # Eppaw, raw
    11620: ['Drumstick pod'], # Drumstick pods, raw
    11621: [], # Drumstick pods, cooked, boiled, drained, without salt
    11624: [], # Leeks, (bulb and lower-leaf portion), freeze-dried
    11625: [], # Parsley, freeze-dried
    11626: [], # Beans, mung, mature seeds, sprouted, canned, drained solids
    11632: [], # Peppers, jalapeno, canned, solids and liquids
    11637: ['Radish', 'white icicle'], # Radishes, white icicle, raw
    11640: [], # Shallots, freeze-dried
    11641: ['Squash', 'summer'], # Squash, summer, all varieties, raw
    11642: [], # Squash, summer, all varieties, cooked, boiled, drained, without salt
    11643: ['Squash', 'winter'], # Squash, winter, all varieties, raw
    11644: [], # Squash, winter, all varieties, cooked, baked, without salt
    11645: [], # Sweet potato, canned, syrup pack, solids and liquids
    11647: [], # Sweet potato, canned, syrup pack, drained solids
    11649: [], # Tomato products, canned, sauce, spanish style
    11653: [], # Beans, pinto, mature seeds, sprouted, raw
    11654: [], # Beans, pinto, mature seeds, sprouted, cooked, boiled, drained, without salt
    11655: [], # Carrot juice, canned
    11656: [], # Corn pudding, home prepared
    11657: [], # Potatoes, mashed, home-prepared, whole milk added
    11658: [], # Spinach souffle
    11659: [], # Sweet potato, cooked, candied, home-prepared
    11660: [], # Tomatoes, red, ripe, cooked, stewed
    11663: [], # Seaweed, agar, dried
    11666: ['Seaweed', 'spirulina', 'Spirulina'], # Seaweed, spirulina, raw
    11667: [], # Seaweed, spirulina, dried
    11669: ['Seaweed', 'wakame', 'Wakame'], # Seaweed, wakame, raw
    11670: ['Hot chili pepper'], # Peppers, hot chili, green, raw
    11671: [], # Potatoes, o'brien, home-prepared
    11672: [], # Potato pancakes
    11674: [], # Potatoes, baked, flesh and skin, without salt
    11675: [], # Potatoes, microwaved, cooked in skin, flesh and skin, without salt
    11676: [], # Radish seeds, sprouted, raw
    11677: ['Shallot'], # Shallots, raw
    11683: [], # Carrot, dehydrated
    11693: [], # Tomatoes, crushed, canned
    11695: ['Tomato', 'orange'], # Tomatoes, orange, raw
    11696: ['Tomato', 'yellow'], # Tomatoes, yellow, raw
    11697: ['Arrowroot'], # Arrowroot, raw
    11698: ['Chrysanthemum leaf'], # Chrysanthemum leaves, raw
    11700: [], # Amaranth leaves, cooked, boiled, drained, with salt
    11701: [], # Arrowhead, cooked, boiled, drained, with salt
    11702: [], # Artichokes, (globe or french), cooked, boiled, drained, with salt
    11703: [], # Artichokes, (globe or french), frozen, cooked, boiled, drained, with salt
    11705: [], # Asparagus, cooked, boiled, drained, with salt
    11707: [], # Asparagus, canned, no salt added, solids and liquids
    11709: [], # Asparagus, frozen, cooked, boiled, drained, with salt
    11710: [], # Balsam-pear (bitter gourd), leafy tips, cooked, boiled, drained, with salt
    11711: [], # Balsam-pear (bitter gourd), pods, cooked, boiled, drained, with salt
    11712: [], # Bamboo shoots, cooked, boiled, drained, with salt
    11713: [], # Beans, kidney, mature seeds, sprouted, cooked, boiled, drained, with salt
    11714: [], # Lima beans, immature seeds, cooked, boiled, drained, with salt
    11715: [], # Lima beans, immature seeds, canned, no salt added, solids and liquids
    11716: [], # Lima beans, immature seeds, frozen, baby, cooked, boiled, drained, with salt
    11717: [], # Lima beans, immature seeds, frozen, fordhook, cooked, boiled, drained, with salt
    11718: [], # Mung beans, mature seeds, sprouted, cooked, boiled, drained, with salt
    11719: [], # Beans, navy, mature seeds, sprouted, cooked, boiled, drained, with salt
    11720: [], # Beans, pinto, immature seeds, frozen, cooked, boiled, drained, with salt
    11721: [], # Beans, pinto, mature seeds, sprouted, cooked, boiled, drained, with salt
    11722: ['Yellow bean', 'snap'], # Beans, snap, yellow, raw
    11723: [], # Beans, snap, green, cooked, boiled, drained, with salt
    11724: [], # Beans, snap, yellow, cooked, boiled, drained, without salt
    11725: [], # Beans, snap, yellow, cooked, boiled, drained, with salt
    11726: [], # Beans, snap, green, canned, no salt added, solids and liquids
    11727: [], # Beans, snap, yellow, canned, regular pack, solids and liquids
    11728: [], # Beans, snap, yellow, canned, no salt added, solids and liquids
    11729: [], # Beans, snap, green, canned, no salt added, drained solids
    11730: [], # Beans, snap, yellow, frozen, all styles, unprepared
    11731: [], # Beans, snap, green, frozen, cooked, boiled, drained, with salt
    11732: [], # Beans, snap, yellow, frozen, cooked, boiled, drained, without salt
    11733: [], # Beans, snap, yellow, frozen, cooked, boiled, drained, with salt
    11734: [], # Beets, cooked, boiled. drained, with salt
    11735: [], # Beets, canned, no salt added, solids and liquids
    11736: [], # Beet greens, cooked, boiled, drained, with salt
    11737: [], # Borage, cooked, boiled, drained, with salt
    11738: [], # Broadbeans, immature seeds, cooked, boiled, drained, with salt
    11739: ['Broccoli leaf'], # Broccoli, leaves, raw
    11740: [], # Broccoli, flower clusters, raw
    11741: ['Broccoli stalk'], # Broccoli, stalks, raw
    11742: [], # Broccoli, cooked, boiled, drained, with salt
    11743: [], # Broccoli, frozen, chopped, cooked, boiled, drained, with salt
    11744: [], # Broccoli, frozen, spears, cooked, boiled, drained, with salt
    11745: [], # Brussels sprouts, cooked, boiled, drained, with salt
    11746: [], # Brussels sprouts, frozen, cooked, boiled, drained, with salt
    11747: [], # Burdock root, cooked, boiled, drained, with salt
    11748: [], # Butterbur, cooked, boiled, drained, with salt
    11749: ['Cabbage', '', 'Cabbage'], # Cabbage, common (danish, domestic, and pointed types), freshly harvest, raw
    11750: [], # Cabbage, common (danish, domestic, and pointed types), stored, raw
    11751: [], # Cabbage, common, cooked, boiled, drained, with salt
    11752: [], # Cabbage, red, cooked, boiled, drained, with salt
    11753: [], # Cabbage, savoy, cooked, boiled, drained, with salt
    11754: [], # Cabbage, chinese (pak-choi), cooked, boiled, drained, with salt
    11755: [], # Cabbage, chinese (pe-tsai), cooked, boiled, drained, with salt
    11756: [], # Cardoon, cooked, boiled, drained, with salt
    11757: [], # Carrots, cooked, boiled, drained, with salt
    11758: [], # Carrots, canned, no salt added, solids and liquids
    11759: [], # Carrots, canned, no salt added, drained solids
    11760: [], # Carrots, frozen, cooked, boiled, drained, with salt
    11761: [], # Cauliflower, cooked, boiled, drained, with salt
    11762: [], # Cauliflower, frozen, cooked, boiled, drained, with salt
    11763: [], # Celeriac, cooked, boiled, drained, with salt
    11764: [], # Celery, cooked, boiled, drained, with salt
    11765: [], # Chard, swiss, cooked, boiled, drained, with salt
    11766: [], # Chayote, fruit, cooked, boiled, drained, with salt
    11767: [], # Chrysanthemum, garland, cooked, boiled, drained, with salt
    11768: [], # Collards, cooked, boiled, drained, with salt
    11769: [], # Collards, frozen, chopped, cooked, boiled, drained, with salt
    11770: [], # Corn, sweet, yellow, cooked, boiled, drained, with salt
    11771: [], # Corn, sweet, yellow, canned, no salt added, solids and liquids (Includes foods for USDA's Food Distribution Program)
    11772: [], # Corn, sweet, yellow, canned, cream style, no salt added
    11773: [], # Corn, sweet, yellow, canned, vacuum pack, no salt added
    11774: [], # Corn, sweet, yellow, frozen, kernels, cut off cob, boiled, drained, with salt
    11775: [], # Corn, sweet, yellow, frozen, kernels on cob, cooked, boiled, drained, with salt
    11777: [], # Cowpeas (blackeyes), immature seeds, cooked, boiled, drained, with salt
    11778: [], # Cowpeas (blackeyes), immature seeds, frozen, cooked, boiled, drained, with salt
    11779: [], # Cowpeas, young pods with seeds, cooked, boiled, drained, with salt
    11780: [], # Cowpeas, leafy tips, cooked, boiled, drained, with salt
    11781: [], # Cress, garden, cooked, boiled, drained, with salt
    11782: [], # Dandelion greens, cooked, boiled, drained, with salt
    11783: [], # Eggplant, cooked, boiled, drained, with salt
    11784: [], # Gourd, white-flowered (calabash), cooked, boiled, drained, with salt
    11785: [], # Gourd, dishcloth (towelgourd), cooked, boiled, drained, with salt
    11786: [], # Drumstick leaves, cooked, boiled, drained, with salt
    11787: [], # Drumstick pods, cooked, boiled, drained, with salt
    11788: [], # Hyacinth-beans, immature seeds, cooked, boiled, drained, with salt
    11789: [], # Jute, potherb, cooked, boiled, drained, with salt
    11790: [], # Kale, cooked, boiled, drained, with salt
    11791: [], # Kale, frozen, cooked, boiled, drained, with salt
    11793: [], # Kohlrabi, cooked, boiled, drained, with salt
    11794: [], # Lambsquarters, cooked, boiled, drained, with salt
    11795: [], # Leeks, (bulb and lower leaf-portion), cooked, boiled, drained, with salt
    11796: [], # Lotus root, cooked, boiled, drained, with salt
    11797: [], # Mushrooms, white, cooked, boiled, drained, with salt
    11798: [], # Mushrooms, shiitake, cooked, with salt
    11799: [], # Mustard greens, cooked, boiled, drained, with salt
    11800: [], # Mustard greens, frozen, cooked, boiled, drained, with salt
    11801: [], # Mustard spinach, (tendergreen), cooked, boiled, drained, with salt
    11802: [], # New zealand spinach, cooked, boiled, drained, with salt
    11803: [], # Okra, cooked, boiled, drained, with salt
    11804: [], # Okra, frozen, cooked, boiled, drained, with salt
    11805: [], # Onions, cooked, boiled, drained, with salt
    11806: [], # Onions, frozen, chopped, cooked, boiled, drained, with salt
    11807: [], # Onions, frozen, whole, cooked, boiled, drained, with salt
    11808: [], # Parsnips, cooked, boiled, drained, with salt
    11809: [], # Peas, edible-podded, cooked, boiled, drained, with salt
    11810: [], # Peas, edible-podded, frozen, cooked, boiled, drained, with salt
    11811: [], # Peas, green, cooked, boiled, drained, with salt
    11812: [], # Peas, green, canned, no salt added, solids and liquids
    11813: [], # Peas, green, canned, no salt added, drained solids
    11814: [], # Peas, green, frozen, cooked, boiled, drained, with salt
    11815: [], # Peas, mature seeds, sprouted, cooked, boiled, drained, with salt
    11816: [], # Peas and carrots, canned, no salt added, solids and liquids
    11817: [], # Peas and carrots, frozen, cooked, boiled, drained, with salt
    11818: [], # Peas and onions, frozen, cooked, boiled, drained, with salt
    11819: ['Red hot chili pepper', '', 'californication.mp3'], # Peppers, hot chili, red, raw
    11820: [], # Peppers, hot chili, red, canned, excluding seeds, solids and liquids
    11821: ['Red pepper', 'sweet'], # Peppers, sweet, red, raw
    11822: [], # Peppers, sweet, green, cooked, boiled, drained, with salt
    11823: [], # Peppers, sweet, red, cooked, boiled, drained, without salt
    11824: [], # Peppers, sweet, red, cooked, boiled, drained, with salt
    11825: [], # Peppers, sweet, green, frozen, chopped, cooked, boiled, drained, with salt
    11826: [], # Pigeonpeas, immature seeds, cooked, boiled, drained, with salt
    11827: [], # Pokeberry shoots, (poke), cooked, boiled, drained, with salt
    11828: [], # Potatoes, baked, flesh and skin, with salt
    11829: [], # Potatoes, baked, flesh, with salt
    11830: [], # Potatoes, baked, skin only, with salt
    11831: [], # Potatoes, boiled, cooked in skin, flesh, with salt
    11832: [], # Potatoes, boiled, cooked in skin, skin, with salt
    11833: [], # Potatoes, boiled, cooked without skin, flesh, with salt
    11834: [], # Potatoes, microwaved, cooked, in skin, flesh and skin, with salt
    11835: [], # Potatoes, microwaved, cooked in skin, flesh, with salt
    11836: [], # Potatoes, microwaved, cooked, in skin, skin with salt
    11837: [], # Potatoes, frozen, whole, cooked, boiled, drained, with salt
    11840: [], # Potatoes, frozen, french fried, par fried, cottage-cut, prepared, heated in oven, with salt
    11841: [], # Potatoes, french fried, all types, salt not added in processing, frozen, oven-heated
    11842: [], # Potatoes, french fried, all types, salt not added in processing, frozen, as purchased
    11843: [], # Potatoes, au gratin, home-prepared from recipe using margarine
    11844: [], # Potatoes, scalloped, home-prepared with margarine
    11845: [], # Pumpkin, cooked, boiled, drained, with salt
    11846: [], # Pumpkin, canned, with salt
    11847: [], # Pumpkin, flowers, cooked, boiled, drained, with salt
    11848: [], # Pumpkin leaves, cooked, boiled, drained, with salt
    11849: [], # Purslane, cooked, boiled, drained, with salt
    11850: [], # Radishes, oriental, cooked, boiled, drained, with salt
    11851: [], # Rutabagas, cooked, boiled, drained, with salt
    11852: [], # Salsify, cooked, boiled, drained, with salt
    11853: [], # Soybeans, green, cooked, boiled, drained, with salt
    11854: [], # Spinach, cooked, boiled, drained, with salt
    11855: [], # Spinach, canned, no salt added, solids and liquids
    11856: [], # Spinach, frozen, chopped or leaf, cooked, boiled, drained, with salt
    11857: [], # Squash, summer, all varieties, cooked, boiled, drained, with salt
    11858: [], # Squash, summer, crookneck and straightneck, cooked, boiled, drained, with salt
    11859: [], # Squash, summer, crookneck and straightneck, frozen, cooked, boiled, drained, with salt
    11860: [], # Squash, summer, scallop, cooked, boiled, drained, with salt
    11861: [], # Squash, summer, zucchini, includes skin, cooked, boiled, drained, with salt
    11862: [], # Squash, summer, zucchini, includes skin, frozen, cooked, boiled, drained, with salt
    11863: [], # Squash, winter, all varieties, cooked, baked, with salt
    11864: [], # Squash, winter, acorn, cooked, baked, with salt
    11865: [], # Squash, winter, acorn, cooked, boiled, mashed, with salt
    11866: [], # Squash, winter, butternut, cooked, baked, with salt
    11867: [], # Squash, winter, butternut, frozen, cooked, boiled, with salt
    11868: [], # Squash, winter, hubbard, baked, with salt
    11869: [], # Squash, winter, hubbard, cooked, boiled, mashed, with salt
    11870: [], # Squash, winter, spaghetti, cooked, boiled, drained, or baked, with salt
    11871: [], # Succotash, (corn and limas), cooked, boiled, drained, with salt
    11872: [], # Succotash, (corn and limas), frozen, cooked, boiled, drained, with salt
    11873: [], # Water convolvulus, cooked, boiled, drained, with salt
    11874: [], # Sweet potato leaves, cooked, steamed, with salt
    11875: [], # Sweet potato, cooked, baked in skin, flesh, with salt
    11876: [], # Sweet potato, cooked, boiled, without skin, with salt
    11877: [], # Sweet potato, frozen, cooked, baked, with salt
    11878: [], # Taro, cooked, with salt
    11879: [], # Taro, leaves, cooked, steamed, with salt
    11880: [], # Taro, shoots, cooked, with salt
    11881: [], # Taro, tahitian, cooked, with salt
    11884: [], # Tomatoes, red, ripe, cooked, with salt
    11885: [], # Tomatoes, red, ripe, canned, packed in tomato juice, no salt added
    11886: [], # Tomato juice, canned, without salt added
    11888: [], # Tomato products, canned, puree, with salt added
    11889: [], # Turnips, cooked, boiled, drained, with salt
    11890: [], # Turnips, frozen, cooked, boiled, drained, with salt
    11891: [], # Turnip greens, cooked, boiled, drained, with salt
    11892: [], # Turnip greens, frozen, cooked, boiled, drained, with salt
    11893: [], # Turnip greens and turnips, frozen, cooked, boiled, drained, with salt
    11894: [], # Vegetables, mixed, frozen, cooked, boiled, drained, with salt
    11895: [], # Waxgourd, (chinese preserving melon), cooked, boiled, drained, with salt
    11896: [], # Winged bean, immature seeds, cooked, boiled, drained, with salt
    11897: [], # Yam, cooked, boiled, drained, or baked, with salt
    11898: [], # Yambean (jicama), cooked, boiled, drained, with salt
    11899: [], # Yardlong bean, cooked, boiled, drained, with salt
    11900: ['Sweet corn', 'white'], # Corn, sweet, white, raw
    11901: [], # Corn, sweet, white, cooked, boiled, drained, without salt
    11902: [], # Corn, sweet, white, cooked, boiled, drained, with salt
    11903: [], # Corn, sweet, white, canned, whole kernel, regular pack, solids and liquids
    11904: [], # Corn, sweet, white, canned, whole kernel, no salt added, solids and liquids
    11905: [], # Corn, sweet, white, canned, whole kernel, drained solids
    11906: [], # Corn, sweet, white, canned, cream style, regular pack
    11907: [], # Corn, sweet, white, canned, cream style, no salt added
    11908: [], # Corn, sweet, white, canned, vacuum pack, regular pack
    11909: [], # Corn, sweet, white, canned, vacuum pack, no salt added
    11910: [], # Corn, sweet, white, frozen, kernels cut off cob, unprepared
    11911: [], # Corn, sweet, white, frozen, kernels cut off cob, boiled, drained, without salt
    11912: [], # Corn, sweet, white, frozen, kernels cut off cob, boiled, drained, with salt
    11913: [], # Corn, sweet, white, frozen, kernels on cob, unprepared
    11914: [], # Corn, sweet, white, frozen, kernels on cob, cooked, boiled, drained, without salt
    11915: [], # Corn, sweet, white, frozen, kernels on cob, cooked, boiled, drained, with salt
    11916: [], # Peppers, sweet, red, canned, solids and liquids
    11917: [], # Peppers, sweet, red, frozen, chopped, unprepared
    11918: [], # Peppers, sweet, red, frozen, chopped, boiled, drained, without salt
    11919: [], # Peppers, sweet, red, frozen, chopped, boiled, drained, with salt
    11921: [], # Peppers, sweet, red, sauteed
    11922: [], # Sesbania flower, cooked, steamed, with salt
    11923: [], # Soybeans, mature seeds, sprouted, cooked, steamed, with salt
    11924: [], # Soybeans, mature seeds, sprouted, cooked, stir-fried, with salt
    11925: [], # Dock, cooked, boiled, drained, with salt
    11926: [], # Lentils, sprouted, cooked, stir-fried, with salt
    11927: [], # Mountain yam, hawaii, cooked, steamed, with salt
    11928: [], # Tree fern, cooked, with salt
    11929: [], # Potatoes, mashed, prepared from granules, without milk, whole milk and margarine
    11930: [], # Potatoes, mashed, dehydrated, prepared from flakes without milk, whole milk and margarine added
    11931: [], # Peppers, sweet, red, freeze-dried
    11932: [], # Beans, snap, yellow, canned, regular pack, drained solids
    11933: [], # Beans, snap, yellow, canned, no salt added, drained solids
    11934: [], # Potatoes, mashed, home-prepared, whole milk and butter added
    11935: ["Catsup", "", "Ketchup"], # Catsup
    11936: [], # Mushrooms, brown, italian, or crimini, exposed to ultraviolet light, raw
    11937: [], # Pickles, cucumber, dill or kosher dill
    11938: [], # Mushroom, white, exposed to ultraviolet light, raw
    11939: [], # Mushrooms, portabella, exposed to ultraviolet light, grilled
    11940: [], # Pickles, cucumber, sweet (includes bread and butter pickles)
    11941: [], # Pickles, cucumber, sour
    11943: [], # Pimento, canned
    11944: [], # Pickle relish, hot dog
    11945: [], # Pickle relish, sweet
    11946: [], # Pickles, cucumber, sour, low sodium
    11947: [], # Pickles, cucumber, dill, reduced sodium
    11948: [], # Pickles, cucumber, sweet, low sodium (includes bread and butter pickles)
    11949: [], # Catsup, low sodium
    11950: ['Enoki mushroom'], # Mushrooms, enoki, raw
    11951: ['Yellow pepper', 'sweet'], # Peppers, sweet, yellow, raw
    11952: ['Radicchio'], # Radicchio, raw
    11953: [], # Squash, zucchini, baby, raw
    11954: ['Tomatillo'], # Tomatillos, raw
    11955: [], # Tomatoes, sun-dried
    11956: [], # Tomatoes, sun-dried, packed in oil, drained
    11957: ['Fennel', 'bulb'], # Fennel, bulb, raw
    11958: [], # Pickle relish, hamburger
    11959: ['Arugula'], # Arugula, raw
    11960: ['Baby carrot'], # Carrots, baby, raw
    11961: [], # Hearts of palm, canned
    11962: [], # Peppers, hot chile, sun-dried
    11963: ['Nopales'], # Nopales, raw
    11964: [], # Nopales, cooked, without salt
    11965: ['Cauliflower', 'green'], # Cauliflower, green, raw
    11967: [], # Cauliflower, green, cooked, no salt added
    11968: [], # Cauliflower, green, cooked, with salt
    11969: [], # Broccoli, chinese, cooked
    11970: [], # Cabbage, napa, cooked
    11972: ['Lemon grass', '', 'Citronella'], # Lemon grass (citronella), raw
    11973: ['Fava bean'], # Beans, fava, in pod, raw
    11974: ['Grape leaf'], # Grape leaves, raw
    11975: [], # Grape leaves, canned
    11976: ['Banana pepper'], # Pepper, banana, raw
    11977: ['Serrano pepper'], # Peppers, serrano, raw
    11978: [], # Peppers, ancho, dried
    11979: ['Jalapeno pepper'], # Peppers, jalapeno, raw
    11980: [], # Peppers, chili, green, canned
    11981: ['Hungarian pepper'], # Peppers, hungarian, raw
    11982: [], # Peppers, pasilla, dried
    11983: [], # Pickles, chowchow, with cauliflower onion mustard, sweet
    11984: ['Epazote'], # Epazote, raw
    11985: ['Fireweed'], # Fireweed, leaves, raw
    11986: [], # Malabar spinach, cooked
    11987: ['Oyster mushroom'], # Mushrooms, oyster, raw
    11988: [], # Fungi, Cloud ears, dried
    11989: [], # Mushrooms, straw, canned, drained solids
    11990: ['Wasabi', 'root'], # Wasabi, root, raw
    11991: ['Yautia', '', 'Tannier'], # Yautia (tannier), raw
    11992: [], # Mushrooms, white, microwaved
    11993: ['Maitake mushroom'], # Mushrooms, maitake, raw
    11994: ['Broccoli', 'chinese'], # Broccoli, chinese, raw
    11995: ['Fiddlehead fern'], # Fiddlehead ferns, raw
    11996: [], # Fiddlehead ferns, frozen, unprepared
    11998: [], # Mushrooms, portabella, exposed to ultraviolet light, raw
    12001: ['Breadfruit seed'], # Seeds, breadfruit seeds, raw
    12003: [], # Seeds, breadfruit seeds, boiled
    12004: ['Breadnut tree seed'], # Seeds, breadnut tree seeds, raw
    12005: [], # Seeds, breadnut tree seeds, dried
    12006: [], # Seeds, chia seeds, dried
    12007: [], # Seeds, cottonseed flour, partially defatted (glandless)
    12008: [], # Seeds, cottonseed flour, low fat (glandless)
    12011: [], # Seeds, cottonseed meal, partially defatted (glandless)
    12012: [], # Seeds, hemp seed, hulled
    12013: [], # Seeds, lotus seeds, dried
    12014: [], # Seeds, pumpkin and squash seed kernels, dried
    12016: [], # Seeds, pumpkin and squash seed kernels, roasted, without salt
    12021: [], # Seeds, safflower seed kernels, dried
    12022: [], # Seeds, safflower seed meal, partially defatted
    12023: [], # Seeds, sesame seeds, whole, dried
    12024: [], # Seeds, sesame seeds, whole, roasted and toasted
    12029: [], # Seeds, sesame seed kernels, toasted, without salt added (decorticated)
    12032: [], # Seeds, sesame flour, partially defatted
    12033: [], # Seeds, sesame flour, low-fat
    12034: [], # Seeds, sesame meal, partially defatted
    12036: [], # Seeds, sunflower seed kernels, dried
    12037: [], # Seeds, sunflower seed kernels, dry roasted, without salt
    12038: [], # Seeds, sunflower seed kernels, oil roasted, without salt
    12039: [], # Seeds, sunflower seed kernels, toasted, without salt
    12040: [], # Seeds, sunflower seed butter, without salt
    12041: [], # Seeds, sunflower seed flour, partially defatted
    12058: ['Acorn nut'], # Nuts, acorns, raw
    12059: [], # Nuts, acorns, dried
    12060: [], # Nuts, acorn flour, full fat
    12061: ["Almond"], # Nuts, almonds
    12062: [], # Nuts, almonds, blanched
    12063: [], # Nuts, almonds, dry roasted, without salt added
    12065: [], # Nuts, almonds, oil roasted, without salt added
    12071: [], # Nuts, almond paste
    12077: [], # Nuts, beechnuts, dried
    12078: [], # Nuts, brazilnuts, dried, unblanched
    12084: [], # Nuts, butternuts, dried
    12085: [], # Nuts, cashew nuts, dry roasted, without salt added
    12086: [], # Nuts, cashew nuts, oil roasted, without salt added
    12087: ['Cashew nut'], # Nuts, cashew nuts, raw
    12088: [], # Nuts, cashew butter, plain, without salt added
    12093: ['Chestnut', 'chinese'], # Nuts, chestnuts, chinese, raw
    12094: [], # Nuts, chestnuts, chinese, dried
    12095: [], # Nuts, chestnuts, chinese, boiled and steamed
    12096: [], # Nuts, chestnuts, chinese, roasted
    12097: ['Chestnut', 'european'], # Nuts, chestnuts, european, raw, unpeeled
    12098: [], # Nuts, chestnuts, european, raw, peeled
    12099: [], # Nuts, chestnuts, european, dried, unpeeled
    12100: [], # Nuts, chestnuts, european, dried, peeled
    12101: [], # Nuts, chestnuts, european, boiled and steamed
    12104: ['Coconut meat'], # Nuts, coconut meat, raw
    12108: [], # Nuts, coconut meat, dried (desiccated), not sweetened
    12109: [], # Nuts, coconut meat, dried (desiccated), sweetened, flaked, packaged
    12110: [], # Nuts, coconut meat, dried (desiccated), sweetened, flaked, canned
    12114: [], # Nuts, coconut meat, dried (desiccated), toasted
    12115: [], # Nuts, coconut cream, raw (liquid expressed from grated meat)
    12116: [], # Nuts, coconut cream, canned, sweetened
    12117: ['Coconut milk'], # Nuts, coconut milk, raw (liquid expressed from grated meat and water)
    12118: [], # Nuts, coconut milk, canned (liquid expressed from grated meat and water)
    12119: [], # Nuts, coconut water (liquid from coconuts)
    12120: ["Hazelnut", "", "Filbert"], # Nuts, hazelnuts or filberts
    12121: [], # Nuts, hazelnuts or filberts, blanched
    12122: [], # Nuts, hazelnuts or filberts, dry roasted, without salt added
    12127: ['Ginkgo nut'], # Nuts, ginkgo nuts, raw
    12128: [], # Nuts, ginkgo nuts, dried
    12129: [], # Nuts, ginkgo nuts, canned
    12130: [], # Nuts, hickorynuts, dried
    12131: ['Macadamia nut'], # Nuts, macadamia nuts, raw
    12132: [], # Nuts, macadamia nuts, dry roasted, without salt added
    12135: [], # Nuts, mixed nuts, dry roasted, with peanuts, without salt added
    12136: [], # Nuts, mixed nuts, dry roasted, with peanuts, salt added, PLANTERS pistachio blend
    12137: [], # Nuts, mixed nuts, oil roasted, with peanuts, without salt added
    12138: [], # Nuts, mixed nuts, oil roasted, without peanuts, without salt added
    12140: [], # Nuts, formulated, wheat-based, unflavored, with salt added
    12141: [], # Nuts, mixed nuts, dry roasted, with peanuts, salt added, CHOSEN ROASTER
    12142: [], # Nuts, pecans
    12143: [], # Nuts, pecans, dry roasted, without salt added
    12144: [], # Nuts, pecans, oil roasted, without salt added
    12145: [], # Nuts, pilinuts, dried
    12147: [], # Nuts, pine nuts, dried
    12149: [], # Nuts, pine nuts, pinyon, dried
    12151: ['Pistachio nut'], # Nuts, pistachio nuts, raw
    12152: [], # Nuts, pistachio nuts, dry roasted, without salt added
    12154: [], # Nuts, walnuts, black, dried
    12155: [], # Nuts, walnuts, english
    12156: [], # Nuts, walnuts, glazed
    12157: [], # Nuts, walnuts, dry roasted, with salt added
    12158: [], # Seeds, breadfruit seeds, roasted
    12160: [], # Seeds, cottonseed kernels, roasted (glandless)
    12163: [], # Seeds, pumpkin and squash seeds, whole, roasted, without salt
    12166: [], # Seeds, sesame butter, tahini, from roasted and toasted kernels (most common type)
    12167: [], # Nuts, chestnuts, european, roasted
    12169: [], # Seeds, sesame butter, paste
    12170: [], # Seeds, sesame flour, high-fat
    12171: [], # Seeds, sesame butter, tahini, from unroasted kernels (non-chemically removed seed coat)
    12174: [], # Seeds, watermelon seed kernels, dried
    12175: [], # Nuts, chestnuts, japanese, dried
    12176: [], # Nuts, coconut milk, frozen (liquid expressed from grated meat and water)
    12177: [], # Nuts, coconut meat, dried (desiccated), creamed
    12179: [], # Nuts, coconut meat, dried (desiccated), sweetened, shredded
    12193: [], # Seeds, sisymbrium sp. seeds, whole, dried
    12195: [], # Nuts, almond butter, plain, without salt added
    12198: [], # Seeds, sesame butter, tahini, from raw and stone ground kernels
    12200: [], # Nuts, formulated, wheat-based, all flavors except macadamia, without salt
    12201: [], # Seeds, sesame seed kernels, dried (decorticated)
    12202: ['Chestnut', 'japanese'], # Nuts, chestnuts, japanese, raw
    12203: [], # Nuts, chestnuts, japanese, boiled and steamed
    12204: [], # Nuts, chestnuts, japanese, roasted
    12205: ['Lotus seed'], # Seeds, lotus seeds, raw
    12206: [], # Nuts, almonds, honey roasted, unblanched
    12220: [], # Seeds, flaxseed
    12516: [], # Seeds, pumpkin and squash seed kernels, roasted, with salt added
    12529: [], # Seeds, sesame seed kernels, toasted, with salt added (decorticated)
    12536: [], # Seeds, sunflower seed kernels from shell, dry roasted, with salt added
    12537: [], # Seeds, sunflower seed kernels, dry roasted, with salt added
    12538: [], # Seeds, sunflower seed kernels, oil roasted, with salt added
    12539: [], # Seeds, sunflower seed kernels, toasted, with salt added
    12540: [], # Seeds, sunflower seed butter, with salt added (Includes foods for USDA's Food Distribution Program)
    12563: [], # Nuts, almonds, dry roasted, with salt added
    12565: [], # Nuts, almonds, oil roasted, with salt added
    12567: [], # Nuts, almonds, oil roasted, with salt added, smoke flavor
    12585: [], # Nuts, cashew nuts, dry roasted, with salt added
    12586: [], # Nuts, cashew nuts, oil roasted, with salt added
    12588: [], # Nuts, cashew butter, plain, with salt added
    12632: [], # Nuts, macadamia nuts, dry roasted, with salt added
    12635: [], # Nuts, mixed nuts, dry roasted, with peanuts, with salt added
    12637: [], # Nuts, mixed nuts, oil roasted, with peanuts, with salt added
    12638: [], # Nuts, mixed nuts, oil roasted, without peanuts, with salt added
    12643: [], # Nuts, pecans, dry roasted, with salt added
    12644: [], # Nuts, pecans, oil roasted, with salt added
    12652: [], # Nuts, pistachio nuts, dry roasted, with salt added
    12663: [], # Seeds, pumpkin and squash seeds, whole, roasted, with salt added
    12665: [], # Nuts, almonds, oil roasted, lightly salted
    12695: [], # Nuts, almond butter, plain, with salt added
    12698: [], # Seeds, sesame butter, tahini, type of kernels unspecified
    12737: [], # Nuts, mixed nuts, oil roasted, with peanuts, lightly salted
    12738: [], # Nuts, mixed nuts, oil roasted, without peanuts, lightly salted
    13000: ['Beef strip steak'], # Beef, grass-fed, strip steaks, lean only, raw
    13001: ['Beef carcass'], # Beef, carcass, separable lean and fat, choice, raw
    13002: [], # Beef, carcass, separable lean and fat, select, raw
    13019: [], # Beef, retail cuts, separable fat, raw
    13020: [], # Beef, retail cuts, separable fat, cooked
    13023: [], # Beef, brisket, whole, separable lean only, all grades, raw
    13047: ['Beef', 'ground boneless'], # Beef, grass-fed, ground, raw
    13055: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, select, cooked, braised
    13065: ['Beef flank steak'], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, choice, raw
    13066: [], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    13067: [], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, broiled
    13068: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, choice, raw
    13069: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13070: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13095: [], # Beef, rib, eye, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, choice, raw
    13096: [], # Beef, rib, eye, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, choice, cooked, broiled
    13097: [], # Beef, rib, eye, small end (ribs 10-12), separable lean only, trimmed to 0" fat, choice, raw
    13098: [], # Beef, rib, eye, small end (ribs 10-12), separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13147: ['Beef shortrib'], # Beef, rib, shortribs, separable lean and fat, choice, raw
    13148: [], # Beef, rib, shortribs, separable lean and fat, choice, cooked, braised
    13149: [], # Beef, rib, shortribs, separable lean only, choice, raw
    13150: [], # Beef, rib, shortribs, separable lean only, choice, cooked, braised
    13156: [], # Beef, round, full cut, separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    13158: [], # Beef, round, full cut, separable lean only, trimmed to 1/4" fat, select, cooked, broiled
    13165: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    13227: [], # Beef, shank crosscuts, separable lean only, trimmed to 1/4" fat, choice, raw
    13228: [], # Beef, shank crosscuts, separable lean only, trimmed to 1/4" fat, choice, cooked, simmered
    13231: ['Beef porterhouse steak'], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8" fat, choice, raw
    13232: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    13235: ['Beef t-bone steak'], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, choice, raw
    13236: [], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    13284: ['Beef rib eye'], # Beef, rib eye, small end (ribs 10-12), separable lean only, trimmed to 0" fat, select, raw
    13285: [], # Beef, chuck, under blade pot roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13293: [], # Beef, chuck, under blade pot roast or steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    13294: [], # Beef, chuck, under blade pot roast or steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    13317: [], # Beef, ground, patties, frozen, cooked, broiled
    13318: ['Beef brain'], # Beef, variety meats and by-products, brain, raw
    13319: [], # Beef, variety meats and by-products, brain, cooked, pan-fried
    13320: [], # Beef, variety meats and by-products, brain, cooked, simmered
    13321: ['Beef heart'], # Beef, variety meats and by-products, heart, raw
    13322: [], # Beef, variety meats and by-products, heart, cooked, simmered
    13323: ['Beef kidney'], # Beef, variety meats and by-products, kidneys, raw
    13324: [], # Beef, variety meats and by-products, kidneys, cooked, simmered
    13325: ['Beef liver'], # Beef, variety meats and by-products, liver, raw
    13326: [], # Beef, variety meats and by-products, liver, cooked, braised
    13327: [], # Beef, variety meats and by-products, liver, cooked, pan-fried
    13328: ['Beef lung'], # Beef, variety meats and by-products, lungs, raw
    13329: [], # Beef, variety meats and by-products, lungs, cooked, braised
    13330: [], # Beef, variety meats and by-products, mechanically separated beef, raw
    13331: ['Beef pancreas'], # Beef, variety meats and by-products, pancreas, raw
    13332: [], # Beef, variety meats and by-products, pancreas, cooked, braised
    13333: ['Beef spleen'], # Beef, variety meats and by-products, spleen, raw
    13334: [], # Beef, variety meats and by-products, spleen, cooked, braised
    13335: ['Beef suet'], # Beef, variety meats and by-products, suet, raw
    13337: ['Beef thymus'], # Beef, variety meats and by-products, thymus, raw
    13338: [], # Beef, variety meats and by-products, thymus, cooked, braised
    13339: ['Beef tongue'], # Beef, variety meats and by-products, tongue, raw
    13340: [], # Beef, variety meats and by-products, tongue, cooked, simmered
    13341: ['Beef tripe'], # Beef, variety meats and by-products, tripe, raw
    13342: [], # Beef, sandwich steaks, flaked, chopped, formed and thinly sliced, raw
    13343: [], # Beef, brisket, flat half, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13344: ['Beef cured'], # Beef, cured, breakfast strips, raw or unheated
    13345: [], # Beef, cured, breakfast strips, cooked
    13346: [], # Beef, cured, corned beef, brisket, raw
    13347: [], # Beef, cured, corned beef, brisket, cooked
    13348: [], # Beef, cured, corned beef, canned
    13349: ['Beef chuck', 'boneless'], # Beef, chuck, under blade pot roast or steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    13350: [], # Beef, cured, dried
    13351: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    13352: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13353: [], # Beef, cured, luncheon meat, jellied
    13354: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13355: [], # Beef, cured, pastrami
    13356: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, all grades, raw
    13357: [], # Sausage, beef, cured, cooked, smoked
    13358: [], # Beef, chopped, cured, smoked
    13359: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, choice, raw
    13361: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, all grades, cooked
    13362: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, choice, cooked
    13363: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, select, cooked
    13364: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, all grades, cooked
    13365: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, choice, cooked
    13366: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, select, cooked
    13367: [], # Beef, brisket, whole, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13368: [], # Beef, brisket, whole, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13369: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13370: [], # Beef, brisket, flat half, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13371: [], # Beef, brisket, point half, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13372: [], # Beef, brisket, point half, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13373: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13375: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    13377: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13378: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 0" fat, select, cooked, braised
    13379: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13380: [], # Beef, chuck, under blade pot roast, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    13381: [], # Beef, chuck, under blade pot roast, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    13382: [], # Beef, chuck, blade roast, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13383: [], # Beef, chuck, under blade pot roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13384: [], # Beef, chuck, under blade pot roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    13386: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    13387: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    13388: [], # Beef, rib, large end (ribs 6-9), separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    13389: [], # Beef, rib, large end (ribs 6-9), separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13390: [], # Beef, rib, large end (ribs 6-9), separable lean only, trimmed to 0" fat, select, cooked, roasted
    13391: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13392: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, choice, cooked, broiled
    13393: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, select, cooked, broiled
    13394: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    13395: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13396: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 0" fat, select, cooked, broiled
    13398: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13399: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    13401: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    13402: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    13404: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    13405: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    13407: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13408: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    13410: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13411: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13413: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 0" fat, select, cooked, braised
    13414: [], # Beef, round, bottom round roast, separable lean only, trimmed to 0" fat, select, cooked, roasted
    13415: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    13416: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    13417: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    13418: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    13419: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13420: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, roasted
    13421: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    13422: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    13423: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    13424: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    13425: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13426: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, select, cooked, roasted
    13428: [], # Beef, round, top round, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    13430: [], # Beef, round, top round, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    13432: [], # Beef, round, top round, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    13436: [], # Beef, round, top round, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13438: [], # Beef, round, top round, separable lean only, trimmed to 0" fat, select, cooked, braised
    13439: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    13440: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    13441: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    13442: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    13443: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13444: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13445: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    13446: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    13447: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    13448: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    13449: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13450: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13451: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13452: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, broiled
    13453: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 0" fat, select, cooked, broiled
    13454: [], # Beef, top sirloin, steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    13455: [], # Beef, top sirloin, steak, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13456: [], # Beef, top sirloin, steak, separable lean only, trimmed to 0" fat, select, cooked, broiled
    13459: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13460: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 0" fat, USDA choice, cooked, broiled
    13463: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 0" fat, USDA select, cooked, broiled
    13464: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8" fat, all grades, raw
    13465: [], # Beef, short loin, porterhouse steak, separable lean only,  trimmed to 1/8" fat, all grades, cooked, grilled
    13466: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    13467: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13468: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8" fat, select, raw
    13469: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    13470: [], # Beef, short loin, porterhouse steak, separable lean only, trimmed to 0" fat, select, cooked, broiled
    13473: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13474: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 0" fat, USDA choice, cooked, broiled
    13477: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 0" fat, USDA select, cooked, broiled
    13478: [], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, all grades, raw
    13479: [], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    13481: [], # Beef, short loin, t-bone steak, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13482: [], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, select, raw
    13483: [], # Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    13484: [], # Beef, short loin, t-bone steak, separable lean only, trimmed to 0" fat, select, cooked, broiled
    13485: [], # Beef, brisket, flat half, separable lean only, trimmed to 0" fat, select, cooked, braised
    13486: ['Beef tip round'], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, all grades, raw
    13487: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, choice, raw
    13488: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 0" fat, select, raw
    13490: [], # Beef, rib, eye, small end (ribs 10- 12) separable lean only, trimmed to 0" fat, select, cooked, broiled
    13491: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    13492: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13493: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13494: [], # Beef, ground, 70% lean meat / 30% fat, crumbles, cooked, pan-browned
    13495: [], # Beef, ground, 70% lean meat / 30% fat, loaf, cooked, baked
    13496: [], # Beef, ground, 70% lean meat / 30% fat, patty cooked, pan-broiled
    13497: [], # Beef, ground, 70% lean meat / 30% fat, patty, cooked, broiled
    13498: ['Beef', 'ground boneless 70% 30%'], # Beef, ground, 70% lean meat / 30% fat, raw
    13499: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean only, trimmed to 0" fat, select, raw
    13500: [], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    13501: [], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13502: [], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13519: ['Beef shoulder top blade steak'], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    13520: [], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    13523: [], # Beef, shoulder top blade steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    13595: ['Beef brisket', 'boneless'], # Beef, brisket, flat half, boneless separable lean only, trimmed to 0" fat, all grades, raw
    13596: [], # Beef, brisket, flat half, boneless, separable lean only, trimmed to 0" fat, choice, raw
    13597: [], # Beef, brisket, flat half, boneless, separable lean only, trimmed to 0" fat, select, raw
    13598: [], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    13647: ['Beef shoulder pot roast'], # Beef, shoulder pot roast or steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    13648: [], # Beef, shoulder pot roast or steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    13649: [], # Beef, shoulder pot roast or steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    13650: [], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    13786: ['Beef chuck eye roast'], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, all grades, raw
    13788: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, choice, raw
    13791: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, select, raw
    13795: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13796: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, all grades, cooked
    13797: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13798: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, choice, cooked
    13799: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, select, raw
    13800: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, select, cooked
    13803: ['Beef brisket', 'whole'], # Beef, brisket, whole, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13804: [], # Beef, brisket, whole, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13805: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13806: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13807: [], # Beef, brisket, point half, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13808: [], # Beef, brisket, point half, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13809: ['Beef arm pot roast'], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13810: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13811: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13812: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    13813: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, select, raw
    13814: [], # Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, braised
    13815: ['Beef blade roast'], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13816: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13817: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13818: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    13819: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, select, raw
    13820: [], # Beef, chuck, blade roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, braised
    13821: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    13822: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13823: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, select, cooked, roasted
    13824: ['Beef rib', 'whole 6-12'], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13825: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13826: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13827: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, choice, raw
    13828: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13829: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13830: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, select, raw
    13831: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13832: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13833: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, prime, raw
    13834: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13835: [], # Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, prime, cooked, roasted
    13838: ['Beef rib', 'large end 6-9'], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13839: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13840: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13841: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, choice, raw
    13842: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13843: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13844: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, select, raw
    13845: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13846: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13847: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, prime, raw
    13848: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13849: [], # Beef, rib, large end (ribs 6-9), separable lean and fat, trimmed to 1/8" fat, prime, cooked, roasted
    13850: ['Beef rib', 'small end 10-12'], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13851: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13852: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13853: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, choice, raw
    13854: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13855: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13856: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, select, raw
    13857: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13858: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13859: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, prime, raw
    13860: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13861: [], # Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, prime, cooked, roasted
    13862: [], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    13863: ['Beef shoulder top blade steak', 'boneless'], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    13864: ['Beef round', 'full cut'], # Beef, round, full cut, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13865: [], # Beef, round, full cut, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13866: [], # Beef, round, full cut, separable lean and fat, trimmed to 1/8" fat, select, raw
    13867: [], # Beef, round, full cut, separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13868: ['Beef round', 'bottom'], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13869: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13870: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13871: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13872: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    13873: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13874: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    13875: [], # Beef, round, bottom round, steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, braised
    13876: [], # Beef, round, bottom round, roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13877: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13878: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13879: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13880: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13881: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, select, raw
    13882: [], # Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13883: ['Beef round', 'tip'], # Beef, round, tip round, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13884: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13885: [], # Beef, round, tip round, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13886: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13887: [], # Beef, round, tip round, separable lean and fat, trimmed to 1/8" fat, select, raw
    13888: [], # Beef, round, tip round, roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13889: [], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    13890: [], # Beef, round, top round, separable lean only, trimmed to 1/8" fat, choice, cooked, pan-fried
    13891: ['Beef round', 'top'], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13892: [], # Beef, round, top round, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, braised
    13893: [], # Beef, round, top round steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13894: [], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13895: [], # Beef, round, top round, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    13896: [], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13897: [], # Beef, round, top round, separable lean and fat, trimmed to 1/8" fat, choice, cooked, pan-fried
    13898: [], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    13899: [], # Beef, round, top round, separable lean and fat, trimmed to 1/8" fat, select, cooked, braised
    13900: [], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13901: [], # Beef, round, top round, separable lean and fat, trimmed to 1/8" fat, prime, raw
    13902: [], # Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13903: [], # Beef, shoulder top blade steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    13904: ['Beef brisket', 'flat half'], # Beef, brisket, flat half, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    13905: ['Beef short loin', 'porterhouse steak'], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13906: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    13907: ['Beef short loin', 't-bone steak'], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13908: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    13909: ['Beef short loin', 'top'], # Beef, short loin, top loin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13910: [], # Beef, loin, top loin, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    13911: [], # Beef, loin, top loin, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13912: [], # Beef, short loin, top loin, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    13913: [], # Beef, loin, top loin, separable lean and fat, trimmed to 1/8" fat, select, raw
    13914: [], # Beef, loin, top loin, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    13915: [], # Beef, short loin, top loin, steak, separable lean and fat, trimmed to 1/8" fat, prime, raw
    13916: [], # Beef, short loin, top loin, separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13917: ['Beef tenderloin', 'steak', 'Beef steak'], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13918: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13919: [], # Beef, tenderloin, roast, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    13920: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13921: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13922: [], # Beef, tenderloin, roast, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    13923: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    13924: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13925: [], # Beef, tenderloin, roast, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    13926: [], # Beef, tenderloin, separable lean and fat, trimmed to 1/8" fat, prime, raw
    13927: [], # Beef, tenderloin, steak, separable lean and fat, trimmed to 1/8" fat, prime, cooked, broiled
    13928: [], # Beef, tenderloin, roast, separable lean and fat, trimmed to 1/8" fat, prime, cooked, roasted
    13929: ['Beef top sirloin', 'steak'], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    13930: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, broiled
    13931: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, choice, raw
    13932: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    13933: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, choice, cooked, pan-fried
    13934: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    13935: [], # Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, broiled
    13937: [], # Beef, chuck, clod roast, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    13940: [], # Beef, chuck, clod roast, separable lean only, trimmed to 0" fat, select, cooked, roasted
    13943: [], # Beef, shoulder steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    13946: [], # Beef, shoulder steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    13948: [], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13949: [], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, select, cooked, broiled
    13950: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    13951: [], # Beef, rib eye, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, select, cooked, broiled
    13952: [], # Beef, rib eye, small end (ribs 10-12), separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    13953: [], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    13954: ['Beef bottom sirloin', 'tri-tip roast'], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, all grades, raw
    13955: [], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    13956: [], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, choice, raw
    13957: [], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    13958: [], # Beef, bottom sirloin, tri-tip roast, separable lean and fat, trimmed to 0" fat, select, raw
    13959: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    13961: [], # Beef, chuck, mock tender steak, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13963: [], # Beef, chuck, mock tender steak, separable lean only, trimmed to 0" fat, select, cooked, broiled
    13965: [], # Beef, chuck, top blade, separable lean only, trimmed to 0" fat, choice, cooked, broiled
    13967: [], # Beef, chuck, top blade, separable lean only, trimmed to 0" fat, select, cooked, broiled
    13968: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    13969: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    13970: ['Beef flank', 'steak'], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, all grades, raw
    13971: [], # Beef, flank, steak, separable lean and fat, trimmed to 0" fat, select, raw
    13972: ['Beef chuck eye roast', 'boneless'], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, all grades, raw
    13973: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, choice, raw
    13974: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean only, trimmed to 0" fat, select, raw
    13975: [], # Beef, brisket, flat half, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    13977: [], # Beef, plate, inside skirt steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    13979: [], # Beef, plate, outside skirt steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    13980: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    13981: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    13982: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    13983: [], # Beef, brisket, flat half, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    13985: [], # Beef, loin, bottom sirloin butt, tri-tip roast, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    14003: [], # Alcoholic beverage, beer, regular, all
    14004: [], # Alcoholic beverage, beer, regular, BUDWEISER
    14005: [], # Alcoholic beverage, beer, light, BUDWEISER SELECT
    14006: [], # Alcoholic beverage, beer, light
    14007: [], # Alcoholic beverage, beer, light, BUD LIGHT
    14009: [], # Alcoholic beverage, daiquiri, canned
    14010: [], # Alcoholic beverage, daiquiri, prepared-from-recipe
    14013: [], # Alcoholic beverage, beer, light, low carb
    14015: [], # Alcoholic beverage, pina colada, canned
    14016: [], # Beverages, almond milk, sweetened, vanilla flavor, ready-to-drink
    14017: [], # Alcoholic beverage, pina colada, prepared-from-recipe
    14019: [], # Alcoholic beverage, tequila sunrise, canned
    14021: [], # Beverages,  Energy drink, Citrus
    14022: [], # Beverages, MONSTER energy drink, low carb
    14024: [], # Beverages, Whiskey sour mix, powder
    14025: [], # Alcoholic beverage, whiskey sour, prepared with water, whiskey and powder mix
    14026: [], # Beverages, THE COCA-COLA COMPANY, NOS Zero, energy drink, sugar-free with guarana, fortified with vitamins B6 and B12
    14027: [], # Alcoholic beverage, whiskey sour, canned
    14028: [], # Beverages, Whiskey sour mix, bottled
    14029: [], # Alcoholic beverage, whiskey sour, prepared from item 14028
    14030: [], # Beverages, THE COCA-COLA COMPANY, NOS energy drink, Original, grape, loaded cherry, charged citrus, fortified with vitamins B6 and B12
    14031: [], # Beverages, water, bottled, yumberry, pomegranate with anti-oxidants, zero calories
    14033: [], # Beverages, ABBOTT, EAS whey protein powder
    14034: [], # Alcoholic beverage, creme de menthe, 72 proof
    14035: [], # Beverages, ABBOTT, EAS soy protein powder
    14036: [], # Beverages, CYTOSPORT, Muscle Milk, ready-to-drink
    14037: [], # Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 80 proof
    14038: [], # Beverages, OCEAN SPRAY, Cran-Energy, Cranberry Energy Juice Drink
    14041: [], # Beverages, NESTLE, Boost plus, nutritional drink, ready-to-drink
    14044: [], # Beverages, SLIMFAST, Meal replacement,  High Protein Shake, Ready-To-Drink, 3-2-1 plan
    14045: [], # Beverages, UNILEVER, SLIMFAST, meal replacement, regular, ready-to-drink,  3-2-1 Plan
    14047: [], # Beverages, UNILEVER, SLIMFAST Shake Mix, powder, 3-2-1 Plan
    14048: [], # Beverages, FUZE, orange mango, fortified with vitamins A, C, E, B6
    14050: [], # Alcoholic beverage, distilled, rum, 80 proof
    14051: [], # Alcoholic beverage, distilled, vodka, 80 proof
    14052: [], # Alcoholic beverage, distilled, whiskey, 86 proof
    14054: [], # Beverages, almond milk, chocolate, ready-to-drink
    14055: [], # Beverages, UNILEVER, SLIMFAST Shake Mix, high protein, whey powder, 3-2-1 Plan,
    14056: [], # Beverages, Acai berry drink, fortified
    14057: [], # Alcoholic beverage, wine, dessert, sweet
    14058: [], # Beverages, Whey protein powder isolate
    14060: [], # Beverages, Energy Drink with carbonated water and high fructose corn syrup
    14061: [], # Beverages, Energy Drink, sugar free
    14062: [], # Beverages, ABBOTT, ENSURE, Nutritional Shake, Ready-to-Drink
    14063: [], # Beverages, chocolate powder, no sugar added
    14064: [], # Beverages, Orange juice, light, No pulp
    14065: [], # Beverages, The COCA-COLA company, Hi-C Flashin' Fruit Punch
    14066: [], # Beverages, Protein powder whey based
    14067: [], # Beverages, Protein powder soy based
    14073: [], # Beverages, ZEVIA, cola
    14074: [], # Beverages, ZEVIA, cola, caffeine free
    14075: [], # Beverages, GEROLSTEINER BRUNNEN GmbH & Co. KG,Gerolsteiner naturally sparkling mineral water,
    14079: [], # Beverages, yellow green colored citrus soft drink with caffeine
    14080: [], # Beverages, rich chocolate, powder
    14082: [], # Beverages, GEROLSTEINER BRUNNEN GmbH & Co. KG (Gerolsteiner), naturally sparkling, mineral bottled water
    14083: [], # Beverages, chocolate malt, powder, prepared with fat free milk
    14084: [], # Alcoholic beverage, wine, table, all
    14086: [], # Beverages, V8 SPLASH Smoothies, Peach Mango
    14087: [], # Beverages, V8 SPLASH Smoothies, Strawberry Banana
    14088: [], # Beverages, V8 SPLASH Smoothies, Tropical Colada
    14090: [], # Beverages, Coconut water, ready-to-drink, unsweetened
    14091: [], # Beverages, almond milk, unsweetened, shelf stable
    14092: [], # Beverages, chocolate almond milk, unsweetened, shelf-stable, fortified with vitamin D2 and E
    14093: [], # Beverages, The COCA-COLA company, Glaceau Vitamin Water, Revive Fruit Punch, fortified
    14095: [], # Beverages, MINUTE MAID, Lemonada, Limeade
    14096: [], # Alcoholic beverage, wine, table, red
    14097: [], # Alcoholic Beverage, wine, table, red, Cabernet Sauvignon
    14098: [], # Alcoholic Beverage, wine, table, red, Cabernet Franc
    14099: [], # Alcoholic Beverage, wine, table, red, Pinot Noir
    14100: [], # Alcoholic Beverage, wine, table, red, Syrah
    14101: [], # Alcoholic Beverage, wine, table, red, Barbera
    14102: [], # Alcoholic Beverage, wine, table, red, Zinfandel
    14103: [], # Alcoholic Beverage, wine, table, red, Petite Sirah
    14105: [], # Alcoholic Beverage, wine, table, red, Claret
    14106: [], # Alcoholic beverage, wine, table, white
    14107: [], # Alcoholic Beverage, wine, table, red, Lemberger
    14108: [], # Alcoholic Beverage, wine, table, red, Sangiovese
    14109: [], # Alcoholic Beverage, wine, table, red, Carignane
    14113: [], # Alcoholic beverage, wine, table, white, Pinot Gris (Grigio)
    14116: [], # Alcoholic beverage, wine, table, white, Chenin Blanc
    14117: [], # Alcoholic beverage, wine, table, white, Fume Blanc
    14119: [], # Beverages, Mixed vegetable and fruit juice drink, with added nutrients
    14120: [], # Alcoholic beverage, wine, table, white, Muller Thurgau
    14121: [], # Beverages, carbonated, club soda
    14124: [], # Alcoholic beverage, wine, table, white, Gewurztraminer
    14125: [], # Alcoholic beverage, wine, table, white, late harvest, Gewurztraminer
    14126: [], # Alcoholic beverage, wine, table, white, Semillon
    14130: [], # Carbonated beverage, cream soda
    14132: [], # Alcoholic beverage, wine, table, white, Riesling
    14134: [], # Alcoholic beverage, wine, table, white, Sauvignon Blanc
    14135: [], # Alcoholic beverage, wine, table, white, late harvest
    14136: [], # Beverages, carbonated, ginger ale
    14137: [], # Beverages, NESTEA, tea, black, ready-to-drink, lemon
    14138: [], # Alcoholic beverage, wine, table, white, Pinot Blanc
    14140: [], # Alcoholic beverage, wine, table, white, Muscat
    14142: [], # Beverages, carbonated, grape soda
    14143: [], # Beverages, carbonated, low calorie, other than cola or pepper,  without caffeine
    14144: [], # Beverages, carbonated, lemon-lime soda, no caffeine
    14145: [], # Beverages, carbonated, SPRITE, lemon-lime, without caffeine
    14146: [], # Beverages, carbonated, low calorie, cola or pepper-type, with aspartame, without caffeine
    14147: [], # Beverages, carbonated, cola, without caffeine
    14148: [], # Beverages, carbonated, cola, regular
    14149: [], # Beverages, carbonated, reduced sugar, cola, contains caffeine and sweeteners
    14150: [], # Beverages, carbonated, orange
    14151: [], # Beverages, carbonated, low calorie, other than cola or pepper, with aspartame, contains caffeine
    14152: [], # Alcoholic Beverage, wine, table, red, Burgundy
    14153: [], # Beverages, carbonated, pepper-type, contains caffeine
    14154: [], # Beverages, Energy drink, RED BULL
    14155: [], # Beverages, carbonated, tonic water
    14156: [], # Beverages, Energy drink, RED BULL, sugar free, with added caffeine, niacin, pantothenic acid, vitamins B6 and B12
    14157: [], # Beverages, carbonated, root beer
    14158: [], # Alcoholic Beverage, wine, table, red, Gamay
    14159: [], # Alcoholic Beverage, wine, table, red, Mouvedre
    14160: [], # Alcoholic beverage, wine, table, white, Chardonnay
    14161: [], # Beverages, Kiwi Strawberry Juice Drink
    14162: [], # Beverages, Apple juice drink, light, fortified with vitamin C
    14163: [], # Beverages, chocolate drink, milk and soy based, ready to drink, fortified
    14164: [], # Beverages, chocolate malt powder, prepared with 1% milk, fortified
    14165: [], # Beverages, carbonated, limeade, high caffeine
    14166: [], # Beverages, carbonated, low calorie, cola or pepper-types, with sodium saccharin, contains caffeine
    14167: [], # Beverages, POWERADE, Zero, Mixed Berry
    14168: [], # Beverages, Carob-flavor beverage mix, powder
    14169: [], # Beverages, Carob-flavor beverage mix, powder, prepared with whole milk
    14171: [], # Beverages, coconut milk, sweetened, fortified with calcium, vitamins A, B12, D2
    14173: [], # Beverages, coffee, ready to drink, vanilla, light, milk based, sweetened
    14174: [], # Beverages, Lemonade fruit juice drink light, fortified with vitamin E and C
    14177: [], # Beverages, chocolate-flavor beverage mix, powder, prepared with whole milk
    14179: [], # Beverages, coffee, ready to drink, milk based, sweetened
    14180: [], # Beverages, coffee, brewed, breakfast blend
    14181: [], # Beverages, chocolate syrup
    14182: [], # Beverages, chocolate syrup, prepared with whole milk
    14183: [], # Beverages, coffee, ready to drink, iced, mocha, milk based
    14185: [], # Beverages, tea, Oolong, brewed
    14187: [], # Beverages, Clam and tomato juice, canned
    14188: [], # Beverages, tea, green, ready to drink, ginseng and honey, sweetened
    14189: [], # Beverages, The COCA-COLA company, Minute Maid, Lemonade
    14190: [], # Beverages, tea, green, ready-to-drink, diet
    14191: [], # Beverages, tea, green, ready-to-drink, citrus, diet, fortified with vitamin C
    14192: [], # Beverages, Cocoa mix, powder
    14194: [], # Beverages, Cocoa mix, powder, prepared with water
    14195: [], # Beverages, Cocoa mix, NESTLE, Hot Cocoa Mix Rich Chocolate With Marshmallows
    14196: [], # Beverages, Cocoa mix, no sugar added, powder
    14197: [], # Cocoa mix, NESTLE, Rich Chocolate Hot Cocoa Mix
    14199: [], # Beverages, tea, black, ready-to-drink, lemon, sweetened
    14201: [], # Beverages, coffee, brewed, prepared with tap water, decaffeinated
    14202: [], # Beverages, coffee, brewed, espresso, restaurant-prepared, decaffeinated
    14203: [], # Beverages, coffee, instant, regular, half the caffeine
    14204: [], # Beverages, coffee and cocoa, instant, decaffeinated, with whitener and low calorie sweetener
    14206: [], # Beverages, tea, green, ready-to-drink, sweetened
    14207: [], # Beverages, tea, ready-to-drink, lemon, diet
    14209: [], # Beverages, coffee, brewed, prepared with tap water
    14210: [], # Beverages, coffee, brewed, espresso, restaurant-prepared
    14211: [], # Beverages, tea, black, ready-to-drink, lemon, diet
    14214: [], # Beverages, coffee, instant, regular, powder
    14215: [], # Beverages, coffee, instant, regular, prepared with water
    14216: [], # Beverages, aloe vera juice drink, fortified with Vitamin C
    14217: [], # Beverages, OCEAN SPRAY, Cran Grape
    14218: [], # Beverages, coffee, instant, decaffeinated, powder
    14219: [], # Beverages, coffee, instant, decaffeinated, prepared with water
    14220: [], # Beverages, OCEAN SPRAY, Cranberry-Apple Juice Drink, bottled
    14221: [], # Beverages, OCEAN SPRAY, Diet Cranberry Juice
    14222: [], # Beverages, coffee, instant, with chicory
    14223: [], # Beverages, coffee, instant, chicory
    14224: [], # Beverages, coffee, instant, mocha, sweetened
    14226: [], # Beverages, OCEAN SPRAY, Light Cranberry and Raspberry Flavored Juice
    14227: [], # Beverages, OCEAN SPRAY, White Cranberry Strawberry Flavored Juice Drink
    14231: [], # Beverages, KRAFT, coffee, instant, French Vanilla Cafe
    14233: [], # Beverages, OCEAN SPRAY, Cran Raspberry Juice Drink
    14234: [], # Beverages, OCEAN SPRAY, Cran Lemonade
    14235: [], # Beverages, OCEAN SPRAY, Diet Cran Cherry
    14236: [], # Beverages, coffee substitute, cereal grain beverage, powder
    14237: [], # Beverages, coffee substitute, cereal grain beverage, prepared with water
    14238: [], # Beverages, cranberry-apple juice drink, bottled
    14239: [], # Alcoholic beverage, malt beer, hard lemonade
    14240: [], # Beverages, cranberry-apricot juice drink, bottled
    14241: [], # Beverages, cranberry-grape juice drink, bottled
    14242: [], # Cranberry juice cocktail, bottled
    14243: [], # Cranberry juice cocktail, bottled, low calorie, with calcium, saccharin and corn sweetener
    14245: [], # Beverages, Eggnog-flavor mix, powder, prepared with whole milk
    14246: [], # Beverages, tea, green, instant, decaffeinated, lemon, unsweetened, fortified with vitamin C
    14247: [], # Beverages, tea, black, ready to drink
    14248: [], # Alcoholic beverage, beer, light, higher alcohol
    14250: [], # Beverages, AMBER, hard cider
    14251: [], # Alcoholic beverages, beer, higher alcohol
    14252: [], # Beverages, Malt liquor beverage
    14253: [], # Alcoholic beverages, wine, rose
    14255: [], # Beverages, OCEAN SPRAY, Cran Pomegranate
    14256: [], # Beverages, OCEAN SPRAY, Cran Cherry
    14257: [], # Beverages, OCEAN SPRAY, Light Cranberry
    14258: [], # Beverages, OCEAN SPRAY, White Cranberry Peach
    14259: [], # Beverages, OCEAN SPRAY, Light Cranberry, Concord Grape
    14260: [], # Beverages, tea, green, brewed, decaffeinated
    14261: [], # Beverages, tea, green, ready to drink, unsweetened
    14262: [], # Beverages, citrus fruit juice drink, frozen concentrate
    14263: [], # Beverages, citrus fruit juice drink, frozen concentrate, prepared with water
    14264: [], # Beverages, fruit punch drink, without added nutrients, canned
    14267: [], # Beverages, Fruit punch drink, with added nutrients, canned
    14268: [], # Beverages, Fruit punch drink, frozen concentrate
    14269: [], # Beverages, Fruit punch drink, frozen concentrate, prepared with water
    14270: [], # Beverages, coffee, instant, vanilla, sweetened, decaffeinated, with non dairy creamer
    14276: [], # Beverages, Tropical Punch, ready-to-drink
    14277: [], # Beverages, grape drink, canned
    14278: [], # Beverages, tea, green, brewed, regular
    14279: [], # Beverages, tea, black, ready-to-drink, peach, diet
    14280: [], # Beverages, tea, black, ready to drink, decaffeinated, diet
    14281: [], # Beverages, tea, black, ready to drink, decaffeinated
    14282: [], # Beverages, grape juice drink, canned
    14284: [], # Beverages, Cranberry juice cocktail
    14285: [], # Beverages, OCEAN SPRAY, Ruby Red cranberry
    14286: [], # Beverages, MOTTS, Apple juice light, fortified with vitamin C
    14287: [], # Beverages, Lemonade, powder
    14288: [], # Lemonade, powder, prepared with water
    14291: [], # Beverages, SNAPPLE, tea, black and green, ready to drink, peach, diet
    14292: [], # Lemonade, frozen concentrate, white
    14293: [], # Lemonade, frozen concentrate, white, prepared with water
    14294: [], # Beverages, SNAPPLE, tea, black and green, ready to drink, lemon, diet
    14296: [], # Beverages, lemonade-flavor drink, powder
    14297: [], # Beverages, lemonade-flavor drink, powder, prepared with water
    14303: [], # Limeade, frozen concentrate, prepared with water
    14305: [], # Malt beverage, includes non-alcoholic beer
    14309: [], # Beverages, OVALTINE, Classic Malt powder
    14310: [], # Beverages, Malted drink mix, natural, with added nutrients, powder, prepared with whole milk
    14311: [], # Beverages, Malted drink mix, natural, powder, dairy based.
    14312: [], # Beverages, Malted drink mix, natural, powder, prepared with whole milk
    14315: [], # Beverages, OVALTINE, chocolate malt powder
    14316: [], # Beverages, Malted drink mix, chocolate, with added nutrients, powder, prepared with whole milk
    14317: [], # Beverages, malted drink mix, chocolate, powder
    14318: [], # Beverages, Malted drink mix, chocolate, powder, prepared with whole milk
    14323: [], # Beverages, orange drink, canned, with added vitamin C
    14327: [], # Beverages, orange and apricot juice drink, canned
    14334: [], # Beverages, pineapple and grapefruit juice drink, canned
    14341: [], # Beverages, pineapple and orange juice drink, canned
    14347: [], # Shake, fast food, vanilla
    14350: [], # Strawberry-flavor beverage mix, powder
    14351: [], # Beverages, Strawberry-flavor beverage mix, powder, prepared with whole milk
    14352: [], # Beverages, tea, black, brewed, prepared with tap water, decaffeinated
    14353: [], # Beverages, tea, instant, decaffeinated, unsweetened
    14355: [], # Beverages, tea, black, brewed, prepared with tap water
    14356: [], # Beverages, tea, instant, decaffeinated, lemon, diet
    14357: [], # Beverages, tea, instant, decaffeinated, lemon, sweetened
    14366: [], # Beverages, tea, instant, unsweetened, powder
    14367: [], # Beverages, tea, instant, unsweetened, prepared with water
    14368: [], # Beverages, tea, instant, lemon, unsweetened
    14370: [], # Beverages, tea, instant, lemon, sweetened, powder
    14371: [], # Beverages, tea, instant, lemon, sweetened, prepared with water
    14375: [], # Beverages, tea, instant, sweetened with sodium saccharin, lemon-flavored, powder
    14376: [], # Beverages, tea, instant, lemon, diet
    14381: [], # Beverages, tea, herb, other than chamomile, brewed
    14384: [], # Beverages, water, bottled, PERRIER
    14385: [], # Beverages, water, bottled, POLAND SPRING
    14390: [], # Beverages, cocoa mix, with aspartame, powder, prepared with water
    14400: [], # Beverages, carbonated, cola, fast-food cola
    14405: [], # Beverages, fruit punch juice drink, frozen concentrate
    14406: [], # Beverages, fruit punch juice drink, frozen concentrate, prepared with water
    14407: [], # Beverages, orange-flavor drink, breakfast type, powder
    14408: [], # Beverages, orange-flavor drink, breakfast type, powder, prepared with water
    14409: [], # Beverages, Orange-flavor drink, breakfast type, low calorie, powder
    14411: [], # Beverages, water, tap, drinking
    14412: [], # Beverages, water, tap, well
    14414: [], # Alcoholic beverage, liqueur, coffee, 53 proof
    14415: [], # Alcoholic beverage, liqueur, coffee with cream, 34 proof
    14416: [], # Beverages, carbonated, low calorie, cola or pepper-type, with aspartame, contains caffeine
    14421: [], # Beverages, coffee substitute, cereal grain beverage, powder, prepared with whole milk
    14422: [], # Beverages, Dairy drink mix, chocolate, reduced calorie, with low-calorie sweeteners, powder
    14423: [], # Beverages, dairy drink mix, chocolate, reduced calorie, with aspartame, powder, prepared with water and ice
    14424: [], # Beverages, Orange-flavor drink, breakfast type, with pulp, frozen concentrate.
    14425: [], # Beverages, Orange-flavor drink, breakfast type, with pulp, frozen concentrate, prepared with water
    14426: [], # Beverages, Orange drink, breakfast type, with juice and pulp, frozen concentrate
    14427: [], # Beverages, Orange drink, breakfast type, with juice and pulp, frozen concentrate, prepared with water
    14428: [], # Beverages, shake, fast food, strawberry
    14429: [], # Beverages, water, tap, municipal
    14430: [], # Cranberry juice cocktail, frozen concentrate
    14431: [], # Cranberry juice cocktail, frozen concentrate, prepared with water
    14432: [], # Beverages, water, bottled, non-carbonated, DANNON
    14433: [], # Beverages, water, bottled, non-carbonated, PEPSI, AQUAFINA
    14434: [], # Beverages, The COCA-COLA company, DASANI, water, bottled, non-carbonated
    14436: [], # Beverages, orange breakfast drink, ready-to-drink, with added nutrients
    14437: [], # Beverages, water, bottled, non-carbonated, CALISTOGA
    14438: [], # Beverages, water, bottled, non-carbonated, CRYSTAL GEYSER
    14439: [], # Water, bottled, non-carbonated, NAYA
    14440: [], # Beverages, DANNON, water, bottled, non-carbonated, with Fluoride
    14450: [], # Beverages, drink mix, QUAKER OATS, GATORADE, orange flavor, powder
    14460: [], # Beverages, PEPSICO QUAKER, Gatorade, G performance O 2, ready-to-drink.
    14461: [], # Beverages, COCA-COLA, POWERADE, lemon-lime flavored, ready-to-drink
    14462: [], # Beverages, Propel Zero, fruit-flavored, non-carbonated
    14475: [], # Beverages, ARIZONA, tea, ready-to-drink, lemon
    14476: [], # Beverages, LIPTON BRISK, tea, black, ready-to-drink, lemon
    14530: [], # Whiskey sour mix, bottled, with added potassium and sodium
    14531: [], # Alcoholic beverage, whiskey sour
    14532: [], # Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 94 proof
    14533: [], # Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 100 proof
    14534: [], # Alcoholic beverage, liqueur, coffee, 63 proof
    14536: [], # Alcoholic beverage, wine, dessert, dry
    14537: [], # Carbonated beverage, low calorie, other than cola or pepper, with sodium saccharin, without caffeine
    14538: [], # Beverages, Cocoa mix, low calorie, powder, with added calcium, phosphorus, aspartame, without added sodium or vitamin A
    14541: [], # Beverages, fruit punch-flavor drink, powder, without added sodium, prepared with water
    14542: [], # Lemonade, frozen concentrate, pink
    14543: [], # Beverages, lemonade, frozen concentrate, pink, prepared with water
    14544: [], # Beverages, tea, black, brewed, prepared with distilled water
    14545: [], # Beverages, tea, herb, brewed, chamomile
    14548: [], # Beverages, tea, instant, lemon, with added ascorbic acid
    14550: [], # Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 86 proof
    14551: [], # Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 90 proof
    14552: [], # Carbonated beverage, chocolate-flavored soda
    14553: [], # Beverages, Wine, non-alcoholic
    14555: ['Water', '', 'Water'], # Water, bottled, generic
    14557: [], # Beverages, chocolate-flavor beverage mix for milk, powder, with added nutrients
    14558: [], # Beverages, chocolate-flavor beverage mix for milk, powder, with added nutrients, prepared with whole milk
    14559: [], # Beverages, water, bottled, non-carbonated, EVIAN
    14599: [], # Beverages, Powerade Zero Ion4, calorie-free, assorted flavors
    14601: [], # Beverages, WENDY'S, tea, ready-to-drink, unsweetened
    14602: [], # Alcoholic Beverage, wine, table, red, Merlot
    14604: [], # Water, non-carbonated, bottles, natural fruit flavors, sweetened with low calorie sweetener
    14605: [], # Beverages, Water with added vitamins and minerals, bottles, sweetened, assorted fruit flavors
    14607: [], # Beverages, V8 SPLASH Juice Drinks, Diet Berry Blend
    14608: [], # Beverages, V8 SPLASH Juice Drinks, Diet Fruit Medley
    14609: [], # Beverages, V8 SPLASH Juice Drinks, Diet Strawberry Kiwi
    14610: [], # Beverages, V8 SPLASH Juice Drinks, Diet Tropical Blend
    14611: [], # Beverages, V8 SPLASH Juice Drinks, Berry Blend
    14612: [], # Beverages, V8 SPLASH Juice Drinks, Fruit Medley
    14613: [], # Beverages, V8 SPLASH Juice Drinks, Guava Passion Fruit
    14614: [], # Beverages, V8 SPLASH Juice Drinks, Mango Peach
    14615: [], # Beverages, V8 SPLASH Juice Drinks, Orange Pineapple
    14616: [], # Beverages, V8 SPLASH Juice Drinks, Orchard Blend
    14617: [], # Beverages, V8 SPLASH Juice Drinks, Strawberry Banana
    14618: [], # Beverages, V8 SPLASH Juice Drinks, Strawberry Kiwi
    14619: [], # Beverages, V8 SPLASH Juice Drinks, Tropical Blend
    14620: [], # Beverages, V8 V-FUSION Juices, Peach Mango
    14621: [], # Beverages, V8 V-FUSION Juices, Strawberry Banana
    14622: [], # Beverages, V8 V-FUSION Juices, Tropical
    14623: [], # Beverages, V8 V- FUSION Juices, Acai Berry
    14625: [], # Beverages, Energy drink, AMP
    14626: [], # Beverages, Energy drink, FULL THROTTLE
    14627: [], # Beverages, Energy Drink, Monster, fortified with vitamins C, B2, B3, B6, B12
    14628: [], # Beverages, Energy drink, AMP, sugar free
    14629: [], # Beverages, Energy drink, ROCKSTAR
    14630: [], # Beverages, Energy drink, ROCKSTAR, sugar free
    14632: [], # Beverages, Meal supplement drink, canned, peanut flavor
    14633: [], # Beverages, Vegetable and fruit juice drink, reduced calorie, with low-calorie sweetener, added vitamin C
    14634: [], # Beverages, milk beverage, reduced fat, flavored and sweetened, Ready-to-drink,  added calcium, vitamin A and vitamin D
    14635: [], # Beverages, vegetable and fruit juice blend, 100% juice, with added vitamins A, C, E
    14636: [], # Beverages, fruit juice drink, reduced sugar, with vitamin E added
    14637: [], # Water, with corn syrup and/or sugar and low calorie sweetener, fruit flavored
    14638: [], # Beverages, Horchata, as served in restaurant
    14639: [], # Beverages, rice milk, unsweetened
    14640: [], # Beverages, Energy drink, VAULT, citrus flavor
    14641: [], # Beverages, Energy drink, VAULT Zero, sugar-free, citrus flavor
    14644: [], # Beverages, PEPSICO QUAKER, Gatorade G2, low calorie
    14645: [], # Beverages, Fruit flavored drink, less than 3% juice, not fortified with vitamin C
    14646: [], # Beverages, Fruit flavored drink containing less than 3% fruit juice, with high vitamin C
    14647: [], # Beverages, Fruit flavored drink, reduced sugar, greater than 3% fruit juice, high vitamin C, added calcium
    14648: [], # Beverages, fruit juice drink, greater than 3% fruit juice, high vitamin C and added thiamin
    14649: [], # Beverages, tea, hibiscus, brewed
    14651: [], # Beverages, fruit juice drink, greater than 3% juice, high vitamin C
    14654: [], # Beverages, nutritional shake mix, high protein, powder
    15001: ['Anchovy fish'], # Fish, anchovy, european, raw
    15002: [], # Fish, anchovy, european, canned in oil, drained solids
    15003: ['Bass fish'], # Fish, bass, fresh water, mixed species, raw
    15004: [], # Fish, bass, striped, raw
    15005: ['Bluefish fish'], # Fish, bluefish, raw
    15006: ['Burbot fish'], # Fish, burbot, raw
    15007: ['Butterfish fish'], # Fish, butterfish, raw
    15008: ['Carp fish'], # Fish, carp, raw
    15009: [], # Fish, carp, cooked, dry heat
    15010: ['Catfish fish', 'wild channel'], # Fish, catfish, channel, wild, raw
    15011: [], # Fish, catfish, channel, cooked, breaded and fried
    15012: [], # Fish, caviar, black and red, granular
    15013: ['Cisco fish'], # Fish, cisco, raw
    15014: [], # Fish, cisco, smoked
    15015: ['Cod fish'], # Fish, cod, Atlantic, raw
    15016: [], # Fish, cod, Atlantic, cooked, dry heat
    15017: [], # Fish, cod, Atlantic, canned, solids and liquid
    15018: [], # Fish, cod, Atlantic, dried and salted
    15019: [], # Fish, cod, Pacific, raw (may have been previously frozen)
    15020: ['Croaker fish'], # Fish, croaker, Atlantic, raw
    15021: [], # Fish, croaker, Atlantic, cooked, breaded and fried
    15022: ['Cusk fish'], # Fish, cusk, raw
    15023: ['Mahimahi fish'], # Fish, mahimahi, raw
    15024: ['Drum fish'], # Fish, drum, freshwater, raw
    15025: ['Eel fish'], # Fish, eel, mixed species, raw
    15026: [], # Fish, eel, mixed species, cooked, dry heat
    15027: [], # Fish, fish sticks, frozen, prepared
    15028: ['Flatfish fish'], # Fish, flatfish (flounder and sole species), raw
    15029: [], # Fish, flatfish (flounder and sole species), cooked, dry heat
    15030: [], # Fish, gefiltefish, commercial, sweet recipe
    15031: ['Grouper fish'], # Fish, grouper, mixed species, raw
    15032: [], # Fish, grouper, mixed species, cooked, dry heat
    15033: ['Haddock fish'], # Fish, haddock, raw
    15034: [], # Fish, haddock, cooked, dry heat
    15035: [], # Fish, haddock, smoked
    15036: ['Halibut fish'], # Fish, halibut, Atlantic and Pacific, raw
    15037: [], # Fish, halibut, Atlantic and Pacific, cooked, dry heat
    15038: [], # Fish, halibut, Greenland, raw
    15039: ['Herring fish'], # Fish, herring, Atlantic, raw
    15040: [], # Fish, herring, Atlantic, cooked, dry heat
    15041: [], # Fish, herring, Atlantic, pickled
    15042: [], # Fish, herring, Atlantic, kippered
    15043: [], # Fish, herring, Pacific, raw
    15044: ['Ling fish'], # Fish, ling, raw
    15045: ['Lingcod fish'], # Fish, lingcod, raw
    15046: ['Mackerel fish'], # Fish, mackerel, Atlantic, raw
    15047: [], # Fish, mackerel, Atlantic, cooked, dry heat
    15048: [], # Fish, mackerel, jack, canned, drained solids
    15049: [], # Fish, mackerel, king, raw
    15050: [], # Fish, mackerel, Pacific and jack, mixed species, raw
    15051: [], # Fish, mackerel, spanish, raw
    15052: [], # Fish, mackerel, spanish, cooked, dry heat
    15053: ['Milkfish fish'], # Fish, milkfish, raw
    15054: ['Monkfish fish'], # Fish, monkfish, raw
    15055: ['Mullet fish'], # Fish, mullet, striped, raw
    15056: [], # Fish, mullet, striped, cooked, dry heat
    15057: ['Ocean perch fish'], # Fish, ocean perch, Atlantic, raw
    15058: [], # Fish, ocean perch, Atlantic, cooked, dry heat
    15059: ['Pout fish'], # Fish, pout, ocean, raw
    15060: ['Perch fish'], # Fish, perch, mixed species, raw
    15061: [], # Fish, perch, mixed species, cooked, dry heat
    15062: ['Pike fish'], # Fish, pike, northern, raw
    15063: [], # Fish, pike, northern, cooked, dry heat
    15064: [], # Fish, pike, walleye, raw
    15065: ['Pollock fish'], # Fish, pollock, Atlantic, raw
    15066: [], # Fish, pollock, Alaska, raw (may contain additives to retain moisture)
    15067: [], # Fish, pollock, Alaska, cooked, dry heat (may contain additives to retain moisture)
    15068: ['Pompano fish'], # Fish, pompano, florida, raw
    15069: [], # Fish, pompano, florida, cooked, dry heat
    15070: ['Rockfish fish'], # Fish, rockfish, Pacific, mixed species, raw
    15071: [], # Fish, rockfish, Pacific, mixed species, cooked, dry heat
    15072: ['Roe fish'], # Fish, roe, mixed species, raw
    15073: ['Roughy fish'], # Fish, roughy, orange, raw
    15074: ['Sablefish fish'], # Fish, sablefish, raw
    15075: [], # Fish, sablefish, smoked
    15076: ['Salmon fish'], # Fish, salmon, Atlantic, wild, raw
    15077: [], # Fish, salmon, chinook, smoked
    15078: [], # Fish, salmon, chinook, raw
    15079: [], # Fish, salmon, chum, raw
    15080: [], # Fish, salmon, chum, canned, drained solids with bone
    15081: [], # Fish, salmon, coho, wild, raw
    15082: [], # Fish, salmon, coho, wild, cooked, moist heat
    15083: [], # Fish, salmon, pink, raw
    15084: [], # Fish, salmon, pink, canned, total can contents
    15085: [], # Fish, salmon, sockeye, raw
    15086: [], # Fish, salmon, sockeye, cooked, dry heat
    15087: [], # Fish, salmon, sockeye, canned, drained solids
    15088: [], # Fish, sardine, Atlantic, canned in oil, drained solids with bone
    15089: [], # Fish, sardine, Pacific, canned in tomato sauce, drained solids with bone
    15090: ['Scup fish'], # Fish, scup, raw
    15091: ['Sea bass fish'], # Fish, sea bass, mixed species, raw
    15092: [], # Fish, sea bass, mixed species, cooked, dry heat
    15093: ['Seatrout fish'], # Fish, seatrout, mixed species, raw
    15094: ['Shad fish'], # Fish, shad, american, raw
    15095: ['Shark fish'], # Fish, shark, mixed species, raw
    15096: [], # Fish, shark, mixed species, cooked, batter-dipped and fried
    15097: ['Sheepshead fish'], # Fish, sheepshead, raw
    15098: [], # Fish, sheepshead, cooked, dry heat
    15099: ['Smelt fish', 'rainbow'], # Fish, smelt, rainbow, raw
    15100: [], # Fish, smelt, rainbow, cooked, dry heat
    15101: ['Snapper fish'], # Fish, snapper, mixed species, raw
    15102: [], # Fish, snapper, mixed species, cooked, dry heat
    15103: ['Spot fish'], # Fish, spot, raw
    15104: ['Sturgeon fish'], # Fish, sturgeon, mixed species, raw
    15105: [], # Fish, sturgeon, mixed species, cooked, dry heat
    15106: [], # Fish, sturgeon, mixed species, smoked
    15107: ['Sucker fish', 'white'], # Fish, sucker, white, raw
    15108: ['Sunfish fish'], # Fish, sunfish, pumpkin seed, raw
    15109: [], # Fish, surimi
    15110: ['Swordfish fish'], # Fish, swordfish, raw
    15111: [], # Fish, swordfish, cooked, dry heat
    15112: ['Tilefish fish'], # Fish, tilefish, raw
    15113: [], # Fish, tilefish, cooked, dry heat
    15114: ['Trout fish'], # Fish, trout, mixed species, raw
    15115: [], # Fish, trout, rainbow, wild, raw
    15116: [], # Fish, trout, rainbow, wild, cooked, dry heat
    15117: ['Tuna fish'], # Fish, tuna, fresh, bluefin, raw
    15118: [], # Fish, tuna, fresh, bluefin, cooked, dry heat
    15119: [], # Fish, tuna, light, canned in oil, drained solids
    15121: [], # Fish, tuna, light, canned in water, drained solids (Includes foods for USDA's Food Distribution Program)
    15123: [], # Fish, tuna, fresh, skipjack, raw
    15124: [], # Fish, tuna, white, canned in oil, drained solids
    15126: [], # Fish, tuna, white, canned in water, drained solids
    15127: [], # Fish, tuna, fresh, yellowfin, raw
    15128: [], # Fish, tuna salad
    15129: ['Turbot fish'], # Fish, turbot, european, raw
    15130: ['Whitefish fish'], # Fish, whitefish, mixed species, raw
    15131: [], # Fish, whitefish, mixed species, smoked
    15132: ['Whiting fish'], # Fish, whiting, mixed species, raw
    15133: [], # Fish, whiting, mixed species, cooked, dry heat
    15134: ['Wolffish fish'], # Fish, wolffish, Atlantic, raw
    15135: ['Yellowtail fish'], # Fish, yellowtail, mixed species, raw
    15136: ['Crab', 'alaska king'], # Crustaceans, crab, alaska king, raw
    15137: [], # Crustaceans, crab, alaska king, cooked, moist heat
    15138: [], # Crustaceans, crab, alaska king, imitation, made from surimi
    15139: ['Crab', 'blue'], # Crustaceans, crab, blue, raw
    15140: [], # Crustaceans, crab, blue, cooked, moist heat
    15141: [], # Crustaceans, crab, blue, canned
    15142: [], # Crustaceans, crab, blue, crab cakes, home recipe
    15143: ['Crab', 'dungeness'], # Crustaceans, crab, dungeness, raw
    15144: ['Crab', 'queen'], # Crustaceans, crab, queen, raw
    15145: ['Crayfish'], # Crustaceans, crayfish, mixed species, wild, raw
    15146: [], # Crustaceans, crayfish, mixed species, wild, cooked, moist heat
    15147: ['Lobster', 'northern'], # Crustaceans, lobster, northern, raw
    15148: [], # Crustaceans, lobster, northern, cooked, moist heat
    15149: ['Shrimp'], # Crustaceans, shrimp, mixed species, raw (may contain additives to retain moisture)
    15150: [], # Crustaceans, shrimp, mixed species, cooked, breaded and fried
    15151: [], # Crustaceans, shrimp, mixed species, cooked, moist heat (may contain additives to retain moisture)
    15152: [], # Crustaceans, shrimp, mixed species, canned
    15153: [], # Crustaceans, shrimp, mixed species, imitation, made from surimi
    15154: ['Spiny lobster'], # Crustaceans, spiny lobster, mixed species, raw
    15155: ['Abalone'], # Mollusks, abalone, mixed species, raw
    15156: [], # Mollusks, abalone, mixed species, cooked, fried
    15157: ['Clam'], # Mollusks, clam, mixed species, raw
    15158: [], # Mollusks, clam, mixed species, cooked, breaded and fried
    15159: [], # Mollusks, clam, mixed species, cooked, moist heat
    15160: [], # Mollusks, clam, mixed species, canned, drained solids
    15162: [], # Mollusks, clam, mixed species, canned, liquid
    15163: ['Cuttlefish'], # Mollusks, cuttlefish, mixed species, raw
    15164: ['Mussel', 'blue'], # Mollusks, mussel, blue, raw
    15165: [], # Mollusks, mussel, blue, cooked, moist heat
    15166: ['Octopus'], # Mollusks, octopus, common, raw
    15167: ['Oyster', 'eastern'], # Mollusks, oyster, eastern, wild, raw
    15168: [], # Mollusks, oyster, eastern, cooked, breaded and fried
    15169: [], # Mollusks, oyster, eastern, wild, cooked, moist heat
    15170: [], # Mollusks, oyster, eastern, canned
    15171: ['Oyster', 'pacific'], # Mollusks, oyster, Pacific, raw
    15172: ['Scallop'], # Mollusks, scallop, mixed species, raw
    15173: [], # Mollusks, scallop, mixed species, cooked, breaded and fried
    15174: [], # Mollusks, scallop, mixed species, imitation, made from surimi
    15175: ['Squid'], # Mollusks, squid, mixed species, raw
    15176: [], # Mollusks, squid, mixed species, cooked, fried
    15177: [], # Mollusks, whelk, unspecified, raw
    15178: [], # Mollusks, whelk, unspecified, cooked, moist heat
    15179: [], # Fish, salmon, chinook, smoked, (lox), regular
    15180: [], # Fish, salmon, chum, canned, without salt, drained solids with bone
    15181: [], # Fish, salmon, pink, canned, without salt, solids with bone and liquid
    15182: [], # Fish, salmon, sockeye, canned, without salt, drained solids with bone
    15183: [], # Fish, tuna, light, canned in oil, without salt, drained solids
    15184: [], # Fish, tuna, light, canned in water, without salt, drained solids
    15185: [], # Fish, tuna, white, canned in oil, without salt, drained solids
    15186: [], # Fish, tuna, white, canned in water, without salt, drained solids
    15187: [], # Fish, bass, freshwater, mixed species, cooked, dry heat
    15188: [], # Fish, bass, striped, cooked, dry heat
    15189: [], # Fish, bluefish, cooked, dry heat
    15190: [], # Fish, burbot, cooked, dry heat
    15191: [], # Fish, butterfish, cooked, dry heat
    15192: [], # Fish, cod, Pacific, cooked, dry heat (may contain additives to retain moisture)
    15193: [], # Fish, cusk, cooked, dry heat
    15194: [], # Fish, mahimahi, cooked, dry heat
    15195: [], # Fish, drum, freshwater, cooked, dry heat
    15196: [], # Fish, halibut, greenland, cooked, dry heat
    15197: [], # Fish, herring, Pacific, cooked, dry heat
    15198: [], # Fish, ling, cooked, dry heat
    15199: [], # Fish, lingcod, cooked, dry heat
    15200: [], # Fish, mackerel, king, cooked, dry heat
    15201: [], # Fish, mackerel, Pacific and jack, mixed species, cooked, dry heat
    15202: [], # Fish, milkfish, cooked, dry heat
    15203: [], # Fish, monkfish, cooked, dry heat
    15204: [], # Fish, pike, walleye, cooked, dry heat
    15205: [], # Fish, pollock, Atlantic, cooked, dry heat
    15206: [], # Fish, pout, ocean, cooked, dry heat
    15207: [], # Fish, roe, mixed species, cooked, dry heat
    15208: [], # Fish, sablefish, cooked, dry heat
    15209: [], # Fish, salmon, Atlantic, wild, cooked, dry heat
    15210: [], # Fish, salmon, chinook, cooked, dry heat
    15211: [], # Fish, salmon, chum, cooked, dry heat
    15212: [], # Fish, salmon, pink, cooked, dry heat
    15213: [], # Fish, scup, cooked, dry heat
    15214: [], # Fish, seatrout, mixed species, cooked, dry heat
    15215: [], # Fish, shad, american, cooked, dry heat
    15216: [], # Fish, spot, cooked, dry heat
    15217: [], # Fish, sucker, white, cooked, dry heat
    15218: [], # Fish, sunfish, pumpkin seed, cooked, dry heat
    15219: [], # Fish, trout, mixed species, cooked, dry heat
    15220: [], # Fish, tuna, skipjack, fresh, cooked, dry heat
    15221: [], # Fish, tuna, yellowfin, fresh, cooked, dry heat
    15222: [], # Fish, turbot, european, cooked, dry heat
    15223: [], # Fish, whitefish, mixed species, cooked, dry heat
    15224: [], # Fish, wolffish, Atlantic, cooked, dry heat
    15225: [], # Fish, yellowtail, mixed species, cooked, dry heat
    15226: [], # Crustaceans, crab, dungeness, cooked, moist heat
    15227: [], # Crustaceans, crab, queen, cooked, moist heat
    15228: [], # Crustaceans, spiny lobster, mixed species, cooked, moist heat
    15229: [], # Mollusks, cuttlefish, mixed species, cooked, moist heat
    15230: [], # Mollusks, octopus, common, cooked, moist heat
    15231: [], # Mollusks, oyster, Pacific, cooked, moist heat
    15232: [], # Fish, roughy, orange, cooked, dry heat
    15233: [], # Fish, catfish, channel, wild, cooked, dry heat
    15234: [], # Fish, catfish, channel, farmed, raw
    15235: [], # Fish, catfish, channel, farmed, cooked, dry heat
    15236: [], # Fish, salmon, Atlantic, farmed, raw
    15237: [], # Fish, salmon, Atlantic, farmed, cooked, dry heat
    15238: [], # Fish, salmon, coho, farmed, raw
    15239: [], # Fish, salmon, coho, farmed, cooked, dry heat
    15240: [], # Fish, trout, rainbow, farmed, raw
    15241: [], # Fish, trout, rainbow, farmed, cooked, dry heat
    15242: [], # Crustaceans, crayfish, mixed species, farmed, raw
    15243: [], # Crustaceans, crayfish, mixed species, farmed, cooked, moist heat
    15244: [], # Mollusks, oyster, eastern, wild, cooked, dry heat
    15245: [], # Mollusks, oyster, eastern, farmed, raw
    15246: [], # Mollusks, oyster, eastern, farmed, cooked, dry heat
    15247: [], # Fish, salmon, coho, wild, cooked, dry heat
    15250: [], # Mollusks, conch, baked or broiled
    15251: [], # Salmon nuggets, breaded, frozen, heated
    15252: [], # Salmon nuggets, cooked as purchased, unheated
    15253: [], # Salmon, sockeye, canned, total can contents
    15260: [], # Fish, salmon, pink, canned, drained solids
    15261: ['Tilapia'], # Fish, tilapia, raw
    15262: [], # Fish, tilapia, cooked, dry heat
    15264: [], # Salmon, sockeye, canned, drained solids, without skin and bones
    15265: [], # Fish, Salmon, pink, canned, drained solids, without skin and bones
    15266: [], # Fish, pollock, Alaska, raw
    15267: [], # Fish, pollock, Alaska, cooked
    15269: [], # Fish, cod, Pacific, cooked
    15270: [], # Crustaceans, shrimp, raw
    15271: [], # Crustaceans, shrimp, cooked
    15274: [], # Fish, trout, brook, raw, New York State
    16001: ['Adzuki'], # Beans, adzuki, mature seeds, raw
    16002: [], # Beans, adzuki, mature seeds, cooked, boiled, without salt
    16003: [], # Beans, adzuki, mature seeds, canned, sweetened
    16004: [], # Yokan, prepared from adzuki beans and sugar
    16005: [], # Beans, baked, home prepared
    16006: [], # Beans, baked, canned, plain or vegetarian
    16007: [], # Beans, baked, canned, with beef
    16008: [], # Beans, baked, canned, with franks
    16009: [], # Beans, baked, canned, with pork
    16010: [], # Beans, baked, canned, with pork and sweet sauce
    16011: [], # Beans, baked, canned, with pork and tomato sauce
    16014: ['Black bean'], # Beans, black, mature seeds, raw
    16015: [], # Beans, black, mature seeds, cooked, boiled, without salt
    16016: ['Black turtle bean'], # Beans, black turtle, mature seeds, raw
    16017: [], # Beans, black turtle, mature seeds, cooked, boiled, without salt
    16018: [], # Beans, black turtle, mature seeds, canned
    16019: ['Cranberry bean'], # Beans, cranberry (roman), mature seeds, raw
    16020: [], # Beans, cranberry (roman), mature seeds, cooked, boiled, without salt
    16021: [], # Beans, cranberry (roman), mature seeds, canned
    16022: ['French bean'], # Beans, french, mature seeds, raw
    16023: [], # Beans, french, mature seeds, cooked, boiled, without salt
    16024: ['Great northern bean'], # Beans, great northern, mature seeds, raw (Includes foods for USDA's Food Distribution Program)
    16025: [], # Beans, great northern, mature seeds, cooked, boiled, without salt
    16026: [], # Beans, great northern, mature seeds, canned
    16027: ['Kidney bean'], # Beans, kidney, all types, mature seeds, raw
    16028: [], # Beans, kidney, all types, mature seeds, cooked, boiled, without salt
    16029: [], # Beans, kidney, all types, mature seeds, canned
    16030: ['Kidney bean', 'california'], # Beans, kidney, california red, mature seeds, raw
    16031: [], # Beans, kidney, california red, mature seeds, cooked, boiled, without salt
    16032: ['Kidney bean', 'red'], # Beans, kidney, red, mature seeds, raw
    16033: [], # Beans, kidney, red, mature seeds, cooked, boiled, without salt
    16034: [], # Beans, kidney, red, mature seeds, canned, solids and liquids
    16035: ['Kidney bean', 'royal'], # Beans, kidney, royal red, mature seeds, raw
    16036: [], # Beans, kidney, royal red, mature seeds, cooked, boiled, without salt
    16037: ['Navy bean'], # Beans, navy, mature seeds, raw
    16038: [], # Beans, navy, mature seeds, cooked, boiled, without salt
    16039: [], # Beans, navy, mature seeds, canned
    16040: ['Pink bean'], # Beans, pink, mature seeds, raw
    16041: [], # Beans, pink, mature seeds, cooked, boiled, without salt
    16042: ['Pinto bean'], # Beans, pinto, mature seeds, raw (Includes foods for USDA's Food Distribution Program)
    16043: [], # Beans, pinto, mature seeds, cooked, boiled, without salt
    16044: [], # Beans, pinto, mature seeds, canned, solids and liquids
    16045: ['Small white bean'], # Beans, small white, mature seeds, raw
    16046: [], # Beans, small white, mature seeds, cooked, boiled, without salt
    16047: ['Yellow bean'], # Beans, yellow, mature seeds, raw
    16048: [], # Beans, yellow, mature seeds, cooked, boiled, without salt
    16049: ['White bean'], # Beans, white, mature seeds, raw
    16050: [], # Beans, white, mature seeds, cooked, boiled, without salt
    16051: [], # Beans, white, mature seeds, canned
    16052: ['Broadbean'], # Broadbeans (fava beans), mature seeds, raw
    16053: [], # Broadbeans (fava beans), mature seeds, cooked, boiled, without salt
    16054: [], # Broadbeans (fava beans), mature seeds, canned
    16055: [], # Carob flour
    16056: ['Chickpea', '', 'Garbanzo bean'], # Chickpeas (garbanzo beans, bengal gram), mature seeds, raw
    16057: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, cooked, boiled, without salt
    16058: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, canned, solids and liquids
    16059: [], # Chili with beans, canned
    16060: ['Cowpea', 'catjang'], # Cowpeas, catjang, mature seeds, raw
    16061: [], # Cowpeas, catjang, mature seeds, cooked, boiled, without salt
    16062: ['Cowpea', 'blackeye crowder southern'], # Cowpeas, common (blackeyes, crowder, southern), mature seeds, raw
    16063: [], # Cowpeas, common (blackeyes, crowder, southern), mature seeds, cooked, boiled, without salt
    16064: [], # Cowpeas, common (blackeyes, crowder, southern), mature seeds, canned, plain
    16065: [], # Cowpeas, common (blackeyes, crowder, southern), mature seeds, canned with pork
    16067: ['Hyacinth bean'], # Hyacinth beans, mature seeds, raw
    16068: [], # Hyacinth beans, mature seeds, cooked, boiled, without salt
    16069: ['Lentil'], # Lentils, raw
    16070: [], # Lentils, mature seeds, cooked, boiled, without salt
    16071: ['Lima bean', 'large'], # Lima beans, large, mature seeds, raw
    16072: [], # Lima beans, large, mature seeds, cooked, boiled, without salt
    16073: [], # Lima beans, large, mature seeds, canned
    16074: ['Lima bean', 'thin seeded'], # Lima beans, thin seeded (baby), mature seeds, raw
    16075: [], # Lima beans, thin seeded (baby), mature seeds, cooked, boiled, without salt
    16076: ['Lupin'], # Lupins, mature seeds, raw
    16077: [], # Lupins, mature seeds, cooked, boiled, without salt
    16078: ['Mothbean'], # Mothbeans, mature seeds, raw
    16079: [], # Mothbeans, mature seeds, cooked, boiled, without salt
    16080: ['Mung bean'], # Mung beans, mature seeds, raw
    16081: [], # Mung beans, mature seeds, cooked, boiled, without salt
    16082: [], # Noodles, chinese, cellophane or long rice (mung beans), dehydrated
    16083: ['Mungo bean'], # Mungo beans, mature seeds, raw
    16084: [], # Mungo beans, mature seeds, cooked, boiled, without salt
    16085: ['Pea', 'green'], # Peas, green, split, mature seeds, raw
    16086: [], # Peas, split, mature seeds, cooked, boiled, without salt
    16087: ['Peanut'], # Peanuts, all types, raw
    16088: [], # Peanuts, all types, cooked, boiled, with salt
    16089: [], # Peanuts, all types, oil-roasted, with salt
    16090: [], # Peanuts, all types, dry-roasted, with salt
    16091: ['Peanut', 'spanish'], # Peanuts, spanish, raw
    16092: [], # Peanuts, spanish, oil-roasted, with salt
    16093: ['Peanut', 'valencia'], # Peanuts, valencia, raw
    16094: [], # Peanuts, valencia, oil-roasted, with salt
    16095: ['Peanut', 'virginia'], # Peanuts, virginia, raw
    16096: [], # Peanuts, virginia, oil-roasted, with salt
    16097: [], # Peanut butter, chunk style, with salt
    16098: [], # Peanut butter, smooth style, with salt (Includes foods for USDA's Food Distribution Program)
    16099: [], # Peanut flour, defatted
    16100: [], # Peanut flour, low fat
    16101: ['Pigeon pea'], # Pigeon peas (red gram), mature seeds, raw
    16102: [], # Pigeon peas (red gram), mature seeds, cooked, boiled, without salt
    16103: [], # Refried beans, canned, traditional style
    16104: [], # Bacon, meatless
    16106: [], # Meat extender
    16107: [], # Sausage, meatless
    16108: ['Soybean'], # Soybeans, mature seeds, raw
    16109: [], # Soybeans, mature cooked, boiled, without salt
    16110: [], # Soybeans, mature seeds, roasted, salted
    16111: [], # Soybeans, mature seeds, dry roasted
    16112: [], # Miso
    16113: [], # Natto
    16114: [], # Tempeh
    16115: ['Soy flour'], # Soy flour, full-fat, raw
    16116: [], # Soy flour, full-fat, roasted
    16117: [], # Soy flour, defatted
    16118: [], # Soy flour, low-fat
    16119: ['Soy meal', 'defatted'], # Soy meal, defatted, raw
    16120: ['Soymilk'], # Soymilk, original and vanilla, unfortified
    16121: [], # Soy protein concentrate, produced by alcohol extraction
    16122: [], # Soy protein isolate
    16123: [], # Soy sauce made from soy and wheat (shoyu)
    16124: [], # Soy sauce made from soy (tamari)
    16125: [], # Soy sauce made from hydrolyzed vegetable protein
    16126: [], # Tofu, firm, prepared with calcium sulfate and magnesium chloride (nigari)
    16127: [], # Tofu, soft, prepared with calcium sulfate and magnesium chloride (nigari)
    16128: [], # Tofu, dried-frozen (koyadofu)
    16129: [], # Tofu, fried
    16130: [], # Okara
    16132: [], # Tofu, salted and fermented (fuyu)
    16133: ['Yardlong bean'], # Yardlong beans, mature seeds, raw
    16134: [], # Yardlong beans, mature seeds, cooked, boiled, without salt
    16135: [], # Winged beans, mature seeds, raw
    16136: [], # Winged beans, mature seeds, cooked, boiled, without salt
    16137: [], # Hummus, home prepared
    16138: ["Falafel"], # Falafel, home-prepared
    16139: [], # Soymilk, original and vanilla, with added calcium, vitamins A and D
    16144: ['Lentil', 'pink red'], # Lentils, pink or red, raw
    16145: [], # Beans, kidney, red, mature seeds, canned, drained solids
    16146: [], # Beans, pinto, canned, drained solids
    16147: [], # Veggie burgers or soyburgers, unprepared
    16149: [], # Peanut spread, reduced sugar
    16150: [], # Peanut butter, smooth, reduced fat
    16155: [], # Peanut butter, smooth, vitamin and mineral fortified
    16156: [], # Peanut butter, chunky, vitamin and mineral fortified
    16157: [], # Chickpea flour (besan)
    16158: ["Hummus"], # Hummus, commercial
    16159: [], # Tofu, extra firm, prepared with nigari
    16160: [], # Tofu, hard, prepared with nigari
    16161: [], # MORI-NU, Tofu, silken, soft
    16162: [], # MORI-NU, Tofu, silken, firm
    16163: [], # MORI-NU, Tofu, silken, extra firm
    16164: [], # MORI-NU, Tofu, silken, lite firm
    16165: [], # MORI-NU, Tofu, silken, lite extra firm
    16166: [], # Soymilk, chocolate, unfortified
    16167: [], # Peanut Butter, smooth (Includes foods for USDA's Food Distribution Program)
    16168: [], # Soymilk, chocolate, with added calcium, vitamins A and D
    16171: [], # Refried beans, canned, vegetarian
    16172: [], # Refried beans, canned, fat-free
    16173: [], # Frijoles rojos volteados (Refried beans, red, canned)
    16174: [], # Tempeh, cooked
    16210: [], # Vitasoy USA, Nasoya Lite Firm Tofu
    16211: [], # Vitasoy USA, Organic Nasoya Super Firm Cubed Tofu
    16212: [], # Vitasoy USA, Organic Nasoya Extra Firm Tofu
    16213: [], # Vitasoy USA, Organic Nasoya Firm Tofu
    16214: [], # Vitasoy USA, Organic Nasoya Silken Tofu
    16215: [], # Vitasoy USA, Vitasoy Organic Creamy Original Soymilk
    16216: [], # Vitasoy USA, Vitasoy Organic Classic Original Soymilk
    16219: [], # Vitasoy USA, Vitasoy Light Vanilla Soymilk
    16222: [], # Soymilk (all flavors), unsweetened, with added calcium, vitamins A and D
    16223: [], # Soymilk (All flavors), enhanced
    16225: [], # Soymilk, original and vanilla, light, with added calcium, vitamins A and D
    16227: [], # Soymilk, chocolate and other flavors, light, with added calcium, vitamins A and D
    16228: [], # Soymilk, original and vanilla, light, unsweetened, with added calcium, vitamins A and D
    16229: [], # Soymilk (All flavors), lowfat, with added calcium, vitamins A and D
    16230: [], # Soymilk (all flavors), nonfat, with added calcium, vitamins A and D
    16231: [], # Soymilk, chocolate, nonfat, with added calcium, vitamins A and D
    16235: [], # SILK Plain, soymilk
    16236: [], # SILK Vanilla, soymilk
    16237: [], # SILK Chocolate, soymilk
    16238: [], # SILK Light Plain, soymilk
    16239: [], # SILK Light Vanilla, soymilk
    16240: [], # SILK Light Chocolate, soymilk
    16241: [], # SILK Plus Omega-3 DHA, soymilk
    16242: [], # SILK Plus for Bone Health, soymilk
    16243: [], # SILK Plus Fiber, soymilk
    16244: [], # SILK Unsweetened, soymilk
    16245: [], # SILK Very Vanilla, soymilk
    16246: [], # SILK Nog, soymilk
    16247: [], # SILK Chai, soymilk
    16248: [], # SILK Mocha, soymilk
    16249: [], # SILK Coffee, soymilk
    16250: [], # SILK Vanilla soy yogurt (family size)
    16251: [], # SILK Vanilla soy yogurt (single serving size)
    16252: [], # SILK Plain soy yogurt
    16253: [], # SILK Strawberry soy yogurt
    16254: [], # SILK Raspberry soy yogurt
    16255: [], # SILK Peach soy yogurt
    16256: [], # SILK Black Cherry soy yogurt
    16257: [], # SILK Blueberry soy yogurt
    16258: [], # SILK Key Lime soy yogurt
    16259: [], # SILK Banana-Strawberry soy yogurt
    16260: [], # SILK Original Creamer
    16261: [], # SILK French Vanilla Creamer
    16262: [], # SILK Hazelnut Creamer
    16271: [], # Vitasoy USA Organic Nasoya, Soft Tofu
    16272: [], # Vitasoy USA Nasoya, Lite Silken Tofu
    16273: [], # Vitasoy USA Organic Nasoya, Tofu Plus Extra Firm
    16274: [], # Vitasoy USA Organic Nasoya, Tofu Plus Firm
    16275: [], # Vitasoy USA Organic Nasoya Sprouted, Tofu Plus Super Firm
    16276: [], # Vitasoy USA Azumaya, Extra Firm Tofu
    16277: [], # Vitasoy USA Azumaya, Firm Tofu
    16278: [], # Vitasoy USA Azumaya, Silken Tofu
    16279: [], # HOUSE FOODS Premium Soft Tofu
    16281: [], # HOUSE FOODS Premium Firm Tofu
    16302: [], # Beans, adzuki, mature seed, cooked, boiled, with salt
    16315: [], # Beans, black, mature seeds, cooked, boiled, with salt
    16316: [], # Beans, black, mature seeds, canned, low sodium
    16317: [], # Beans, black turtle, mature seeds, cooked, boiled, with salt
    16320: [], # Beans, cranberry (roman), mature seeds, cooked, boiled, with salt
    16323: [], # Beans, french, mature seeds, cooked, boiled, with salt
    16325: [], # Beans, great northern, mature seeds, cooked, boiled, with salt
    16326: [], # Beans, great northern, mature seeds, canned, low sodium
    16328: [], # Beans, kidney, all types, mature seeds, cooked, boiled, with salt
    16331: [], # Beans, kidney, california red, mature seeds, cooked, boiled, with salt
    16333: [], # Beans, kidney, red, mature seeds, cooked, boiled, with salt
    16335: [], # Beans, kidney, red, mature seeds, canned, drained solids, rinsed in tap water
    16336: [], # Beans, kidney, royal red, mature seeds, cooked, boiled with salt
    16337: [], # Beans, kidney, red, mature seeds, canned, solids and liquid, low sodium
    16338: [], # Beans, navy, mature seeds, cooked, boiled, with salt
    16341: [], # Beans, pink, mature seeds, cooked, boiled, with salt
    16343: [], # Beans, pinto, mature seeds, cooked, boiled, with salt
    16345: [], # Beans, pinto, mature seeds, canned, drained solids, rinsed in tap water
    16346: [], # Beans, small white, mature seeds, cooked, boiled, with salt
    16347: [], # Beans, pinto, mature seeds, canned, solids and liquids, low sodium
    16348: [], # Beans, yellow, mature seeds, cooked, boiled, with salt
    16350: [], # Beans, white, mature seeds, cooked, boiled, with salt
    16353: [], # Broadbeans (fava beans), mature seeds, cooked, boiled, with salt
    16357: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, cooked, boiled, with salt
    16358: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, canned, drained solids
    16359: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, canned, drained, rinsed in tap water
    16360: [], # Chickpeas (garbanzo beans, bengal gram), mature seeds, canned, solids and liquids, low sodium
    16361: [], # Cowpeas, catjang, mature seeds, cooked, boiled, with salt
    16363: [], # Cowpeas, common (blackeyes, crowder, southern), mature seeds, cooked, boiled, with salt
    16368: [], # Hyacinth beans, mature seeds, cooked, boiled, with salt
    16370: [], # Lentils, mature seeds, cooked, boiled, with salt
    16372: [], # Lima beans, large, mature seeds, cooked, boiled, with salt
    16375: [], # Lima beans, thin seeded (baby), mature seeds, cooked, boiled, with salt
    16377: [], # Lupins, mature seeds, cooked, boiled, with salt
    16379: [], # Mothbeans, mature seeds, cooked, boiled, with salt
    16381: [], # Mung beans, mature seeds, cooked, boiled, with salt
    16384: [], # Mungo beans, mature seeds, cooked, boiled, with salt
    16386: [], # Peas, split, mature seeds, cooked, boiled, with salt
    16389: [], # Peanuts, all types, oil-roasted, without salt
    16390: [], # Peanuts, all types, dry-roasted, without salt
    16392: [], # Peanuts, spanish, oil-roasted, without salt
    16394: [], # Peanuts, valencia, oil-roasted, without salt
    16396: [], # Peanuts, virginia, oil-roasted, without salt
    16397: [], # Peanut butter, chunk style, without salt
    16398: [], # Peanut butter, smooth style, without salt
    16399: [], # Peanut butter with omega-3, creamy
    16402: [], # Pigeon peas (red gram), mature seeds, cooked, boiled, with salt
    16403: [], # Refried beans, canned, traditional, reduced sodium
    16409: [], # Soybeans, mature seeds, cooked, boiled, with salt
    16410: [], # Soybeans, mature seeds, roasted, no salt added
    16420: [], # Soy protein concentrate, produced by acid wash
    16422: [], # Soy protein isolate, potassium type
    16424: [], # Soy sauce made from soy and wheat (shoyu), low sodium
    16425: [], # Soy sauce, reduced sodium, made from hydrolyzed vegetable protein
    16426: ['Tofu', 'firm'], # Tofu, raw, firm, prepared with calcium sulfate
    16427: ['Tofu', 'regular'], # Tofu, raw, regular, prepared with calcium sulfate
    16428: [], # Tofu, dried-frozen (koyadofu), prepared with calcium sulfate
    16429: [], # Tofu, fried, prepared with calcium sulfate
    16432: [], # Tofu, salted and fermented (fuyu), prepared with calcium sulfate
    16434: [], # Yardlong beans, mature seeds, cooked, boiled, with salt
    16436: [], # Winged beans, mature seeds, cooked, boiled, with salt
    17000: [], # Veal, Australian, rib, rib roast, separable lean only, raw
    17001: [], # Lamb, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17002: [], # Lamb, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/4" fat, choice, cooked
    17003: [], # Lamb, composite of trimmed retail cuts, separable lean only, trimmed to 1/4" fat, choice, raw
    17004: [], # Lamb, composite of trimmed retail cuts, separable lean only, trimmed to 1/4" fat, choice, cooked
    17005: [], # Lamb, composite of trimmed retail cuts, separable fat, trimmed to 1/4" fat, choice, raw
    17006: [], # Lamb, composite of trimmed retail cuts, separable fat, trimmed to 1/4" fat, choice, cooked
    17007: ['Lamb foreshank'], # Lamb, foreshank, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17008: [], # Lamb, foreshank, separable lean and fat, trimmed to 1/4" fat, choice, cooked, braised
    17009: [], # Lamb, foreshank, separable lean only, trimmed to 1/4" fat, choice, raw
    17010: [], # Lamb, foreshank, separable lean only, trimmed to 1/4" fat, choice, cooked, braised
    17011: ['Lamb leg', 'whole'], # Lamb, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/4" fat, choice, raw
    17012: [], # Lamb, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17013: [], # Lamb, leg, whole (shank and sirloin), separable lean only, trimmed to 1/4" fat, choice, raw
    17014: [], # Lamb, leg, whole (shank and sirloin), separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17015: ['Lamb leg', 'shank half'], # Lamb, leg, shank half, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17016: [], # Lamb, leg, shank half, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17017: [], # Lamb, leg, shank half, separable lean only, trimmed to 1/4" fat, choice, raw
    17018: [], # Lamb, leg, shank half, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17019: ['Lamb leg', 'sirloin half'], # Lamb, leg, sirloin half, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17020: [], # Lamb, leg, sirloin half, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17021: [], # Lamb, leg, sirloin half, separable lean only, trimmed to 1/4" fat, choice, raw
    17022: [], # Lamb, leg, sirloin half, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17023: ['Lamb loin'], # Lamb, loin, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17024: [], # Lamb, loin, separable lean and fat, trimmed to 1/4" fat, choice, cooked, broiled
    17025: [], # Lamb, loin, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17026: [], # Lamb, loin, separable lean only, trimmed to 1/4" fat, choice, raw
    17027: [], # Lamb, loin, separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    17028: [], # Lamb, loin, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17029: ['Lamb rib'], # Lamb, rib, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17030: [], # Lamb, rib, separable lean and fat, trimmed to 1/4" fat, choice, cooked, broiled
    17031: [], # Lamb, rib, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17032: [], # Lamb, rib, separable lean only, trimmed to 1/4" fat, choice, raw
    17033: [], # Lamb, rib, separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    17034: [], # Lamb, rib, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17035: ['Lamb shoulder', 'whole'], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/4" fat, choice, raw
    17036: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/4" fat, choice, cooked, braised
    17037: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/4" fat, choice, cooked, broiled
    17038: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17039: [], # Lamb, shoulder, whole (arm and blade), separable lean only, trimmed to 1/4" fat, choice, raw
    17040: [], # Lamb, shoulder, whole (arm and blade), separable lean only, trimmed to 1/4" fat, choice, cooked, braised
    17041: [], # Lamb, shoulder, whole (arm and blade), separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    17042: [], # Lamb, shoulder, whole (arm and blade), separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17043: ['Lamb shoulder', 'arm'], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17044: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/4" fat, choice, cooked, braised
    17045: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/4" fat, choice, cooked, broiled
    17046: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17047: [], # Lamb, shoulder, arm, separable lean only, trimmed to 1/4" fat, choice, raw
    17048: [], # Lamb, shoulder, arm, separable lean only, trimmed to 1/4" fat, choice, cooked, braised
    17049: [], # Lamb, shoulder, arm, separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    17050: [], # Lamb, shoulder, arm, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17051: ['Lamb shoulder', 'blade'], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/4" fat, choice, raw
    17052: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/4" fat, choice, cooked, braised
    17053: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/4" fat, choice, cooked, broiled
    17054: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/4" fat, choice, cooked, roasted
    17055: [], # Lamb, shoulder, blade, separable lean only, trimmed to 1/4" fat, choice, raw
    17056: [], # Lamb, shoulder, blade, separable lean only, trimmed to 1/4" fat, choice, cooked, braised
    17057: [], # Lamb, shoulder, blade, separable lean only, trimmed to 1/4" fat, choice, cooked, broiled
    17058: [], # Lamb, shoulder, blade, separable lean only, trimmed to 1/4" fat, choice, cooked, roasted
    17059: [], # Lamb, cubed for stew or kabob (leg and shoulder), separable lean only, trimmed to 1/4" fat, raw
    17060: [], # Lamb, cubed for stew or kabob (leg and shoulder), separable lean only, trimmed to 1/4" fat, cooked, braised
    17061: [], # Lamb, cubed for stew or kabob (leg and shoulder), separable lean only, trimmed to 1/4" fat, cooked, broiled
    17062: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean and fat, raw
    17063: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean and fat, cooked
    17064: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean only, raw
    17065: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean only, cooked
    17066: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable fat, raw
    17067: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable fat, cooked
    17068: [], # Lamb, New Zealand, imported, fore-shank, separable lean and fat, raw
    17069: [], # Lamb, New Zealand, imported, fore-shank, separable lean and fat, cooked, braised
    17070: [], # Lamb, New Zealand, imported, fore-shank, separable lean only, raw
    17071: [], # Lamb, New Zealand, imported, fore-shank, separable lean only, cooked, braised
    17072: [], # Lamb, New Zealand, imported, leg chop/steak, bone-in, separable lean and fat, raw
    17073: [], # Lamb, New Zealand, imported, frozen, leg, whole (shank and sirloin), separable lean and fat, cooked, roasted
    17074: [], # Lamb, New Zealand, imported, leg chop/steak, bone-in, separable lean only, raw
    17075: [], # Lamb, New Zealand, imported, frozen, leg, whole (shank and sirloin), separable lean only, cooked, roasted
    17076: [], # Lamb, New Zealand, imported, loin chop, separable lean and fat, raw
    17077: [], # Lamb, New Zealand, imported, frozen, loin, separable lean and fat, cooked, broiled
    17078: [], # Lamb, New Zealand, imported, loin chop, separable lean only, raw
    17079: [], # Lamb, New Zealand, imported, frozen, loin, separable lean only, cooked, broiled
    17080: [], # Lamb, New Zealand, imported, rack - partly frenched, separable lean and fat, raw
    17081: [], # Lamb, New Zealand, imported, rack - partly frenched, separable lean and fat, cooked, fast roasted
    17082: [], # Lamb, New Zealand, imported, rack - partly frenched, separable lean only, raw
    17083: [], # Lamb, New Zealand, imported, rack - partly frenched, separable lean only, cooked, fast roasted
    17084: [], # Lamb, New Zealand, imported, square-cut shoulder, separable lean and fat, raw
    17085: [], # Lamb, New Zealand, imported, frozen, shoulder, whole (arm and blade), separable lean and fat, cooked, braised
    17086: [], # Lamb, New Zealand, imported, square-cut shoulder, separable lean only, raw
    17087: [], # Lamb, New Zealand, imported, frozen, shoulder, whole (arm and blade), separable lean only, cooked, braised
    17088: [], # Veal, composite of trimmed retail cuts, separable lean and fat, raw
    17089: [], # Veal, composite of trimmed retail cuts, separable lean and fat, cooked
    17090: [], # Veal, composite of trimmed retail cuts, separable lean only, raw
    17091: [], # Veal, composite of trimmed retail cuts, separable lean only, cooked
    17092: [], # Veal, composite of trimmed retail cuts, separable fat, raw
    17093: [], # Veal, composite of trimmed retail cuts, separable fat, cooked
    17094: ['Veal leg'], # Veal, leg (top round), separable lean and fat, raw
    17095: [], # Veal, leg (top round), separable lean and fat, cooked, braised
    17096: [], # Veal, leg (top round), separable lean and fat, cooked, pan-fried, breaded
    17097: [], # Veal, leg (top round), separable lean and fat, cooked, pan-fried, not breaded
    17098: [], # Veal, leg (top round), separable lean and fat, cooked, roasted
    17099: [], # Veal, leg (top round), separable lean only, raw
    17100: [], # Veal, leg (top round), separable lean only, cooked, braised
    17101: [], # Veal, leg (top round), separable lean only, cooked, pan-fried, breaded
    17102: [], # Veal, leg (top round), separable lean only, cooked, pan-fried, not breaded
    17103: [], # Veal, leg (top round), separable lean only, cooked, roasted
    17104: ['Veal loin'], # Veal, loin, separable lean and fat, raw
    17105: [], # Veal, loin, separable lean and fat, cooked, braised
    17106: [], # Veal, loin, separable lean and fat, cooked, roasted
    17107: [], # Veal, loin, separable lean only, raw
    17108: [], # Veal, loin, separable lean only, cooked, braised
    17109: [], # Veal, loin, separable lean only, cooked, roasted
    17110: ['Veal rib'], # Veal, rib, separable lean and fat, raw
    17111: [], # Veal, rib, separable lean and fat, cooked, braised
    17112: [], # Veal, rib, separable lean and fat, cooked, roasted
    17113: [], # Veal, rib, separable lean only, raw
    17114: [], # Veal, rib, separable lean only, cooked, braised
    17115: [], # Veal, rib, separable lean only, cooked, roasted
    17116: ['Veal shoulder', 'whole'], # Veal, shoulder, whole (arm and blade), separable lean and fat, raw
    17117: [], # Veal, shoulder, whole (arm and blade), separable lean and fat, cooked, braised
    17118: [], # Veal, shoulder, whole (arm and blade), separable lean and fat, cooked, roasted
    17119: [], # Veal, shoulder, whole (arm and blade), separable lean only, raw
    17120: [], # Veal, shoulder, whole (arm and blade), separable lean only, cooked, braised
    17121: [], # Veal, shoulder, whole (arm and blade), separable lean only, cooked, roasted
    17122: ['Veal shoulder', 'arm'], # Veal, shoulder, arm, separable lean and fat, raw
    17123: [], # Veal, shoulder, arm, separable lean and fat, cooked, braised
    17124: [], # Veal, shoulder, arm, separable lean and fat, cooked, roasted
    17125: [], # Veal, shoulder, arm, separable lean only, raw
    17126: [], # Veal, shoulder, arm, separable lean only, cooked, braised
    17127: [], # Veal, shoulder, arm, separable lean only, cooked, roasted
    17128: ['Veal shoulder', 'blade chop'], # Veal, shoulder, blade chop, separable lean and fat, raw
    17129: [], # Veal, shoulder, blade, separable lean and fat, cooked, braised
    17130: [], # Veal, shoulder, blade, separable lean and fat, cooked, roasted
    17131: [], # Veal, shoulder, blade chop, separable lean only, raw
    17132: [], # Veal, shoulder, blade, separable lean only, cooked, braised
    17133: [], # Veal, shoulder, blade, separable lean only, cooked, roasted
    17134: ['Veal sirloin'], # Veal, sirloin, separable lean and fat, raw
    17135: [], # Veal, sirloin, separable lean and fat, cooked, braised
    17136: [], # Veal, sirloin, separable lean and fat, cooked, roasted
    17137: [], # Veal, sirloin, separable lean only, raw
    17138: [], # Veal, sirloin, separable lean only, cooked, braised
    17139: [], # Veal, sirloin, separable lean only, cooked, roasted
    17140: [], # Veal, cubed for stew (leg and shoulder), separable lean only, raw
    17141: [], # Veal, cubed for stew (leg and shoulder), separable lean only, cooked, braised
    17142: ['Veal', 'ground'], # Veal, ground, raw
    17143: [], # Veal, ground, cooked, broiled
    17144: ['Antelope'], # Game meat, antelope, raw
    17145: [], # Game meat, antelope, cooked, roasted
    17146: ['Bear'], # Game meat, bear, raw
    17147: [], # Game meat, bear, cooked, simmered
    17148: [], # Bison, ground, grass-fed, cooked
    17149: ['Bison', 'ground'], # Bison, ground, grass-fed, raw
    17150: ['Beaver'], # Game meat, beaver, raw
    17151: [], # Game meat, beaver, cooked, roasted
    17152: ['Beefalo'], # Game meat, beefalo, composite of cuts, raw
    17153: [], # Game meat, beefalo, composite of cuts, cooked, roasted
    17154: [], # Veal, Australian, separable fat, raw
    17155: [], # Veal, Australian, rib, rib roast, separable lean and fat, raw
    17156: ['Bison'], # Game meat, bison, separable lean only, raw
    17157: [], # Game meat, bison, separable lean only, cooked, roasted
    17158: ['Boar'], # Game meat, boar, wild, raw
    17159: [], # Game meat, boar, wild, cooked, roasted
    17160: ['Buffalo'], # Game meat, buffalo, water, raw
    17161: [], # Game meat, buffalo, water, cooked, roasted
    17162: ['Caribou'], # Game meat, caribou, raw
    17163: [], # Game meat, caribou, cooked, roasted
    17164: ['Deer'], # Game meat, deer, raw
    17165: [], # Game meat, deer, cooked, roasted
    17166: ['Elk'], # Game meat, elk, raw
    17167: [], # Game meat, elk, cooked, roasted
    17168: ['Goat'], # Game meat, goat, raw
    17169: [], # Game meat, goat, cooked, roasted
    17170: ['Horse'], # Game meat, horse, raw
    17171: [], # Game meat, horse, cooked, roasted
    17172: ['Moose'], # Game meat, moose, raw
    17173: [], # Game meat, moose, cooked, roasted
    17174: ['Muskrat'], # Game meat, muskrat, raw
    17175: [], # Game meat, muskrat, cooked, roasted
    17176: [], # Game meat, opossum, cooked, roasted
    17177: [], # Game meat, rabbit, domesticated, composite of cuts, raw
    17178: [], # Game meat, rabbit, domesticated, composite of cuts, cooked, roasted
    17179: [], # Game meat, rabbit, domesticated, composite of cuts, cooked, stewed
    17180: ['Rabbit'], # Game meat, rabbit, wild, raw
    17181: [], # Game meat, rabbit, wild, cooked, stewed
    17182: [], # Game meat, raccoon, cooked, roasted
    17183: ['Squirrel'], # Game meat, squirrel, raw
    17184: [], # Game meat, squirrel, cooked, roasted
    17185: ['Lamb brain'], # Lamb, variety meats and by-products, brain, raw
    17186: [], # Lamb, variety meats and by-products, brain, cooked, braised
    17187: [], # Lamb, variety meats and by-products, brain, cooked, pan-fried
    17188: ['Veal brain'], # Veal, variety meats and by-products, brain, raw
    17189: [], # Veal, variety meats and by-products, brain, cooked, braised
    17190: [], # Veal, variety meats and by-products, brain, cooked, pan-fried
    17191: ['Lamb heart'], # Lamb, variety meats and by-products, heart, raw
    17192: [], # Lamb, variety meats and by-products, heart, cooked, braised
    17193: ['Veal heart'], # Veal, variety meats and by-products, heart, raw
    17194: [], # Veal, variety meats and by-products, heart, cooked, braised
    17195: ['Lamb kidney'], # Lamb, variety meats and by-products, kidneys, raw
    17196: [], # Lamb, variety meats and by-products, kidneys, cooked, braised
    17197: ['Veal kidney'], # Veal, variety meats and by-products, kidneys, raw
    17198: [], # Veal, variety meats and by-products, kidneys, cooked, braised
    17199: ['Lamb liver'], # Lamb, variety meats and by-products, liver, raw
    17200: [], # Lamb, variety meats and by-products, liver, cooked, braised
    17201: [], # Lamb, variety meats and by-products, liver, cooked, pan-fried
    17202: ['Veal liver'], # Veal, variety meats and by-products, liver, raw
    17203: [], # Veal, variety meats and by-products, liver, cooked, braised
    17204: [], # Veal, variety meats and by-products, liver, cooked, pan-fried
    17205: ['Lamb lung'], # Lamb, variety meats and by-products, lungs, raw
    17206: [], # Lamb, variety meats and by-products, lungs, cooked, braised
    17207: ['Veal lung'], # Veal, variety meats and by-products, lungs, raw
    17208: [], # Veal, variety meats and by-products, lungs, cooked, braised
    17209: [], # Lamb, variety meats and by-products, mechanically separated, raw
    17210: ['Lamb pancreas'], # Lamb, variety meats and by-products, pancreas, raw
    17211: [], # Lamb, variety meats and by-products, pancreas, cooked, braised
    17212: ['Veal pancreas'], # Veal, variety meats and by-products, pancreas, raw
    17213: [], # Veal, variety meats and by-products, pancreas, cooked, braised
    17214: ['Lamb spleen'], # Lamb, variety meats and by-products, spleen, raw
    17215: [], # Lamb, variety meats and by-products, spleen, cooked, braised
    17216: ['Veal spleen'], # Veal, variety meats and by-products, spleen, raw
    17217: [], # Veal, variety meats and by-products, spleen, cooked, braised
    17218: ['Veal thymus'], # Veal, variety meats and by-products, thymus, raw
    17219: [], # Veal, variety meats and by-products, thymus, cooked, braised
    17220: ['Lamb tongue'], # Lamb, variety meats and by-products, tongue, raw
    17221: [], # Lamb, variety meats and by-products, tongue, cooked, braised
    17222: ['Veal tongue'], # Veal, variety meats and by-products, tongue, raw
    17223: [], # Veal, variety meats and by-products, tongue, cooked, braised
    17224: ['Lamb', 'ground'], # Lamb, ground, raw
    17225: [], # Lamb, ground, cooked, broiled
    17226: [], # Lamb, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17227: [], # Lamb, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, choice, cooked
    17228: [], # Lamb, foreshank, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17229: [], # Lamb, foreshank, separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17230: [], # Lamb, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, choice, raw
    17231: [], # Lamb, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17232: [], # Lamb, leg, shank half, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17233: [], # Lamb, leg, shank half, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17234: [], # Lamb, leg, sirloin half, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17235: [], # Lamb, leg, sirloin half, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17236: [], # Lamb, loin, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17237: [], # Lamb, loin, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    17238: [], # Lamb, loin, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17239: [], # Lamb, rib, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17240: [], # Lamb, rib, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    17241: [], # Lamb, rib, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17242: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, choice, raw
    17243: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    17244: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    17245: [], # Lamb, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17246: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17247: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    17248: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17249: [], # Lamb, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, choice, roasted
    17250: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, choice, raw
    17251: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    17252: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, choice, cooked, broiled
    17253: [], # Lamb, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    17254: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, raw
    17255: [], # Lamb, New Zealand, imported, frozen, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, cooked
    17256: [], # Lamb, New Zealand, imported, frozen, foreshank, separable lean and fat, trimmed to 1/8" fat, raw
    17257: [], # Lamb, New Zealand, imported, frozen, foreshank, separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17258: [], # Lamb, New Zealand, imported, frozen, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, raw
    17259: [], # Lamb, New Zealand, imported, frozen, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17260: [], # Lamb, New Zealand, imported, frozen, loin, separable lean and fat, trimmed to 1/8" fat, raw
    17261: [], # Lamb, New Zealand, imported, frozen, loin, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17262: [], # Lamb, new zealand, imported, frozen, rib, separable lean and fat, trimmed to 1/8" fat, raw
    17263: [], # Lamb, New Zealand, imported, frozen, rib, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17264: [], # Lamb, New Zealand, imported, frozen, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, raw
    17265: [], # Lamb, New Zealand, imported, frozen, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17267: [], # Game meat, bison, top sirloin, separable lean only, trimmed to 0" fat, raw
    17268: [], # Game meat, bison, ribeye, separable lean only, trimmed to 0" fat, raw
    17269: [], # Game meat, bison, shoulder clod, separable lean only, trimmed to 0" fat, raw
    17270: [], # Veal, breast, separable fat, cooked
    17271: ['Veal breast', 'boneless whole'], # Veal, breast, whole, boneless, separable lean and fat, raw
    17272: [], # Veal, breast, whole, boneless, separable lean and fat, cooked, braised
    17273: [], # Veal, breast, plate half, boneless, separable lean and fat, cooked, braised
    17274: [], # Veal, breast, point half, boneless, separable lean and fat, cooked, braised
    17275: [], # Veal, breast, whole, boneless, separable lean only, cooked, braised
    17276: [], # Veal, shank (fore and hind), separable lean and fat, raw
    17277: [], # Veal, shank (fore and hind), separable lean and fat, cooked, braised
    17278: [], # Veal, shank (fore and hind), separable lean only, raw
    17279: [], # Veal, shank (fore and hind), separable lean only, cooked, braised
    17280: [], # Lamb, Australian, imported, fresh, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, raw
    17281: [], # Lamb, Australian, imported, fresh, composite of trimmed retail cuts, separable lean and fat, trimmed to 1/8" fat, cooked
    17282: [], # Lamb, Australian, imported, fresh, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, raw
    17283: [], # Lamb, Australian, imported, fresh, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, cooked
    17284: [], # Lamb, Australian, imported, fresh, separable fat, raw
    17285: [], # Lamb, Australian, imported, fresh, separable fat, cooked
    17286: [], # Lamb, Australian, imported, fresh, foreshank, separable lean and fat, trimmed to 1/8" fat, raw
    17287: [], # Lamb, Australian, imported, fresh, foreshank, separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17288: [], # Lamb, Australian, imported, fresh, foreshank, separable lean only, trimmed to 1/8" fat, raw
    17289: [], # Lamb, Australian, imported, fresh, foreshank, separable lean only, trimmed to 1/8" fat, cooked, braised
    17290: [], # Lamb, Australian, imported, fresh, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, raw
    17291: [], # Lamb, Australian, imported, fresh, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17292: [], # Lamb, Australian, imported, fresh, leg, whole (shank and sirloin), separable lean only, trimmed to 1/8" fat, raw
    17293: [], # Lamb, Australian, imported, fresh, leg, whole (shank and sirloin), separable lean only, trimmed to 1/8" fat, cooked, roasted
    17294: [], # Lamb, Australian, imported, fresh, leg, shank half, separable lean and fat, trimmed to 1/8" fat, raw
    17295: [], # Lamb, Australian, imported, fresh, leg, shank half, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17296: [], # Lamb, Australian, imported, fresh, leg, shank half, separable lean only, trimmed to 1/8" fat, raw
    17297: [], # Lamb, Australian, imported, fresh, leg, shank half, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17298: [], # Lamb, Australian, imported, fresh, leg, sirloin half, boneless, separable lean and fat, trimmed to 1/8" fat, raw
    17299: [], # Lamb, Australian, imported, fresh, leg, sirloin half, boneless, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17300: [], # Lamb, Australian, imported, fresh, leg, sirloin half, boneless, separable lean only, trimmed to 1/8" fat, raw
    17301: [], # Lamb, Australian, imported, fresh, leg, sirloin half, boneless, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17302: [], # Lamb, Australian, imported, fresh, leg, sirloin chops, boneless, separable lean and fat, trimmed to 1/8" fat, raw
    17303: [], # Lamb, Australian, imported, fresh, leg, sirloin chops, boneless, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17304: [], # Lamb, Australian, imported, fresh, leg, sirloin chops, boneless, separable lean only, trimmed to 1/8" fat, raw
    17305: [], # Lamb, Australian, imported, fresh, leg, sirloin chops, boneless, separable lean only, trimmed to 1/8" fat, cooked, broiled
    17306: [], # Lamb, Australian, imported, fresh, leg, center slice, bone-in, separable lean and fat, trimmed to 1/8" fat, raw
    17307: [], # Lamb, Australian, imported, fresh, leg, center slice, bone-in, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17308: [], # Lamb, Australian, imported, fresh, leg, center slice, bone-in, separable lean only, trimmed to 1/8" fat, raw
    17309: [], # Lamb, Australian, imported, fresh, leg, center slice, bone-in, separable lean only, trimmed to 1/8" fat, cooked, broiled
    17310: [], # Lamb, Australian, imported, fresh, loin, separable lean and fat, trimmed to 1/8" fat, raw
    17311: [], # Lamb, Australian, imported, fresh, loin, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17312: [], # Lamb, Australian, imported, fresh, loin, separable lean only, trimmed to 1/8" fat, raw
    17313: [], # Lamb, Australian, imported, fresh, loin, separable lean only, trimmed to 1/8" fat, cooked, broiled
    17314: [], # Lamb, Australian, imported, fresh, rib chop/rack roast, frenched, bone-in, separable lean and fat, trimmed to 1/8" fat, raw
    17315: [], # Lamb, Australian, imported, fresh, rib chop, frenched, bone-in, separable lean and fat, trimmed to 1/8" fat, cooked, grilled
    17316: [], # Lamb, Australian, imported, fresh, rib chop/rack roast, frenched, bone-in, separable lean only, trimmed to 1/8" fat, raw
    17317: [], # Lamb, Australian, imported, fresh, rib chop, frenched, bone-in, separable lean only, trimmed to 1/8" fat, cooked, grilled
    17318: [], # Lamb, Australian, imported, fresh, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, raw
    17319: [], # Lamb, Australian, imported, fresh, shoulder, whole (arm and blade), separable lean and fat, trimmed to 1/8" fat, cooked
    17320: [], # Lamb, Australian, imported, fresh, shoulder, whole (arm and blade), separable lean only,   trimmed to 1/8" fat, raw
    17321: [], # Lamb, Australian, imported, fresh, shoulder, whole (arm and blade), separable lean only, trimmed to 1/8" fat, cooked
    17322: [], # Lamb, Australian, imported, fresh, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, raw
    17323: [], # Lamb, Australian, imported, fresh, shoulder, arm, separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17324: [], # Lamb, Australian, imported, fresh, shoulder, arm, separable lean only, trimmed to 1/8" fat, raw
    17325: [], # Lamb, Australian, imported, fresh, shoulder, arm, separable lean only,   trimmed to 1/8" fat, cooked, braised
    17326: [], # Lamb, Australian, imported, fresh, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, raw
    17327: [], # Lamb, Australian, imported, fresh, shoulder, blade, separable lean and fat, trimmed to 1/8" fat, cooked, broiled
    17328: [], # Lamb, Australian, imported, fresh, shoulder, blade, separable lean only, trimmed to 1/8" fat, raw
    17329: [], # Lamb, Australian, imported, fresh, shoulder ,blade, separable lean only, trimmed to 1/8" fat, cooked, broiled
    17330: ['Bison', 'ground'], # Game meat , bison, ground, raw
    17331: [], # Game meat, bison, ground, cooked, pan-broiled
    17332: [], # Game meat , bison, top sirloin, separable lean only, 1" steak, cooked, broiled
    17333: [], # Game meat, bison, chuck, shoulder clod, separable lean only, cooked, braised
    17334: [], # Game meat, bison, chuck, shoulder clod, separable lean only, raw
    17335: [], # Game meat, bison, ribeye, separable lean only, 1" steak, cooked, broiled
    17336: [], # Game meat, bison, top round, separable lean only, 1" steak, cooked, broiled
    17337: [], # Game meat, bison, top round, separable lean only, 1" steak, raw
    17338: ['Elk', 'ground'], # Game meat, elk, ground, raw
    17339: [], # Game meat, elk, ground, cooked, pan-broiled
    17340: [], # Game meat, elk, loin, separable lean only, cooked, broiled
    17341: [], # Game meat, elk, round, separable lean only, cooked, broiled
    17342: [], # Game meat, elk, tenderloin, separable lean only, cooked, broiled
    17343: ['Deer', 'ground'], # Game meat, deer, ground, raw
    17344: [], # Game meat, deer, ground, cooked, pan-broiled
    17345: [], # Game meat, deer, loin, separable lean only, 1" steak, cooked, broiled
    17346: [], # Game meat, deer, shoulder clod, separable lean only, cooked, braised
    17347: [], # Game meat, deer, tenderloin, separable lean only, cooked, broiled
    17348: [], # Game meat, deer, top round, separable lean only, 1" steak, cooked, broiled
    17349: [], # Veal, Australian, shank, fore, bone-in, separable lean only, raw
    17350: [], # Veal, Australian, shank, fore, bone-in, separable lean and fat, raw
    17351: [], # Veal, Australian, shank, hind, bone-in, separable lean only, raw
    17352: [], # Veal, Australian, shank, hind, bone-in, separable lean and fat, raw
    17353: [], # Lamb, Australian, ground,  85% lean / 15% fat, raw
    17354: [], # Lamb, New Zealand, imported, Intermuscular fat, cooked
    17355: [], # Lamb, New Zealand, imported, Intermuscular fat, raw
    17356: [], # Lamb, New Zealand, imported, subcutaneous fat, raw
    17357: [], # Lamb, New Zealand, imported, brains, cooked, soaked and fried
    17358: [], # Lamb, New Zealand, imported, brains, raw
    17359: [], # Lamb, New Zealand, imported, breast, separable lean only, cooked, braised
    17360: [], # Lamb, New Zealand, imported, breast, separable lean only, raw
    17361: [], # Lamb, New Zealand, imported, chump, boneless, separable lean only, cooked, fast roasted
    17362: [], # Lamb, New Zealand, imported, subcutaneous fat, cooked
    17363: [], # Lamb, New Zealand, imported, chump, boneless, separable lean only, raw
    17364: [], # Lamb, New Zealand, imported, kidney, cooked, soaked and fried
    17365: [], # Lamb, New Zealand, imported, flap, boneless, separable lean only, cooked, braised
    17366: [], # Lamb, New Zealand, imported, flap, boneless, separable lean only, raw
    17367: [], # Lamb, New Zealand, imported, kidney, raw
    17368: [], # Lamb, New Zealand, imported, liver, cooked, soaked and fried
    17369: [], # Lamb, New Zealand, imported, liver, raw
    17370: [], # Lamb, New Zealand, imported, ground lamb, cooked, braised
    17371: [], # Lamb, New Zealand, imported, ground lamb, raw
    17372: [], # Lamb, New Zealand, imported, heart, cooked, soaked and simmered
    17373: [], # Lamb, New Zealand, imported, heart, raw
    17374: [], # Lamb, New Zealand, imported, sweetbread, cooked, soaked and simmered
    17375: [], # Lamb, New Zealand, imported, sweetbread, raw
    17376: [], # Lamb, New Zealand, imported, testes, cooked, soaked and fried
    17377: [], # Lamb, New Zealand, imported, testes, raw
    17378: [], # Lamb, New Zealand, imported, tongue - swiss cut, cooked, soaked and simmered
    17379: [], # Lamb, New Zealand, imported, tongue - swiss cut, raw
    17380: [], # Lamb, New Zealand, imported, tunnel-boned leg, chump off, shank off, separable lean only, cooked, slow roasted
    17381: [], # Lamb, New Zealand, imported, tunnel-boned leg, chump off, shank off, separable lean only, raw
    17382: [], # Lamb, New Zealand, imported, square-cut shoulder chops, separable lean only, cooked, braised
    17383: [], # Lamb, New Zealand, imported, square-cut shoulder chops, separable lean only, raw
    17384: [], # Lamb, New Zealand, imported, tenderloin, separable lean only, cooked, fast fried
    17385: [], # Lamb, New Zealand, imported, tenderloin, separable lean only, raw
    17386: [], # Lamb, New Zealand, imported, loin saddle, separable lean only, cooked, fast roasted
    17387: [], # Lamb, New Zealand, imported, loin saddle, separable lean only, raw
    17388: [], # Lamb, New Zealand, imported, loin, boneless, separable lean only, cooked, fast roasted
    17389: [], # Lamb, New Zealand, imported, loin, boneless, separable lean only, raw
    17390: [], # Lamb, New Zealand, imported, hind-shank, separable lean only, cooked, braised
    17391: [], # Lamb, New Zealand, imported, hind-shank, separable lean only, raw
    17392: [], # Lamb, New Zealand, imported, neck chops, separable lean only, raw
    17393: [], # Lamb, New Zealand, imported, neck chops, separable lean only, cooked, braised
    17394: [], # Lamb, New Zealand, imported, netted shoulder, rolled, boneless, separable lean only, cooked, slow roasted
    17395: [], # Lamb, New Zealand, imported, netted shoulder, rolled, boneless, separable lean only, raw
    17396: [], # Lamb, New Zealand, imported, rack - fully frenched, separable lean only, cooked, fast roasted
    17397: [], # Lamb, New Zealand, imported, rack - fully frenched, separable lean only, raw
    17398: [], # Lamb, New Zealand, imported, loin chop, separable lean only, cooked, fast fried
    17399: [], # Lamb, New Zealand, imported, square-cut shoulder, separable lean only, cooked, slow roasted
    17400: [], # Lamb, New Zealand, imported, leg chop/steak, bone-in, separable lean only, cooked, fast fried
    17401: [], # Lamb, New Zealand, imported, flap, boneless, separable lean and fat, cooked, braised
    17402: [], # Lamb, New Zealand, imported, flap, boneless, separable lean and fat, raw
    17403: [], # Lamb, New Zealand, imported, hind-shank, separable lean and fat, cooked, braised
    17404: [], # Lamb, New Zealand, imported, hind-shank, separable lean and fat, raw
    17405: [], # Lamb, New Zealand, imported, leg chop/steak, bone-in, separable lean and fat, cooked, fast fried
    17406: [], # Lamb, New Zealand, imported, loin chop, separable lean and fat, cooked, fast fried
    17407: [], # Lamb, New Zealand, imported, loin saddle, separable lean and fat, cooked, fast roasted
    17408: [], # Lamb, New Zealand, imported, loin saddle, separable lean and fat, raw
    17409: [], # Lamb, New Zealand, imported, loin, boneless, separable lean and fat, cooked, fast roasted
    17410: [], # Lamb, New Zealand, imported, loin, boneless, separable lean and fat, raw
    17411: [], # Lamb, New Zealand, imported, neck chops, separable lean and fat, cooked, braised
    17412: [], # Lamb, New Zealand, imported, neck chops, separable lean and fat, raw
    17413: [], # Lamb, New Zealand, imported, netted shoulder, rolled, boneless, separable lean and fat, cooked, slow roasted
    17414: [], # Lamb, New Zealand, imported, netted shoulder, rolled, boneless, separable lean and fat, raw
    17415: [], # Lamb, New Zealand, imported, square-cut shoulder chops, separable lean and fat, cooked, braised
    17416: [], # Lamb, New Zealand, imported, square-cut shoulder chops, separable lean and fat, raw
    17417: [], # Lamb, New Zealand, imported, square-cut shoulder, separable lean and fat, cooked, slow roasted
    17418: [], # Lamb, New Zealand, imported, tenderloin, separable lean and fat, cooked, fast fried
    17419: [], # Lamb, New Zealand, imported, rack - fully frenched, separable lean and fat, cooked, fast roasted
    17420: [], # Lamb, New Zealand, imported, rack - fully frenched, separable lean and fat, raw
    17421: [], # Lamb, New Zealand, imported, tunnel-boned leg, chump off, shank off, separable lean and fat, cooked, slow roasted
    17422: [], # Lamb, New Zealand, imported, tunnel-boned leg, chump off, shank off, separable lean and fat, raw
    17423: [], # Lamb, New Zealand, imported, tenderloin, separable lean and fat, raw
    17424: [], # Veal, ground, cooked, pan-fried
    17425: [], # Veal, leg, top round, cap off, cutlet, boneless, cooked, grilled
    17426: [], # Veal, leg, top round, cap off, cutlet, boneless, raw
    17427: [], # Veal, loin, chop, separable lean only, cooked, grilled
    17428: [], # Veal, shank, separable lean only, raw
    17429: [], # Veal, foreshank, osso buco, separable lean only, cooked, braised
    17430: [], # Veal, shoulder, blade chop, separable lean only, cooked, grilled
    17431: [], # Veal, external fat only, raw
    17432: [], # Veal, external fat only, cooked
    17433: [], # Veal, seam fat only, raw
    17434: [], # Veal, seam fat only, cooked
    17435: [], # Veal, shank, separable lean and fat, raw
    17436: [], # Veal, foreshank, osso buco, separable lean and fat, cooked, braised
    17437: [], # Veal, loin, chop, separable lean and fat, cooked, grilled
    17438: [], # Veal, shoulder, blade chop, separable lean and fat, cooked, grilled
    17439: [], # Lamb, Australian, imported, fresh, leg, bottom, boneless, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17440: [], # Lamb, Australian, imported, fresh, leg, hindshank, heel on, bone-in, separable lean only, trimmed to 1/8" fat, cooked, braised
    17441: [], # Lamb, Australian, imported, fresh, leg, hindshank, heel on, bone-in, separable lean only, trimmed to 1/8" fat, raw
    17442: [], # Lamb, Australian, imported, fresh, tenderloin, boneless, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17443: [], # Lamb, Australian, imported, fresh, tenderloin, boneless, separable lean only, trimmed to 1/8" fat, raw
    17444: [], # Lamb, Australian, imported, fresh, leg, bottom, boneless, separable lean only, trimmed to 1/8" fat, raw
    17445: [], # Lamb, Australian, imported, fresh, leg, trotter off, bone-in, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17446: [], # Lamb, Australian, imported, fresh, leg, trotter off, bone-in, separable lean only, trimmed to 1/8" fat, raw
    17447: [], # Lamb, Australian, imported, fresh, rack, roast, frenched, denuded, bone-in, separable lean only, trimmed to 0" fat, cooked, roasted
    17448: [], # Lamb, Australian, imported, fresh, rack, roast, frenched, bone-in, separable lean only, trimmed to 1/8" fat, cooked, roasted
    17449: [], # Lamb, Australian, imported, fresh, external fat, cooked
    17450: [], # Lamb, Australian, imported, fresh, external fat, raw
    17451: [], # Lamb, Australian, imported, fresh, seam fat, cooked
    17452: [], # Lamb, Australian, imported, fresh, seam fat, raw
    17453: [], # Lamb, Australian, imported, fresh, leg, bottom, boneless, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17454: [], # Lamb, Australian, imported, fresh, leg, bottom, boneless, separable lean and fat, trimmed to 1/8" fat, raw
    17455: [], # Lamb, Australian, imported, fresh, leg, hindshank, heel on, bone-in, separable lean and fat, trimmed to 1/8" fat, cooked, braised
    17456: [], # Lamb, Australian, imported, fresh, leg, hindshank, heel on, bone-in, separable lean and fat, trimmed to 1/8" fat, raw
    17457: [], # Lamb, Australian, imported, fresh, leg, trotter off, bone-in, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17458: [], # Lamb, Australian, imported, fresh, leg, trotter off, bone-in, separable lean and fat, trimmed to 1/8" fat, raw
    17459: [], # Lamb, Australian, imported, fresh, tenderloin, boneless, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17460: [], # Lamb, Australian, imported, fresh, tenderloin, boneless, separable lean and fat, trimmed to 1/8" fat, raw
    17461: [], # Lamb, Australian, imported, fresh, rib chop, frenched, denuded, bone-in, separable lean only, trimmed to 0" fat, cooked, grilled
    17462: [], # Lamb, Australian, imported, fresh, rack, roast, frenched, denuded, bone-in, separable lean and fat, trimmed to 0" fat, cooked, roasted
    17463: [], # Lamb, Australian, imported, fresh, rack, roast, frenched, bone-in, separable lean and fat, trimmed to 1/8" fat, cooked, roasted
    17464: [], # Lamb, Australian, imported, fresh, rib chop, frenched, denuded, bone-in, separable lean and fat, trimmed to 0" fat, cooked, grilled
    18001: [], # Bagels, plain, enriched, with calcium propionate (includes onion, poppy, sesame)
    18002: [], # Bagels, plain, enriched, with calcium propionate (includes onion, poppy, sesame), toasted
    18003: [], # Bagels, egg
    18005: [], # Bagels, cinnamon-raisin
    18006: [], # Bagels, cinnamon-raisin, toasted
    18007: [], # Bagels, oat bran
    18009: [], # Biscuits, plain or buttermilk, frozen, baked
    18010: [], # Biscuits, plain or buttermilk, dry mix
    18011: [], # Biscuits, plain or buttermilk, dry mix, prepared
    18012: [], # Biscuits, plain or buttermilk, refrigerated dough, lower fat
    18013: [], # Biscuits, plain or buttermilk, refrigerated dough, lower fat, baked
    18014: [], # Biscuits, plain or buttermilk, refrigerated dough, higher fat
    18015: [], # Biscuits, plain or buttermilk, refrigerated dough, higher fat, baked
    18016: [], # Biscuits, plain or buttermilk, prepared from recipe
    18017: [], # Biscuits, mixed grain, refrigerated dough
    18019: ["Banana bread"], # Bread, banana, prepared from recipe, made with margarine
    18021: [], # Bread, boston brown, canned
    18022: [], # Bread, cornbread, dry mix, enriched (includes corn muffin mix)
    18023: [], # Bread, cornbread, dry mix, prepared with 2% milk, 80% margarine, and eggs
    18024: [], # Bread, cornbread, prepared from recipe, made with low fat (2%) milk
    18025: [], # Bread, cracked-wheat
    18027: ["Egg bread"], # Bread, egg
    18028: [], # Bread, egg, toasted
    18029: ["French bread"], # Bread, french or vienna (includes sourdough)
    18030: [], # Bread, french or vienna, toasted (includes sourdough)
    18032: [], # Bread, irish soda, prepared from recipe
    18033: ["Italian bread"], # Bread, Italian
    18036: [], # Bread, multi-grain, toasted (includes whole-grain)
    18037: ["Oat bran bread"], # Bread, oat bran
    18038: [], # Bread, oat bran, toasted
    18039: ["Oatmeal bread"], # Bread, oatmeal
    18040: [], # Bread, oatmeal, toasted
    18041: [], # Bread, pita, white, enriched
    18042: ["Whole-wheat bread"], # Bread, pita, whole-wheat
    18043: [], # Bread, protein (includes gluten)
    18044: [], # Bread, pumpernickel
    18047: [], # Bread, raisin, enriched
    18048: [], # Bread, raisin, enriched, toasted
    18049: [], # Bread, reduced-calorie, oat bran
    18050: [], # Bread, reduced-calorie, oat bran, toasted
    18051: [], # Bread, reduced-calorie, oatmeal
    18053: [], # Bread, reduced-calorie, rye
    18055: [], # Bread, reduced-calorie, wheat
    18057: [], # Bread, reduced-calorie, white
    18059: [], # Bread, rice bran
    18060: ["Rye bread"], # Bread, rye
    18061: [], # Bread, rye, toasted
    18064: ["Wheat bread", "", "Bread"], # Bread, wheat
    18065: [], # Bread, wheat, toasted
    18069: [], # Bread, white, commercially prepared (includes soft bread crumbs)
    18070: [], # Bread, white, commercially prepared, toasted
    18071: [], # Bread, white, prepared from recipe, made with nonfat dry milk
    18073: [], # Bread, white, prepared from recipe, made with low fat (2%) milk
    18075: [], # Bread, whole-wheat, commercially prepared
    18076: [], # Bread, whole-wheat, commercially prepared, toasted
    18077: [], # Bread, whole-wheat, prepared from recipe
    18078: [], # Bread, whole-wheat, prepared from recipe, toasted
    18079: ["Bread crumb"], # Bread, crumbs, dry, grated, plain
    18080: ["Bread stick"], # Bread, sticks, plain
    18081: ["Bread stuffing"], # Bread, stuffing, dry mix
    18082: [], # Bread, stuffing, dry mix, prepared
    18084: [], # Bread, stuffing, cornbread, dry mix
    18085: [], # Bread, stuffing, cornbread, dry mix, prepared
    18086: [], # Cake, angelfood, commercially prepared
    18088: [], # Cake, angelfood, dry mix, prepared
    18090: [], # Cake, boston cream pie, commercially prepared
    18092: [], # Cake, pudding-type, carrot, dry mix
    18095: [], # Cake, cherry fudge with chocolate frosting
    18096: [], # Cake, chocolate, commercially prepared with chocolate frosting, in-store bakery
    18097: [], # Cake, pudding-type, chocolate, dry mix
    18101: [], # Cake, chocolate, prepared from recipe without frosting
    18102: [], # Cake, white, prepared from recipe with coconut frosting
    18103: [], # Cake, coffeecake, cheese
    18104: [], # Cake, coffeecake, cinnamon with crumb topping, commercially prepared, enriched
    18105: [], # Cake, coffeecake, creme-filled with chocolate frosting
    18106: [], # Cake, coffeecake, fruit
    18108: [], # Cake, coffeecake, cinnamon with crumb topping, dry mix, prepared
    18110: [], # Cake, fruitcake, commercially prepared
    18114: [], # Cake, gingerbread, dry mix
    18116: [], # Cake, gingerbread, prepared from recipe
    18119: [], # Cake, pineapple upside-down, prepared from recipe
    18120: [], # Cake, pound, commercially prepared, butter (includes fresh and frozen)
    18121: [], # Cake, pound, commercially prepared, other than all butter, enriched
    18126: [], # Cake, shortcake, biscuit-type, prepared from recipe
    18127: [], # Cake, snack cakes, creme-filled, chocolate with frosting
    18128: [], # Cake, snack cakes, creme-filled, sponge
    18131: [], # Cake, white, dry mix, special dietary (includes lemon-flavored)
    18133: [], # Cake, sponge, commercially prepared
    18134: [], # Cake, sponge, prepared from recipe
    18135: [], # Cake, pudding-type, white, enriched, dry mix
    18139: [], # Cake, white, prepared from recipe without frosting
    18140: [], # Cake, yellow, commercially prepared, with chocolate frosting, in-store bakery
    18141: [], # Cake, yellow, commercially prepared, with vanilla frosting
    18142: [], # Cake, pudding-type, yellow, dry mix
    18144: [], # Cake, yellow, enriched, dry mix
    18146: [], # Cake, yellow, prepared from recipe without frosting
    18147: [], # Cake, cheesecake, commercially prepared
    18148: [], # Cake, cheesecake, prepared from mix, no-bake type
    18151: [], # Cookies, brownies, commercially prepared
    18152: [], # Cookies, brownies, dry mix, regular
    18154: [], # Cookies, brownies, prepared from recipe
    18155: [], # Cookies, butter, commercially prepared, enriched
    18156: [], # Cookies, fudge, cake-type (includes trolley cakes)
    18157: [], # Cookies, chocolate wafers
    18158: [], # Cookies, chocolate chip, commercially prepared, regular, lower fat
    18159: [], # Cookies, chocolate chip, commercially prepared, regular, higher fat, enriched
    18160: [], # Cookies, chocolate chip, commercially prepared, soft-type
    18161: [], # Cookies, chocolate chip, dry mix
    18163: [], # Cookies, chocolate chip, refrigerated dough
    18164: [], # Cookies, chocolate chip, refrigerated dough, baked
    18165: [], # Cookies, chocolate chip, prepared from recipe, made with margarine
    18166: [], # Cookies, chocolate sandwich, with creme filling, regular
    18167: [], # Cookies, chocolate sandwich, with creme filling, regular, chocolate-coated
    18168: [], # Cookies, chocolate sandwich, with extra creme filling
    18170: [], # Cookies, fig bars
    18171: [], # Cookies, fortune
    18172: [], # Cookies, gingersnaps
    18173: [], # Cookies, graham crackers, plain or honey (includes cinnamon)
    18174: [], # Cookies, graham crackers, chocolate-coated
    18175: [], # Cookies, ladyfingers, with lemon juice and rind
    18176: [], # Cookies, marshmallow, chocolate-coated (includes marshmallow pies)
    18177: [], # Cookies, molasses
    18178: [], # Cookies, oatmeal, commercially prepared, regular
    18179: [], # Cookies, oatmeal, commercially prepared, soft-type
    18180: [], # Cookies, oatmeal, dry mix
    18182: [], # Cookies, oatmeal, refrigerated dough
    18183: [], # Cookies, oatmeal, refrigerated dough, baked
    18184: [], # Cookies, oatmeal, with raisins
    18185: [], # Cookies, peanut butter, commercially prepared, regular
    18186: [], # Cookies, peanut butter, commercially prepared, soft-type
    18187: [], # Cookies, peanut butter, refrigerated dough
    18188: [], # Cookies, peanut butter, refrigerated dough, baked
    18189: [], # Cookies, peanut butter, prepared from recipe
    18190: [], # Cookies, peanut butter sandwich, regular
    18191: [], # Cookies, raisin, soft-type
    18192: [], # Cookies, shortbread, commercially prepared, plain
    18193: [], # Cookies, shortbread, commercially prepared, pecan
    18196: [], # Cookies, brownies, dry mix, sugar free
    18198: [], # Cookies, chocolate chip, commercially prepared, special dietary
    18199: [], # Cookies, chocolate sandwich, with creme filling, special dietary
    18200: [], # Cookies, oatmeal, commercially prepared, special dietary
    18201: [], # Cookies, peanut butter sandwich, special dietary
    18202: [], # Cookies, sugar wafer, with creme filling, sugar free
    18204: [], # Cookies, sugar, commercially prepared, regular (includes vanilla)
    18205: [], # Cookies, sugar, refrigerated dough
    18206: [], # Cookies, sugar, refrigerated dough, baked
    18209: [], # Cookies, sugar wafers with creme filling, regular
    18210: [], # Cookies, vanilla sandwich with creme filling
    18211: [], # Puff pastry, frozen, ready-to-bake, baked
    18212: [], # Cookies, vanilla wafers, lower fat
    18213: [], # Cookies, vanilla wafers, higher fat
    18214: [], # Crackers, cheese, regular
    18215: [], # Crackers, cheese, sandwich-type with peanut butter filling
    18216: [], # Crackers, crispbread, rye
    18217: [], # Crackers, matzo, plain
    18218: [], # Crackers, matzo, egg
    18219: [], # Crackers, matzo, whole-wheat
    18220: [], # Crackers, melba toast, plain
    18221: [], # Crackers, melba toast, rye (includes pumpernickel)
    18222: [], # Crackers, melba toast, wheat
    18223: [], # Crackers, milk
    18224: [], # Crackers, rusk toast
    18225: [], # Crackers, rye, sandwich-type with cheese filling
    18226: [], # Crackers, rye, wafers, plain
    18227: [], # Crackers, rye, wafers, seasoned
    18228: [], # Crackers, saltines (includes oyster, soda, soup)
    18229: [], # Crackers, standard snack-type, regular
    18230: [], # Crackers, standard snack-type, sandwich, with cheese filling
    18231: [], # Crackers, standard snack-type, sandwich, with peanut butter filling
    18232: [], # Crackers, wheat, regular
    18233: [], # Crackers, wheat, sandwich, with cheese filling
    18234: [], # Crackers, wheat, sandwich, with peanut butter filling
    18235: [], # Crackers, whole-wheat
    18236: [], # Cracker, meal
    18237: [], # Cream puff shell, prepared from recipe
    18239: [], # Croissants, butter
    18240: [], # Croissants, apple
    18241: [], # Croissants, cheese
    18242: [], # Croutons, plain
    18243: [], # Croutons, seasoned
    18244: [], # Danish pastry, cinnamon, enriched
    18245: [], # Danish pastry, cheese
    18246: [], # Danish pastry, fruit, enriched (includes apple, cinnamon, raisin, lemon, raspberry, strawberry)
    18248: [], # Doughnuts, cake-type, plain (includes unsugared, old-fashioned)
    18249: [], # Doughnuts, cake-type, plain, chocolate-coated or frosted
    18250: [], # Doughnuts, cake-type, plain, sugared or glazed
    18251: [], # Doughnuts, cake-type, chocolate, sugared or glazed
    18253: [], # Doughnuts, french crullers, glazed
    18254: [], # Doughnuts, yeast-leavened, with creme filling
    18255: [], # Doughnuts, yeast-leavened, glazed, enriched (includes honey buns)
    18256: [], # Doughnuts, yeast-leavened, with jelly filling
    18258: [], # Muffins, English, plain, enriched, with ca prop (includes sourdough)
    18259: [], # Muffins, English, plain, toasted, enriched, with calcium propionate (includes sourdough)
    18260: [], # Muffins, English, mixed-grain (includes granola)
    18262: [], # Muffins, English, raisin-cinnamon (includes apple-cinnamon)
    18263: [], # Muffins, English, raisin-cinnamon, toasted (includes apple-cinnamon)
    18264: [], # Muffins, English, wheat
    18266: [], # Muffins, English, whole-wheat
    18268: [], # French toast, frozen, ready-to-heat
    18269: [], # French toast, prepared from recipe, made with low fat (2%) milk
    18270: [], # Hush puppies, prepared from recipe
    18271: [], # Ice cream cones, cake or wafer-type
    18272: [], # Ice cream cones, sugar, rolled-type
    18273: [], # Muffins, plain, prepared from recipe, made with low fat (2%) milk
    18274: [], # Muffins, blueberry, commercially prepared (Includes mini-muffins)
    18275: [], # Muffins, blueberry, dry mix
    18277: [], # Muffins, blueberry, toaster-type
    18278: [], # Muffins, blueberry, prepared from recipe, made with low fat (2%) milk
    18279: [], # Muffins, corn, commercially prepared
    18280: [], # Muffins, corn, dry mix, prepared
    18281: [], # Muffins, corn, toaster-type
    18282: [], # Muffins, corn, prepared from recipe, made with low fat (2%) milk
    18283: [], # Muffins, oat bran
    18284: [], # Muffins, wheat bran, dry mix
    18288: [], # Pancakes plain, frozen, ready-to-heat (includes buttermilk)
    18289: [], # Pancakes, plain, dry mix, complete (includes buttermilk)
    18290: [], # Pancakes, plain, dry mix, complete, prepared
    18291: [], # Pancakes, plain, dry mix, incomplete (includes buttermilk)
    18292: [], # Pancakes, plain, dry mix, incomplete, prepared
    18293: [], # Pancakes, plain, prepared from recipe
    18294: [], # Pancakes, blueberry, prepared from recipe
    18295: [], # Pancakes, buckwheat, dry mix, incomplete
    18297: [], # Pancakes, special dietary, dry mix
    18299: [], # Pancakes, whole-wheat, dry mix, incomplete
    18300: [], # Pancakes, whole-wheat, dry mix, incomplete, prepared
    18301: [], # Pie, apple, commercially prepared, enriched flour
    18302: [], # Pie, apple, prepared from recipe
    18303: [], # Pie, banana cream, prepared from mix, no-bake type
    18304: [], # Pie, banana cream, prepared from recipe
    18305: [], # Pie, blueberry, commercially prepared
    18306: [], # Pie, blueberry, prepared from recipe
    18308: [], # Pie, cherry, commercially prepared
    18309: [], # Pie, cherry, prepared from recipe
    18310: [], # Pie, chocolate creme, commercially prepared
    18312: [], # Pie, chocolate mousse, prepared from mix, no-bake type
    18313: [], # Pie, coconut creme, commercially prepared
    18314: [], # Pie, coconut cream, prepared from mix, no-bake type
    18316: [], # Pie, coconut custard, commercially prepared
    18317: [], # Pie, egg custard, commercially prepared
    18319: [], # Pie, fried pies, fruit
    18320: [], # Pie, lemon meringue, commercially prepared
    18321: [], # Pie, lemon meringue, prepared from recipe
    18322: [], # Pie, mince, prepared from recipe
    18323: [], # Pie, peach
    18324: [], # Pie, pecan, commercially prepared
    18325: [], # Pie, pecan, prepared from recipe
    18326: [], # Pie, pumpkin, commercially prepared
    18327: [], # Pie, pumpkin, prepared from recipe
    18328: [], # Pie, vanilla cream, prepared from recipe
    18332: [], # Pie crust, standard-type, dry mix
    18333: [], # Pie crust, standard-type, dry mix, prepared, baked
    18334: [], # Pie crust, standard-type, frozen, ready-to-bake, enriched
    18335: [], # Pie crust, standard-type, frozen, ready-to-bake, enriched, baked
    18336: [], # Pie crust, standard-type, prepared from recipe, baked
    18337: [], # Puff pastry, frozen, ready-to-bake
    18338: [], # Phyllo dough
    18339: [], # Popovers, dry mix, enriched
    18342: [], # Rolls, dinner, plain, commercially prepared (includes brown-and-serve)
    18344: [], # Rolls, dinner, egg
    18345: [], # Rolls, dinner, oat bran
    18346: [], # Rolls, dinner, rye
    18347: [], # Rolls, dinner, wheat
    18348: [], # Rolls, dinner, whole-wheat
    18349: [], # Rolls, french
    18350: [], # Rolls, hamburger or hotdog, plain
    18351: [], # Rolls, hamburger or hotdog, mixed-grain
    18353: [], # Rolls, hard (includes kaiser)
    18354: [], # Strudel, apple
    18355: [], # Sweet rolls, cheese
    18356: [], # Sweet rolls, cinnamon, commercially prepared with raisins
    18357: [], # Sweet rolls, cinnamon, refrigerated dough with frosting
    18358: [], # Sweet rolls, cinnamon, refrigerated dough with frosting, baked
    18360: [], # Taco shells, baked
    18361: [], # Toaster pastries, brown-sugar-cinnamon
    18362: [], # Toaster pastries, fruit (includes apple, blueberry, cherry, strawberry)
    18363: [], # Tortillas, ready-to-bake or -fry, corn
    18364: [], # Tortillas, ready-to-bake or -fry, flour, refrigerated
    18365: [], # Waffles, plain, frozen, ready-to-heat
    18367: [], # Waffles, plain, prepared from recipe
    18368: [], # Wonton wrappers (includes egg roll wrappers)
    18369: [], # Leavening agents, baking powder, double-acting, sodium aluminum sulfate
    18370: [], # Leavening agents, baking powder, double-acting, straight phosphate
    18371: [], # Leavening agents, baking powder, low-sodium
    18372: [], # Leavening agents, baking soda
    18373: [], # Leavening agents, cream of tartar
    18374: [], # Leavening agents, yeast, baker's, compressed
    18375: [], # Leavening agents, yeast, baker's, active dry
    18376: [], # Bread, crumbs, dry, grated, seasoned
    18377: [], # Cookies, oatmeal, prepared from recipe, without raisins
    18378: [], # Cookies, chocolate chip, prepared from recipe, made with butter
    18383: [], # Bread, protein, (includes gluten), toasted
    18384: [], # Bread, rice bran, toasted
    18386: [], # Muffins, blueberry, toaster-type, toasted
    18388: [], # Muffins, wheat bran, toaster-type with raisins, toasted
    18390: [], # Pancakes, buttermilk, prepared from recipe
    18396: [], # Rolls, dinner, plain, prepared from recipe, made with low fat (2%) milk
    18399: [], # Pie crust, cookie-type, prepared from recipe, graham cracker, chilled
    18400: [], # Crackers, matzo, egg and onion
    18401: [], # Pie crust, cookie-type, prepared from recipe, vanilla wafer, chilled
    18402: [], # Pie crust, standard-type, prepared from recipe, unbaked
    18403: [], # Waffles, plain, frozen, ready -to-heat, toasted
    18406: [], # Bagels, plain, enriched, without calcium propionate (includes onion, poppy, sesame)
    18407: [], # Bagels, plain, unenriched, with calcium propionate (includes onion, poppy, sesame)
    18408: [], # Bagels, plain, unenriched, without calcium propionate(includes onion, poppy, sesame)
    18412: [], # Bread, cornbread, dry mix, unenriched (includes corn muffin mix)
    18413: ["Pita bread"], # Bread, pita, white, unenriched
    18414: ["Raisin bread"], # Bread, raisin, unenriched
    18416: [], # Bread, white, commercially prepared, low sodium, no salt
    18417: [], # Cake, coffeecake, cinnamon with crumb topping, commercially prepared, unenriched
    18418: [], # Cake, pound, commercially prepared, other than all butter, unenriched
    18419: [], # Cake, pudding-type, white, unenriched, dry mix
    18420: [], # Cake, yellow, unenriched, dry mix
    18421: [], # Cookies, butter, commercially prepared, unenriched
    18422: [], # Cookies, chocolate chip, commercially prepared, regular, higher fat, unenriched
    18423: [], # Cookies, ladyfingers, without lemon juice and rind
    18424: [], # Crackers, melba toast, plain, without salt
    18425: [], # Crackers, saltines, low salt (includes oyster, soda, soup)
    18426: [], # Crackers, saltines, unsalted tops (includes oyster, soda, soup)
    18427: [], # Crackers, standard snack-type, regular, low salt
    18428: [], # Crackers, wheat, low salt
    18429: [], # Crackers, whole-wheat, low salt
    18430: [], # Danish pastry, cinnamon, unenriched
    18431: [], # Danish pastry, fruit, unenriched (includes apple, cinnamon, raisin, strawberry)
    18432: [], # Bread, white, commercially prepared, toasted, low sodium no salt
    18433: [], # Danish pastry, lemon, unenriched
    18434: [], # Crackers, cheese, low sodium
    18435: [], # Danish pastry, raspberry, unenriched
    18436: [], # Doughnuts, yeast-leavened, glazed, unenriched (includes honey buns)
    18437: [], # English muffins, plain, enriched, without calcium propionate(includes sourdough)
    18438: [], # English muffins, plain, unenriched, with calcium propionate (includes sourdough)
    18439: [], # English muffins, plain, unenriched, without calcium propionate (includes sourdough)
    18443: [], # Pie, apple, commercially prepared, unenriched flour
    18444: [], # Pie, fried pies, cherry
    18445: [], # Pie, fried pies, lemon
    18446: [], # Pie crust, standard-type, frozen, ready-to-bake, unenriched
    18447: [], # Popovers, dry mix, unenriched
    18448: [], # Taco shells, baked, without added salt
    18449: [], # Tortillas, ready-to-bake or -fry, corn, without added salt
    18450: [], # Tortillas, ready-to-bake or -fry, flour, without added calcium
    18451: [], # Cake, pound, commercially prepared, fat-free
    18453: [], # Cake, yellow, light, dry mix
    18457: [], # Crackers, saltines, fat-free, low-sodium
    18459: [], # Tart, breakfast, low fat
    18513: [], # Archway Home Style Cookies, Sugar Free Oatmeal
    18522: [], # Archway Home Style Cookies, Chocolate Chip Ice Box
    18524: [], # Archway Home Style Cookies, Coconut Macaroon
    18527: [], # Archway Home Style Cookies, Date Filled Oatmeal
    18528: [], # Archway Home Style Cookies, Dutch Cocoa
    18529: [], # Archway Home Style Cookies, Frosty Lemon
    18532: [], # Archway Home Style Cookies, Iced Molasses
    18533: [], # Archway Home Style Cookies, Iced Oatmeal
    18535: [], # Archway Home Style Cookies, Molasses
    18537: [], # Archway Home Style Cookies, Oatmeal
    18538: [], # Archway Home Style Cookies, Oatmeal Raisin
    18539: [], # Archway Home Style Cookies, Old Fashioned Molasses
    18540: [], # Archway Home Style Cookies, Old Fashioned Windmill Cookies
    18541: [], # Archway Home Style Cookies, Peanut Butter
    18544: [], # Archway Home Style Cookies, Raspberry Filled
    18547: [], # Archway Home Style Cookies, Strawberry Filled
    18562: [], # Archway Home Style Cookies, Reduced Fat Ginger Snaps
    18566: [], # Artificial Blueberry Muffin Mix, dry
    18567: [], # Kraft, Stove Top Stuffing Mix Chicken Flavor
    18603: [], # George Weston Bakeries, Brownberry Sage and Onion Stuffing Mix, dry
    18608: [], # Keebler, Keebler Chocolate Graham SELECTS
    18610: [], # Continental Mills, Krusteaz Almond Poppyseed Muffin Mix, Artificially Flavored, dry
    18612: [], # Mckee Baking, Little Debbie Nutty Bars, Wafers with Peanut Butter, Chocolate Covered
    18614: [], # Martha White Foods, Martha White's Chewy Fudge Brownie Mix, dry
    18615: [], # Martha White Foods, Martha White's Buttermilk Biscuit Mix, dry
    18616: [], # Mission Foods, Mission Flour Tortillas, Soft Taco, 8 inch
    18617: [], # Nabisco, Nabisco Grahams Crackers
    18619: [], # Nabisco, Nabisco Oreo Crunchies, Cookie Crumb Topping
    18621: [], # Nabisco, Nabisco Ritz Crackers
    18629: [], # Pillsbury, Buttermilk Biscuits, Artificial Flavor, refrigerated dough
    18630: [], # Pillsbury, Chocolate Chip Cookies, refrigerated dough
    18631: [], # Pillsbury, Crusty French Loaf, refrigerated dough
    18633: [], # Pillsbury Grands, Buttermilk Biscuits, refrigerated dough
    18634: [], # Pillsbury Golden Layer Buttermilk Biscuits, Artificial Flavor, refrigerated dough
    18635: [], # Pillsbury, Cinnamon Rolls with Icing, refrigerated dough
    18637: [], # Kraft Foods, Shake N Bake Original Recipe, Coating for Pork, dry
    18639: [], # George Weston Bakeries, Thomas English Muffins
    18640: [], # Heinz, Weight Watcher, Chocolate Eclair, frozen
    18641: [], # Interstate Brands Corp, Wonder Hamburger Rolls
    18651: [], # Nabisco, Nabisco Snackwell's Fat Free Devil's Food Cookie Cakes
    18927: [], # Crackers, cheese, sandwich-type with cheese filling
    18932: [], # Waffles, buttermilk, frozen, ready-to-heat
    18933: [], # Waffle, buttermilk, frozen, ready-to-heat, toasted
    18934: [], # Waffle, buttermilk, frozen, ready-to-heat, microwaved
    18935: [], # Waffle, plain, frozen, ready-to-heat, microwave
    18936: [], # Pancakes, plain, frozen, ready-to-heat, microwave (includes buttermilk)
    18938: [], # Toaster Pastries, fruit, frosted (include apples, blueberry, cherry, strawberry)
    18939: [], # Toaster pastries, fruit, toasted (include apple, blueberry, cherry, strawberry)
    18940: [], # Muffin, blueberry, commercially prepared, low-fat
    18942: [], # Pie Crust, Cookie-type, Graham Cracker, Ready Crust
    18943: [], # Pie Crust, Cookie-type, Chocolate, Ready Crust
    18944: [], # Pie, Dutch Apple, Commercially Prepared
    18945: [], # Pie crust, deep dish, frozen, unbaked, made with enriched flour
    18946: [], # Pie crust, refrigerated, regular, baked
    18947: [], # Pie crust, deep dish, frozen, baked, made with enriched flour
    18948: [], # Pie crust, refrigerated, regular, unbaked
    18949: [], # Crackers, whole-wheat, reduced fat
    18950: [], # Crackers, wheat, reduced fat
    18951: [], # Waffles, chocolate chip, frozen, ready-to-heat
    18952: [], # Tostada shells, corn
    18953: [], # Bread, salvadoran sweet cheese (quesadilla salvadorena)
    18954: [], # Bread, pound cake type, pan de torta salvadoran
    18955: [], # Bread, pan dulce, sweet yeast bread
    18956: [], # Keikitos (muffins), Latino bakery item
    18957: [], # Cake, pound, Bimbo Bakeries USA, Panque Casero, home baked style
    18958: [], # Pan Dulce, La Ricura, Salpora de Arroz con Azucar, cookie-like, contains wheat flour and rice flour
    18959: [], # Pastry, Pastelitos de Guava (guava pastries)
    18960: [], # Crackers, snack, Goya Crackers
    18961: [], # Crackers, cream, Gamesa Sabrosas
    18962: [], # Crackers, cream, La Moderna Rikis Cream Crackers
    18963: [], # Garlic bread, frozen
    18964: [], # Cinnamon buns, frosted (includes honey buns)
    18965: [], # Crackers, cheese, reduced fat
    18966: [], # Crackers, saltines, whole wheat (includes multi-grain)
    18967: [], # Bread, white wheat
    18968: [], # Bagels, wheat
    18969: [], # Cream puff, eclair, custard or cream filled, iced
    18970: [], # Tortillas, ready-to-bake or -fry, flour, shelf stable
    18971: [], # Bread, potato
    18972: [], # Bread, cheese
    18973: [], # Focaccia, Italian flatbread, plain
    19000: [], # SCHIFF,TIGER'S MILK BAR
    19001: [], # Candies, TOBLERONE, milk chocolate with honey and almond nougat
    19002: [], # Snacks, beef jerky, chopped and formed
    19003: [], # Snacks, corn-based, extruded, chips, plain
    19004: [], # Snacks, corn-based, extruded, chips, barbecue-flavor
    19005: [], # Snacks, corn-based, extruded, cones, plain
    19007: [], # Snacks, corn-based, extruded, onion-flavor
    19008: [], # Snacks, corn-based, extruded, puffs or twists, cheese-flavor
    19009: [], # Snacks, KRAFT, CORNNUTS, plain
    19010: [], # Snacks, crisped rice bar, chocolate chip
    19013: [], # Snacks, fruit leather, pieces
    19014: [], # Snacks, fruit leather, rolls
    19015: [], # Snacks, granola bars, hard, plain
    19016: [], # Snacks, granola bars, hard, almond
    19017: [], # Snacks, granola bars, hard, chocolate chip
    19018: [], # Fruit syrup
    19020: [], # Snacks, granola bars, soft, uncoated, plain
    19021: [], # Snacks, granola bars, soft, uncoated, peanut butter
    19022: [], # Snacks, granola bars, soft, uncoated, raisin
    19024: [], # Snacks, granola bars, soft, coated, milk chocolate coating, chocolate chip
    19025: [], # Candies, honey-combed, with peanut butter
    19026: [], # Snacks, granola bars, soft, coated, milk chocolate coating, peanut butter
    19027: [], # Snacks, granola bars, soft, uncoated, peanut butter and chocolate chip
    19029: [], # Topping, SMUCKER'S MAGIC SHELL
    19030: [], # Syrup, fruit flavored
    19031: [], # Snacks, oriental mix, rice-based
    19034: [], # Snacks, popcorn, air-popped
    19035: [], # Snacks, popcorn, oil-popped, microwave, regular flavor, no trans fat
    19036: [], # Snacks, popcorn, cakes
    19038: [], # Snacks, popcorn, caramel-coated, with peanuts
    19039: [], # Snacks, popcorn, caramel-coated, without peanuts
    19040: [], # Snacks, popcorn, cheese-flavor
    19041: [], # Snacks, pork skins, plain
    19042: [], # Snacks, potato chips, barbecue-flavor
    19043: [], # Snacks, potato chips, sour-cream-and-onion-flavor
    19045: [], # Snacks, potato chips, made from dried potatoes, reduced fat
    19046: [], # Snacks, potato chips, made from dried potatoes, sour-cream and onion-flavor
    19047: [], # Snacks, pretzels, hard, plain, salted
    19048: [], # Snacks, pretzels, hard, confectioner's coating, chocolate-flavor
    19049: [], # Snacks, M&M MARS, COMBOS Snacks Cheddar Cheese Pretzel
    19050: [], # Snacks, pretzels, hard, whole-wheat including both salted and unsalted
    19051: [], # Snacks, rice cracker brown rice, plain
    19052: [], # Snacks, rice cakes, brown rice, buckwheat
    19053: [], # Snacks, rice cakes, brown rice, sesame seed
    19056: [], # Snacks, tortilla chips, plain, white corn, salted
    19057: [], # Snacks, tortilla chips, nacho cheese
    19058: [], # Snacks, tortilla chips, ranch-flavor
    19059: [], # Snacks, trail mix, regular
    19061: [], # Snacks, trail mix, tropical
    19062: [], # Snacks, trail mix, regular, with chocolate chips, salted nuts and seeds
    19063: [], # Snacks, tortilla chips, taco-flavor
    19064: [], # Candies, TOOTSIE ROLL, chocolate-flavor roll
    19065: [], # Candies, ALMOND JOY Candy Bar
    19067: [], # Candies, TWIZZLERS CHERRY BITES
    19068: [], # Candies, NESTLE, BIT-O'-HONEY Candy Chews
    19069: [], # Candies, NESTLE, BUTTERFINGER Bar
    19070: [], # Candies, butterscotch
    19071: [], # Candies, carob, unsweetened
    19074: [], # Candies, caramels
    19075: [], # Candies, CARAMELLO Candy Bar
    19076: [], # Candies, caramels, chocolate-flavor roll
    19077: [], # Baking chocolate, unsweetened, liquid
    19078: [], # Baking chocolate, unsweetened, squares
    19079: [], # Candies, confectioner's coating, yogurt
    19080: [], # Candies, semisweet chocolate
    19081: [], # Candies, sweet chocolate
    19083: [], # Candies, sweet chocolate coated fondant
    19084: [], # Candies, HERSHEY'S GOLDEN ALMOND SOLITAIRES
    19085: [], # Candies, confectioner's coating, butterscotch
    19086: [], # Candies, confectioner's coating, peanut butter
    19087: [], # Candies, white chocolate
    19088: [], # Ice creams, vanilla, light
    19089: [], # Ice creams, vanilla, rich
    19090: [], # Ice creams, french vanilla, soft-serve
    19091: [], # Candies, YORK Peppermint Pattie
    19092: [], # Candies, TWIZZLERS NIBS CHERRY BITS
    19093: [], # Candies, SYMPHONY Milk Chocolate Bar
    19094: [], # Desserts, flan, caramel custard, prepared-from-recipe
    19095: ['Vanilla ice cream'], # Ice creams, vanilla
    19096: [], # Ice creams, vanilla, light, soft-serve
    19097: [], # Sherbet, orange
    19098: [], # Candies, 5TH AVENUE Candy Bar
    19099: [], # Candies, fondant, prepared-from-recipe
    19100: [], # Candies, fudge, chocolate, prepared-from-recipe
    19101: [], # Candies, fudge, chocolate, with nuts, prepared-from-recipe
    19102: [], # Candies, fudge, peanut butter, prepared-from-recipe
    19103: [], # Candies, fudge, vanilla, prepared-from-recipe
    19104: [], # Candies, fudge, vanilla with nuts
    19105: [], # Candies, NESTLE, GOOBERS Chocolate Covered Peanuts
    19106: [], # Candies, gumdrops, starch jelly pieces
    19107: [], # Candies, hard
    19108: [], # Candies, jellybeans
    19109: [], # Candies, KIT KAT Wafer Bar
    19110: [], # Candies, KRACKEL Chocolate Bar
    19111: [], # Candies, NESTLE, BABY RUTH Bar
    19112: [], # Candies, TWIZZLERS Strawberry Twists Candy
    19113: [], # Syrups, table blends, pancake, with butter
    19114: [], # Ice creams, chocolate, light
    19115: [], # Candies, MARS SNACKFOOD US, MARS Almond Bar
    19116: [], # Candies, marshmallows
    19117: [], # Candies, halavah, plain
    19118: [], # Candies, NESTLE, OH HENRY! Bar
    19119: [], # Candies, NESTLE, CHUNKY Bar
    19120: [], # Candies, milk chocolate
    19121: [], # Puddings, banana, dry mix, instant, prepared with 2% milk
    19122: [], # Puddings, banana, dry mix, regular, prepared with 2% milk
    19123: [], # Puddings, chocolate, dry mix, instant, prepared with 2% milk
    19124: [], # Baking chocolate, mexican, squares
    19125: [], # Chocolate-flavored hazelnut spread
    19126: [], # Candies, milk chocolate coated peanuts
    19127: [], # Candies, milk chocolate coated raisins
    19128: [], # Syrups, table blends, pancake, reduced-calorie
    19129: [], # Syrups, table blends, pancake
    19130: [], # Candies, HERSHEY'S POT OF GOLD Almond Bar
    19132: [], # Candies, milk chocolate, with almonds
    19134: [], # Candies, milk chocolate, with rice cereal
    19135: [], # Candies, MARS SNACKFOOD US, MILKY WAY Bar
    19136: [], # Candies, HERSHEY'S SKOR Toffee Bar
    19137: [], # Toppings, strawberry
    19138: [], # Candies, truffles, prepared-from-recipe
    19139: [], # Baking chocolate, MARS SNACKFOOD US, M&M's Semisweet Chocolate Mini Baking Bits
    19140: [], # Candies, MARS SNACKFOOD US, M&M's Peanut Chocolate Candies
    19141: [], # Candies, MARS SNACKFOOD US, M&M's Milk Chocolate Candies
    19142: [], # Candies, MOUNDS Candy Bar
    19143: [], # Candies, MR. GOODBAR Chocolate Bar
    19144: [], # Candies, NESTLE, 100 GRAND Bar
    19145: [], # Candies, NESTLE, CRUNCH Bar and Dessert Topping
    19146: [], # Baking chocolate, MARS SNACKFOOD US, M&M's Milk Chocolate Mini Baking Bits
    19147: [], # Candies, peanut bar
    19148: [], # Candies, peanut brittle, prepared-from-recipe
    19149: [], # Candies, NESTLE, RAISINETS Chocolate Covered Raisins
    19150: [], # Candies, REESE'S Peanut Butter Cups
    19151: [], # Candies, REESE'S PIECES Candy
    19152: [], # Candies, ROLO Caramels in Milk Chocolate
    19153: [], # Candies, NESTLE, AFTER EIGHT Mints
    19154: [], # Candies, sesame crunch
    19155: [], # Candies, MARS SNACKFOOD US, SNICKERS Bar
    19156: [], # Candies, MARS SNACKFOOD US, STARBURST Fruit Chews, Original fruits
    19157: [], # Candies, MARS SNACKFOOD US, M&M's MINIs Milk Chocolate Candies
    19159: [], # Candies, MARS SNACKFOOD US, 3 MUSKETEERS Bar
    19160: [], # Candies, MARS SNACKFOOD US, TWIX Caramel Cookie Bars
    19161: [], # Candies, MARS SNACKFOOD US, TWIX Peanut Butter Cookie Bars
    19162: [], # Candies, WHATCHAMACALLIT Candy Bar
    19163: [], # Chewing gum
    19164: [], # Candies, SPECIAL DARK Chocolate Bar
    19165: [], # Cocoa, dry powder, unsweetened
    19166: [], # Cocoa, dry powder, unsweetened, processed with alkali
    19168: [], # Desserts, egg custard, baked, prepared-from-recipe
    19169: [], # Egg custards, dry mix
    19170: [], # Egg custards, dry mix, prepared with whole milk
    19171: [], # Cocoa, dry powder, unsweetened, HERSHEY'S European Style Cocoa
    19172: [], # Gelatin desserts, dry mix
    19173: [], # Gelatin desserts, dry mix, prepared with water
    19175: [], # Gelatin desserts, dry mix, reduced calorie, with aspartame
    19176: [], # Gelatin desserts, dry mix, reduced calorie, with aspartame, prepared with water
    19177: [], # Gelatins, dry powder, unsweetened
    19181: [], # Candies, YORK BITES
    19182: [], # Desserts, mousse, chocolate, prepared-from-recipe
    19183: [], # Puddings, chocolate, ready-to-eat
    19184: [], # Puddings, chocolate, dry mix, instant
    19185: [], # Puddings, chocolate, dry mix, instant, prepared with whole milk
    19186: [], # Desserts, apple crisp, prepared-from-recipe
    19187: [], # Flan, caramel custard, dry mix
    19188: [], # Puddings, chocolate, dry mix, regular
    19189: [], # Puddings, chocolate, dry mix, regular, prepared with whole milk
    19190: [], # Puddings, chocolate, dry mix, regular, prepared with 2% milk
    19191: [], # Puddings, coconut cream, dry mix, instant, prepared with 2% milk
    19193: [], # Puddings, rice, ready-to-eat
    19194: [], # Puddings, rice, dry mix
    19195: [], # Puddings, rice, dry mix, prepared with whole milk
    19198: [], # Puddings, tapioca, dry mix
    19199: [], # Puddings, tapioca, dry mix, prepared with whole milk
    19201: [], # Puddings, vanilla, ready-to-eat
    19202: [], # Puddings, vanilla, dry mix, instant
    19203: [], # Puddings, vanilla, dry mix, instant, prepared with whole milk
    19204: [], # Puddings, lemon, dry mix, instant, prepared with 2% milk
    19205: [], # Egg custards, dry mix, prepared with 2% milk
    19206: [], # Puddings, vanilla, dry mix, regular
    19207: [], # Puddings, vanilla, dry mix, regular, prepared with whole milk
    19208: [], # Puddings, rice, dry mix, prepared with 2% milk
    19209: [], # Puddings, tapioca, dry mix, prepared with 2% milk
    19212: [], # Puddings, vanilla, dry mix, regular, prepared with 2% milk
    19213: [], # Rennin, chocolate, dry mix, prepared with 2% milk
    19214: [], # Rennin, vanilla, dry mix, prepared with 2% milk
    19216: [], # Candies, praline, prepared-from-recipe
    19217: [], # Frozen novelties, ice type, fruit, no sugar added
    19218: [], # Puddings, tapioca, ready-to-eat
    19219: [], # Puddings, coconut cream, dry mix, regular, prepared with 2% milk
    19220: [], # Desserts, rennin, chocolate, dry mix
    19221: [], # Rennin, chocolate, dry mix, prepared with whole milk
    19222: [], # Desserts, rennin, vanilla, dry mix
    19223: [], # Rennin, vanilla, dry mix, prepared with whole milk
    19225: [], # Desserts, rennin, tablets, unsweetened
    19226: [], # Frostings, chocolate, creamy, ready-to-eat
    19227: [], # Frostings, coconut-nut, ready-to-eat
    19228: [], # Frostings, cream cheese-flavor, ready-to-eat
    19230: [], # Frostings, vanilla, creamy, ready-to-eat
    19231: [], # Flan, caramel custard, dry mix, prepared with 2% milk
    19232: [], # Flan, caramel custard, dry mix, prepared with whole milk
    19233: [], # Puddings, vanilla, ready-to-eat, fat free
    19234: [], # Puddings, tapioca, ready-to-eat, fat free
    19235: [], # Puddings, chocolate, ready-to-eat, fat free
    19236: [], # Candies, HERSHEY'S MILK CHOCOLATE WITH ALMOND BITES
    19238: [], # Candies, REESE'S BITES
    19239: [], # Candies, REESE'S NUTRAGEOUS Candy Bar
    19240: [], # Frostings, chocolate, creamy, dry mix
    19241: [], # Frostings, chocolate, creamy, dry mix, prepared with butter
    19243: [], # Candies, HEATH BITES
    19244: [], # Frostings, vanilla, creamy, dry mix
    19246: [], # Frostings, white, fluffy, dry mix
    19247: [], # Frostings, white, fluffy, dry mix, prepared with water
    19248: [], # Candies, HERSHEY'S, ALMOND JOY BITES
    19249: [], # Candies, HERSHEY, REESESTICKS crispy wafers, peanut butter, milk chocolate
    19250: [], # Candies, HERSHEY, KIT KAT BIG KAT Bar
    19252: [], # Candies, REESE'S, FAST BREAK, milk chocolate peanut butter and soft nougats
    19254: [], # Candies, MARS SNACKFOOD US, DOVE Milk Chocolate
    19255: [], # Candies, MARS SNACKFOOD US, DOVE Dark Chocolate
    19256: [], # Candies, MARS SNACKFOOD US, MILKY WAY Caramels, milk chocolate covered
    19258: [], # Candies, MARS SNACKFOOD US, MILKY WAY Caramels. dark chocolate covered
    19260: [], # Ice creams, vanilla, light, no sugar added
    19263: [], # Frozen novelties, fruit and juice bars
    19265: [], # Ice creams, chocolate, light, no sugar added
    19268: [], # Candies, dark chocolate coated coffee beans
    19269: [], # Snacks, GENERAL MILLS, BETTY CROCKER Fruit Roll Ups, berry flavored, with vitamin C
    19270: ['Chocolate ice cream'], # Ice creams, chocolate
    19271: [], # Ice creams, strawberry
    19272: [], # Snacks, FARLEY CANDY, FARLEY Fruit Snacks, with vitamins A, C, and E
    19273: [], # Snacks, SUNKIST, SUNKIST Fruit Roll, strawberry, with vitamins A, C, and E
    19274: [], # Snacks, fruit leather, pieces, with vitamin C
    19279: [], # Candies, milk chocolate coated coffee beans
    19280: [], # Frozen novelties, ice type, lime
    19281: [], # Frozen novelties, ice type, italian, restaurant-prepared
    19283: [], # Frozen novelties, ice type, pop
    19292: [], # Candies, MARS SNACKFOOD US, M&M's Crispy Chocolate Candies
    19293: [], # Frozen yogurts, vanilla, soft-serve
    19294: [], # Fruit butters, apple
    19295: [], # Candies, MARS SNACKFOOD US, SNICKERS MUNCH bar
    19296: ["Honey", "", "Honey"], # Honey
    19297: [], # Jams and preserves
    19300: [], # Jellies
    19301: [], # Candies, fudge, chocolate marshmallow, with nuts, prepared-by-recipe
    19302: [], # Candies, MARS SNACKFOOD US, SNICKERS Almond bar
    19303: [], # Marmalade, orange
    19304: [], # Molasses
    19306: [], # Candies, MARS SNACKFOOD US, POP'ABLES SNICKERS Brand Bite Size Candies
    19307: [], # Candies, MARS SNACKFOOD US, POP'ABLES MILKY WAY Brand Bite Size Candies
    19308: [], # Candies, MARS SNACKFOOD US, POP'ABLES 3 MUSKETEERS Brand Bite Size Candies
    19309: [], # Candies, MARS SNACKFOOD US, STARBURST Fruit Chews, Fruit and Creme
    19310: [], # Pectin, unsweetened, dry mix
    19312: [], # Pie fillings, apple, canned
    19313: [], # Candies, MARS SNACKFOOD US, STARBURST Fruit Chews, Tropical fruits
    19314: [], # Pie fillings, canned, cherry
    19315: [], # Candies, MARS SNACKFOOD US, STARBURST Sour Fruit Chews
    19318: [], # Puddings, banana, dry mix, instant
    19319: [], # Puddings, banana, dry mix, instant, prepared with whole milk
    19320: [], # Puddings, banana, dry mix, regular
    19321: [], # Puddings, banana, dry mix, regular, prepared with whole milk
    19322: [], # Puddings, coconut cream, dry mix, instant
    19323: [], # Puddings, coconut cream, dry mix, instant, prepared with whole milk
    19324: [], # Puddings, coconut cream, dry mix, regular
    19325: [], # Puddings, coconut cream, dry mix, regular, prepared with whole milk
    19326: [], # Candies, MARS SNACKFOOD US, COCOAVIA Chocolate Bar
    19327: [], # Candies, MARS SNACKFOOD US, COCOAVIA Blueberry and Almond Chocolate Bar
    19328: [], # Candies, MARS SNACKFOOD US, COCOAVIA Crispy Chocolate Bar
    19330: [], # Puddings, lemon, dry mix, instant
    19331: [], # Puddings, lemon, dry mix, instant, prepared with whole milk
    19332: [], # Puddings, lemon, dry mix, regular
    19333: [], # Pudding, lemon, dry mix, regular, prepared with sugar, egg yolk and water
    19334: ["Brown sugar"], # Sugars, brown
    19335: ["Sugar"], # Sugars, granulated
    19336: ["Powdered sugar"], # Sugars, powdered
    19337: ["Aspartame sweetener"], # Sweeteners, tabletop, aspartame, EQUAL, packets
    19340: ["Maple sugar"], # Sugars, maple
    19345: [], # Syrups, chocolate, HERSHEY'S Genuine Chocolate Flavored Lite Syrup
    19348: [], # Syrups, chocolate, fudge-type
    19349: ["Corn syrup", "dark"], # Syrups, corn, dark
    19350: ["Corn syrup", "light"], # Syrups, corn, light
    19351: [], # Syrups, corn, high-fructose
    19352: ["Malt syrup"], # Syrups, malt
    19353: ["Maple syrup"], # Syrups, maple
    19355: [], # Syrups, sorghum
    19359: [], # Candies, MARS SNACKFOOD US, SNICKERS CRUNCHER
    19360: [], # Syrups, table blends, pancake, with 2% maple
    19362: [], # Syrups, table blends, corn, refiner, and sugar
    19363: [], # Candies, MARS SNACKFOOD US, SKITTLES Wild Berry Bite Size Candies
    19364: [], # Toppings, butterscotch or caramel
    19365: [], # Toppings, marshmallow cream
    19366: [], # Toppings, pineapple
    19367: [], # Toppings, nuts in syrup
    19368: [], # Candies, MARS SNACKFOOD US, SKITTLES Tropical Bite Size Candies
    19369: [], # Candies, MARS SNACKFOOD US, SKITTLES Sours Original
    19370: [], # Candies, MARS SNACKFOOD US, SKITTLES Original Bite Size Candies
    19371: [], # Frostings, vanilla, creamy, dry mix, prepared with margarine
    19372: [], # Frostings, chocolate, creamy, dry mix, prepared with margarine
    19375: [], # Frostings, glaze, prepared-from-recipe
    19379: [], # Candies, fudge, chocolate marshmallow, prepared-from-recipe
    19382: [], # Candies, taffy, prepared-from-recipe
    19383: [], # Candies, toffee, prepared-from-recipe
    19384: [], # Candies, divinity, prepared-from-recipe
    19387: [], # Frozen novelties, ice type, pineapple-coconut
    19393: [], # Frozen yogurts, chocolate, soft-serve
    19400: [], # Snacks, banana chips
    19401: [], # Snacks, cornnuts, barbecue-flavor
    19403: [], # Snacks, crisped rice bar, almond
    19404: [], # Snacks, granola bars, soft, uncoated, chocolate chip
    19405: [], # Snacks, granola bars, soft, uncoated, chocolate chip, graham and marshmallow
    19406: [], # Snacks, granola bars, soft, uncoated, nut and raisin
    19407: [], # Snacks, beef sticks, smoked
    19408: [], # Snacks, pork skins, barbecue-flavor
    19409: [], # Frostings, glaze, chocolate, prepared-from-recipe, with butter, NFSMI Recipe No. C-32
    19410: [], # Snack, potato chips, made from dried potatoes, plain
    19411: [], # Snacks, potato chips, plain, salted
    19412: [], # Snacks, potato chips, made from dried potatoes, cheese-flavor
    19413: [], # Snacks, rice cakes, brown rice, corn
    19414: [], # Snacks, rice cakes, brown rice, multigrain
    19415: [], # Snacks, potato sticks
    19416: [], # Snacks, rice cakes, brown rice, rye
    19418: [], # Snacks, sesame sticks, wheat-based, salted
    19419: [], # Snacks, corn cakes
    19420: [], # Snacks, granola bars, hard, peanut butter
    19421: [], # Snacks, potato chips, cheese-flavor
    19422: [], # Snacks, potato chips, reduced fat
    19423: [], # Snacks, potato chips, fat-free, made with olestra
    19424: [], # Snacks, tortilla chips, nacho-flavor, reduced fat
    19433: [], # Tortilla chips, low fat, baked without fat
    19434: [], # Cheese puffs and twists, corn based, baked, low fat
    19435: [], # Snacks, granola bar, fruit-filled, nonfat
    19436: [], # Popcorn, sugar syrup/caramel, fat-free
    19437: [], # Snacks, potato chips, fat free, salted
    19438: [], # Snacks, KELLOGG, KELLOGG'S RICE KRISPIES TREATS Squares
    19439: [], # Snacks, KELLOGG, KELLOGG'S Low Fat Granola Bar, Crunchy Almond/Brown Sugar
    19440: [], # Snacks, M&M MARS, KUDOS Whole Grain Bar, chocolate chip
    19441: [], # Snacks, KELLOGG, KELLOGG'S, NUTRI-GRAIN Cereal Bars, fruit
    19444: [], # Snacks, tortilla chips, low fat, made with olestra, nacho cheese
    19445: [], # Snacks, potato chips, made from dried potatoes, fat-free, made with olestra
    19524: [], # Snacks, taro chips
    19701: [], # Candies, semisweet chocolate, made with butter
    19702: [], # Gelatin desserts, dry mix, with added ascorbic acid, sodium-citrate and salt
    19703: [], # Gelatin desserts, dry mix, reduced calorie, with aspartame, added phosphorus, potassium, sodium, vitamin C
    19704: [], # Gelatin desserts, dry mix, reduced calorie, with aspartame, no added sodium
    19705: [], # Puddings, banana, dry mix, instant, with added oil
    19706: [], # Puddings, banana, dry mix, regular, with added oil
    19708: [], # Puddings, lemon, dry mix, regular, with added oil, potassium, sodium
    19709: [], # Puddings, tapioca, dry mix, with no added salt
    19710: [], # Puddings, vanilla, dry mix, regular, with added oil
    19719: [], # Jams and preserves, apricot
    19720: [], # Syrups, table blends, pancake, with 2% maple, with added potassium
    19800: [], # Snacks, corn cakes, very low sodium
    19802: [], # Snacks, corn-based, extruded, puffs or twists, cheese-flavor, unenriched
    19804: [], # Snacks, corn-based, extruded, chips, barbecue-flavor, made with enriched masa flour
    19806: [], # Snacks, popcorn, air-popped (Unsalted)
    19807: [], # Snacks, popcorn, oil-popped, white popcorn, salt added
    19809: [], # Snacks, potato chips, plain, made with partially hydrogenated soybean oil, salted
    19810: [], # Snacks, potato chips, plain, made with partially hydrogenated soybean oil, unsalted
    19811: [], # Snacks, potato chips, plain, unsalted
    19812: [], # Snacks, pretzels, hard, plain, made with unenriched flour, salted
    19813: [], # Snacks, pretzels, hard, plain, made with unenriched flour, unsalted
    19814: [], # Snacks, pretzels, hard, plain, made with enriched flour, unsalted
    19816: [], # Snacks, rice cakes, brown rice, plain, unsalted
    19817: [], # Snacks, rice cakes, brown rice, buckwheat, unsalted
    19818: [], # Snacks, rice cakes, brown rice, multigrain, unsalted
    19819: [], # Snacks, rice cakes, brown rice, sesame seed, unsalted
    19820: [], # Snacks, sesame sticks, wheat-based, unsalted
    19821: [], # Snacks, trail mix, regular, unsalted
    19822: [], # Snacks, trail mix, regular, with chocolate chips, unsalted nuts and seeds
    19823: [], # Potato chips, without salt, reduced fat
    19833: [], # Snacks, tortilla chips, low fat, unsalted
    19856: [], # Frozen novelties, juice type, POPSICLE SCRIBBLERS
    19857: [], # Snacks, tortilla chips, nacho-flavor, made with enriched masa flour
    19858: [], # Candies, sugar-coated almonds
    19860: [], # Cocoa, dry powder, hi-fat or breakfast, processed with alkali
    19866: [], # Candies, soft fruit and nut squares
    19867: [], # Ice creams, vanilla, fat free
    19868: [], # Sweeteners, tabletop, sucralose, SPLENDA packets
    19871: [], # Frozen novelties, No Sugar Added, FUDGSICLE pops
    19873: [], # Frozen novelties, ice type, sugar free, orange, cherry, and grape POPSICLE pops
    19874: [], # Frozen novelties, KLONDIKE, SLIM-A-BEAR Fudge Bar, 98% fat free, no sugar added
    19875: [], # Ice creams, BREYERS, All Natural Light Vanilla
    19876: [], # Ice creams, BREYERS, All Natural Light French Vanilla
    19877: [], # Ice creams, BREYERS, 98% Fat Free Vanilla
    19878: [], # Ice creams, BREYERS, All Natural Light Vanilla Chocolate Strawberry
    19879: [], # Ice creams, BREYERS, All Natural Light Mint Chocolate Chip
    19880: [], # Ice creams, BREYERS, No Sugar Added, Butter Pecan
    19881: [], # Ice creams, BREYERS, No Sugar Added, French Vanilla
    19882: [], # Ice creams, BREYERS, No Sugar Added, Vanilla
    19883: [], # Ice creams, BREYERS, No Sugar Added, Vanilla Fudge Twirl
    19884: [], # Ice creams, BREYERS, No Sugar Added, Vanilla Chocolate Strawberry
    19886: [], # Frozen novelties, KLONDIKE, SLIM-A-BEAR Chocolate Cone
    19887: [], # Frozen novelties, KLONDIKE, SLIM-A-BEAR Vanilla Sandwich
    19890: [], # Frozen novelties, KLONDIKE, SLIM-A-BEAR, No Sugar Added, Stickless Bar
    19891: [], # Frozen novelties, No Sugar Added CREAMSICLE Pops
    19892: [], # Frozen novelties, Sugar Free, CREAMSICLE Pops
    19893: [], # Ice creams, BREYERS, All Natural Light French Chocolate
    19894: [], # Ice creams, BREYERS, 98% Fat Free Chocolate
    19895: [], # Ice creams, BREYERS, No Sugar Added, Chocolate Caramel
    19896: [], # Candies, REESE's Fast Break, milk chocolate, peanut butter, soft nougats, candy bar
    19897: [], # Candies, MARS SNACKFOOD US, COCOAVIA Chocolate Covered Almonds
    19898: [], # Ice creams, regular, low carbohydrate, vanilla
    19899: [], # Ice creams, regular, low carbohydrate, chocolate
    19902: [], # Chocolate, dark, 45- 59% cacao solids
    19903: [], # Chocolate, dark, 60-69% cacao solids
    19904: [], # Chocolate, dark, 70-85% cacao solids
    19905: [], # Candies, chocolate, dark, NFS (45-59% cacao solids 90%; 60-69% cacao solids 5%; 70-85% cacao solids 5%)
    19906: [], # Sweeteners, for baking, brown, contains sugar and sucralose
    19907: [], # Sweeteners, for baking, contains sugar and sucralose
    19908: [], # Sugar, turbinado
    19909: [], # Sweeteners, sugar substitute, granulated, brown
    19910: [], # Candies, crispy bar with peanut butter filling
    19911: [], # Syrup, maple, Canadian
    19912: [], # Sweetener, syrup, agave
    19913: [], # Candies, NESTLE, BUTTERFINGER Crisp
    19914: [], # Candies, M&M MARS 3 MUSKETEERS Truffle Crisp
    19916: [], # Syrups, chocolate, HERSHEY'S Sugar free, Genuine Chocolate Flavored, Lite Syrup
    19917: [], # Candies, M&M MARS Pretzel Chocolate Candies
    19918: [], # Sweetener, herbal extract powder from Stevia leaf
    19919: [], # Candies, fruit snacks, with high vitamin C
    19920: [], # Jams, preserves, marmalades, sweetened with fruit juice
    19921: [], # Candies, Tamarind
    19922: [], # Candies, coconut bar, not chocolate covered
    19923: [], # Candies, HERSHEYS, PAYDAY Bar
    19924: [], # Syrup, NESTLE, chocolate
    20001: [], # Amaranth grain, uncooked
    20002: [], # Amaranth grain, cooked
    20003: [], # Arrowroot flour
    20004: [], # Barley, hulled
    20005: ['Barley', 'pearled'], # Barley, pearled, raw
    20006: [], # Barley, pearled, cooked
    20008: [], # Buckwheat
    20009: [], # Buckwheat groats, roasted, dry
    20010: [], # Buckwheat groats, roasted, cooked
    20011: [], # Buckwheat flour, whole-groat
    20012: ["Bulgur", "dry"], # Bulgur, dry
    20013: ["Bulgur", "cooked"], # Bulgur, cooked
    20014: [], # Corn grain, yellow
    20015: [], # Corn bran, crude
    20016: [], # Corn flour, whole-grain, yellow
    20017: [], # Corn flour, masa, enriched, white
    20018: [], # Corn flour, yellow, degermed, unenriched
    20019: [], # Corn flour, masa, unenriched, white
    20020: [], # Cornmeal, whole-grain, yellow
    20022: [], # Cornmeal, degermed, enriched, yellow
    20023: [], # Cornmeal, yellow, self-rising, bolted, plain, enriched
    20024: [], # Cornmeal, yellow, self-rising, bolted, with wheat flour added, enriched
    20025: [], # Cornmeal, yellow, self-rising, degermed, enriched
    20027: [], # Cornstarch
    20028: [], # Couscous, dry
    20029: [], # Couscous, cooked
    20030: [], # Hominy, canned, white
    20031: ['Millet'], # Millet, raw
    20032: [], # Millet, cooked
    20033: ['Oat bran'], # Oat bran, raw
    20034: [], # Oat bran, cooked
    20035: ["Quinoa"], # Quinoa, uncooked
    20036: ['Rice', 'brown long-grain'], # Rice, brown, long-grain, raw (Includes foods for USDA's Food Distribution Program)
    20037: [], # Rice, brown, long-grain, cooked (Includes foods for USDA's Food Distribution Program)
    20038: [], # Oats (Includes foods for USDA's Food Distribution Program)
    20040: ['Rice', 'brown medium-grain'], # Rice, brown, medium-grain, raw (Includes foods for USDA's Food Distribution Program)
    20041: [], # Rice, brown, medium-grain, cooked (Includes foods for USDA's Food Distribution Program)
    20042: [], # Rice, brown, parboiled, dry, UNCLE BEN'S
    20044: [], # Rice, white, long-grain, regular, raw, enriched
    20045: [], # Rice, white, long-grain, regular, enriched, cooked
    20046: [], # Rice, white, long-grain, parboiled, enriched, dry
    20047: [], # Rice, white, long-grain, parboiled, enriched, cooked
    20048: [], # Rice, white, long-grain, precooked or instant, enriched, dry
    20049: [], # Rice, white, long-grain, precooked or instant, enriched, prepared
    20050: [], # Rice, white, medium-grain, raw, enriched
    20051: [], # Rice, white, medium-grain, enriched, cooked
    20052: [], # Rice, white, short-grain, enriched, uncooked
    20053: [], # Rice, white, short-grain, enriched, cooked
    20054: [], # Rice, white, glutinous, unenriched, uncooked
    20055: [], # Rice, white, glutinous, unenriched, cooked
    20058: [], # Rice, white, steamed, Chinese restaurant
    20060: [], # Rice bran, crude
    20061: ["Rice flour"], # Rice flour, white, unenriched
    20062: [], # Rye grain
    20063: [], # Rye flour, dark
    20064: [], # Rye flour, medium
    20065: [], # Rye flour, light
    20066: [], # Semolina, enriched
    20067: [], # Sorghum grain
    20068: ["Tapioca"], # Tapioca, pearl, dry
    20069: [], # Triticale
    20070: [], # Triticale flour, whole-grain
    20071: [], # Wheat, hard red spring
    20072: [], # Wheat, hard red winter
    20073: [], # Wheat, soft red winter
    20074: [], # Wheat, hard white
    20075: [], # Wheat, soft white
    20076: ["Durum wheat flour"], # Wheat, durum
    20077: ["Bran wheat flour"], # Wheat bran, crude
    20078: ["Germ wheat flour"], # Wheat germ, crude
    20080: ["Wheat flour", "whole-grain"], # Wheat flour, whole-grain (Includes foods for USDA's Food Distribution Program)
    20081: [], # Wheat flour, white, all-purpose, enriched, bleached
    20082: [], # Wheat flour, white, all-purpose, self-rising, enriched
    20083: [], # Wheat flour, white, bread, enriched
    20084: [], # Wheat flour, white, cake, enriched
    20086: [], # Wheat flour, white, tortilla mix, enriched
    20087: [], # Wheat, sprouted
    20088: ['Rice', 'wild'], # Wild rice, raw
    20089: [], # Wild rice, cooked
    20090: [], # Rice flour, brown
    20091: [], # Pasta, gluten-free, corn, dry
    20092: [], # Pasta, gluten-free, corn, cooked
    20093: ['Pasta', 'fresh-refrigerated plain'], # Pasta, fresh-refrigerated, plain, as purchased
    20094: [], # Pasta, fresh-refrigerated, plain, cooked
    20095: ['Pasta', 'fresh-refrigerated spinach'], # Pasta, fresh-refrigerated, spinach, as purchased
    20096: [], # Pasta, fresh-refrigerated, spinach, cooked
    20097: [], # Pasta, homemade, made with egg, cooked
    20098: [], # Pasta, homemade, made without egg, cooked
    20105: [], # Macaroni, vegetable, enriched, dry
    20106: [], # Macaroni, vegetable, enriched, cooked
    20109: [], # Noodles, egg, dry, enriched
    20110: [], # Noodles, egg, enriched, cooked
    20111: [], # Noodles, egg, spinach, enriched, dry
    20112: [], # Noodles, egg, spinach, enriched, cooked
    20113: [], # Noodles, chinese, chow mein
    20114: [], # Noodles, japanese, soba, dry
    20115: [], # Noodles, japanese, soba, cooked
    20116: [], # Noodles, japanese, somen, dry
    20117: [], # Noodles, japanese, somen, cooked
    20118: [], # Noodles, flat, crunchy, Chinese restaurant
    20120: [], # Pasta, dry, enriched
    20121: [], # Pasta, cooked, enriched, without added salt
    20124: ["Pasta", "whole-wheat dry"], # Pasta, whole-wheat, dry (Includes foods for USDA's Food Distribution Program)
    20125: [], # Pasta, whole-wheat, cooked (Includes foods for USDA's Food Distribution Program)
    20126: [], # Spaghetti, spinach, dry
    20127: [], # Spaghetti, spinach, cooked
    20129: [], # Wheat flours, bread, unenriched
    20130: [], # Barley flour or meal
    20131: [], # Barley malt flour
    20132: [], # Oat flour, partially debranned
    20133: [], # Rice noodles, dry
    20134: [], # Rice noodles, cooked
    20135: [], # Pasta, whole grain, 51% whole wheat, remaining unenriched semolina, dry
    20136: [], # Pasta, whole grain, 51% whole wheat, remaining unenriched semolina, cooked
    20137: [], # Quinoa, cooked
    20138: [], # Wheat, KAMUT khorasan, uncooked
    20139: [], # Wheat, KAMUT khorasan, cooked
    20140: [], # Spelt, uncooked
    20141: [], # Spelt, cooked
    20142: [], # Teff, uncooked
    20143: [], # Teff, cooked
    20310: [], # Noodles, egg, cooked, enriched, with added salt
    20314: [], # Corn grain, white
    20315: [], # Corn flour, whole-grain, blue (harina de maiz morado)
    20316: [], # Corn flour, whole-grain, white
    20317: [], # Corn flour, yellow, masa, enriched
    20320: [], # Cornmeal, whole-grain, white
    20321: [], # Pasta, cooked, enriched, with added salt
    20322: [], # Cornmeal, degermed, enriched, white
    20323: [], # Cornmeal, white, self-rising, bolted, plain, enriched
    20324: [], # Cornmeal, white, self-rising, bolted, with wheat flour added, enriched
    20325: [], # Cornmeal, white, self-rising, degermed, enriched
    20330: [], # Hominy, canned, yellow
    20345: [], # Rice, white, long-grain, regular, cooked, enriched, with salt
    20381: [], # Wheat flour, white, all-purpose, enriched, calcium-fortified
    20409: [], # Noodles, egg, dry, unenriched
    20410: [], # Noodles, egg, unenriched, cooked, without added salt
    20420: [], # Pasta, dry, unenriched
    20421: [], # Pasta, cooked, unenriched, without added salt
    20422: [], # Cornmeal, degermed, unenriched, yellow
    20444: ['Rice', 'white long-grain regular'], # Rice, white, long-grain, regular, raw, unenriched
    20445: [], # Rice, white, long-grain, regular, unenriched, cooked without salt
    20446: [], # Rice, white, long-grain, parboiled, unenriched, dry
    20447: [], # Rice, white, long-grain, parboiled, unenriched, cooked
    20450: ['Rice', 'white medium-grain'], # Rice, white, medium-grain, raw, unenriched
    20451: [], # Rice, white, medium-grain, cooked, unenriched
    20452: ['Rice', 'white short-grain'], # Rice, white, short-grain, raw, unenriched
    20453: [], # Rice, white, short-grain, cooked, unenriched
    20466: [], # Semolina, unenriched
    20481: ["Wheat flour", "all-purpose unenriched"], # Wheat flour, white, all-purpose, unenriched
    20510: [], # Noodles, egg, cooked, unenriched, with added salt
    20521: [], # Pasta, cooked, unenriched, with added salt
    20522: [], # Cornmeal, degermed, unenriched, white
    20523: [], # Spaghetti, protein-fortified, cooked, enriched (n x 6.25)
    20545: [], # Rice, white, long-grain, regular, cooked, unenriched, with salt
    20581: [], # Wheat flour, white, all-purpose, enriched, unbleached
    20622: [], # Spaghetti, protein-fortified, dry, enriched (n x 6.25)
    20623: [], # Wheat flour, white (industrial), 9% protein, bleached, enriched
    20624: [], # Wheat flour, white (industrial), 9% protein, bleached, unenriched
    20628: [], # Wheat flour, white (industrial), 10% protein, bleached, enriched
    20629: [], # Wheat flour, white (industrial), 10% protein, bleached, unenriched
    20630: [], # Wheat flour, white (industrial), 10% protein, unbleached, enriched
    20634: [], # Wheat flour, white (industrial), 11.5% protein, bleached, enriched
    20635: [], # Wheat flour, white (industrial), 11.5% protein, bleached, unenriched
    20636: [], # Wheat flour, white (industrial), 11.5% protein, unbleached, enriched
    20640: [], # Wheat flour, white (industrial), 13% protein, bleached, enriched
    20641: [], # Wheat flour, white (industrial), 13% protein, bleached, unenriched
    20645: [], # Wheat flour, white (industrial), 15% protein, bleached, enriched
    20646: [], # Wheat flour, white (industrial), 15% protein, bleached, unenriched
    20647: [], # Millet flour
    20648: [], # Sorghum flour, whole-grain
    20649: [], # Wheat flour, whole-grain, soft wheat
    20650: [], # Sorghum flour, refined, unenriched
    20651: [], # Rice, brown, parboiled, cooked, UNCLE BENS
    20652: [], # Pasta, whole grain, 51% whole wheat, remaining enriched semolina, cooked (Includes foods for USDA's Food Distribution Program)
    20653: [], # Pasta, whole grain, 51% whole wheat, remaining enriched semolina, dry (Includes foods for USDA's Food Distribution Program)
    20654: [], # Pasta, gluten-free, brown rice flour, cooked, TINKYADA
    20655: [], # Pasta, gluten-free, corn flour and quinoa flour, cooked, ANCIENT HARVEST
    20656: [], # Pasta, gluten-free, rice flour and rice bran extract, cooked, DE BOLES
    20657: [], # Pasta, gluten-free, corn and rice flour, cooked
    21003: [], # Fast foods, biscuit, with egg and bacon
    21004: [], # Fast foods, biscuit, with egg and ham
    21005: [], # Fast Foods, biscuit, with egg and sausage
    21007: [], # Fast foods, biscuit, with egg, cheese, and bacon
    21008: [], # Fast foods, biscuit, with ham
    21009: [], # Fast foods, biscuit, with sausage
    21010: [], # Fast foods, biscuit, with crispy chicken fillet
    21012: [], # Fast foods, croissant, with egg, cheese, and bacon
    21013: [], # Fast foods, croissant, with egg, cheese, and ham
    21014: [], # Fast foods, croissant, with egg, cheese, and sausage
    21018: [], # Fast foods, egg, scrambled
    21020: [], # Fast foods, english muffin, with cheese and sausage
    21021: [], # Fast foods, english muffin, with egg, cheese, and canadian bacon
    21022: [], # Fast foods, english muffin, with egg, cheese, and sausage
    21024: [], # Fast foods, french toast sticks
    21026: [], # Fast foods, potatoes, hash browns, round pieces or patty
    21028: [], # Fast foods, vanilla, light, soft-serve ice cream, with cone
    21032: [], # Fast foods, sundae, caramel
    21033: [], # Fast foods, sundae, hot fudge
    21034: [], # Fast foods, sundae, strawberry
    21059: [], # Fast foods, shrimp, breaded and fried
    21060: [], # Fast foods, burrito, with beans
    21061: [], # Fast foods, burrito, with beans and cheese
    21063: [], # Fast foods, burrito, with beans and beef
    21064: [], # Fast foods, burrito, with beans, cheese, and beef
    21078: [], # Fast foods, nachos, with cheese
    21080: [], # Fast foods, nachos, with cheese, beans, ground beef, and tomatoes
    21082: [], # Fast foods, taco with beef, cheese and lettuce, hard shell
    21089: [], # Fast foods, cheeseburger; single, regular patty; plain
    21090: [], # Fast foods, cheeseburger; single, regular patty, with condiments
    21091: [], # Fast foods, cheeseburger; single, regular patty, with condiments and vegetables
    21094: [], # Fast foods, cheeseburger, double, regular patty and bun, with condiments
    21096: [], # Fast foods, cheeseburger; single, large patty; plain
    21102: [], # Fast foods, chicken fillet sandwich, plain with pickles
    21105: [], # Fast foods, fish sandwich, with tartar sauce
    21106: [], # Fast foods, fish sandwich, with tartar sauce and cheese
    21107: [], # Fast foods, hamburger; single, regular patty; plain
    21108: [], # Fast foods, hamburger; single, regular patty; with condiments
    21121: [], # Fast foods, roast beef sandwich, plain
    21124: [], # Fast foods, submarine sandwich, cold cut on white bread with lettuce and tomato
    21125: [], # Fast foods, submarine sandwich, roast beef on white bread with lettuce and tomato
    21126: [], # Fast foods, submarine sandwich, tuna on white bread with lettuce and tomato
    21127: [], # Fast foods, coleslaw
    21129: [], # Fast foods, hush puppies
    21130: [], # Fast foods, onion rings, breaded and fried
    21138: [], # Fast foods, potato, french fried in vegetable oil
    21139: [], # Fast foods, potato, mashed
    21141: [], # BURGER KING, Vanilla Shake
    21142: [], # Fast food, biscuit
    21143: [], # CHICK-FIL-A, Chick-n-Strips
    21144: [], # CHICK-FIL-A, hash browns
    21145: [], # School Lunch, pizza, BIG DADDY'S LS 16" 51% Whole Grain Rolled Edge Cheese Pizza, frozen
    21146: [], # School Lunch, pizza, BIG DADDY'S LS 16" 51% Whole Grain Rolled Edge Turkey Pepperoni Pizza, frozen
    21147: [], # School Lunch, pizza, TONY'S SMARTPIZZA Whole Grain 4x6 Cheese Pizza 50/50 Cheese, frozen
    21148: [], # School Lunch, pizza, TONY'S SMARTPIZZA Whole Grain 4x6 Pepperoni Pizza 50/50 Cheese, frozen
    21149: [], # School Lunch, pizza, TONY'S Breakfast Pizza Sausage, frozen
    21150: [], # SUBWAY, sweet onion chicken teriyaki sub on white bread with lettuce, tomato and sweet onion sauce
    21151: [], # Fast foods, submarine sandwich, sweet onion chicken teriyaki on white bread with lettuce, tomato and sweet onion sauce
    21152: [], # SUBWAY, SUBWAY CLUB sub on white bread with lettuce and tomato
    21153: [], # Fast foods, submarine sandwich, turkey, roast beef and ham on white bread with lettuce and tomato
    21154: [], # Fast foods, submarine sandwich, oven roasted chicken on white bread with lettuce and tomato
    21155: [], # Fast foods, submarine sandwich, turkey breast on white bread with lettuce and tomato
    21156: [], # Fast foods, submarine sandwich, ham on white bread with lettuce and tomato
    21157: [], # SUBWAY, meatball marinara sub on white bread (no toppings)
    21158: [], # Fast foods, submarine sandwich, meatball marinara on white bread
    21159: [], # SUBWAY, steak & cheese sub on white bread with American cheese, lettuce and tomato
    21160: [], # Fast foods, submarine sandwich, steak and cheese on white bread with cheese, lettuce and tomato
    21161: [], # SUBWAY, B.L.T. sub on white bread with bacon, lettuce and tomato
    21162: [], # Fast foods, submarine sandwich, bacon, lettuce, and tomato on white bread
    21202: [], # Fast foods, hamburger, large, single patty, with condiments
    21207: [], # SUBWAY, turkey breast sub on white bread with lettuce and tomato
    21209: [], # SUBWAY, black forest ham sub on white bread with lettuce and tomato
    21210: [], # SUBWAY, roast beef sub on white bread with lettuce and tomato
    21211: [], # SUBWAY, oven roasted chicken sub on white bread with lettuce and tomato
    21213: [], # SUBWAY, cold cut sub on white bread with lettuce and tomato
    21214: [], # SUBWAY, tuna sub on white bread with lettuce and tomato
    21224: [], # Pizza, cheese topping, regular crust, frozen, cooked
    21225: [], # Pizza, cheese topping, rising crust, frozen, cooked
    21226: [], # Pizza, meat and vegetable topping, regular crust, frozen, cooked
    21227: [], # Pizza, meat and vegetable topping, rising crust, frozen, cooked
    21228: [], # McDONALD'S, Hamburger
    21229: [], # Fast foods, chicken, breaded and fried, boneless pieces, plain
    21230: [], # Fast Foods, crispy chicken filet sandwich, with lettuce and mayonnaise
    21232: [], # McDONALD'S, FILET-O-FISH
    21233: [], # McDONALD'S, Cheeseburger
    21234: [], # McDONALD'S, QUARTER POUNDER
    21235: [], # McDONALD'S, QUARTER POUNDER with Cheese
    21237: [], # McDONALD'S, BIG MAC
    21238: [], # McDONALD'S, french fries
    21239: [], # WENDY'S, CLASSIC SINGLE Hamburger, no cheese
    21240: [], # WENDY'S, CLASSIC SINGLE Hamburger, with cheese
    21241: [], # WENDY'S, Jr. Hamburger, without cheese
    21242: [], # WENDY'S, Jr. Hamburger, with cheese
    21243: [], # WENDY'S, CLASSIC DOUBLE, with cheese
    21244: [], # WENDY'S, Homestyle Chicken Fillet Sandwich
    21245: [], # WENDY'S, Ultimate Chicken Grill Sandwich
    21246: [], # WENDY'S, Chicken Nuggets
    21247: [], # WENDY'S, french fries
    21248: [], # WENDY'S, Frosty Dairy Dessert
    21249: [], # BURGER KING, french fries
    21250: [], # BURGER KING, Hamburger
    21251: [], # BURGER KING, Cheeseburger
    21252: [], # BURGER KING, WHOPPER, no cheese
    21253: [], # BURGER KING, WHOPPER, with cheese
    21254: [], # BURGER KING, DOUBLE WHOPPER, no cheese
    21255: [], # BURGER KING, DOUBLE WHOPPER, with cheese
    21256: [], # BURGER KING, Chicken Strips
    21258: [], # BURGER KING, Premium Fish Sandwich
    21259: [], # BURGER KING, Original Chicken Sandwich
    21260: [], # TACO BELL, Original Taco with beef, cheese and lettuce
    21261: [], # TACO BELL, Soft Taco with beef, cheese and lettuce
    21262: [], # TACO BELL, Soft Taco with chicken, cheese and lettuce
    21263: [], # TACO BELL, Soft Taco with steak
    21264: [], # TACO BELL, Bean Burrito
    21265: [], # TACO BELL, BURRITO SUPREME with beef
    21266: [], # TACO BELL, BURRITO SUPREME with chicken
    21267: [], # TACO BELL, BURRITO SUPREME with steak
    21268: [], # TACO BELL, Nachos
    21269: [], # TACO BELL, Nachos Supreme
    21270: [], # TACO BELL, Taco Salad
    21271: [], # PIZZA HUT 12" Cheese Pizza, Hand-Tossed Crust
    21272: [], # PIZZA HUT 12" Cheese Pizza, Pan Crust
    21273: [], # PIZZA HUT 12" Cheese Pizza, THIN 'N CRISPY Crust
    21274: [], # PIZZA HUT 12" Pepperoni Pizza, Hand-Tossed Crust
    21275: [], # PIZZA HUT 12" Pepperoni Pizza, Pan Crust
    21276: [], # PIZZA HUT 12" Super Supreme Pizza, Hand-Tossed Crust
    21277: [], # DOMINO'S 14" Cheese Pizza, Classic Hand-Tossed Crust
    21278: [], # DOMINO'S 14" Cheese Pizza, Ultimate Deep Dish Crust
    21279: [], # DOMINO'S 14" Cheese Pizza, Crunchy Thin Crust
    21280: [], # DOMINO'S 14" Pepperoni Pizza, Classic Hand-Tossed Crust
    21281: [], # DOMINO'S 14" Pepperoni Pizza, Ultimate Deep Dish Crust
    21282: [], # DOMINO'S 14" EXTRAVAGANZZA FEAST Pizza, Classic Hand-Tossed Crust
    21283: [], # PAPA JOHN'S 14" Cheese Pizza, Original Crust
    21284: [], # PAPA JOHN'S 14" Pepperoni Pizza, Original Crust
    21285: [], # PAPA JOHN'S 14" The Works Pizza, Original Crust
    21286: [], # PAPA JOHN'S 14" Cheese Pizza, Thin Crust
    21287: [], # LITTLE CAESARS 14" Original Round Cheese Pizza, Regular Crust
    21288: [], # LITTLE CAESARS 14" Original Round Pepperoni Pizza, Regular Crust
    21289: [], # LITTLE CAESARS 14" Original Round Meat and Vegetable Pizza, Regular Crust
    21290: [], # LITTLE CAESARS 14" Cheese Pizza, Large Deep Dish Crust
    21291: [], # LITTLE CAESARS 14" Pepperoni Pizza, Large Deep Dish Crust
    21292: [], # LITTLE CAESARS 14" Cheese Pizza, Thin Crust
    21293: [], # PIZZA HUT 14" Cheese Pizza, Hand-Tossed Crust
    21294: [], # PIZZA HUT 14" Cheese Pizza, Pan Crust
    21295: [], # PIZZA HUT 14" Cheese Pizza, THIN 'N CRISPY Crust
    21296: [], # PIZZA HUT 14" Pepperoni Pizza, Hand-Tossed Crust
    21297: [], # PIZZA HUT 14" Pepperoni Pizza, Pan Crust
    21298: [], # PIZZA HUT 14" Super Supreme Pizza, Hand-Tossed Crust
    21299: [], # Fast Food, Pizza Chain, 14" pizza, cheese topping, regular crust
    21300: [], # Fast Food, Pizza Chain, 14" pizza, cheese topping, thick crust
    21301: [], # Fast Food, Pizza Chain, 14" pizza, cheese topping, thin crust
    21302: [], # Fast Food, Pizza Chain, 14" pizza, pepperoni topping, regular crust
    21303: [], # Fast Food, Pizza Chain, 14" pizza, pepperoni topping, thick crust
    21304: [], # Fast Food, Pizza Chain, 14" pizza, meat and vegetable topping, regular crust
    21305: [], # Fast foods, griddle cake sandwich, egg, cheese, and sausage
    21306: [], # Fast foods, griddle cake sandwich, sausage
    21307: [], # Fast foods, griddle cake sandwich, egg, cheese, and bacon
    21309: [], # McDONALD'S, Chicken McNUGGETS
    21319: [], # McDONALD'S, Hash Brown
    21321: [], # McDONALD'S, Hotcakes (plain)
    21327: [], # McDONALD'S, Bacon, Egg & Cheese McGRIDDLES
    21328: [], # McDONALD'S, Sausage McGRIDDLES
    21329: [], # McDONALD'S, Sausage, Egg & Cheese McGRIDDLES
    21333: [], # McDONALD'S, Vanilla Reduced Fat Ice Cream Cone
    21334: [], # McDONALD'S, Strawberry Sundae
    21335: [], # McDONALD'S, Hot Caramel Sundae
    21336: [], # McDONALD'S, Hot Fudge Sundae
    21338: [], # McDONALD'S, McFLURRY with M&M'S CANDIES
    21339: [], # McDONALD'S, McFLURRY with OREO cookies
    21340: [], # McDONALD'S, Sausage Burrito
    21341: [], # McDONALD'S, BIG BREAKFAST
    21344: [], # McDONALD'S, Double Cheeseburger
    21345: [], # McDONALD'S, DOUBLE QUARTER POUNDER with Cheese
    21350: [], # McDONALD'S, BIG MAC (without Big Mac Sauce)
    21355: [], # McDONALD'S, McCHICKEN Sandwich
    21356: [], # McDONALD'S, McCHICKEN Sandwich (without mayonnaise)
    21357: [], # McDONALD'S, Egg McMUFFIN
    21358: [], # McDONALD'S, Sausage McMUFFIN
    21359: [], # McDONALD'S, Sausage McMUFFIN with Egg
    21360: [], # McDONALD'S, Bacon Egg & Cheese Biscuit
    21361: [], # McDONALD'S, Sausage Biscuit
    21362: [], # McDONALD'S, Sausage Biscuit with Egg
    21363: [], # McDONALD'S, Deluxe Breakfast, with syrup and margarine
    21364: [], # McDONALD'S, Hotcakes and Sausage
    21365: [], # McDONALD'S, Hotcakes (with 2 pats margarine & syrup)
    21376: [], # McDONALD'S, Bacon Ranch Salad with Grilled Chicken
    21377: [], # McDONALD'S Bacon Ranch Salad with Crispy Chicken
    21378: [], # McDONALD'S, Bacon Ranch Salad without chicken
    21379: [], # McDONALD'S, Side Salad
    21380: [], # McDONALD'S, Fruit 'n Yogurt Parfait
    21381: [], # McDONALD'S, Fruit 'n Yogurt Parfait (without granola)
    21382: [], # McDONALD'S, FILET-O-FISH (without tartar sauce)
    21383: [], # BURGER KING, CROISSAN'WICH with Sausage, Egg and Cheese
    21384: [], # BURGER KING, CROISSAN'WICH with Sausage and Cheese
    21385: [], # BURGER KING, CROISSAN'WICH with Egg and Cheese
    21386: [], # BURGER KING, french toast sticks
    21387: [], # BURGER KING, Hash Brown Rounds
    21388: [], # Fast foods, miniature cinnamon rolls
    21389: [], # Fast foods, hamburger; double, large patty; with condiments, vegetables and mayonnaise
    21390: [], # Fast foods, hamburger; single, large patty; with condiments, vegetables and mayonnaise
    21393: [], # Fast foods, hamburger; single, regular patty; double decker bun with condiments and special sauce
    21395: [], # Fast foods, cheeseburger; double, regular patty; with condiments
    21396: [], # Fast foods, cheeseburger; double, large patty; with condiments
    21397: [], # Fast foods, cheeseburger; single, large patty; with condiments, vegetables and mayonnaise
    21398: [], # Fast foods, cheeseburger; single, large patty; with condiments
    21399: [], # Fast Foods, cheeseburger; double, large patty; with condiments, vegetables and mayonnaise
    21400: [], # Fast foods, cheeseburger; double, regular patty; double decker bun with condiments and special sauce
    21401: [], # Fast foods, chicken tenders
    21410: [], # Fast foods, bagel, with egg, sausage patty, cheese, and condiments
    21411: [], # Fast foods, bagel, with breakfast steak, egg, cheese, and condiments
    21412: [], # Light Ice Cream, soft serve, blended with milk chocolate candies
    21413: [], # Light Ice Cream, soft serve, blended with cookie pieces
    21415: [], # POPEYES, biscuit
    21416: [], # POPEYES, Coleslaw
    21417: [], # POPEYES, Mild Chicken Strips, analyzed 2006
    21418: [], # POPEYES, Spicy Chicken Strips, analyzed 2006
    21419: [], # KFC, biscuit
    21420: [], # KFC, Coleslaw
    21421: [], # KFC, Crispy Chicken Strips
    21422: [], # KFC, Popcorn Chicken
    21424: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Skin and Breading
    21425: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Breast, meat only, skin and breading removed
    21426: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Drumstick, meat only, skin and breading removed
    21427: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Thigh, meat only, skin and breading removed
    21428: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Wing, meat only, skin and breading removed
    21429: [], # KFC, Fried Chicken, EXTRA CRISPY, Skin and Breading
    21430: [], # KFC, Fried Chicken, EXTRA CRISPY, Breast, meat only, skin and breading removed
    21431: [], # KFC, Fried Chicken, EXTRA CRISPY, Drumstick, meat only, skin and breading removed
    21432: [], # KFC, Fried Chicken, EXTRA CRISPY, Thigh, meat only, skin and breading removed
    21433: [], # KFC, Fried Chicken, EXTRA CRISPY, Wing, meat only, skin and breading removed
    21434: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Breast, meat and skin with breading
    21435: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Drumstick, meat and skin with breading
    21436: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Thigh, meat and skin with breading
    21437: [], # KFC, Fried Chicken, ORIGINAL RECIPE, Wing, meat and skin with breading
    21438: [], # KFC, Fried Chicken, EXTRA CRISPY, Breast, meat and skin with breading
    21439: [], # KFC, Fried Chicken, EXTRA CRISPY, Drumstick, meat and skin with breading
    21440: [], # KFC, Fried Chicken, EXTRA CRISPY, Thigh, meat and skin with breading
    21441: [], # KFC, Fried Chicken, EXTRA CRISPY, Wing, meat and skin with breading
    21442: [], # POPEYES, Fried Chicken, Mild, Breast, meat only, skin and breading removed
    21443: [], # POPEYES, Fried Chicken, Mild, Drumstick, meat only, skin and breading removed
    21444: [], # POPEYES, Fried Chicken, Mild, Skin and Breading
    21445: [], # POPEYES, Fried Chicken, Mild, Thigh, meat only, skin and breading removed
    21446: [], # POPEYES, Fried Chicken, Mild, Wing, meat only, skin and breading removed
    21456: [], # POPEYES, Fried Chicken, Mild, Breast, meat and skin with breading
    21457: [], # POPEYES, Fried Chicken, Mild, Drumstick, meat and skin with breading
    21458: [], # POPEYES, Fried Chicken, Mild, Thigh, meat and skin with breading
    21459: [], # POPEYES, Fried Chicken, Mild, Wing, meat and skin with breading
    21461: [], # Fast foods, grilled chicken, bacon and tomato club sandwich, with cheese, lettuce, and mayonnaise
    21462: [], # Fast foods, crispy chicken, bacon, and tomato club sandwich, with cheese, lettuce, and mayonnaise
    21463: [], # Yogurt parfait, lowfat, with fruit and granola
    21464: [], # Fast Foods, Fried Chicken, Breast, meat only, skin and breading removed
    21465: [], # Fast Foods, Fried Chicken, Drumstick, meat only, skin and breading removed
    21466: [], # Fast Foods, Fried Chicken, Thigh, meat only, skin and breading removed
    21467: [], # Fast Foods, Fried Chicken, Wing, meat only, skin and breading removed
    21468: [], # Fast Foods, Fried Chicken, Skin and breading from all pieces
    21469: [], # Fast Foods, Fried Chicken, Breast, meat and skin and breading
    21470: [], # Fast Foods, Fried Chicken, Drumstick, meat and skin with breading
    21471: [], # Fast Foods, Fried Chicken, Thigh, meat and skin and breading
    21472: [], # Fast Foods, Fried Chicken, Wing, meat and skin and breading
    21473: [], # DIGIORNO Pizza, cheese topping, cheese stuffed crust, frozen, baked
    21474: [], # DIGIORNO Pizza, cheese topping, rising crust, frozen, baked
    21475: [], # DIGIORNO Pizza, cheese topping, thin crispy crust, frozen, baked
    21476: [], # DIGIORNO Pizza, pepperoni topping, cheese stuffed crust, frozen, baked
    21477: [], # DIGIORNO Pizza, pepperoni topping, rising crust, frozen, baked
    21478: [], # DIGIORNO Pizza, pepperoni topping, thin crispy crust, frozen, baked
    21479: [], # DIGIORNO Pizza, supreme topping, rising crust, frozen, baked
    21480: [], # DIGIORNO Pizza, supreme topping, thin crispy crust, frozen, baked
    21482: [], # Fast Food, Pizza Chain, 14" pizza, sausage topping, thick crust
    21483: [], # Fast Food, Pizza Chain, 14" pizza, sausage topping, thin crust
    21484: [], # Fast Food, Pizza Chain, 14" pizza, sausage topping, regular crust
    21485: [], # Fast Food, Pizza Chain, 14" pizza, pepperoni topping, thin crust
    21486: [], # Fast foods, taco with beef, cheese and lettuce, soft
    21487: [], # Fast foods, taco with chicken, lettuce and cheese, soft
    21488: [], # Fast foods, quesadilla, with chicken
    21490: [], # Fast Foods, grilled chicken filet sandwich, with lettuce, tomato and spread
    21491: [], # PIZZA HUT 14" Pepperoni Pizza, THIN 'N CRISPY Crust
    21492: [], # DOMINO'S 14" Pepperoni Pizza, Crunchy Thin Crust
    21493: [], # DOMINO'S 14" Sausage Pizza, Crunchy Thin Crust
    21494: [], # DOMINO'S 14" Sausage Pizza, Classic Hand-Tossed Crust
    21495: [], # DOMINO'S 14" Sausage Pizza, Ultimate Deep Dish Crust
    21496: [], # PIZZA HUT 14" Sausage Pizza, THIN 'N CRISPY Crust
    21497: [], # PIZZA HUT 14" Sausage Pizza, Hand-Tossed Crust
    21498: [], # PIZZA HUT 14" Sausage Pizza, Pan Crust
    21505: [], # Pizza, cheese topping, thin crust, frozen, cooked
    21506: [], # BURGER KING, Double Cheeseburger
    21507: [], # WENDY'S, Double Stack, with cheese
    21508: [], # WEND'YS, Crispy Chicken Sandwich
    21509: [], # BURGER KING, Onion Rings
    21510: [], # WENDY'S, DAVE'S Hot 'N Juicy 1/4 LB, single
    21511: [], # Fast Food, Pizza Chain, 14" pizza, cheese topping, stuffed crust
    21512: [], # PIZZA HUT 14" Cheese Pizza, Stuffed Crust
    21517: [], # Fast foods, crispy chicken in tortilla, with lettuce, cheese, and ranch sauce
    21518: [], # Fast foods, grilled chicken in tortilla, with lettuce, cheese, and ranch sauce
    21519: [], # Fast foods, breakfast burrito, with egg, cheese, and sausage
    21520: [], # Fast foods, breadstick, soft, prepared with garlic and parmesan cheese
    21521: [], # Fast foods, strawberry banana smoothie made with ice and low-fat yogurt
    21522: [], # McDONALD'S, Southern Style Chicken Biscuit
    21523: [], # McDONALD'S, RANCH SNACK WRAP, Crispy
    21524: [], # McDONALD'S, RANCH SNACK WRAP, Grilled
    21525: [], # PIZZA HUT, breadstick, parmesan garlic
    21526: [], # CHICK-FIL-A, chicken sandwich
    21527: [], # ARBY'S, roast beef sandwich, classic
    21600: [], # School Lunch, pizza, cheese topping, thin crust, whole grain, frozen, cooked
    21601: [], # School Lunch, pizza, cheese topping, thick crust, whole grain, frozen, cooked
    21602: [], # School Lunch, pizza, pepperoni topping, thin crust, whole grain, frozen, cooked
    21603: [], # School Lunch, pizza, pepperoni topping, thick crust, whole grain, frozen, cooked
    21604: [], # School Lunch, pizza, sausage topping, thin crust, whole grain, frozen, cooked
    21605: [], # School Lunch, pizza, sausage topping, thick crust, whole grain, frozen, cooked
    21610: [], # School Lunch, chicken patty, whole grain breaded
    21611: [], # School Lunch, chicken nuggets, whole grain breaded
    22247: [], # Macaroni and Cheese, canned entree
    22401: [], # Spaghetti with meat sauce, frozen entree
    22402: [], # Beef macaroni with tomato sauce, frozen entree, reduced fat
    22522: [], # Pasta with Sliced Franks in Tomato Sauce, canned entree
    22528: [], # Turkey Pot Pie, frozen entree
    22529: [], # Beef Pot Pie, frozen entree, prepared
    22535: [], # HOT POCKETS, CROISSANT POCKETS Chicken, Broccoli, and Cheddar Stuffed Sandwich, frozen
    22537: [], # HOT POCKETS Ham 'N Cheese Stuffed Sandwich, frozen
    22899: [], # Ravioli, cheese-filled, canned
    22900: [], # Ravioli, meat-filled, with tomato sauce or meat sauce, canned
    22901: [], # Tortellini, pasta with cheese filling, fresh-refrigerated, as purchased
    22902: [], # Pizza, meat topping, thick crust, frozen, cooked
    22903: [], # Pizza, pepperoni topping, regular crust, frozen, cooked
    22904: [], # Chili con carne with beans, canned entree
    22905: [], # Beef stew, canned entree
    22906: [], # Chicken pot pie, frozen entree, prepared
    22908: [], # Beef, corned beef hash, with potato, canned
    22910: [], # Lasagna, cheese, frozen, prepared
    22911: [], # Chili, no beans, canned entree
    22912: [], # Spaghetti, with meatballs in tomato sauce, canned
    22914: [], # Pasta with tomato sauce, no meat, canned
    22915: [], # Lasagna with meat & sauce, low-fat, frozen entree
    22916: [], # Lasagna with meat & sauce, frozen entree
    22917: [], # Burrito, beef and bean, frozen
    22918: [], # Burrito, bean and cheese, frozen
    22919: [], # Macaroni and Cheese, canned, microwavable
    22928: [], # Burrito, beef and bean, microwaved
    22953: [], # Egg rolls, pork, refrigerated, heated
    22954: [], # Egg rolls, chicken, refrigerated, heated
    22955: [], # Egg rolls, vegetable, frozen, prepared
    22956: [], # Lasagna, Vegetable, frozen, baked
    22957: [], # Turkey, stuffing, mashed potatoes w/gravy, assorted vegetables, frozen, microwaved
    22958: [], # Rice bowl with chicken, frozen entree, prepared (includes fried, teriyaki, and sweet and sour varieties)
    22959: [], # Macaroni and cheese dinner with dry sauce mix, boxed, uncooked
    22960: [], # Macaroni and cheese, dry mix, prepared with 2% milk and 80% stick margarine from dry mix
    22961: [], # HOT POCKETS, meatballs & mozzarella stuffed sandwich, frozen
    22962: [], # LEAN POCKETS, Ham N Cheddar
    22963: [], # Lean Pockets, Meatballs & Mozzarella
    22969: [], # Chili with beans, microwavable bowls
    22970: [], # Macaroni and cheese, frozen entree
    22971: [], # Potato salad with egg
    22972: [], # Pulled pork in barbecue sauce
    22973: [], # Corn dogs, frozen, prepared
    22974: [], # Chicken, nuggets, dark and white meat, precooked, frozen, not reheated
    22975: [], # Chicken, nuggets, white meat, precooked, frozen, not reheated
    22976: [], # Ravioli, cheese with tomato sauce, frozen, not prepared, includes regular and light entrees
    22977: [], # Lasagna with meat sauce, frozen, prepared
    22978: [], # Chicken tenders, breaded, frozen, prepared
    22998: [], # RICE-A-RONI, chicken flavor, unprepared
    22999: [], # Rice and vermicelli mix, chicken flavor, prepared with 80% margarine
    23000: [], # Beef, shoulder pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23001: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23002: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23003: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    23004: [], # Beef, short loin, porterhouse steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23005: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23006: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23007: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, select, raw
    23008: [], # Beef, short loin, t-bone steak, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23030: [], # Beef, round, knuckle, tip side, steak, separable lean and fat, trimmed to 0" fat, choice, raw
    23031: [], # Beef, round, knuckle, tip side, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23032: [], # Beef, round, knuckle, tip side, steak, separable lean and fat , trimmed to 0" fat, select, raw
    23033: [], # Beef, round, knuckle, tip side, steak, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23034: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, choice, raw
    23035: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23036: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, select, raw
    23037: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, choice, raw
    23038: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23039: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, select, raw
    23040: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23041: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, choice, raw
    23042: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23043: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, select, raw
    23044: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23045: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, choice, raw
    23046: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23047: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, select, raw
    23048: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23049: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, choice, raw
    23050: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23051: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, select, raw
    23052: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23053: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, all grades, raw
    23054: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23055: [], # Beef, round, knuckle, tip side, steak, separable lean and fat, trimmed to 0" fat, all grades, raw
    23056: [], # Beef, round, knuckle, tip side, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23057: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, all grades, raw
    23058: [], # Beef, chuck, shoulder clod, shoulder top and center steaks, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23059: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, all grades, raw
    23060: [], # Beef, chuck, shoulder clod, top blade, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23061: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, all grades, raw
    23062: [], # Beef, round, knuckle, tip center, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23063: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, all grades, raw
    23064: [], # Beef, round, outside round, bottom round, steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23065: [], # Beef, chuck, shoulder clod, shoulder tender, medallion, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23066: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23067: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, select, raw
    23068: [], # Beef, chuck, short ribs, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23069: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    23070: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    23071: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    23072: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23073: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, select, raw
    23074: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23075: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23076: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23077: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23078: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23079: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23080: [], # Beef, chuck eye steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23081: [], # Beef, shoulder pot roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    23082: [], # Beef, shoulder pot roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    23083: [], # Beef, shoulder pot roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    23084: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    23085: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    23086: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    23087: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23088: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23089: [], # Beef, chuck, mock tender steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23090: [], # Beef, chuck for stew, separable lean and fat, all grades, cooked, braised
    23091: [], # Beef, chuck for stew, separable lean and fat, select, cooked, braised
    23092: [], # Beef, chuck for stew, separable lean and fat, choice, cooked, braised
    23093: [], # Beef, chuck for stew, separable lean and fat, all grades, raw
    23094: [], # Beef, chuck for stew, separable lean and fat, select, raw
    23095: [], # Beef, chuck for stew, separable lean and fat, choice, raw
    23096: [], # Beef, chuck, under blade steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, braised
    23097: [], # Beef, chuck, under blade steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, braised
    23098: [], # Beef, chuck, under blade steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    23099: [], # Beef, chuck, under blade pot roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23100: [], # Beef, rib eye steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    23101: [], # Beef, rib eye roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, choice, cooked, roasted
    23102: [], # Beef, chuck, under blade pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23103: [], # Beef, chuck, under blade pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23104: [], # Beef, chuck, under blade pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23105: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23106: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23107: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23108: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, all grades, raw
    23109: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, choice, raw
    23110: [], # Beef, chuck, under blade center steak, boneless, Denver Cut, separable lean and fat, trimmed to 0" fat, select, raw
    23111: [], # Beef, shoulder pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23112: [], # Beef, shoulder pot roast or steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23113: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    23114: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    23115: [], # Beef, chuck eye roast, boneless, America's Beef Roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    23116: [], # Beef, chuck, under blade steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23117: [], # Beef, chuck, under blade steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23118: [], # Beef, chuck, under blade steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23119: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23120: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23121: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23122: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23123: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23124: [], # Beef, chuck, mock tender steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23125: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23126: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23127: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23128: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23129: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23130: [], # Beef, chuck, short ribs, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23131: [], # Beef, shoulder pot roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23132: [], # Beef, shoulder pot roast, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23133: [], # Beef, shoulder pot roast, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23134: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23135: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23136: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23137: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23138: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23139: [], # Beef, chuck eye Country-Style ribs, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23140: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23141: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23142: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23143: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23144: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23145: [], # Beef, chuck eye steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23146: [], # Beef, rib eye roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, all grades, cooked, roasted
    23147: [], # Beef, rib eye roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, select, cooked, roasted
    23148: [], # Beef, rib eye steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    23149: [], # Beef, rib eye steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23150: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, all grades, raw
    23151: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, choice, raw
    23152: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, select, raw
    23153: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, all grades, raw
    23154: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, choice, raw
    23155: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, select, raw
    23156: [], # Beef, rib eye steak, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    23157: [], # Beef, rib eye steak, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    23158: [], # Beef, rib eye steak, bone-in, lip-on, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23159: [], # Beef, rib eye roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, all grades, cooked, roasted
    23160: [], # Beef, rib eye roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, choice, cooked, roasted
    23161: [], # Beef, rib eye roast, boneless, lip-on, separable lean only, trimmed to 1/8" fat, select, cooked, roasted
    23162: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23163: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, all grades, raw
    23164: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23165: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, choice, raw
    23166: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23167: [], # Beef, plate steak, boneless, inside skirt, separable lean only, trimmed to 0" fat, select, raw
    23168: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23169: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, all grades, raw
    23170: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23171: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, choice, raw
    23172: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23173: [], # Beef, plate steak, boneless, outside skirt, separable lean only, trimmed to 0" fat, select, raw
    23174: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23175: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, all grades, raw
    23176: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23177: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, choice, raw
    23178: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23179: [], # Beef, rib eye steak, boneless, lip off, separable lean only, trimmed to 0" fat, select, raw
    23180: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, all grades, cooked, braised
    23181: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, all grades, raw
    23182: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, choice, cooked, braised
    23183: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, choice, raw
    23184: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, select, cooked, braised
    23185: [], # Beef, rib, back ribs, bone-in, separable lean only, trimmed to 0" fat, select, raw
    23186: [], # Beef, rib eye steak, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    23187: [], # Beef, rib eye steak, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23188: [], # Beef, rib eye steak, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23189: [], # Beef, rib eye roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    23190: [], # Beef, rib eye roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    23191: [], # Beef, rib eye roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    23192: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23193: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23194: [], # Beef, rib eye steak/roast, bone-in, lip-on, separable lean and fat, trimmed to 1/8" fat, select, raw
    23195: [], # Beef, rib eye steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    23196: [], # Beef, rib eye steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23197: [], # Beef, rib eye steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23198: [], # Beef, rib eye roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    23199: [], # Beef, rib eye roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    23200: [], # Beef, rib eye roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    23201: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23202: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23213: [], # Beef, rib eye steak/roast, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, select, raw
    23214: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23215: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23216: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23217: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, all grades, raw
    23218: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, choice, raw
    23219: [], # Beef, plate steak, boneless, inside skirt, separable lean and fat, trimmed to 0" fat, select, raw
    23220: [], # Beef, ground, unspecified fat content, cooked
    23221: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23222: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23223: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23224: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, all grades, raw
    23225: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, choice, raw
    23226: [], # Beef, plate steak, boneless, outside skirt, separable lean and fat, trimmed to 0" fat, select, raw
    23227: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23228: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23229: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23230: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, all grades, raw
    23231: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, choice, raw
    23232: [], # Beef, rib eye steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, select, raw
    23233: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, all grades, cooked, braised
    23234: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, choice, cooked, braised
    23235: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, select, cooked, braised
    23236: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, all grades, raw
    23237: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, choice, raw
    23238: [], # Beef, rib, back ribs, bone-in, separable lean and fat, trimmed to 0" fat, select, raw
    23239: [], # Beef, loin, top sirloin petite roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    23240: [], # Beef, loin, top sirloin petite roast/filet, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23241: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    23242: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    23243: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23244: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, all grades, raw
    23245: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, choice, raw
    23246: [], # Beef, loin, top sirloin cap steak, boneless, separable lean only, trimmed to 1/8" fat, select, raw
    23247: [], # Beef, top loin filet, boneless, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    23248: [], # Beef, top loin filet, boneless, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    23249: [], # Beef, top loin filet, boneless, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23250: [], # Beef, top loin petite roast, boneless, separable lean only, trimmed to 1/8" fat, all grades, cooked, roasted
    23251: [], # Beef, top loin petite roast, boneless, separable lean only, trimmed to 1/8" fat, choice, cooked, roasted
    23252: [], # Beef, top loin petite roast, boneless, separable lean only, trimmed to 1/8" fat, select, cooked, roasted
    23253: [], # Beef, top loin petite roast/filet, boneless, separable lean only, trimmed to 1/8" fat, all grades, raw
    23254: [], # Beef, top loin petite roast/filet, boneless, separable lean only, trimmed to 1/8" fat, choice, raw
    23255: [], # Beef, top loin petite roast/filet, boneless, separable lean only, trimmed to 1/8" fat, select, raw
    23256: [], # Beef, loin, top sirloin filet, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23257: [], # Beef, loin, top sirloin filet, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23258: [], # Beef, loin, top sirloin filet, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23259: [], # Beef, loin, top sirloin petite roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    23260: [], # Beef, loin, top sirloin petite roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, roasted
    23261: [], # Beef, loin, top sirloin petite roast/filet, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23262: [], # Beef, loin, top sirloin petite roast/filet, boneless, separable lean only, trimmed to 0" fat, select, raw
    23263: [], # Beef, ribeye  petite roast/filet, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23264: [], # Beef, ribeye  petite roast/filet, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23265: [], # Beef, ribeye  petite roast/filet, boneless, separable lean only, trimmed to 0" fat, select, raw
    23266: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23267: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23268: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23269: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23270: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23271: [], # Beef, ribeye cap steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23272: [], # Beef, ribeye filet, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23273: [], # Beef, ribeye filet, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23274: [], # Beef, ribeye filet, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23275: [], # Beef, ribeye petite roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    23276: [], # Beef, ribeye petite roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    23277: [], # Beef, ribeye petite roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, roasted
    23278: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23279: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    23280: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23281: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23282: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23283: [], # Beef, loin, top sirloin cap steak, boneless, separable lean and fat, trimmed to 1/8" fat, select, raw
    23284: [], # Beef, top loin filet, boneless, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23285: [], # Beef, top loin filet, boneless, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    23286: [], # Beef, top loin filet, boneless, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23287: [], # Beef, top loin petite roast, boneless, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, roasted
    23288: [], # Beef, top loin petite roast, boneless, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted
    23289: [], # Beef, top loin petite roast, boneless, separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted
    23290: [], # Beef, top loin petite roast/filet, boneless, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23291: [], # Beef, top loin petite roast/filet, boneless, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23292: [], # Beef, top loin petite roast/filet, boneless, separable lean and fat, trimmed to 1/8" fat, select, raw
    23293: [], # Beef, Australian, imported, grass-fed, ground, 85% lean / 15% fat, raw
    23294: [], # Beef, Australian, imported, grass-fed, loin, tenderloin steak/roast, boneless, separable lean only, raw
    23295: [], # Beef, Australian, imported, Wagyu, loin, tenderloin steak/roast, boneless, separable lean only, Aust. marble score 4/5, raw
    23296: [], # Beef, Australian, imported, grass-fed,  external fat, raw
    23297: [], # Beef, Australian, imported, grass-fed, seam fat, raw
    23298: [], # Beef, Australian, imported, Wagyu, external fat, Aust. marble score 4/5, raw
    23299: [], # Beef, Australian, imported, Wagyu, seam fat, Aust. marble score 4/5, raw
    23300: [], # Beef, Australian, imported, Wagyu, external fat, Aust. marble score 9, raw
    23301: [], # Beef, Australian, imported, Wagyu, seam fat, Aust. marble score 9, raw
    23302: [], # Beef, Australian, imported, grass-fed, loin, tenderloin steak/roast, boneless, separable lean and fat, raw
    23303: [], # Beef, Australian, imported, grass-fed, loin, top loin steak/roast, boneless, separable lean only, raw
    23304: [], # Beef, Australian, imported, Wagyu, loin, tenderloin steak/roast, boneless, separable lean and fat, Aust. marble score 4/5, raw
    23305: [], # Beef, Australian, imported, grass-fed, loin, top loin steak/roast, boneless, separable lean and fat, raw
    23306: [], # Beef, Australian, imported, grass-fed, loin, top sirloin cap-off steak/roast, boneless, separable lean only, raw
    23307: [], # Beef, Australian, imported, grass-fed, rib, ribeye steak/roast lip-on, boneless, separable lean only, raw
    23308: [], # Beef, Australian, imported, grass-fed, round, bottom round steak/roast, boneless, separable lean only, raw
    23309: [], # Beef, Australian, imported, grass-fed, round, top round cap-off steak/roast, boneless, separable lean only, raw
    23310: [], # Beef, Australian, imported, Wagyu, loin, tenderloin steak/roast, boneless, separable lean only, Aust. marble score 9, raw
    23311: [], # Beef, Australian, imported, Wagyu, loin, top loin steak/roast, boneless, separable lean only, Aust. marble score 4/5, raw
    23312: [], # Beef, Australian, imported, Wagyu, loin, top loin steak/roast, boneless, separable lean only, Aust. marble score 9, raw
    23313: [], # Beef, Australian, imported, Wagyu, rib, small end rib steak/roast, boneless, separable lean only, Aust. marble score 4/5, raw
    23314: [], # Beef, Australian, imported, Wagyu, rib, small end rib steak/roast, boneless, separable lean only, Aust. marble score 9, raw
    23315: [], # Beef, Australian, imported, grass-fed, loin, top sirloin cap-off steak/roast, boneless, separable lean and fat, raw
    23316: [], # Beef, Australian, imported, grass-fed, rib, ribeye steak/roast lip-on, boneless, separable lean and fat, raw
    23317: [], # Beef, Australian, imported, grass-fed, round, bottom round steak/roast, boneless, separable lean and fat, raw
    23318: [], # Beef, Australian, imported, grass-fed, round, top round cap-off steak/roast, boneless, separable lean and fat, raw
    23319: [], # Beef, Australian, imported, Wagyu, loin, top loin steak/roast, boneless, separable lean and fat, Aust. marble score 4/5, raw
    23320: [], # Beef, Australian, imported, Wagyu, loin, top loin steak/roast, separable lean and fat, Aust. marble score 9, raw
    23321: [], # Beef, Australian, imported, Wagyu, rib, small end rib steak/roast, boneless, separable lean and fat, Aust. marble score 4/5, raw
    23322: [], # Beef, Australian, imported, Wagyu, rib, small end rib steak/roast, boneless, separable lean and fat, Aust. marble score 9, raw
    23323: [], # Beef, Australian, imported, Wagyu, loin, tenderloin steak/roast, boneless, separable lean and fat, Aust. marble score 9, raw
    23324: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23325: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23326: [], # Beef, round, top round steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23327: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23328: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23329: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23330: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23331: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23332: [], # Beef, round, eye of round roast, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23333: [], # Beef, round, eye of round steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23334: [], # Beef, round, eye of round steak, boneless separable lean and fat, trimmed to 0" fat, choice, raw
    23335: [], # Beef, round, eye of round steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23336: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23337: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23338: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23339: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, all grades, raw
    23340: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, choice, raw
    23341: [], # Beef, loin, top loin steak, boneless, lip off, separable lean and fat, trimmed to 0" fat, select, raw
    23342: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, raw
    23343: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, choice, raw
    23344: [], # Beef, loin, tenderloin steak, boneless, separable lean and fat, trimmed to 0" fat, select, raw
    23345: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    23346: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    23347: [], # Beef, loin, tenderloin roast, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    23348: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    23349: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    23350: [], # Beef, round, top round roast, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    23351: [], # Beef, round, eye of round steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23352: [], # Beef, round, eye of round steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23353: [], # Beef, round, eye of round steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23354: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23355: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23356: [], # Beef, round, top round steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23357: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23358: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23359: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, select, raw
    23360: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23361: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23362: [], # Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0" fat, select, raw
    23363: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23364: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23365: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23366: [], # Beef, loin, tenderloin roast, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23367: [], # Beef, loin, tenderloin roast, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23368: [], # Beef, loin, tenderloin roast, boneless, separable lean only, trimmed to 0" fat, select, raw
    23369: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, all grades, raw
    23370: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, choice, raw
    23371: [], # Beef, loin, top loin steak, boneless, lip off, separable lean only, trimmed to 0" fat, select, raw
    23372: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, all grades, raw
    23373: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, choice, raw
    23374: [], # Beef, loin, tenderloin steak, boneless, separable lean only, trimmed to 0" fat, select, raw
    23375: [], # Beef, loin, tenderloin roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    23376: [], # Beef, loin, tenderloin roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    23377: [], # Beef, loin, tenderloin roast, separable lean only, boneless, trimmed to 0" fat, select, cooked, roasted
    23378: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    23379: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    23380: [], # Beef, round, top round roast, boneless, separable lean only, trimmed to 0" fat, select, cooked, roasted
    23381: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23382: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, choice, cooked, grilled
    23383: [], # Beef, round, eye of round steak, boneless, separable lean only, trimmed to 0" fat, select, cooked, grilled
    23384: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, select, raw
    23385: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, choice, raw
    23386: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, all grades, raw
    23387: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, select, raw
    23388: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, raw
    23389: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, cooked, grilled
    23390: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, select, cooked, grilled
    23391: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, all grades, cooked, grilled
    23392: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, choice, cooked, grilled
    23393: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23394: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8" fat, all grades, cooked, grilled
    23395: [], # Beef, loin, top loin steak, boneless, lip-on, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23397: [], # Beef, New Zealand, imported, bolar blade, separable lean only, cooked, fast roasted
    23398: [], # Beef, New Zealand, imported, bolar blade, separable lean only, raw
    23399: [], # Beef, New Zealand, imported, brisket navel end, separable lean only, cooked, braised
    23401: [], # Beef, New Zealand, imported, brisket navel end, separable lean only, raw
    23402: [], # Beef, New Zealand, imported, brisket point end, separable lean only, cooked, braised
    23403: [], # Beef, New Zealand, imported, brisket point end, separable lean only, raw
    23404: [], # Beef, New Zealand, imported, chuck eye roll, separable lean only, raw
    23405: [], # Beef, New Zealand, imported, chuck eye roll, separable lean only, cooked, braised
    23406: [], # Beef, New Zealand, imported, cube roll, separable lean only, cooked, fast roasted
    23407: [], # Beef, New Zealand, imported, cube roll, separable lean only, raw
    23408: [], # Beef, New Zealand, imported, eye round, separable lean only, cooked, slow roasted
    23409: [], # Beef, New Zealand, imported, eye round, separable lean only, raw
    23410: [], # Beef, New Zealand, imported, flank, separable lean only, cooked, braised
    23411: [], # Beef, New Zealand, imported, flank, separable lean only, raw
    23412: [], # Beef, New Zealand, imported, flat, separable lean only, cooked, braised
    23413: [], # Beef, New Zealand, imported, flat, separable lean only, raw
    23414: [], # Beef, New Zealand, imported, variety meats and by-products, heart, cooked, boiled
    23415: [], # Beef, New Zealand, imported, variety meats and by-products, heart, raw
    23416: [], # Beef, New Zealand, imported, hind shin, separable lean only, cooked, braised
    23417: [], # Beef, New Zealand, imported, hind shin, separable lean only, raw
    23418: [], # Beef, New Zealand, imported, inside, raw
    23419: [], # Beef, New Zealand, imported, intermuscular fat, cooked
    23420: [], # Beef, New Zealand, imported, intermuscular fat, raw
    23421: [], # Beef, New Zealand, imported, variety meats and by-products, kidney, cooked, boiled
    23422: [], # Beef, New Zealand, imported, knuckle, cooked, fast fried
    23423: [], # Beef, New Zealand, imported, variety meats and by-products, kidney, raw
    23424: [], # Beef, New Zealand, imported, variety meats and by-products liver, cooked, boiled
    23425: [], # Beef, New Zealand, imported, variety meats and by-products, liver, raw
    23426: [], # Beef, New Zealand, imported, manufacturing beef, cooked, boiled
    23427: [], # Beef, New Zealand, imported, manufacturing beef, raw
    23428: [], # Beef, New Zealand, imported, oyster blade, separable lean only, cooked, braised
    23429: [], # Beef, New Zealand, imported, oyster blade, separable lean only, raw
    23430: [], # Beef, New Zealand, imported, ribs prepared, cooked, fast roasted
    23431: [], # Beef, New Zealand, imported, ribs prepared, raw
    23432: [], # Beef, New Zealand, imported, rump centre, separable lean only, cooked, fast fried
    23433: [], # Beef, New Zealand, imported, striploin, separable lean only, cooked, fast fried
    23434: [], # Beef, New Zealand, imported, striploin, separable lean only, raw
    23435: [], # Beef, New Zealand, imported, subcutaneous fat, cooked
    23436: [], # Beef, New Zealand, imported, subcutaneous fat, raw
    23437: [], # Beef, New Zealand, imported, sweetbread, cooked, boiled
    23438: [], # Beef, New Zealand, imported, sweetbread, raw
    23439: [], # Beef, New Zealand, imported, tenderloin, separable lean only, cooked, fast fried
    23440: [], # Beef, New Zealand, imported, oyster blade, separable lean and fat, raw
    23441: [], # Beef, New Zealand, imported, tenderloin, separable lean only, raw
    23442: [], # Beef, New Zealand, imported, variety meats and by-products, tongue, cooked, boiled
    23443: [], # Beef, New Zealand, imported, variety meats and by-products, tongue, raw
    23444: [], # Beef, New Zealand, imported, variety meats and by-products, tripe cooked, boiled
    23445: [], # Beef, New Zealand, imported, variety meats and by-products, tripe uncooked, raw
    23446: [], # Beef, New Zealand, imported, bolar blade, separable lean and fat, cooked, fast roasted
    23447: [], # Beef, New Zealand, imported, bolar blade, separable lean and fat, raw
    23448: [], # Beef, New Zealand, imported, brisket navel end, separable lean and fat, cooked, braised
    23449: [], # Beef, New Zealand, imported, brisket navel end, separable lean and fat, raw
    23450: [], # Beef, New Zealand, imported, brisket point end, separable lean and fat, cooked, braised
    23451: [], # Beef, New Zealand, imported, brisket point end, separable lean and fat, raw
    23452: [], # Beef, New Zealand, imported, chuck eye roll, separable lean and fat, cooked, braised
    23453: [], # Beef, New Zealand, imported, chuck eye roll, separable lean and fat, raw
    23454: [], # Beef, New Zealand, imported, cube roll, separable lean and fat, cooked, fast roasted
    23455: [], # Beef, New Zealand, imported, cube roll, separable lean and fat, raw
    23456: [], # Beef, New Zealand, imported, eye round, separable lean and fat, cooked, slow roasted
    23457: [], # Beef, New Zealand, imported, eye round, separable lean and fat, raw
    23458: [], # Beef, New Zealand, imported, flank, separable lean and fat, cooked, braised
    23459: [], # Beef, New Zealand, imported, flank, separable lean and fat, raw
    23460: [], # Beef, New Zealand, imported, flat, separable lean and fat, cooked, braised
    23461: [], # Beef, New Zealand, imported, flat, separable lean and fat, raw
    23462: [], # Beef, New Zealand, imported, hind shin, separable lean and fat, cooked, braised
    23463: [], # Beef, New Zealand, imported, hind shin, separable lean and fat, raw
    23464: [], # Beef, New Zealand, imported, oyster blade, separable lean and fat, cooked, braised
    23465: [], # Beef, New Zealand, imported, rump centre, separable lean and fat, cooked, fast fried
    23466: [], # Beef, New Zealand, imported, rump centre, separable lean only, raw
    23467: [], # Beef, New Zealand, imported, rump centre, separable lean and fat, raw
    23468: [], # Beef, New Zealand, imported, striploin, separable lean and fat, cooked, fast fried
    23469: [], # Beef, New Zealand, imported, striploin, separable lean and fat, raw
    23470: [], # Beef, New Zealand, imported, tenderloin, separable lean and fat, cooked, fast fried
    23471: [], # Beef, New Zealand, imported, tenderloin, separable lean and fat, raw
    23472: [], # Beef, ground, 93% lean meat / 7% fat, raw
    23473: [], # Beef, ground, 93% lean meat / 7% fat, patty, cooked, broiled
    23474: [], # Beef, ground, 93% lean meat /7% fat, patty, cooked, pan-broiled
    23475: [], # Beef, ground, 93% lean meat / 7% fat, loaf, cooked, baked
    23476: [], # Beef, ground, 93% lean meat / 7% fat, crumbles, cooked, pan-browned
    23477: [], # Beef, ground, 97% lean meat / 3% fat, raw
    23478: [], # Beef, ground, 97% lean meat / 3% fat, patty, cooked, broiled
    23479: [], # Beef, ground, 97% lean meat /3% fat, patty, cooked, pan-broiled
    23480: [], # Beef, ground, 97% lean meat / 3% fat, loaf, cooked, baked
    23481: [], # Beef, ground, 97% lean meat / 3% fat, crumbles, cooked, pan-browned
    23482: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, all grades, raw
    23483: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, all grades, raw
    23484: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, all grades, cooked
    23485: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, all grades, raw
    23490: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, choice, raw
    23491: [], # Beef composite, separable lean only, trimmed to 1/8" fat, choice, cooked
    23494: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, choice, raw
    23495: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, choice, raw
    23496: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 0" fat, select, raw
    23497: [], # Beef, composite of trimmed retail cuts, separable lean and fat, trimmed to 0" fat, select, raw
    23498: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, select, cooked
    23499: [], # Beef, composite of trimmed retail cuts, separable lean only, trimmed to 1/8" fat, select, raw
    23509: [], # Beef, chuck, mock tender steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    23511: [], # Beef, chuck, top blade, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    23513: [], # Beef, chuck, clod roast, separable lean only, trimmed to 1/4" fat, all grades, raw
    23514: [], # Beef, chuck, clod roast, separable lean only, trimmed to 0" fat, all grades, cooked, roasted
    23515: [], # Beef, chuck, clod roast, separable lean only, trimmed to 1/4" fat, all grades, cooked, roasted
    23516: [], # Beef, shoulder steak, boneless, separable lean only, trimmed to 0" fat, all grades, cooked, grilled
    23517: [], # Beef, chuck, clod steak, separable lean only, trimmed to 1/4" fat, all grades, cooked, braised
    23519: [], # Beef, chuck, mock tender steak, separable lean and fat, trimmed to 0" fat, USDA choice, cooked, broiled
    23521: [], # Beef, chuck, mock tender steak, separable lean and fat, trimmed to 0" fat, USDA select, cooked, broiled
    23523: [], # Beef, chuck, top blade, separable lean and fat, trimmed to 0" fat, choice, cooked, broiled
    23525: [], # Beef, chuck, top blade, separable lean and fat, trimmed to 0" fat, select, cooked, broiled
    23528: [], # Beef, chuck, clod roast, separable lean and fat, trimmed to 0" fat, choice, cooked, roasted
    23531: [], # Beef, chuck, clod roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted
    23533: [], # Beef, shoulder steak, boneless, separable lean and fat, trimmed to 0" fat, choice, cooked, grilled
    23536: [], # Beef, shoulder steak, boneless, separable lean and fat, trimmed to 0" fat, select, cooked, grilled
    23540: [], # Beef, plate, inside skirt steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    23541: [], # Beef, plate, outside skirt steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    23545: [], # Beef, loin, bottom sirloin butt, tri-tip steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    23547: [], # Beef, chuck, mock tender steak, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    23549: [], # Beef, chuck, top blade, separable lean and fat, trimmed to 0" fat, all grades, cooked, broiled
    23552: [], # Beef, chuck, clod roast, separable lean and fat, trimmed to 0" fat, all grades, cooked, roasted
    23554: [], # Beef, shoulder steak, boneless, separable lean and fat, trimmed to 0" fat, all grades, cooked, grilled
    23557: [], # Beef, ground, 95% lean meat / 5% fat, raw
    23558: [], # Beef, ground, 95% lean meat / 5% fat, patty, cooked, broiled
    23559: [], # Beef, ground, 95% lean meat / 5% fat, patty, cooked, pan-broiled
    23560: [], # Beef, ground, 95% lean meat / 5% fat, crumbles, cooked, pan-browned
    23561: [], # Beef, ground, 95% lean meat / 5% fat, loaf, cooked, baked
    23562: [], # Beef, ground, 90% lean meat / 10% fat, raw
    23563: [], # Beef, ground, 90% lean meat / 10% fat, patty, cooked, broiled
    23564: [], # Beef, ground, 90% lean meat / 10% fat, patty, cooked, pan-broiled
    23565: [], # Beef, ground, 90% lean meat / 10% fat, crumbles, cooked, pan-browned
    23566: [], # Beef, ground, 90% lean meat / 10% fat, loaf, cooked, baked
    23567: [], # Beef, ground, 85% lean meat / 15% fat, raw (Includes foods for USDA's Food Distribution Program)
    23568: [], # Beef, ground, 85% lean meat / 15% fat, patty, cooked, broiled
    23569: [], # Beef, ground, 85% lean meat / 15% fat, patty, cooked, pan-broiled
    23570: [], # Beef, ground, 85% lean meat / 15% fat, crumbles, cooked, pan-browned
    23571: [], # Beef, ground, 85% lean meat / 15% fat, loaf, cooked, baked
    23572: [], # Beef, ground, 80% lean meat / 20% fat, raw
    23573: [], # Beef, ground, 80% lean meat / 20% fat, patty, cooked, broiled
    23574: [], # Beef, ground, 80% lean meat / 20% fat, patty, cooked, pan-broiled
    23575: [], # Beef, ground, 80% lean meat / 20% fat, crumbles, cooked, pan-browned
    23576: [], # Beef, ground, 80% lean meat / 20% fat, loaf, cooked, baked
    23577: [], # Beef, ground, 75% lean meat / 25% fat, raw
    23578: [], # Beef, ground, 75% lean meat / 25% fat, patty, cooked, broiled
    23579: [], # Beef, ground, 75% lean meat / 25% fat, patty, cooked, pan-broiled
    23580: [], # Beef, ground, 75% lean meat / 25% fat, crumbles, cooked, pan-browned
    23581: [], # Beef, ground, 75% lean meat / 25% fat, loaf, cooked, baked
    23582: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, select, raw
    23583: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, select, raw
    23584: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, select, raw
    23585: [], # Beef, short loin, top loin, steak, separable lean only, trimmed to 1/8" fat, select, raw
    23586: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, select, cooked, broiled
    23587: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, select, cooked, broiled
    23588: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, select, cooked, broiled
    23589: [], # Beef, short loin, top loin, steak, separable lean only, trimmed to 1/8" fat, select, cooked, grilled
    23590: [], # Beef, round, bottom round , roast, separable lean only, trimmed to 1/8" fat, select, cooked, roasted
    23591: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, select, cooked, roasted
    23592: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, select, cooked, broiled
    23593: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 1/8" fat, select, cooked, braised
    23594: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, all grades, raw
    23595: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, all grades, cooked, braised
    23596: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, all grades, raw
    23597: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, all grades, raw
    23598: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, all grades, cooked, roasted
    23599: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, all grades, raw
    23600: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, all grades, cooked, broiled
    23601: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, all grades, raw
    23602: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, all grades, cooked, braised
    23603: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, all grades, raw
    23604: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, all grades, cooked
    23605: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 1/8" fat, all grades, cooked, braised
    23606: [], # Beef, short loin, top loin, steak, separable lean only, trimmed to 1/8" fat, all grades, cooked, broiled
    23607: [], # Beef, short loin, top loin steak, separable lean only, trimmed to 1/8" fat, all grades, raw
    23608: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, all grades, cooked, broiled
    23609: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, all grades, raw
    23610: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, all grades, cooked, broiled
    23611: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, all grades, raw
    23612: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, choice, raw
    23613: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, choice, raw
    23614: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, choice, cooked, braised
    23615: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, choice, cooked, braised
    23616: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, choice, raw
    23617: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, choice, raw
    23618: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, choice, raw
    23619: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, choice, cooked, roasted
    23620: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, choice, cooked, roasted
    23621: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, choice, cooked, broiled
    23622: [], # Beef, round, bottom round, steak, separable lean only, trimmed to 1/8" fat, choice, cooked, braised
    23623: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, choice, raw
    23624: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, choice, raw
    23625: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, choice, raw
    23626: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8"fat, choice, cooked, broiled
    23627: [], # Beef, short loin, top loin, steak, separable lean only, trimmed to 1/8" fat, choice, raw
    23628: [], # Beef, tenderloin, steak, separable lean only, trimmed to 1/8" fat, choice, cooked, broiled
    23629: [], # Beef, top sirloin, steak, separable lean only, trimmed to 1/8" fat, choice, cooked, broiled
    23630: [], # Beef, short loin, top loin, steak, separable lean only, trimmed to 1/8" fat, choice, cooked, broiled
    23631: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, select, raw
    23632: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, select, raw
    23633: [], # Beef, chuck, arm pot roast, separable lean only, trimmed to 1/8" fat, select, cooked, braised
    23634: [], # Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, select, cooked, braised
    23635: [], # Beef, round, eye of round, roast, separable lean only, trimmed to 1/8" fat, select, raw
    23636: [], # Beef, round, top round, steak, separable lean only, trimmed to 1/8" fat, select, raw
    23637: [], # Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, select, raw
    23638: [], # Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, all grades, cooked, broiled
    23640: [], # Beef, variety meats and by-products, tripe, cooked, simmered
    23646: [], # Beef, bottom sirloin, tri-tip roast, separable lean only, trimmed to 0" fat, all grades, raw
    23647: [], # Beef, bottom sirloin, tri-tip roast, separable lean only, trimmed to 0" fat, choice, cooked, roasted
    23648: [], # Beef, bottom sirloin, tri-tip roast, separable lean only, trimmed to 0" fat, choice, raw
    23649: [], # Beef, bottom sirloin, tri-tip roast, separable lean only, trimmed to 0" fat, select, cooked, roasted
    23650: [], # Beef, bottom sirloin, tri-tip roast, separable lean only, trimmed to 0" fat, select, raw
    23651: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, all grades, raw
    23652: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, choice, raw
    23653: [], # Beef, round, tip round, roast, separable lean only, trimmed to 0" fat, select, raw
    23654: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, all grades, cooked, broiled
    23655: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, select, cooked, broiled
    23656: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, all grades, raw
    23657: [], # Beef, flank, steak, separable lean only, trimmed to 0" fat, select, raw
    23658: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, choice, raw
    23659: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, select, raw
    23660: [], # Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, choice, cooked, braised
    25000: [], # Snacks, popcorn, microwave, 94% fat free
    25001: [], # Snacks, popcorn, microwave, low fat
    25003: [], # Snacks, candy rolls, yogurt-covered, fruit flavored with high vitamin C
    25004: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON Chewy Chocolate Peanut Bar
    25005: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON MULTIGRAIN CRUNCH BAR
    25006: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON Double Chocolate Nut Bar
    25007: [], # Snacks, M&M MARS, KUDOS Whole Grain Bars, peanut butter
    25008: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON Honey Nut Oat Bar
    25009: [], # Snacks, M&M MARS, KUDOS Whole Grain Bar, M&M's milk chocolate
    25010: [], # Formulated bar, MARS SNACKFOOD US, COCOAVIA, Chocolate Almond Snack Bar
    25012: [], # Snacks, sweet potato chips, unsalted
    25013: [], # Snacks, FRITOLAY, SUNCHIPS, Multigrain Snack, original flavor
    25014: [], # Snacks, popcorn, microwave, regular (butter) flavor, made with partially hydrogenated oil
    25015: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON Protein Performance Bar, Caramel Nut Rush
    25016: [], # Formulated bar, MARS SNACKFOOD US, SNICKERS MARATHON Energy Bar, all flavors
    25017: [], # Formulated bar, POWER BAR, chocolate
    25018: [], # Formulated bar, MARS SNACKFOOD US, COCOAVIA, Chocolate Blueberry Snack Bar
    25020: [], # Formulated bar, SLIM-FAST OPTIMA meal bar, milk chocolate peanut
    25021: [], # Formulated bar, LUNA BAR, NUTZ OVER CHOCOLATE
    25022: [], # Snacks, FRITOLAY, SUNCHIPS, multigrain, French onion flavor
    25023: [], # Snacks, FRITOLAY, SUNCHIPS, Multigrain Snack, Harvest Cheddar flavor
    25024: [], # Pretzels, soft, unsalted
    25025: [], # Snacks, soy chips or crisps, salted
    25026: [], # Popcorn, microwave, regular (butter) flavor, made with palm oil
    25027: [], # Snacks, plantain chips, salted
    25028: [], # Tortilla chips, yellow, plain, salted
    25030: [], # Snacks, vegetable chips, HAIN CELESTIAL GROUP, TERRA CHIPS
    25031: [], # Formulated bar, ZONE PERFECT CLASSIC CRUNCH BAR, mixed flavors
    25032: [], # Snacks, granola bar, KASHI GOLEAN, chewy, mixed flavors
    25033: [], # Snacks, granola bar, KASHI TLC Bar, chewy, mixed flavors
    25034: [], # Snacks, granola bar, KASHI GOLEAN, crunchy, mixed flavors
    25035: [], # Snacks, granola bar, chewy, reduced sugar, all flavors
    25036: [], # Snacks, granola bites, mixed flavors
    25037: [], # Snacks, pita chips, salted
    25038: [], # Snacks, granola bars, soft, almond, confectioners coating
    25039: [], # Snacks, granola bars, QUAKER OATMEAL TO GO, all flavors
    25040: [], # Snacks, vegetable chips, made from garden vegetables
    25041: [], # Snacks, granola bar, KASHI TLC Bar, crunchy, mixed flavors
    25043: [], # Snacks, candy bits, yogurt covered with vitamin C
    25045: [], # Formulated bar, high fiber, chewy, oats and chocolate
    25046: [], # Snacks, bagel chips, plain
    25048: [], # Snacks, NUTRI-GRAIN FRUIT AND NUT BAR
    25050: [], # Snacks, yucca (cassava) chips, salted
    25051: [], # Snacks, CLIF BAR, mixed flavors
    25052: [], # Snacks, granola bar, QUAKER, chewy, 90 Calorie Bar
    25053: [], # Snacks, granola bar, GENERAL MILLS NATURE VALLEY, SWEET&SALTY NUT, peanut
    25054: [], # Snacks, granola bar, GENERAL MILLS, NATURE VALLEY, with yogurt coating
    25055: [], # Snacks, granola bar, GENERAL MILLS, NATURE VALLEY, CHEWY TRAIL MIX
    25056: [], # Snacks, granola bar, QUAKER, DIPPS, all flavors
    25059: [], # Snacks, brown rice chips
    25060: [], # Snack, Pretzel, hard chocolate coated
    25062: [], # Snack, Mixed Berry Bar
    25063: [], # Snacks, potato chips, made from dried potatoes (preformed), multigrain
    25064: [], # Snacks, potato chips, lightly salted
    25065: [], # Snacks, Pretzels, gluten- free made with cornstarch and potato flour
    25066: [], # Snacks, peas, roasted, wasabi-flavored
    25067: [], # Formulated Bar, SOUTH BEACH protein bar
    25068: [], # Snack, BALANCE, original bar
    25070: [], # Snacks, shrimp cracker
    25071: [], # Rice crackers
    27000: [], # Soup, egg drop, Chinese restaurant
    27001: [], # Soup, hot and sour, Chinese restaurant
    27002: [], # Soup, wonton, Chinese restaurant
    27035: [], # Soup, ramen noodle, dry, any flavor, reduced fat, reduced sodium
    27042: [], # Soup, clam chowder, new england, canned, ready-to-serve
    27043: [], # Soup, clam chowder, new england, reduced sodium, canned, ready-to-serve
    27044: [], # Soup, chicken noodle, reduced sodium, canned, ready-to-serve
    27045: [], # Soup, beef and vegetables, reduced sodium, canned, ready-to-serve
    27046: [], # Sauce, duck, ready-to-serve
    27047: [], # Sauce, salsa, verde, ready-to-serve
    27048: [], # Sauce, steak, tomato based
    27049: [], # Sauce, tartar, ready-to-serve
    27050: [], # Sauce, sweet and sour, ready-to-serve
    27051: [], # Sauce, cocktail, ready-to-serve
    27052: [], # Dip, salsa con queso, cheese and salsa- medium
    27054: [], # Dip, TOSTITOS, salsa con queso, medium
    27055: [], # Sauce, barbecue, SWEET BABY RAY'S, original
    27056: [], # Sauce, barbecue, BULL'S-EYE, original
    27057: [], # Sauce, barbecue, KC MASTERPIECE, original
    27058: [], # Sauce, barbecue, OPEN PIT, original
    27059: [], # Sauce, peanut, made from peanut butter, water, soy sauce
    27060: [], # Soup, chunky vegetable, reduced sodium, canned, ready-to-serve
    27061: [], # Gravy, HEINZ Home Style, classic chicken
    27062: [], # Soup, beef barley, ready to serve
    27063: [], # Sauce, enchilada, red, mild, ready to serve
    27064: [], # Wasabi
    27065: [], # Dip, bean, original flavor
    27066: [], # Sauce, horseradish
    27068: [], # Dip, FRITO'S, bean, original flavor
    28285: [], # Bread, chapati or roti, whole wheat, commercially prepared, frozen
    28286: [], # Bread, paratha, whole wheat, commercially prepared, frozen
    28287: [], # Bread, naan, whole wheat, commercially prepared, refrigerated
    28288: [], # Bread, roll, Mexican, bollilo
    28289: [], # Cookie, vanilla with caramel, coconut, and chocolate coating
    28290: [], # Cookie, with peanut butter filling, chocolate-coated
    28291: [], # Cookies, animal, with frosting or icing
    28292: [], # Crackers, multigrain
    28293: [], # Cookie, butter or sugar, with chocolate icing or filling
    28294: [], # Cookie, chocolate, with icing or coating
    28295: [], # Tortillas, ready-to-bake or -fry, whole wheat
    28296: [], # Cake, snack cakes, creme-filled, chocolate with frosting, low-fat, with added fiber
    28297: [], # Cake, snack cakes, not chocolate, with icing or filling, low-fat, with added fiber
    28298: [], # Cookies, brownies, commercially prepared, reduced fat, with added fiber
    28299: [], # Cookies, chocolate sandwich, with creme filling, reduced fat
    28300: [], # Cookies, oatmeal sandwich, with creme filling
    28301: [], # Cookies, peanut butter, commercially prepared, sugar free
    28302: [], # Cookies, graham crackers, plain or honey, lowfat
    28303: [], # Crackers, cheese, whole grain
    28304: [], # Waffles, whole wheat, lowfat, frozen, ready-to-heat
    28305: [], # Pancakes, plain, reduced fat
    28306: [], # Bread, chapati or roti, plain, commercially prepared
    28307: [], # Bread, naan, plain, commercially prepared, refrigerated
    28308: [], # Crackers, standard snack-type, with whole wheat
    28309: [], # Cookies, coconut macaroon
    28310: [], # Cookies, shortbread, reduced fat
    28311: [], # Cookies, sugar wafer, chocolate-covered
    28312: [], # Rolls, hamburger or hot dog, wheat/cracked wheat
    28313: [], # Rolls, hamburger or hot dog, whole wheat
    28314: [], # Crackers, sandwich-type, peanut butter filled, reduced fat
    28315: [], # Bread, cinnamon
    28316: [], # Bread, wheat, sprouted
    28317: [], # Bread, wheat, sprouted, toasted
    28318: [], # Bread, french or vienna, whole wheat
    28319: [], # Bagels, whole grain white
    28320: [], # English muffins, whole grain white
    28321: [], # Rolls, hamburger, whole grain white, calcium-fortified
    28322: [], # Bagels, multigrain
    28324: [], # Pancakes, whole wheat, dry mix, incomplete
    28325: [], # Crackers, toast thins, low sodium
    28326: [], # Crackers, whole grain, sandwich-type, with peanut butter filling
    28327: [], # Crackers, water biscuits
    28328: [], # Cookies, chocolate chip sandwich, with creme filling
    28329: [], # Cookies, chocolate, made with rice cereal
    28330: [], # Cookies, marshmallow, with rice cereal and chocolate chips
    28331: [], # Crackers, flavored, fish-shaped
    28332: [], # Cookies, gluten-free, chocolate sandwich, with creme filling
    28333: [], # Cookies, gluten-free, chocolate wafer
    28334: [], # Cookies, gluten-free, lemon wafer
    28335: [], # Cookies, gluten-free, vanilla sandwich, with creme filling
    28336: [], # Bread, gluten-free, white, made with potato extract, rice starch, and rice flour
    28337: [], # Bread, gluten-free, white, made with rice flour, corn starch, and/or tapioca
    28338: [], # Bread, gluten-free, white, made with tapioca starch and brown rice flour
    28339: [], # Bread, gluten-free, whole grain, made with tapioca starch and brown rice flour
    28340: [], # Rolls, gluten-free, white, made with brown rice flour, tapioca starch, and potato starch
    28341: [], # Rolls, gluten-free, white, made with rice flour, rice starch, and corn starch
    28342: [], # Rolls, gluten-free, white, made with brown rice flour, tapioca starch, and sorghum flour
    28343: [], # Rolls, gluten-free, whole grain, made with tapioca starch and brown rice flour
    28344: [], # Crackers, gluten-free, multigrain and vegetable, made with corn starch and white rice flour
    28345: [], # Crackers, gluten-free, multi-seeded and multigrain
    28346: [], # Waffles, gluten-free, frozen, ready-to-heat
    28347: [], # Pancakes, gluten-free, frozen, ready-to-heat
    28348: [], # Rolls, dinner, sweet
    28349: [], # Cookies, oatmeal, reduced fat
    28350: [], # Cookies, chocolate cream covered biscuit sticks
    28351: [], # Cookies, Marie biscuit
    28352: [], # Cookies, vanilla sandwich with creme filling, reduced fat
    28354: [], # Andrea's, Gluten Free Soft Dinner Roll
    28355: [], # Crunchmaster, Multi-Grain Crisps, Snack Crackers, Gluten-Free
    28356: [], # Glutino, Gluten Free Cookies, Chocolate Vanilla Creme
    28357: [], # Glutino, Gluten Free Cookies, Vanilla Creme
    28358: [], # Glutino, Gluten Free Wafers, Lemon Flavored
    28359: [], # Glutino, Gluten Free Wafers, Milk Chocolate
    28360: [], # Mary's Gone Crackers, Original Crackers, Organic Gluten Free
    28361: [], # Pepperidge Farm, Goldfish, Baked Snack Crackers, Cheddar
    28362: [], # Pepperidge Farm, Goldfish, Baked Snack Crackers, Explosive Pizza
    28363: [], # Pepperidge Farm, Goldfish, Baked Snack Crackers, Original
    28364: [], # Pepperidge Farm, Goldfish, Baked Snack Crackers, Parmesan
    28365: [], # Pepperidge Farm, Goldfish, Baked Snack Crackers, Pizza
    28366: [], # Rudi's, Gluten-Free Bakery, Original Sandwich Bread
    28367: [], # Sage Valley, Gluten Free Vanilla Sandwich Cookies
    28368: [], # Schar, Gluten-Free, Classic White Rolls
    28369: [], # Schar, Gluten-Free, Wheat-Free, Classic White Bread
    28370: [], # Udi's, Gluten Free, Classic French Dinner Rolls
    28371: [], # Udi's, Gluten Free, Soft & Delicious White Sandwich Bread
    28372: [], # Udi's, Gluten Free, Soft & Hearty Whole Grain Bread
    28373: [], # Udi's, Gluten Free, Whole Grain Dinner Rolls
    28374: [], # Van's, Gluten Free, Totally Original Pancakes
    28375: [], # Van's, Gluten Free, Totally Original Waffles
    28376: [], # Van's, The Perfect 10, Crispy Six Whole Grain + Four Seed Baked Crackers, Gluten Free
    28397: [], # Bread, multi-grain (includes whole-grain)
    28399: [], # Cookies, animal crackers (includes arrowroot, tea biscuits)
    31019: [], # Seaweed, Canadian Cultivated EMI-TSUNOMATA, dry
    31020: [], # Seaweed, Canadian Cultivated EMI-TSUNOMATA, rehydrated
    31021: [], # Potatoes, hash brown, refrigerated, unprepared
    31022: [], # Potatoes, hash brown, refrigerated, prepared, pan-fried in canola oil
    31023: [], # Sweet Potatoes, french fried, frozen as packaged, salt added in processing
    31024: [], # Sweet Potatoes, french fried, crosscut, frozen, unprepared
    31025: [], # Sweet Potato puffs, frozen, unprepared
    31026: [], # Potatoes, yellow fleshed, roasted, salt added in processing, frozen, unprepared
    31027: [], # Potatoes, yellow fleshed, french fried, frozen, unprepared
    31028: [], # Potatoes, yellow fleshed, hash brown, shredded, salt added in processing, frozen, unprepared
    31029: [], # Potatoes, french fried, wedge cut, frozen, unprepared
    31030: [], # Potatoes, french fried, steak cut, salt not added in processing, frozen, unprepared
    31031: [], # Potatoes, french fried, cross cut, frozen, unprepared
    31033: [], # Ginger root, pickled, canned, with artificial sweetener
    31034: [], # Peppers, hot pickled, canned
    31035: [], # Vegetable juice, BOLTHOUSE FARMS, DAILY GREENS
    31036: [], # Potatoes, mashed, ready-to-eat
    32000: [], # Rice and vermicelli mix, beef flavor, unprepared
    32001: [], # Rice and vermicelli mix, beef flavor, prepared with 80% margarine
    32002: [], # Rice and vermicelli mix, rice pilaf flavor, unprepared
    32003: [], # Rice and vermicelli mix, rice pilaf flavor, prepared with 80% margarine
    32004: [], # Macaroni and cheese, box mix with cheese sauce, unprepared
    32005: [], # Macaroni and cheese, box mix with cheese sauce, prepared
    32006: [], # Taquitos, frozen, chicken and cheese, oven-heated
    32007: [], # Taquitos, frozen, beef and cheese, oven-heated
    32008: [], # Pasta mix, classic cheeseburger macaroni, unprepared
    32009: [], # Pasta mix, classic beef, unprepared
    32010: [], # Pasta mix, Italian lasagna, unprepared
    32011: [], # Yellow rice with seasoning, dry packet mix, unprepared
    32012: [], # Pizza rolls, frozen, unprepared
    32013: [], # Potsticker or wonton, pork and vegetable, frozen, unprepared
    32014: [], # Macaroni or noodles with cheese, made from reduced fat packaged mix, unprepared
    32015: [], # Turnover, cheese-filled, tomato-based sauce, frozen, unprepared
    32016: [], # Macaroni or noodles with cheese, microwaveable, unprepared
    32017: [], # Pasta mix, Italian four cheese lasagna, unprepared
    32018: [], # Spanish rice mix, dry mix, unprepared
    32019: [], # Lasagna, cheese, frozen, unprepared
    32020: [], # Chicken, thighs, frozen, breaded, reheated
    32021: [], # Spanish rice mix, dry mix, prepared (with canola/vegetable oil blend or diced tomatoes and margarine)
    32024: [], # Rice mix, cheese flavor, dry mix, unprepared
    32025: [], # Dumpling, potato- or cheese-filled, frozen
    32026: [], # Turnover, chicken- or turkey-, and vegetable-filled, reduced fat, frozen
    32027: [], # Turnover, meat- and cheese-filled, tomato-based sauce, reduced fat, frozen
    32028: [], # Turnover, filled with egg, meat and cheese, frozen
    32029: [], # Rice mix, white and wild, flavored, unprepared
    32031: [], # Salisbury steak with gravy, frozen
    32032: [], # Sausage, egg and cheese breakfast biscuit
    32034: [], # HUNGRY MAN, Salisbury Steak With Gravy, frozen, unprepared
    32035: [], # BANQUET, Salisbury Steak With Gravy, family size, frozen, unprepared
    32036: [], # JIMMY DEAN, Sausage, Egg, and Cheese Breakfast Biscuit, frozen, unprepared
    33862: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Newborn, with ARA and DHA, powder
    33863: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Premium LIPIL, Infant, powder
    33864: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Premium LIPIL, Infant, Liquid concentrate, not reconstituted
    33865: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Premium, Infant, Liquid concentrate, not reconstituted
    33866: [], # Infant formula, MEAD JOHNSON, ENFAMIL, ENFAGROW, GENTLEASE, Toddler transitions, with ARA and DHA, powder
    33867: [], # Infant formula, GERBER, GOOD START, PROTECT PLUS, powder
    33868: [], # Infant Formula, GERBER GOOD START 2, GENTLE PLUS, powder
    33869: [], # Infant formula, GERBER, GOOD START 2, PROTECT PLUS, powder
    33870: [], # Infant formula, MEAD JOHNSON, ENFAMIL, ENFAGROW, Soy, Toddler transitions, with ARA and DHA,  powder
    33871: [], # Infant formula, ABBOTT NUTRITION, SIMILAC, GO AND GROW, powder, with ARA and DHA
    33872: [], # Infant formula, GERBER, GOOD START 2 SOY, with iron, powder
    33873: [], # Infant formula, MEAD JOHNSON, ENFAMIL, NUTRAMIGEN, PurAmino, powder, not reconstituted
    33874: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Premature, 20 calories ready-to-feed Low iron
    33875: [], # Infant formula, MEAD JOHNSON, ENFAMIL, Premature, 24 calories ready-to-feed Low iron
    33876: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Premium, Infant, ready-to-feed
    33877: [], # Infant Formula, MEAD JOHNSON, ENFAMIL, Premium, Infant, powder
    33878: [], # Babyfood, GERBER, Banana with orange medley
    33881: [], # Babyfood, rice cereal, dry, EARTHS BEST ORGANIC WHOLE GRAIN, fortified only with iron
    35001: [], # Agutuk, fish/berry with seal oil (Alaskan ice cream) (Alaska Native)
    35003: [], # Agutuk, meat-caribou (Alaskan ice cream) (Alaska Native)
    35004: [], # Ascidians (tunughnak) (Alaska Native)
    35007: [], # Bear, black, meat (Alaska Native)
    35008: [], # Bear, polar, meat, raw (Alaska Native)
    35009: [], # Whale, beluga, meat, dried (Alaska Native)
    35010: [], # Whale, beluga, eyes (Alaska Native)
    35011: [], # Whale, beluga, meat, raw (Alaska Native)
    35012: [], # Whale, beluga, flipper, raw (Alaska Native)
    35013: [], # Whale, beluga, liver, raw (Alaska Native)
    35014: [], # Oil, beluga, whale (Alaska Native)
    35015: [], # Blackberries, wild, raw (Alaska Native)
    35016: [], # Fish, blackfish, whole (Alaska Native)
    35017: [], # Blueberries, wild, frozen (Alaska Native)
    35021: [], # Caribou, bone marrow, raw (Alaska Native)
    35022: [], # Caribou, eye, raw (Alaska Native)
    35023: [], # Caribou, liver, raw (Alaska Native)
    35024: [], # Stew/soup, caribou (Alaska Native)
    35025: [], # Caribou, tongue, raw (Alaska Native)
    35026: [], # Chiton, leathery, gumboots (Alaska Native)
    35027: [], # Cloudberries, raw (Alaska Native)
    35028: [], # Cockles, raw (Alaska Native)
    35029: [], # Cranberries, wild, bush, raw (Alaska Native)
    35030: [], # Cranberry, low bush or lingenberry, raw (Alaska Native)
    35034: [], # Fish, devilfish, meat (Alaska Native)
    35038: [], # Fireweed, young leaves, raw (Alaska Native)
    35039: [], # Fish, herring eggs on giant kelp, Pacific (Alaska Native)
    35040: [], # Fish, herring eggs, Pacific, dry (Alaska Native)
    35041: [], # Fish, herring eggs, Pacific, plain (Alaska Native)
    35042: [], # Fish, herring, Pacific, flesh, air-dried, packed in oil (Alaska Native)
    35043: [], # Huckleberries, raw (Alaska Native)
    35046: [], # Fish, lingcod, meat, raw (Alaska Native)
    35047: [], # Fish, lingcod, liver (Alaska Native)
    35048: [], # Stew, moose (Alaska Native)
    35049: [], # Moose, meat, raw (Alaska Native)
    35050: [], # Mashu roots, raw (Alaska Native)
    35051: [], # Moose, liver, braised (Alaska Native)
    35052: [], # Mouse nuts, roots (Alaska Native)
    35053: [], # Mouse nuts, seedlings (Alaska Native)
    35054: [], # Octopus (Alaska Native)
    35055: [], # Seal, bearded (Oogruk), meat, dried (Alaska Native)
    35056: [], # Seal, bearded (Oogruk), meat, raw (Alaska Native)
    35057: [], # Oil, bearded seal (Oogruk) (Alaska Native)
    35058: [], # Oopah (tunicate), whole animal (Alaska Native)
    35059: [], # Owl, horned, flesh, raw (Alaska Native)
    35060: [], # Fish, pike, northern, liver (Alaska Native)
    35063: [], # Rhubarb, wild, leaves (Alaska Native)
    35064: [], # Fish, salmon, tipnuk, fermented (Alaska Native)
    35065: [], # Fish, salmon, king, chinook, kippered, canned (Alaska Native)
    35066: [], # Fish, salmon, king, chinook, smoked and canned (Alaska Native)
    35067: [], # Fish, salmon, king, chinook, smoked, brined (Alaska Native)
    35068: [], # Fish, salmon, king, chinook, liver (Alaska Native)
    35069: [], # Duck, scoter, white-winged, meat (Alaska Native)
    35070: [], # Sea cucumber, yane (Alaska Native)
    35071: [], # Seal, ringed, meat (Alaska Native)
    35072: [], # Seal, ringed, liver (Alaska Native)
    35073: [], # Soup, fish, homemade (Alaska Native)
    35074: [], # Sourdock, young leaves (Alaska Native)
    35075: [], # Squirrel, ground, meat (Alaska Native)
    35078: [], # Tea, tundra, herb and laborador combination (Alaska Native)
    35079: [], # Walrus, meat, dried (Alaska Native)
    35080: [], # Deer (venison), sitka, raw (Alaska Native)
    35081: [], # Walrus, meat, raw (Alaska Native)
    35082: [], # Walrus, meat and subcutaneous fat raw (Alaska Native)
    35083: [], # Walrus, liver, raw (Alaska Native)
    35084: [], # Oil, walrus (Alaska Native)
    35085: [], # Whale, bowhead, subcutaneous fat (blubber) (Alaska Native)
    35086: [], # Whale, bowhead, skin and subcutaneous fat (muktuk) (Alaska Native)
    35087: [], # Oil, whale, bowhead (Alaska Native)
    35088: [], # Fish, whitefish, broad, liver (Alaska Native)
    35089: [], # Fish, whitefish, mixed species, raw (Alaska Native)
    35091: [], # Fish, whitefish, broad, head, eyes, cheeks and soft bones (Alaska Native)
    35092: [], # Willow, leaves in oil (Alaska Native)
    35093: [], # Willow, young leaves, chopped (Alaska Native)
    35130: [], # Mush, blue corn with ash (Navajo)
    35131: [], # Cornmeal, blue (Navajo)
    35132: [], # Melon, banana (Navajo)
    35133: [], # Chilchen (Red Berry Beverage) (Navajo)
    35134: [], # Corn, dried (Navajo)
    35135: [], # Corn, white, steamed (Navajo)
    35136: [], # Cornmeal, white (Navajo)
    35137: [], # Cornmeal, yellow (Navajo)
    35138: [], # Squash, Indian, raw (Navajo)
    35139: [], # Squash, Indian, cooked, boiled (Navajo)
    35140: [], # Bread, kneel down (Navajo)
    35141: [], # Mutton, cooked, roasted (Navajo)
    35142: [], # Frybread, made with lard (Navajo)
    35143: [], # Tortilla, includes plain and from mutton sandwich (Navajo)
    35144: [], # Stew, dumpling with mutton (Navajo)
    35145: [], # Stew, hominy with mutton (Navajo)
    35146: [], # Stew, mutton, corn, squash (Navajo)
    35147: [], # Tamales (Navajo)
    35148: [], # Stew, steamed corn (Navajo)
    35149: [], # Fish, halibut, raw, with skin (Alaska Native)
    35150: [], # Fish, salmon, coho (silver), raw (Alaska Native)
    35151: [], # Fish, salmon, sockeye (red), raw (Alaska Native)
    35152: [], # Fish, Salmon, Chum, raw (Alaska Native)
    35153: [], # Fish, salmon, king (chinook), raw (Alaska Native)
    35154: [], # Salmonberries, raw (Alaska Native)
    35155: [], # Blueberries, wild, raw (Alaska Native)
    35156: [], # Oil, spotted seal (Alaska Native)
    35157: [], # Fish, salmon, red, canned, bones removed (Alaska Native)
    35158: [], # Fish, whitefish, eggs (Alaska Native)
    35160: [], # Caribou, rump meat, half dried (Alaska Native)
    35161: [], # Caribou, shoulder meat, dried (Alaska Native)
    35162: [], # Caribou, hind quarter meat, raw (Alaska Native)
    35164: [], # Seal, bearded (Oogruk), meat, dried, in oil (Alaska Native)
    35165: [], # Fish, whitefish, dried (Alaska Native)
    35166: [], # Fish, salmon, red, (sockeye), canned, smoked (Alaska Native)
    35167: [], # Fish, salmon, red, (sockeye), kippered (Alaska Native)
    35168: [], # Fish, salmon, king, with skin, kippered, (Alaska Native)
    35169: [], # Fish, sheefish, raw (Alaska Native)
    35170: [], # Seal, bearded (Oogruk), meat, low quadrant, raw (Alaska Native)
    35171: [], # Fish, salmon, chum, dried (Alaska Native)
    35172: [], # Elk, free range, ground, cooked patties (Shoshone Bannock)
    35173: [], # Elk, free range, ground, raw (Shoshone Bannock)
    35174: [], # Buffalo, free range, top round steak, raw (Shoshone Bannock)
    35175: [], # Seal, bearded (Oogruk), meat, partially dried (Alaska Native)
    35176: [], # Buffalo, free range, top round steak, cooked (Shoshone Bannock)
    35177: [], # Elk, free range, roast, eye of round, raw (Shoshone Bannock)
    35178: [], # Elk, free range, roast, eye of round, cooked (Shoshone Bannock)
    35179: [], # Chokecherries, raw, pitted (Shoshone Bannock)
    35180: [], # Steelhead trout, dried, flesh (Shoshone Bannock)
    35181: [], # Steelhead trout, boiled, canned (Alaska Native)
    35182: [], # Acorn stew (Apache)
    35183: [], # Corn, dried, yellow (Northern Plains Indians)
    35184: [], # Smelt, dried (Alaska Native)
    35185: [], # Frybread, made with lard (Apache)
    35186: [], # Corned beef and potatoes in tortilla (Apache)
    35187: [], # Tennis Bread, plain (Apache)
    35188: [], # Fish, halibut, cooked, with skin (Alaska Native)
    35190: [], # Salmon, red (sockeye), filets with skin, smoked (Alaska Native)
    35192: [], # Agave, raw (Southwest)
    35193: [], # Agave, cooked (Southwest)
    35194: [], # Agave, dried (Southwest)
    35195: [], # Cattail, Narrow Leaf Shoots (Northern Plains Indians)
    35196: [], # Lambsquarters, raw (Northern Plains Indians)
    35197: [], # Lambsquarters, steamed (Northern Plains Indians)
    35198: [], # Prickly pears, raw (Northern Plains Indians)
    35199: [], # Prickly pears, broiled (Northern Plains Indians)
    35200: [], # Prairie Turnips, raw (Northern Plains Indians)
    35201: [], # Prairie Turnips, boiled (Northern Plains Indians)
    35202: [], # Raspberries, wild (Northern Plains Indians)
    35203: [], # Rose Hips, wild (Northern Plains Indians)
    35204: [], # Chokecherries, raw, pitted (Northern Plains Indians)
    35205: [], # Stinging Nettles, blanched (Northern Plains Indians)
    35206: [], # Plums, wild (Northern Plains Indians)
    35207: [], # Pinon Nuts, roasted (Navajo)
    35211: [], # Caribou, hind quarter, meat, cooked (Alaska Native)
    35225: [], # Agutuk, fish with shortening (Alaskan ice cream) (Alaska Native)
    35226: [], # Sea lion, Steller, liver (Alaska Native)
    35227: [], # Sea lion, Steller, kidney (Alaska Native)
    35228: [], # Sea lion, Steller, heart (Alaska Native)
    35229: [], # Sea lion, Steller, meat (Alaska Native)
    35230: [], # Sea lion, Steller, meat with fat (Alaska Native)
    35231: [], # Sea lion, Steller, fat (Alaska Native)
    35232: [], # Wocas, dried seeds, Oregon, yellow pond lily (Klamath)
    35233: [], # Hazelnuts, beaked (Northern Plains Indians)
    35234: [], # Piki bread, made from blue cornmeal (Hopi)
    35235: [], # Wocas, tuber, cooked, Oregon, yellow pond lily (Klamath)
    35236: [], # Stew, pinto bean and hominy, badufsuki (Hopi)
    35237: [], # Tamales, masa and pork filling (Hopi)
    35238: [], # Tea, herbal, brewed, Hohoysi (Hopi)
    35239: [], # Tortilla, blue corn, Sakwavikaviki (Hopi)
    35240: [], # Bread, blue corn, somiviki (Hopi)
    36000: [], # APPLEBEE'S, 9 oz house sirloin steak
    36001: [], # APPLEBEE'S, Double Crunch Shrimp
    36002: [], # APPLEBEE'S, french fries
    36003: [], # APPLEBEE'S, KRAFT, Macaroni & Cheese, from kid's menu
    36004: [], # APPLEBEE'S, mozzarella sticks
    36005: [], # APPLEBEE'S, chicken tenders, from kids' menu
    36006: [], # T.G.I. FRIDAY'S, FRIDAY'S Shrimp, breaded
    36007: [], # T.G.I. FRIDAY'S, french fries
    36008: [], # T.G.I. FRIDAY'S, fried mozzarella
    36009: [], # T.G.I. FRIDAY'S, macaroni & cheese, from kid's menu
    36010: [], # T.G.I. FRIDAY'S, chicken fingers, from kids' menu
    36011: [], # T.G.I. FRIDAY'S, classic sirloin steak (10 oz)
    36012: [], # Restaurant, family style, fried mozzarella sticks
    36013: [], # Restaurant, family style, sirloin steak
    36014: [], # Restaurant, family style, french fries
    36015: [], # Restaurant, family style, chicken fingers, from kid's menu
    36016: [], # Restaurant, family style, shrimp, breaded and fried
    36017: [], # Restaurant, family style, macaroni & cheese, from kids' menu
    36018: [], # APPLEBEE'S, fish, hand battered
    36019: [], # APPLEBEE'S, chili
    36020: [], # T.G.I. FRIDAY'S, chicken fingers
    36021: [], # APPLEBEE'S, coleslaw
    36022: [], # APPLEBEE'S, crunchy onion rings
    36023: [], # APPLEBEE'S, chicken tenders platter
    36024: [], # CRACKER BARREL, chicken tenderloin platter, fried
    36025: [], # CRACKER BARREL, coleslaw
    36026: [], # CRACKER BARREL, onion rings, thick-cut
    36027: [], # DENNY'S, chicken strips
    36028: [], # DENNY'S, coleslaw
    36029: [], # DENNY'S, fish fillet, battered or breaded, fried
    36030: [], # DENNY'S, hash browns
    36031: [], # DENNY'S, onion rings
    36032: [], # DENNY'S, spaghetti and meatballs
    36033: [], # Restaurant, family style, fish fillet, battered or breaded, fried
    36034: [], # Restaurant, family style, chicken tenders
    36035: [], # Restaurant, family style, coleslaw
    36036: [], # Restaurant, family style, onion rings
    36037: [], # Restaurant, family style, chili with meat and beans
    36038: [], # Restaurant, family style, spaghetti and meatballs
    36039: [], # Restaurant, family style, hash browns
    36040: [], # CRACKER BARREL, macaroni n' cheese
    36041: [], # Restaurant, Italian, lasagna with meat
    36042: [], # OLIVE GARDEN, lasagna classico
    36043: [], # CARRABBA'S ITALIAN GRILL, lasagne
    36044: [], # ON THE BORDER, Mexican rice
    36045: [], # ON THE BORDER, refried beans
    36046: [], # Restaurant, Italian, spaghetti with pomodoro sauce (no meat)
    36047: [], # OLIVE GARDEN, spaghetti with pomodoro sauce
    36048: [], # CARRABBA'S ITALIAN GRILL, spaghetti with pomodoro sauce
    36049: [], # ON THE BORDER, cheese enchilada
    36050: [], # Restaurant, Mexican, cheese enchilada
    36051: [], # ON THE BORDER, cheese quesadilla
    36052: [], # Restaurant, Mexican, cheese quesadilla
    36053: [], # CARRABBA'S ITALIAN GRILL, cheese ravioli with marinara sauce
    36054: [], # OLIVE GARDEN, cheese ravioli with marinara sauce
    36055: [], # Restaurant, Italian, cheese ravioli with marinara sauce
    36056: [], # Restaurant, Mexican, cheese tamales
    36057: [], # CARRABBA'S ITALIAN GRILL, chicken parmesan without cavatappi pasta
    36058: [], # OLIVE GARDEN, chicken parmigiana without pasta
    36059: [], # Restaurant, Italian, chicken parmesan without pasta
    36060: [], # ON THE BORDER, soft taco with ground beef, cheese and lettuce
    36061: [], # Restaurant, Mexican, soft taco with ground beef, cheese and lettuce
    36401: [], # Restaurant, Latino, chicken and rice, entree, prepared
    36403: [], # Restaurant, Latino, empanadas, beef, prepared
    36404: [], # Restaurant, Latino, arroz con leche (rice pudding)
    36405: [], # Restaurant, Latino, Arroz con frijoles negros (rice and black beans)
    36406: [], # Restaurant, Latino, Arroz con habichuelas colorados (Rice And Red Beans)
    36407: [], # Restaurant, Latino, Arroz con grandules (rice and pigeonpeas)
    36408: [], # Restaurant, Latino, pupusas con frijoles (pupusas, bean)
    36409: [], # Restaurant, Latino, pupusas con queso (pupusas, cheese)
    36410: [], # Restaurant, Latino, pupusas del cerdo (pupusas, pork)
    36411: [], # Restaurant, Latino, tamale, corn
    36412: [], # Restaurant, Latino, tamale, pork
    36413: [], # Restaurant, Latino, black bean soup
    36414: [], # Restaurant, Latino, tripe soup
    36415: [], # Restaurant, Latino, arepa (unleavened cornmeal bread)
    36416: [], # Restaurant, Latino, bunuelos (fried yeast bread)
    36417: [], # Restaurant, Mexican, spanish rice
    36418: [], # Restaurant, Mexican, refried beans
    36601: [], # Restaurant, Chinese, egg rolls, assorted
    36602: [], # Restaurant, Chinese, fried rice, without meat
    36603: [], # Restaurant, Chinese, beef and vegetables
    36604: [], # CRACKER BARREL, chicken tenderloin platter, fried, from kid's menu
    36605: [], # CRACKER BARREL, country fried shrimp platter
    36606: [], # CRACKER BARREL, farm raised catfish platter
    36607: [], # CRACKER BARREL, steak fries
    36608: [], # CRACKER BARREL, grilled sirloin steak
    36609: [], # CRACKER BARREL, macaroni n' cheese plate, from kid's menu
    36610: [], # DENNY'S, french fries
    36611: [], # DENNY'S, mozzarella cheese sticks
    36612: [], # DENNY'S, golden fried shrimp
    36613: [], # DENNY'S, macaroni & cheese, from kid's menu
    36614: [], # DENNY'S, chicken nuggets, star shaped, from kid's menu
    36615: [], # DENNY'S, top sirloin steak
    36617: [], # Restaurant, Chinese, lemon chicken
    36618: [], # Restaurant, Chinese, general tso's chicken
    36619: [], # Restaurant, Chinese, kung pao chicken
    36620: [], # Restaurant, Chinese, shrimp and vegetables
    36621: [], # Restaurant, Chinese, sweet and sour chicken
    36622: [], # Restaurant, Chinese, sweet and sour pork
    36623: [], # Restaurant, Chinese, chicken chow mein
    36624: [], # Restaurant, Chinese, vegetable chow mein, without meat or noodles
    36625: [], # Restaurant, Chinese, vegetable lo mein, without meat
    36626: [], # Restaurant, Chinese, chicken and vegetables
    36629: [], # Restaurant, Chinese, orange chicken
    36630: [], # Restaurant, Italian, spaghetti with meat sauce
    36631: [], # OLIVE GARDEN, spaghetti with meat sauce
    36632: [], # CARRABBA'S ITALIAN GRILL, spaghetti with meat sauce
    36633: [], # Restaurant, Chinese, sesame chicken
    42040: [], # Syrups, grenadine
    42055: [], # Beverages, fruit-flavored drink, dry powdered mix, low calorie, with aspartame
    42063: [], # Pectin, liquid
    42074: [], # Frozen novelties, ice cream type, vanilla ice cream, light, no sugar added, chocolate coated
    42116: [], # Creamy dressing, made with sour cream and/or buttermilk and oil, reduced calorie
    42117: [], # Imitation cheese, american or cheddar, low cholesterol
    42119: [], # Babyfood, banana juice with low fat yogurt
    42120: [], # Babyfood, mixed fruit juice with low fat yogurt
    42128: [], # Ham, turkey, sliced, extra lean, prepackaged or deli
    42129: [], # Bologna, beef and pork, low fat
    42131: [], # Milk dessert, frozen, milk-fat free, chocolate
    42135: [], # Whipped topping, frozen, low fat
    42136: [], # Cream substitute, powdered, light
    42137: [], # Salad dressing, peppercorn dressing, commercial, regular
    42138: [], # Mayonnaise, reduced-calorie or diet, cholesterol-free
    42139: [], # Granola bar, soft, milk chocolate coated, peanut butter
    42140: [], # Salad dressing, italian dressing, reduced calorie
    42141: [], # Cream substitute, liquid, light
    42148: [], # Candies, MARS SNACKFOOD US, M&M's Peanut Butter Chocolate Candies
    42150: [], # Babyfood, apple yogurt dessert, strained
    42151: [], # Vegetable oil-butter spread, reduced calorie
    42153: [], # Salad dressing, blue or roquefort cheese dressing, light
    42155: [], # Cheese, monterey, low fat
    42157: [], # Creamy dressing, made with sour cream and/or buttermilk and oil, reduced calorie, fat-free
    42158: [], # Creamy dressing, made with sour cream and/or buttermilk and oil, reduced calorie, cholesterol-free
    42161: [], # Bologna, beef, low fat
    42171: [], # Salad dressing, french dressing, reduced calorie
    42173: [], # Sausage, turkey and pork, fresh, bulk, patty or link, cooked
    42178: [], # Mayonnaise, made with tofu
    42179: [], # Frankfurter, beef, low fat
    42183: [], # Candies, MARS SNACKFOOD US, TWIX chocolate fudge cookie bars
    42185: [], # Frozen yogurts, chocolate, nonfat milk, sweetened without sugar
    42186: [], # Frozen yogurts, chocolate
    42187: [], # Frozen yogurts, flavors other than chocolate
    42189: [], # Milk, buttermilk, fluid, cultured, reduced fat
    42190: [], # Pork sausage rice links, brown and serve, cooked
    42192: [], # Salad dressing, blue or roquefort cheese dressing, fat-free
    42193: [], # Salad Dressing, mayonnaise-like, fat-free
    42196: [], # Candies, MARS SNACKFOOD US, MILKY WAY Midnight Bar
    42200: [], # Papad
    42204: [], # Rice cake, cracker (include hain mini rice cakes)
    42227: [], # Candies, MARS SNACKFOOD US, M&M's Almond Chocolate Candies
    42230: [], # Salad Dressing, coleslaw, reduced fat
    42231: [], # Oil, flaxseed, cold pressed
    42235: [], # Cheese, cottage, lowfat, 1% milkfat, lactose reduced
    42236: [], # Cereals ready-to-eat, frosted oat cereal with marshmallows
    42237: [], # Cereals ready-to-eat, WEETABIX whole grain cereal
    42240: [], # Cereals ready-to-eat, POST, HONEY BUNCHES OF OATS, with almonds
    42256: [], # Margarine-like, vegetable oil spread, stick or tub, sweetened
    42259: [], # Snacks, popcorn, home-prepared, oil-popped, unsalted
    42261: [], # Cereals ready-to-eat, POST, GREAT GRAINS Crunchy Pecan Cereal
    42265: [], # Cereals ready-to-eat, POST, GREAT GRAINS, Raisin, Date & Pecan
    42266: [], # Babyfood, juice, apple-sweet potato
    42267: [], # Babyfood, juice, orange-carrot
    42270: [], # Beverages, Orange juice drink
    42272: [], # Snacks, granola bar, with coconut, chocolate coated
    42278: [], # Babyfood, vegetable and brown rice, strained
    42279: [], # Babyfood, peas and brown rice
    42280: [], # Frankfurter, meat and poultry, low fat
    42281: [], # Gums, seed gums (includes locust bean, guar)
    42283: [], # Snacks, potato chips, white, restructured, baked
    42284: [], # Babyfood, baked product, finger snacks cereal fortified
    42285: [], # Babyfood, cereal, brown rice, dry, instant
    42286: [], # Babyfood, green beans and turkey, strained
    42289: [], # Oil, corn and canola
    42290: [], # Milk, fluid, nonfat, calcium fortified (fat free or skim)
    42291: [], # Peanut butter, reduced sodium
    42297: [], # Cereals ready-to-eat, POST GREAT GRAINS Banana Nut Crunch
    42303: [], # Cheese, muenster, low fat
    42304: [], # Cheese, mozzarella, nonfat
    42307: [], # Margarine-like, butter-margarine blend, 80% fat, stick, without salt
    42309: [], # Margarine-like, vegetable oil-butter spread, reduced calorie, tub, with salt
    42316: [], # Babyfood, carrots, toddler
    43004: [], # Babyfood, dessert, banana pudding, strained
    43006: [], # Babyfood, fruit, tutti frutti, strained
    43007: [], # Babyfood, fruit, tutti frutti, junior
    43008: [], # Babyfood, dinner, chicken and rice
    43015: ['Caesar dressing'], # Salad dressing, caesar dressing, regular
    43016: ['Coleslaw dressing'], # Salad dressing, coleslaw
    43017: ['Green goddess dressing'], # Salad dressing, green goddess, regular
    43019: ['Sweet and sour dressing'], # Salad dressing, sweet and sour
    43020: [], # Salad dressing, blue or roquefort cheese, low calorie
    43021: [], # Salad dressing, caesar, low calorie
    43026: [], # Syrups, sugar free
    43027: [], # Jellies, no sugar (with sodium saccharin), any flavors
    43028: [], # Jams and preserves, no sugar (with sodium saccharin), any flavor
    43031: [], # Candies, chocolate covered, caramel with nuts
    43046: [], # Candies, nougat, with almonds
    43057: [], # Candies, gum drops, no sugar or low calorie (sorbitol)
    43058: [], # Candies, hard, dietetic or low calorie (sorbitol)
    43059: [], # Candies, chocolate covered, low sugar or low calorie
    43060: [], # Chewing gum, sugarless
    43075: [], # Fluid replacement, electrolyte solution (include PEDIALYTE)
    43098: [], # Pie fillings, cherry, low calorie
    43100: [], # Breakfast bars, oats, sugar, raisins, coconut (include granola bar)
    43109: [], # Pretzels, soft
    43112: [], # Beans, chili, barbecue, ranch style, cooked
    43114: [], # Vermicelli, made from soy
    43125: [], # Beans, liquid from stewed kidney beans
    43128: [], # Chicken, meatless
    43130: [], # Frankfurter, meatless
    43131: [], # Luncheon slices, meatless
    43132: [], # Meatballs, meatless
    43134: [], # Vegetarian fillets
    43135: [], # Sandwich spread, meatless
    43137: [], # Vegetarian meatloaf or patties
    43142: [], # Radishes, hawaiian style, pickled
    43143: [], # Cabbage, japanese style, fresh, pickled
    43144: [], # Cabbage, mustard, salted
    43146: [], # Eggplant, pickled
    43154: [], # Alcoholic beverage, wine, cooking
    43155: [], # Alcoholic beverage, wine, light
    43158: [], # Sweeteners, tabletop, saccharin (sodium saccharin)
    43205: [], # Beverage, instant breakfast powder, chocolate, not reconstituted
    43212: [], # Bacon bits, meatless
    43214: [], # Butter replacement, without fat, powder
    43215: [], # Salad dressing, buttermilk, lite
    43216: [], # Sweeteners, tabletop, fructose, dry, powder
    43217: [], # Tomato sauce, canned, no salt added
    43218: [], # Cereals ready-to-eat, ALPEN
    43241: [], # Cereals ready-to-eat, FAMILIA
    43245: [], # Cereals ready-to-eat, wheat and bran, presweetened with nuts and fruits
    43260: [], # Beverage, instant breakfast powder, chocolate, sugar-free, not reconstituted
    43261: [], # Yogurt, fruit variety, nonfat
    43268: [], # Whipped cream substitute, dietetic, made from powdered mix
    43269: [], # Frozen novelties, ice cream type, sundae, prepackaged
    43273: [], # Cheese, cottage, with vegetables
    43274: [], # Cheese, cream, low fat
    43275: [], # Cheese, pasteurized process, American, low fat
    43276: [], # Cheese spread, cream cheese base
    43278: [], # Cheese, american cheddar, imitation
    43282: [], # Quail, cooked, total edible
    43283: [], # Pheasant, cooked, total edible
    43285: [], # Eggs, scrambled, frozen mixture
    43287: [], # Dove, cooked (includes squab)
    43297: [], # Pork, oriental style, dehydrated
    43299: [], # Soybean, curd cheese
    43311: [], # Potatoes, canned, drained solids, no salt added
    43312: [], # Vegetables, mixed (corn, lima beans, peas, green beans, carrots) canned, no salt added
    43325: [], # Pork, cured, ham, boneless, low sodium, extra lean and regular, roasted
    43326: [], # Pork, cured, ham, low sodium, lean and fat, cooked
    43327: [], # Pork, cured, ham, boneless, low sodium, extra lean (approximately 5% fat), roasted
    43329: [], # Salad dressing, mayonnaise and mayonnaise-type, low calorie
    43331: [], # Salad dressing, bacon and tomato
    43340: [], # Cheese, parmesan, low sodium
    43344: [], # Jams, preserves, marmalade, reduced sugar
    43345: [], # Beverages, fruit-flavored drink, powder, with high vitamin C with other added vitamins, low calorie
    43346: [], # Frozen novelties, juice type, orange
    43352: [], # Cheese, cottage, lowfat, 1% milkfat, no sodium added
    43355: [], # Mayonnaise, low sodium, low calorie or diet
    43364: [], # Snacks, tortilla chips, unsalted, white corn
    43365: [], # Tomato and vegetable juice, low sodium
    43366: [], # Turkey, wing, smoked, cooked, with skin, bone removed
    43367: [], # Turkey, drumstick, smoked, cooked, with skin, bone removed
    43369: [], # Beverages, Chocolate-flavored drink, whey and milk based
    43378: [], # Pork, cured, bacon, cooked, broiled, pan-fried or roasted, reduced sodium
    43382: [], # Cranberry juice, unsweetened
    43384: [], # Beef, bologna, reduced sodium
    43387: [], # Turnip greens, canned, no salt added
    43390: [], # Turkey, light or dark meat, smoked, cooked, with skin, bone removed
    43391: [], # Turkey, light or dark meat, smoked, cooked, skin and bone removed
    43392: [], # Hearts of palm, raw
    43393: [], # Cereals ready-to-eat, POST, Shredded Wheat n' Bran, spoon-size
    43396: [], # Cheese, cottage, lowfat, 1% milkfat, with vegetables
    43398: [], # Cheese, pasteurized process, cheddar or American, low sodium
    43401: [], # Beverages, coffee, instant, with whitener, reduced calorie
    43404: [], # Beverages, cranberry-apple juice drink, low calorie, with vitamin C added
    43405: [], # Cheese, swiss, low sodium
    43406: [], # Yeast extract spread
    43408: [], # Babyfood, juice, pear
    43410: [], # Chicken, meatless, breaded, fried
    43417: [], # Babyfood, meat, beef with vegetables, toddler
    43432: [], # Babyfood, dinner, macaroni, beef and tomato sauce, toddler
    43441: [], # Rolls, pumpernickel
    43447: [], # Snacks, corn-based, extruded, chips, unsalted
    43449: [], # Beans, baked, canned, no salt added
    43450: [], # Frozen novelties, juice type, juice with cream
    43476: [], # Tofu yogurt
    43479: [], # Alcoholic beverage, rice (sake)
    43483: [], # Millet, puffed
    43495: [], # Cereals ready-to-eat, OAT BRAN FLAKES, HEALTH VALLEY
    43497: [], # Jellyfish, dried, salted
    43506: [], # Frozen novelties, ice cream type, chocolate or caramel covered, with nuts
    43507: [], # Frankfurter, low sodium
    43514: [], # Frozen novelties, ice type, pop, with low calorie sweetener
    43523: [], # Babyfood, mixed fruit yogurt, strained
    43528: [], # Beverages, ABBOTT, ENSURE PLUS, ready-to-drink
    43529: [], # Babyfood, rice and apples, dry
    43535: [], # Babyfood, juice, apple - cherry
    43536: [], # Babyfood, dessert, peach yogurt
    43537: [], # Babyfood, dessert, blueberry yogurt, strained
    43539: [], # Babyfood, dessert, banana yogurt, strained
    43541: [], # Ice creams, chocolate, rich
    43543: [], # Milk, imitation, non-soy
    43544: [], # Babyfood, cereal, rice with pears and apple, dry, instant fortified
    43546: [], # Babyfood, banana no tapioca, strained
    43550: [], # Babyfood, banana apple dessert, strained
    43566: [], # Snacks, tortilla chips, light (baked with less oil)
    43570: [], # Cereals ready-to-eat, POST, HONEY BUNCHES OF OATS, honey roasted
    43572: [], # Popcorn, microwave, low fat and sodium
    43585: [], # Babyfood, fruit supreme dessert
    43589: [], # Cheese, swiss, low fat
    43595: [], # Breakfast bar, corn flake crust with fruit
    43597: [], # Cheese, mozzarella, low sodium
    43598: [], # Mayonnaise dressing, no cholesterol
    44005: [], # Oil, corn, peanut, and olive
    44018: [], # Sweeteners, tabletop, fructose, liquid
    44061: [], # Puddings, chocolate flavor, low calorie, instant, dry mix
    44074: [], # Babyfood, grape juice, no sugar, canned
    44110: [], # Jellies, reduced sugar, home preserved
    44158: [], # Pie fillings, blueberry, canned
    44203: [], # Beverages, Cocktail mix, non-alcoholic, concentrated, frozen
    44258: [], # Puddings, chocolate flavor, low calorie, regular, dry mix
    44259: [], # Puddings, all flavors except chocolate, low calorie, regular, dry mix
    44260: [], # Puddings, all flavors except chocolate, low calorie, instant, dry mix
    48052: [], # Vital wheat gluten
    80200: [], # Frog legs, raw
    83110: [], # Fish, mackerel, salted
    90240: [], # Mollusks, scallop, (bay and sea), cooked, steamed
    90480: [], # Syrup, Cane
    90560: [], # Mollusks, snail, raw
    93600: [], # Turtle, green, raw
}
