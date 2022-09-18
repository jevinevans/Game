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
from typing import Optional, ValuesView

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

MODIFIER_DATA = {"filename": "modifiers.json", "data": {}, "objects": {}}


# def mod_name_duplicate_check(): # TODO Create Me

def update_data():
    db.update_data(MODIFIER_DATA)

    # Compare objects, add missing and update existing
    for id, data in MODIFIER_DATA["data"].items():

        # Add any new objects
        if id not in MODIFIER_DATA["objects"]:
            MODIFIER_DATA["objects"][id] = Modifier(**data)


def export_data():
    for id, data in MODIFIER_DATA['objects'].items():
        MODIFIER_DATA["data"][id] = data.export()

    db.update_data(MODIFIER_DATA)


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
                mod_val /= 100
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val*100}%")
            if yes_no_validation("Confirm mod creation?"):
                mults[mod_type] = mod_val

        if yes_no_validation("Would you like to add another modifier?"):
            available_mods.remove(mod_type)
        else:
            break

    if yes_no_validation(f"Validate Modifier: {name}\n\tAdds: {adds}\n\tMults: {mults}\n\r"):

        new_mod = Modifier(name=name, adds=adds, mults=mults)

        MODIFIER_DATA["data"][new_mod.id] = new_mod.export()
        update_data()
        if from_method:
            return new_mod


def select_modifier():
    if MODIFIER_DATA["data"]:
        return char_manager_choice_selection(MODIFIER_DATA["data"], "name", "_id")
    logger.warning("There are no modifiers available.")
    return None


def show_modifier():
    show_mod_id = select_modifier()
    if show_mod_id:
        show_mod = MODIFIER_DATA['objects'][show_mod_id]
        print(show_mod.details())


# def edit_modifier(mod_id=None):
#     # Because these can be edited with other methods, need to make sure its call
#     edit_mod = select_modifier()

#     if edit_mod:
#         # print out mod information
#         # Print out editable
#     raise NotImplementedError


def delete_modifier():
    del_mod_id = select_modifier()
    if del_mod_id:
        del_mod = MODIFIER_DATA["data"][del_mod_id]
        if yes_no_validation(f"Do you want to delete \"{del_mod['name']}\"?"):
            print(f"Deleting {del_mod['name']}")
            del MODIFIER_DATA["data"][del_mod_id]
            del MODIFIER_DATA["object"][del_mod_id]
            update_data()
            return
    logger.warning("There are currently no modifiers to delete.")

MODIFIER_MENU = {
    "name": "Manage Mods",
    "description": "This is the menu to manage Modifiers which can be used for weapons an applied to stats.",
    "menu_items": [
        {"name": "New Modifier", "action": build_modifier},
        {"name": "View Modifier Details", "action": show_modifier},
        # {"name": "Edit Modifier", "action": edit_modifier},
        {"name": "Delete Modifier", "action": delete_modifier},
    ],
}


MODIFIER_DATA = db.load_data(MODIFIER_DATA)

for id, data in MODIFIER_DATA["data"].items():
    MODIFIER_DATA["objects"][id] = Modifier(**data)
