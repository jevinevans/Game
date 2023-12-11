"""
Description: Manager for user to create and manage groupings of levels for game play
Developer: Jevin Evans
Date: 12.7.2023
"""

# from loguru import logger

LEVEL_PACK_DATA = {"filename": "level_packs.json", "data": {}, "objects": {}}


def load_data():
    raise NotImplementedError


def update_data():
    raise NotImplementedError


def export_data():
    raise NotImplementedError


def create_level_pack():
    raise NotImplementedError


def show_level_pack():
    raise NotImplementedError


def get_level_pack():
    raise NotImplementedError


def delete_level_pack():
    raise NotImplementedError


MENU = {
    "name": "Level Pack Manager",
    "description": "Create and manage packs of levels.",
    "menu_items": [
        {"title": "Create new Level Pack", "value": create_level_pack},
        {"title": "Show Level Pack(s)", "value": show_level_pack},
        {"title": "Remove Level Pack(s)", "value": delete_level_pack},
    ],
}
