"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: This defines lists and functions for certain constands
"""
# Item Types: 0 - Head, 1 - Chest, 2 - Back, 3 - Pants, 4 - Weapon
ITEM_TYPES = ["Head", "Chest", "Back", "Pants", "Weapon"]

# Armor Types: 0 - Light,  1 - Medium,  2 - Heavy, -1 - (Weapons don't have armor types)
ARMOR_TYPES = ["Light", "Medium", "Heavy", ""]

# Weapon Types: 0 - Sword, 1 - Wand, 2 - Knife, -1 - (Not a Weapon)
WEAPON_TYPES = ["Sword", "Wand", "Knife", "Spear", "Bow", ""]


# TODO Add descriptions
# This defines the type of abilities, their effect target (Damage = enemies, Boost = Self), List of available attributes
ABILITY_TYPES = {
    "Magic": {"target": "enemy", "m_type": "adds", "mods": ["health", "defense"]},
    "Physical": {"target": "enemy", "m_type": "adds", "mods": ["health", "defense"]},
    "Restore": {"target": "self", "m_type": "mults", "mods": ["health", "defense", "energy"]},
    "Buff": {
        "target": "self",
        "m_type": "mults",
        "mods": ["health", "energy", "attack", "defense"],
    },
    "Debuff": {
        "target": "enemy",
        "m_type": "mults",
        "mods": ["health", "energy", "attack", "defense"],
    },
    "None": {
        "target": "None",
        "m_type": "adds",
        "mods": [],
    },  # TODO: Change to 'Basic' types or something that is not none
}


# def get_ability_effect_type(a_type: str) -> Tuple[str, int]:
#     "Returns the effect type of the provided ability"
#     return ABILITY_TYPES[a_type]


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
