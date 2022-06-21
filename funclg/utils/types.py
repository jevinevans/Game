"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: This defines lists and functions for certain constands
"""
from typing import Tuple

# Item Types: 0 - Head, 1 - Chest, 2 - Back, 3 - Pants, 4 - Weapon
ITEM_TYPES = ["Head", "Chest", "Back", "Pants", "Weapon"]

# Armor Types: 0 - Light,  1 - Medium,  2 - Heavy, -1 - (Weapons don't have armor types)
ARMOR_TYPES = ["Light", "Medium", "Heavy", ""]

# Weapon Types: 0 - Sword, 1 - Wand, 2 - Knife, -1 - (Not a Weapon)
WEAPON_TYPES = ["Sword", "Wand", "Knife", "Spear", "Bow", ""]

DAMAGE_TYPES = {
    "Magic": ("Damage", -1),
    "Physical": ("Damage", -1),
    "Healing": ("Boost", 1),
    "Repair": ("Boost", 1),
    "Buff": ("Boost", 1),
    "Debuff": ("Damage", -1),
    "None": ("None", 0),
}


# Contains all valid stat types that a modifier can affect
MODIFIER_TYPES = ["health", "energy", "attack", "defense"]
MOD_ADD_RANGE = 500
MOD_MULT_RANGE = 100

def get_ability_effect_type(a_type: str) -> Tuple[str, int]:
    "Returns the effect type of the provided ability"
    return DAMAGE_TYPES[a_type]


def get_item_type(item_type: int) -> str:
    return ITEM_TYPES[item_type]


def get_armor_type(armor_type: int) -> str:
    return ARMOR_TYPES[armor_type]


def get_weapon_type(weapon_type: int) -> str:
    return WEAPON_TYPES[weapon_type]


def get_item_description(item_type=0, armor_type=0, weapon_type=-1) -> str:
    item = ""

    if item_type == 4 and weapon_type != -1:
        item += get_weapon_type(weapon_type)
    elif item_type < 4:
        item += get_item_type(item_type)

    if armor_type != -1:
        item = get_armor_type(armor_type) + " " + item

    return "[" + item + "]"
