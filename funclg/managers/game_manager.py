"""
Description: Manages game setttings
Developer: Jevin Evans
Date: 10.8.2023
"""

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.utils.input_validation import selection_validation
from funclg.utils.level_icons import level_icons

GAME_DATA = {"filename": "game_settings.json", "data": {}, "objects": {}}


def load_data():
    db.load_data(GAME_DATA)
    update_data()


def update_data():
    # Will load many different types of data
    _load_level_icons(GAME_DATA["data"]["level_icons"])


def _load_level_icons(icon_data: list):
    icons_sets = []

    for icon_set in icon_data:
        icons_sets.append(level_icons(**icon_set))

    GAME_DATA["objects"]["level_icons"] = icons_sets


def select_level_icons():
    if GAME_DATA["objects"]:
        return selection_validation(
            "Which level icon set would you like to use for your levels?",
            GAME_DATA["objects"]["level_icons"],
        )
    logger.error("There are no level icons loaded.")
    raise SystemError("No level icons loaded.")


if __name__ == "__main__":
    load_data()


# TODO: Future: Consider a custom create capability
