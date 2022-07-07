"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

import json
import os
import re
from typing import Any, Dict

from loguru import logger

DATA_DIR = "funclg/data/"


def validate_filename(filename: str) -> str:
    assert filename.endswith(".json")
    data_path = re.sub(r"funclg\/.*", DATA_DIR, os.path.dirname(__file__))
    return os.path.join(data_path, filename)


def load_data(filename: str):
    data = {}
    try:
        filename = validate_filename(filename)
        with open(filename, "r", encoding="utf-8") as load_file:
            data = json.load(load_file)

    except AssertionError as error:
        logger.error(error)
        print(f"{filename} is not the correct format file.")
    except FileNotFoundError as error:
        logger.error(error)
        print(f"Could not find file: {filename}")

    return data


def update_data(filename: str, data: Dict[str, Any]):
    "Define me"
    db_table = load_data(filename)
    db_table.update(data)
    try:
        filename = validate_filename(filename)
        with open(filename, "w", encoding="utf-8") as write_file:
            json.dump(db_table, write_file)
        return True
    except FileNotFoundError as error:
        logger.error(error)
        print(f"Error updating database: file not found {filename}")
        return False


## Reference
## https://www.freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1/
