"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing equipment.
"""

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    yes_no_validation,
)

EQUIPMENT_DATA = {"filename": "equipment.json", "data": {}}

# TODO design these to be just the creation function
def _new_weapon():
    print("TODO: Build New Weapon Section")
    raise NotImplementedError


def _new_body_armor():
    print("TODO: Build New Body Armor Section")
    raise NotImplementedError


def _edit_weapon():
    print("TODO: Build Edit Weapon Section")
    raise NotImplementedError


def _edit_body_armor():
    print("TODO: Build Edit Body Armor Section")
    raise NotImplementedError


def _delete_weapon():
    print("TODO: Build Delete Weapon Section")
    raise NotImplementedError


def _delete_body_armor():
    print("TODO: Build Delete Body Armor Section")
    raise NotImplementedError


def build_equipment():
    print("TODO: Build New Equipment")
    raise NotImplementedError


def select_equipment():
    raise NotImplementedError


def edit_equipment():
    print("TODO: Build Edit Equipment Section")
    raise NotImplementedError


def delete_equipment():
    print("TODO: Build Delete Equipment Section")
    raise NotImplementedError


EQUIPMENT_MENU = {
    "name": "Manage Equipment",
    "description": "This the menu to create armor and weapons for characters to use.",
    "menu_items": [
        {"name": "New Equipment", "action": build_equipment},
        {"name": "Edit Equipment", "action": edit_equipment},
        {"name": "Delete Equipment", "action": delete_equipment},
    ],
}

# TODO: Remove me
# EQUIPMENT_DATA = db.load_data(EQUIPMENT_DATA)
