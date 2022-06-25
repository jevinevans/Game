"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

import json
import os

from loguru import logger


def get_data_path():
    return globals.get("DATA_PATH", "")


# TODO: add process to check to see if file in data path, either needs to provide full path or file name in the data folder
def load_data(filename: str):
    data_path = get_data_path()
    data = {}
    try:
        assert filename.endswith(".json")
        filename = os.path.join(data_path, filename)
        with open(filename, encoding="utf-8") as load_file:
            data = json.load(load_file)

    except (FileNotFoundError, AssertionError) as error:
        logger.warning(error)
        print(f"{error}\n - No data could be loaded for {filename}")

    return data


# TODO: Define update process
def update_data(filename: str, data):
    "Define me"
    # Needs to load file, call load function,
    # Needs to add the new object
    # Write the file back
