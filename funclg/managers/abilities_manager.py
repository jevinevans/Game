"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing abilities.
"""

from funclg.character.abilities import Abilities


def build_ability():
    print("TODO: Build New Ability Section")


def edit_ability():
    print("TODO: Build Edit Ability Section")


def delete_ability():
    print("TODO: Build Delete Ability Section")


ABILITY_MENU = {
    "name": "Manage Abilities",
    "description": "This is the menu to create abilities to add to Roles for characters to use.",
    "menu_items": [
        {"name": "Add New Ability", "action": build_ability},
        {"name": "Edit Ability", "action": edit_ability},
        {"name": "Delete Ability", "action": delete_ability},
    ],
}
