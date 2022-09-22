"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from funclg.utils.menu_funcs import Menu

from . import abilities_manager as ability_man
from . import character_manager as char_man
from . import equipment_manager as equip_man
from . import modifier_manager as mod_man
from . import roles_manager as role_man

MENUS = [
    char_man.CHARACTER_MENU,
    role_man.ROLES_MENU,
    ability_man.ABILITY_MENU,
    equip_man.EQUIPMENT_MENU,
    mod_man.MODIFIER_MENU,
]

# UPDATERS = [

# ]


def build_manager_menu():
    builder_menu = Menu("Manage Game", "This is the menu to manage all character items.")
    for menu in MENUS:
        sub_menu = Menu.build_menu(**menu)
        builder_menu.add_item(sub_menu.name, sub_menu)
    return builder_menu

# def save_data():