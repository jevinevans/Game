"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing characters.
"""
from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.character import Character
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    yes_no_validation,
)

CHARACTER_DATA = {"filename": "characters.json", "data": {}, "objects": {}}


def build_character():
    # TODO: Update initialization process so that the role decides the armor type for the character and then all armor and equips will validate for the role
    print("TODO: Build New Character Section")
    raise NotImplementedError


def select_character():
    raise NotImplementedError


def edit_character():
    print("TODO: Build Edit Character Section")
    raise NotImplementedError


def delete_character():
    print("TODO: Build Delete Character Section")
    raise NotImplementedError


CHARACTER_MENU = {
    "name": "Manage Characters",
    "description": "This is the menu to create characters to use in game.",
    "menu_items": [
        {"name": "New Character", "action": build_character},
        {"name": "Edit Character", "action": edit_character},
        {"name": "Delete Character", "action": delete_character},
    ],
}

# TODO: Remove me
# db.load_data(CHARACTER_DATA)
# update_data()
