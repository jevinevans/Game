"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: This defines lists and functions for certain constands
"""

# TODO: Consider changing IT, AT and WT to enums
# Item Types: 0 - Head, 1 - Chest, 2 - Back, 3 - Pants, 4 - Weapon
ITEM_TYPES = ["Head", "Chest", "Back", "Pants", "Weapon"]

# Armor Types: 0 - Light,  1 - Medium,  2 - Heavy,
ARMOR_TYPES = ["Light", "Medium", "Heavy"]

# Weapon Types: Weapon Name, Armor Type Restriction
WEAPON_TYPES = {"Sword": 2, "Spear": 2, "Wand": 1, "Staff": 1, "Knife": 0, "Bow": 0, "Unknown": 0}


# This defines the type of abilities, their effect target (Damage = enemies, Boost = Self), List of available attributes
ABILITY_TYPES = {
    "Magic": {"target": "enemy", "m_type": "base", "mods": ["health", "defense"]},
    "Physical": {"target": "enemy", "m_type": "base", "mods": ["health", "defense"]},
    "Restore": {"target": "self", "m_type": "percentage", "mods": ["health", "defense", "energy"]},
    "Buff": {
        "target": "self",
        "m_type": "percentage",
        "mods": ["health", "energy", "attack", "defense"],
    },
    "Debuff": {
        "target": "enemy",
        "m_type": "percentage",
        "mods": ["health", "energy", "attack", "defense"],
    },
    "Basic": {
        "target": "Other",
        "m_type": "base",
        "mods": [],
    },
}


def get_item_type(item_type: int) -> str:
    return ITEM_TYPES[item_type]


def get_armor_type(armor_type: int) -> str:
    return ARMOR_TYPES[armor_type]


def get_item_description(item_type=0, armor_type=0, weapon_type="Unknown") -> str:
    item = ""

    if item_type == 4:
        item += weapon_type
    elif item_type < 4:
        item += get_item_type(item_type)

    if armor_type != -1:
        item = get_armor_type(armor_type) + " " + item

    return "[" + item + "]"
