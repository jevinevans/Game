"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing characters.
"""

from funclg.character.character import Character


def build_new_character():
    print("TODO: Build New Character Section")


def edit_character():
    print("TODO: Build Edit Character Section")


def delete_character():
    print("TODO: Build Delete Character Section")


CHARACTER_MENU = {
    "name": "Manage Characters",
    "description": "This is the menu to create characters to use in game.",
    "menu_items": [
        {"name": "New Character", "action": build_new_character},
        {"name": "Edit Character", "action": edit_character},
        {"name": "Delete Character", "action": delete_character},
    ],
}
