"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from funclg.utils.menu_funcs import Menu

from . import equipment_manager as equip_man
from . import abilities_manager as ability_man
from . import roles_manager as role_man
from . import character_manager as char_man

MANAGERS = [
    char_man,
    role_man,
    ability_man,
    equip_man,
]


def build_manager_menu():
    builder_menu = Menu("Manage Game", "This is the menu to manage all character items.")
    for manager in MANAGERS:
        sub_menu = Menu.build_menu(**manager.MENU)
        builder_menu.add_item(sub_menu.name, sub_menu)
    return builder_menu


def save_data():
    for manager in MANAGERS:
        manager.export_data()
