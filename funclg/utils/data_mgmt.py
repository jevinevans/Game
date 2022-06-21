"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

import json
import os
from loguru import logger

DATA_PATH = ''

def setup_data_path(main_path:str):
    global DATA_PATH
    DATA_PATH = os.path.join(main_path, "data")

# TODO: add process to check to see if file in data path, either needs to provide full path or file name in the data folder
def load_data(filename: str):
    data = {}
    try:
        assert filename.endswith(".json")
        assert filename.startswith(DATA_PATH) # Change to look for if not just add
        with open(filename, encoding="utf-8") as load_file:
            data = json.load(load_file)

    except Exception as error:
        logger.warning(error)
        print(f"{error}\n - No data could be loaded for {filename}")

    return data


# TODO: Define update process
def update_data(filename:str, data):
    "Define me"
    # Needs to load file, call load function,
    # Needs to add the new object
    # Write the file back