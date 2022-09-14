"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing abilities.
"""

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.abilities import Abilities
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    yes_no_validation,
)

ABILITIES_DATA = {"filename":"abilities.json", "data":{}}

def build_ability():
    print("TODO: Build New Ability Section")
    raise NotImplementedError

def select_ability():
    raise NotImplementedError

def edit_ability():
    print("TODO: Build Edit Ability Section")
    raise NotImplementedError

def delete_ability():
    print("TODO: Build Delete Ability Section")
    raise NotImplementedError

ABILITY_MENU = {
    "name": "Manage Abilities",
    "description": "This is the menu to create abilities to add to Roles for characters to use.",
    "menu_items": [
        {"name": "Add New Ability", "action": build_ability},
        {"name": "Edit Ability", "action": edit_ability},
        {"name": "Delete Ability", "action": delete_ability},
    ],
}

ABILITIES_DATA = db.load_data(ABILITIES_DATA)