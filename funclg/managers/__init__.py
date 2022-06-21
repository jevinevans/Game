"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from funclg.utils.menu_funcs import Menu

from .abilities_manager import ABILITY_MENU
from .character_manager import CHARACTER_MENU
from .equipment_manager import EQUIPMENT_MENU
from .modifier_manager import MODIFIER_MENU
from .roles_manager import ROLES_MENU

MENUS = [ABILITY_MENU, CHARACTER_MENU, EQUIPMENT_MENU, MODIFIER_MENU, ROLES_MENU]


def build_manager_menu():
    builder_menu = Menu("Manage Game", "This is the menu to manage all character items.")
    for menu in MENUS:
        sub_menu = Menu.build_menu(**menu)
        builder_menu.add_item(sub_menu.name, sub_menu)
    return builder_menu
