"""
Description: Manages game setttings
Developer: Jevin Evans
Date: 10.8.2023
"""

from typing import Any

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.utils.game_enums import LevelIcons
from funclg.utils.input_validation import selection_validation

GAME_DATA = {"filename": "game_settings.json", "data": {}, "objects": {}}


def load_data():
    db.load_data(GAME_DATA)
    update_data()


def update_data():
    # Will load many different types of data
    _load_level_icons(GAME_DATA["data"]["level_icons"])


def _load_level_icons(icon_data: dict[str, Any]):
    icons_sets = {}

    for name, icon_set in icon_data.items():
        icons_sets[name] = LevelIcons(**icon_set)

    GAME_DATA["objects"]["level_icons"] = icons_sets


def select_level_icons():
    if icons := GAME_DATA["objects"]["level_icons"]:
        print(
            "Below are the game icon styles in a mini grid surrounding the icons for the player, key, space, enemy, and boss (respectively):"
        )
        for name, icon in icons.items():
            print(name, icon, "\n")

        choice = selection_validation(
            "Which level icon set would you like to use for your levels?", list(icons)
        )
        return icons[choice]
    logger.error("There are no level icons loaded.")
    raise SystemError("No level icons loaded.")


if __name__ == "__main__":
    load_data()

# TODO: Future: Consider a custom create capability
