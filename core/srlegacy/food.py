import json

import core.models

COLUMN_NAMES = (  # Corresponding origin column names to model fields
    "NDB_No",  # id
    "FdGrp_Cd",  # -
    "Long_Desc",  # name
    "Shrt_Desc",  # -
    "ComName",  # common_name
    "ManufacName",  # -
    "Survey",  # -
    "Ref_desc",  # -
    "Refuse",  # -
    "SciName",  # -
    "N_Factor",  # n_factor
    "Pro_Factor",  # pro_factor
    "Fat_Factor",  # fat_factor
    "CHO_Factor",  # cho_factor
)

CONVERT_TYPES = {
    "NDB_No": int,
    "FdGrp_Cd": int,
    "Long_Desc": str,
    "Shrt_Desc": str,
    "ComName": str,
    "ManufacName": str,
    "Survey": str,
    "Ref_desc": str,
    "Refuse": int,
    "SciName": str,
    "N_Factor": float,
    "Pro_Factor": float,
    "Fat_Factor": float,
    "CHO_Factor": float,
}

COLUMN_TO_FIELD = {
    "NDB_No": "id",
    "Long_Desc": "name",
    "ComName": "common_name",
    "N_Factor": "n_factor",
    "Pro_Factor": "pro_factor",
    "Fat_Factor": "fat_factor",
    "CHO_Factor": "cho_factor",
}


def parse_row(row):
    row = row.strip().split("^")
    row = [r.strip("~") for r in row]
    row = [r if r else None for r in row]
    row[0] = row[0].lstrip("0")
    row[1] = row[1].lstrip("0")
    row = dict(zip(COLUMN_NAMES, row))
    row = {k: CONVERT_TYPES[k](v) if v else v for k, v in row.items()}
    row = {COLUMN_TO_FIELD[k]: v for k, v in row.items() if k in COLUMN_TO_FIELD.keys()}
    return row


def main(filename):
    to_add = []
    with open(filename, encoding="cp1250") as f:
        for i, row in enumerate(f):
            parsed = parse_row(row)
            to_add.append(core.models.Food(**parsed))
            # Bulk create every 5000 entries to save RAM
            if i % 5000 == 0:
                core.models.Food.objects.bulk_create(to_add)
                to_add.clear()
    core.models.Food.objects.bulk_create(to_add)
