import json

from core.models import Food, FoodNutrition, FoodWeight

DATA_COLUMN_NAMES = (  # Corresponding origin column names to model fields
    "NDB_No",  # food
    "Nutr_No",  # id
    "Nutr_Val",  # value
    "Num_Data_Pts",  # -
    "Std_Error",  # -
    "Src_Cd",  # -
    "Deriv_Cd",  # -
    "Ref_NDB_No",  # -
    "Add_Nutr_Mark",  # -
    "Num_Studies",  # -
    "Min",  # -
    "Max",  # -
    "DF",  # -
    "Low_EB",  # -
    "Up_EB",  # -
    "Stat_cmt",  # -
    "AddMod_Date",  # -
)

DEF_COLUMN_NAMES = (  # Corresponding origin column names to model fields
    "Nutr_No",  # -
    "Units",  # units
    "Tagname",  # tagname
    "NutrDesc",  # desc
    "Num_Dec",  # -
    "SR_Order",  # -
)

DATA_CONVERT_TYPES = {
    "NDB_No": int,
    "Nutr_No": int,
    "Nutr_Val": float,
    "Num_Data_Pts": float,
    "Std_Error": float,
    "Src_Cd": str,
    "Deriv_Cd": str,
    "Ref_NDB_No": str,
    "Add_Nutr_Mark": str,
    "Num_Studies": int,
    "Min": float,
    "Max": float,
    "DF": int,
    "Low_EB": float,
    "Up_EB": float,
    "Stat_cmt": str,
    "AddMod_Date": str,
}

DEF_CONVERT_TYPES = {
    "Nutr_No": int,
    "Units": str,
    "Tagname": str,
    "NutrDesc": str,
    "Num_Dec": str,
    "SR_Order": int,
}

DATA_COLUMN_TO_FIELD = {"NDB_No": "food", "Nutr_No": "def_id", "Nutr_Val": "value"}

DEF_COLUMN_TO_FIELD = {
    "Nutr_No": "id",
    "Units": "units",
    "Tagname": "tagname",
    "NutrDesc": "desc",
}


def parse_row(row):
    row = row.strip().split("^")
    row = [r.strip("~") for r in row]
    row = [r if r else None for r in row]
    row[0] = row[0].lstrip("0")
    row[1] = row[1].lstrip("0")
    row = dict(zip(DATA_COLUMN_NAMES, row))
    row = {k: DATA_CONVERT_TYPES[k](v) if v else v for k, v in row.items()}
    row = {
        DATA_COLUMN_TO_FIELD[k]: v
        for k, v in row.items()
        if k in DATA_COLUMN_TO_FIELD.keys()
    }
    row["food"] = Food.objects.get(pk=row["food"])
    return row


def get_def_data(def_data):
    ret = {}
    with open(def_data, encoding="cp1250") as f:
        for row in f:
            row = row.strip().split("^")
            row = [r.strip("~") for r in row]
            row = [r if r else None for r in row]
            row[0] = row[0].lstrip("0")
            row = dict(zip(DEF_COLUMN_NAMES, row))
            row = {k: DEF_CONVERT_TYPES[k](v) if v else v for k, v in row.items()}
            row = {
                DEF_COLUMN_TO_FIELD[k]: v
                for k, v in row.items()
                if k in DEF_COLUMN_TO_FIELD.keys()
            }
            ret[row["id"]] = {k: v for k, v in row.items() if k != "id"}
    return ret


def join_def_data(parsed, def_data):
    ret = {**parsed, **def_data[parsed["def_id"]]}
    ret = {k: v for k, v in ret.items() if k != "def_id"}
    return ret


def main(filename, def_data):
    to_add = []
    def_data = get_def_data(def_data)
    with open(filename, encoding="cp1250") as f:
        for i, row in enumerate(f):
            parsed = parse_row(row)
            parsed = join_def_data(parsed, def_data)
            to_add.append(FoodNutrition(**parsed))
            # Bulk create every 5000 entries to save RAM
            if i % 5000 == 0:
                FoodNutrition.objects.bulk_create(to_add)
                to_add.clear()
    FoodNutrition.objects.bulk_create(to_add)
