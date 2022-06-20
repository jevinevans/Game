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
from funclg.utils.input_validation import string_validation
from funclg.utils.types import MODIFIER_TYPES

# def _create_add():


def build_modifier(name: Optional[str] = ""):
    # TODO: REMOVE TODO Print
    print("TODO: Build New Modifier Section")
    print("Lets create a new Modifier:")
    if name:
        print(f"Name: {name}")
    else:
        print("Please name the modifier?")
        name = string_validation("Name")


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
