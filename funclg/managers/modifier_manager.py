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
from random import randint
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

# TODO: Create/modify the build to allow for random creation
"""
    Modifiers are specific to the item that they are attached to and do not need to have custom names. This manager needs to be updated to just create the adds and mults of a mod and return that dictionary to a calling function. Modifiers will not be directly custom created or tracked.

"""

MODIFIER_DATA = {"filename": "modifiers.json", "data": {}, "objects": {}}


# def mod_name_duplicate_check(): # TODO Create Me


def update_data():  # TODO Delete Function
    db.update_data(MODIFIER_DATA)

    # Compare objects, add missing and update existing
    for _id, data in MODIFIER_DATA["data"].items():

        # Add any new objects
        if _id not in MODIFIER_DATA["objects"]:
            MODIFIER_DATA["objects"][_id] = Modifier(**data)


def export_data():  # TODO Delete Function
    for _id, data in MODIFIER_DATA["objects"].items():
        MODIFIER_DATA["data"][_id] = data.export()

    db.update_data(MODIFIER_DATA)


def generate_modifier(item_type: str = ""):
    adds, mults = {}, {}

    mod_types = ["attack", "energy", "health", "defense"]

    if item_type == "armor":
        mod_types = ["health", "defense"]

    elif item_type == "weapon":
        mod_types = ["energy", "attack"]

    add_mod = mod_types.pop(randint(0, len(mod_types)))
    add_value = randint(1, Modifier.MOD_ADD_RANGE)
    try:
        mult_mod = mod_types.pop(randint(0, len(mod_types)))
    except IndexError:
        mult_mod = mod_types.pop()

    mult_value = randint(1, Modifier.MOD_MULT_RANGE)

    while mult_value > 1:
        mult_value /= 100
    mult_value = round(mult_value, 2)

    adds.setdefault(add_mod, add_value)
    mults.setdefault(mult_mod, mult_value)

    return {"adds": adds, "mults": mults}


# TODO: Change function to be allow the user to define each attribute of the MOD type, for each type decide if wanted or not, if so which type (percetage or base) (positive or nega), return values.
def build_modifier(name: Optional[str] = ""):
    available_mods = Modifer.MODIFIER_TYPES.copy()
    adds, mults = {}, {}
    from_method = False

    print("\nStarting Modifier Creation...\n")
    if name:
        from_method = True
        print(f"Name: {name}")
    else:
        name = string_validation("Please name the modifier?", "Name")

    while True:
        print("Select which stats you want to modify.")
        mod_type = list_choice_selection(available_mods)

        if list_choice_selection(["Base Change", "Percentage Change"]) == "Base Change":
            mod_val = number_range_validation(-Modifier.MOD_ADD_RANGE, Modifier.MOD_ADD_RANGE)

            print(f"You created modifier: {mod_type} {mod_val}")
            if yes_no_validation("Confirm creation?"):
                adds[mod_type] = mod_val

        else:
            mod_val = number_range_validation(-Modifier.MOD_MULT_RANGE, Modifier.MOD_MULT_RANGE)
            while mod_val > 1:
                mod_val /= 100
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val*100}%")
            if yes_no_validation("Confirm mod creation?"):
                mults[mod_type] = mod_val

        if yes_no_validation("Would you like to add another modifier?"):
            available_mods.remove(mod_type)
        else:
            logger.debug("Constructing modifier...")
            break

    if yes_no_validation(f"Validate Modifier: {name}\n\tAdds: {adds}\n\tMults: {mults}\n\r"):

        new_mod = Modifier(name=name, adds=adds, mults=mults)

        MODIFIER_DATA["data"][new_mod.id] = new_mod.export()
        update_data()
        if from_method:
            return new_mod


def select_modifier():  # TODO Delete Function
    if MODIFIER_DATA["data"]:
        return char_manager_choice_selection(MODIFIER_DATA["data"], "name", "_id")
    logger.warning("There are no modifiers available.")
    return None


def show_modifier():  # TODO Delete Function
    show_mod_id = select_modifier()
    if show_mod_id:
        show_mod = MODIFIER_DATA["objects"][show_mod_id]
        print(show_mod.details())


def delete_modifier():  # TODO Delete Function
    del_mod_id = select_modifier()
    if del_mod_id:
        del_mod = MODIFIER_DATA["data"][del_mod_id]
        if yes_no_validation(f"Do you want to delete \"{del_mod['name']}\"?"):
            print(f"Deleting {del_mod['name']}")
            del MODIFIER_DATA["data"][del_mod_id]
            del MODIFIER_DATA["objects"][del_mod_id]
            update_data()
            return
    else:
        logger.warning("There are currently no modifiers to delete.")


# TODO Delete Function
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


# TODO Delete Function
MODIFIER_DATA = db.load_data(MODIFIER_DATA)

# TODO Delete Function
for _id, _data in MODIFIER_DATA["data"].items():
    MODIFIER_DATA["objects"][_id] = Modifier(**_data)
