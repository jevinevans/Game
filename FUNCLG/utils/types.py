#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/13/2021                                                                 #
#   Program: Types                                                                  #
#   Description: This defines lists and functions for certain constands             #
#####################################################################################

# Item Types: 0 - Head, 1 - Chest, 2 - Back, 3 - Pants, 4 - Weapon
ITEM_TYPES = ["Head", "Chest", "Back", "Pants", "Weapon"]

# Armor Types: 0 - Light,  1 - Medium,  2 - Heavy
ARMOR_TYPES = ["Light", "Medium", "Heavy"]

# Weapon Types: 0 - Sword, 1 - Wand, 2 - Knife
WEAPON_TYPES = ["Sword", "Wand", "Knife"]


def getItemType(IT: int) -> str:
    return ITEM_TYPES[IT]


def getArmorType(AT: int) -> str:
    return ARMOR_TYPES[AT]


def getWeaponType(WT: int) -> str:
    return WEAPON_TYPES[WT]


def getItemDescription(IT=None, AT=None, WT=None) -> str:
    item = ""

    if IT is not None:
        if IT == 4 and WT is not None:
            item += getWeaponType(WT)
        else:
            item += getItemType(IT)
    elif WT is not None:
        item = getWeaponType(WT)
    else:
        item = "Broken Item"

    if AT is not None:
        item = getArmorType(AT) + " " + item

    return "[" + item + "]"
