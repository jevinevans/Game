"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing roles.
"""

from funclg.character.roles import Roles


def build_role():
    print("TODO: Build New Role Section")


def edit_role():
    print("TODO: Build Edit Role Section")


def delete_role():
    print("TODO: Build Delete Role Section")


ROLES_MENU = {
    "name": "Manage Roles",
    "description": "This is the menu to manage character roles/classes. Build a class and the attributes to go with it.",
    "menu_items": [
        {"name": "New Role", "action": build_role},
        {"name": "Edit Role", "action": edit_role},
        {"name": "Delete Role", "action": delete_role},
    ],
}
