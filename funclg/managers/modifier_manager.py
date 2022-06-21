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

from funclg.character.modifiers import Modifier
from funclg.utils.input_validation import (
    list_choice_selection,
    number_range_validation,
    string_validation,
    yes_no_validation,
)
from funclg.utils.menu_funcs import Menu
from funclg.utils.types import MOD_ADD_RANGE, MOD_MULT_RANGE, MODIFIER_TYPES
import funclg.utils.data_mgmt as db
# TODO: Create/modify the build to allow for random creation

MODIFIER_DATA = "modifiers.json"

def build_modifier(name: Optional[str] = "", from_method:Optional[bool] = False):
    available_mods = MODIFIER_TYPES.copy()
    adds, mults = {}
    print("Lets create a new Modifier:")
    if name:
        print(f"Name: {name}")
    else:
        print("Please name the modifier?")
        name = string_validation("Name")

    print("Now select which stats you want to modify.")
    while True:
        mod_type = list_choice_selection(available_mods)

        if list_choice_selection(["Base Change", "Percentage Change"]) == "Base Change":
            mod_val = number_range_validation(-MOD_ADD_RANGE, MOD_ADD_RANGE)

            print(f"You created modifier {mod_type}:{mod_val}")
            if yes_no_validation("Confirm creation?"):
                adds[mod_type] = mod_val
            else:
                continue

        else:
            mod_val = number_range_validation(-MOD_MULT_RANGE, MOD_MULT_RANGE)
            while mod_val > 1:
                mod_val /= 10
            print(f"You created modifier {mod_type}:{mod_val}%")
            if yes_no_validation("Confirm creation?"):
                mults[mod_type] = mod_val
            else:
                continue

        if yes_no_validation("Would you like to add another?"):
            available_mods.remove(mod_type)
        else:
            break
    new_mod = Modifier(name=name, adds=adds, mults=mults)
    
    if from_method:
        return new_mod
    # TODO: Replace with proper info
    db.update_data(MODIFIER_DATA, new_mod) 


def edit_modifier():
    print("TODO: Build Edit Modifier Section")


def delete_modifier():
    print("TODO: Build Delete Modifier Section")


MODIFIER_MENU = {
    "name": "Manage Mods",
    "sub-menu": {
        "1": {"name": "New Modifier", "function": build_modifier},
        "2": {"name": "Edit Modifier", "function": edit_modifier},
        "3": {"name": "Delete Modifier", "function": delete_modifier},
    },
}
