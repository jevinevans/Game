"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing modifiers.
"""
###
# May use the builder class
# - This needs to be able to read all of the available and accepted stats
# - allow the user/app to build out modifiers that can be used on abilities and equipment.
###
from typing import Optional

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.modifiers import Modifier
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    number_range_validation,
    string_validation,
    yes_no_validation,
)
from funclg.utils.types import MOD_ADD_RANGE, MOD_MULT_RANGE, MODIFIER_TYPES

# TODO: Create/modify the build to allow for random creation

MODIFIER_DATA = {"filename": "modifiers.json", "data": {}}


# def mod_name_duplicate_check(): # TODO Create Me
# def export_db() # TODO Create me
# Needs to change all Modifiers to a json like form to be written out
# def load_db() # TODO Create me
# Needs to load all data from json and convert items into modifiers to be used in game


def build_modifier(name: Optional[str] = ""):
    available_mods = MODIFIER_TYPES.copy()
    adds, mults = {}, {}
    from_method = False

    # TODO: Add name validation check, this needs to be a function so that it can be called in other managers
    print("Create a new Modifier:")
    if name:
        from_method = True
        print(f"Name: {name}")
    else:
        print("Please name the modifier?")
        name = string_validation("Name")

    while True:
        print("Select which stats you want to modify.")
        mod_type = list_choice_selection(available_mods)

        if list_choice_selection(["Base Change", "Percentage Change"]) == "Base Change":
            mod_val = number_range_validation(-MOD_ADD_RANGE, MOD_ADD_RANGE)

            print(f"You created modifier: {mod_type} {mod_val}")
            if yes_no_validation("Confirm creation?"):
                adds[mod_type] = mod_val

        else:
            mod_val = number_range_validation(-MOD_MULT_RANGE, MOD_MULT_RANGE)
            while mod_val > 1:
                mod_val /= 10
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val}%")
            if yes_no_validation("Confirm creation?"):
                mults[mod_type] = mod_val

        if yes_no_validation("Would you like to add another?"):
            available_mods.remove(mod_type)
        else:
            break

    new_mod = Modifier(name=name, adds=adds, mults=mults)

    MODIFIER_DATA["data"][new_mod._id] = new_mod.export()
    db.update_data(MODIFIER_DATA)
    if from_method:
        return new_mod


def select_modifier():
    if MODIFIER_DATA["data"]:
        mod_id = char_manager_choice_selection(MODIFIER_DATA["data"], "name", "_id")
        return MODIFIER_DATA["data"][mod_id]
    logger.warning("There are no modifiers available.")
    return None


def edit_modifier():
    print("TODO: Build Edit Modifier Section")


def delete_modifier():
    del_mod = select_modifier()
    if del_mod:
        if yes_no_validation(f"Do you want to delete \"{del_mod['name']}\"?"):
            print(f"Deleting {del_mod}")
            del MODIFIER_DATA["data"][del_mod["_id"]]
            db.update_data(MODIFIER_DATA)
            return
    logger.warning("There are currently no modifiers to delete.")


MODIFIER_MENU = {
    "name": "Manage Mods",
    "description": "This is the menu to manage Modifiers which can be used for weapons an applied to stats.",
    "menu_items": [
        {"name": "New Modifier", "action": build_modifier},
        {"name": "Edit Modifier", "action": edit_modifier},
        {"name": "Delete Modifier", "action": delete_modifier},
    ],
}

MODIFIER_DATA = db.load_data(MODIFIER_DATA)
