"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: This defines lists and functions for certain constands
"""
from typing import Tuple

# Item Types: 0 - Head, 1 - Chest, 2 - Back, 3 - Pants, 4 - Weapon
ITEM_TYPES = ["Head", "Chest", "Back", "Pants", "Weapon"]

# Armor Types: 0 - Light,  1 - Medium,  2 - Heavy
ARMOR_TYPES = ["Light", "Medium", "Heavy"]

# Weapon Types: 0 - Sword, 1 - Wand, 2 - Knife
WEAPON_TYPES = ["Sword", "Wand", "Knife"]

ABILITY_TYPES = {
    "Magic": ("Damage", -1),
    "Physical": ("Damage", -1),
    "Healing": ("Boost", 1),
    "Repair": ("Boost", 1),
    "None": ("None", 0),
}


def get_ability_effect_type(a_type: str) -> Tuple[str, int]:
    "Returns the effect type of the provided ability"
    return ABILITY_TYPES[a_type]


def get_item_type(item_type: int) -> str:
    return ITEM_TYPES[item_type]


def get_armor_type(armor_type: int) -> str:
    return ARMOR_TYPES[armor_type]


def get_weapon_type(weapon_type: int) -> str:
    return WEAPON_TYPES[weapon_type]


def get_item_description(item_type=None, armor_type=None, weapon_type=None) -> str:
    item = ""

    if item_type is not None:
        if item_type == 4 and weapon_type is not None:
            item += get_weapon_type(weapon_type)
        else:
            item += get_item_type(item_type)
    elif weapon_type is not None:
        item = get_weapon_type(weapon_type)
    else:
        item = "Broken Item"

    if armor_type is not None:
        item = get_armor_type(armor_type) + " " + item

    return "[" + item + "]"
