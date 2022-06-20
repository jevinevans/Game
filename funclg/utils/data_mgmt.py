"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

import json

from loguru import logger


def load_data(filename: str):
    data = {}
    try:
        assert filename.endswith(".json")
        assert "/data/" in filename
        with open(filename, encoding="utf-8") as load_file:
            data = json.load(load_file)

    except Exception as error:
        logger.warning(error)
        print(f"{error}\n - No data could be loaded for {filename}")

    return data
