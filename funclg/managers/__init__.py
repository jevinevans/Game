"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from .abilities_manager import ABILITY_MENU
from .character_manager import CHARACTER_MENU
from .equipment_manager import EQUIPMENT_MENU
from .modifier_manager import MODIFIER_MENU
from .roles_manager import ROLES_MENU

MENUS = [ABILITY_MENU, CHARACTER_MENU, EQUIPMENT_MENU, MODIFIER_MENU, ROLES_MENU]


def build_manager_menu():
    builder_menu = {}
    for index, menu in enumerate(MENUS, start=1):
        builder_menu[str(index)] = menu

    return builder_menu
