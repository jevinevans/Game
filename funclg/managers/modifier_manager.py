"""
May use the builder class
- This needs to be able to read all of the available and accepted stats
- allow the user/app to build out modifiers that can be used on abilities and equipment.
"""

from distutils.command.build import build

from funclg.character.modifiers import Modifier
from funclg.utils.types import MODIFIER_TYPES


def build_modifier():
    print("TODO: Build New Modifier Section")


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
