"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

import json
import os
import random
import re
from datetime import datetime, timezone
from string import ascii_uppercase
from typing import Any, Dict, Union

from loguru import logger

DATA_DIR = ["funclg", "data"]
ID_LENGTH = 24


def id_gen(prefix: str = "FUNCLG", existing: Union[str, None] = ""):
    if existing and len(existing) == ID_LENGTH:
        return existing

    id_time = str(int(datetime.now(timezone.utc).timestamp()))
    rand_str_length = ID_LENGTH - len(id_time) - len(prefix) - 3
    rand_str = "".join(random.choice(ascii_uppercase) for _ in range(rand_str_length))
    return prefix + "-" + id_time[0:5] + "-" + rand_str + "-" + id_time[5:]


def validate_filename(filename: str) -> str:
    try:
        assert filename.endswith(".json")
        data_path = re.sub(r"funclg/.*", f"{os.sep}".join(DATA_DIR), os.path.dirname(__file__))
        return os.path.join(data_path, filename)
    except AssertionError as error:
        raise error


# TODO may need to move assertion error to validate method
def load_data(game_data: Dict[str, Any]):
    filename = validate_filename(game_data["filename"])
    try:
        if os.path.getsize(filename):
            with open(filename, "r", encoding="utf-8") as load_file:
                game_data["data"] = json.load(load_file)

    except json.JSONDecodeError:
        logger.error(f"{game_data['filename']}: malformed data")
    except FileNotFoundError:
        logger.error(f"{game_data['filename']}: Creating new database entry.")
        with open(filename, "a", encoding="utf-8"):
            logger.debug(f"Creating {filename}")
            os.utime(filename)
    except AssertionError:
        logger.error(f"{filename}: Incorrect format file.")
    return game_data


def update_data(game_data: Dict[str, Any]):
    try:
        filename = validate_filename(game_data["filename"])
        with open(filename, "w", encoding="utf-8") as write_file:
            json.dump(game_data["data"], write_file)
        logger.info(f"Saved {filename.split(os.sep)[-1].split('.')[0].capitalize()}")
        return True
    except FileNotFoundError as error:
        logger.error(error)
        print("Error updating database: could not write file.")
        return False


## Reference
## https://www.freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1/
