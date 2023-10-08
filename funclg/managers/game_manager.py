"""
Description: Manages game setttings
Developer: Jevin Evans
Date: 10.8.2023
"""

from typing import Any

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.utils.level_icons import level_icons

GAME_DATA = {"filename": "game_settings.json", "data": {}, "objects": {}}


def load_data():
    db.load_data(GAME_DATA)
    update_data()


def update_data():
    # Will load many different types of data
    _load_level_icons(GAME_DATA["data"]["level_icons"])


# TODO: Change back to dictionary so that it can be used for selection option.


def _load_level_icons(icon_data: list):
    icons_sets = []

    for icon_set in icon_data:
        icons_sets.append(level_icons(**icon_set))

    GAME_DATA["objects"]["level_icons"] = icons_sets


if __name__ == "__main__":
    load_data()
