"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing roles.
"""

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.roles import Roles
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    yes_no_validation,
)

ROLES_DATA = {"filename": "roles.json", "data": {}, "objects": {}}

# def mod_name_duplicate_check(): # TODO Create Me
# def export_db() # TODO Create me
# Needs to change all Modifiers to a json like form to be written out
# def load_db() # TODO Create me
# Needs to load all data from json and convert items into modifiers to be used in game


def build_role():
    raise NotImplementedError


def select_role():
    if ROLES_DATA["data"]:
        role_id = char_manager_choice_selection(ROLES_DATA["data"], "name", "_id")
        return ROLES_DATA["data"][role_id]
    logger.warning("There are no roles available.")
    return None


def edit_role():
    raise NotImplementedError


def delete_role():
    del_role = select_role()
    if del_role:
        if yes_no_validation(f"Do you want to delete \"{del_role['name']}\"?"):
            print(f"Deleteing {del_role}")
            del ROLES_DATA["data"][del_role["_id"]]
            db.update_data(ROLES_DATA)
    logger.warning("There are no roles available.")


ROLES_MENU = {
    "name": "Manage Roles",
    "description": "This is the menu to manage character roles/classes. Build a class and the attributes to go with it.",
    "menu_items": [
        {"name": "New Role", "action": build_role},
        {"name": "Edit Role", "action": edit_role},
        {"name": "Delete Role", "action": delete_role},
    ],
}

# TODO Remove me
# ROLES_DATA = db.load_data(ROLES_DATA)
