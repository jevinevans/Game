"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from funclg.utils.menu_funcs import Menu

from . import abilities_manager as ability_man
from . import character_manager as char_man
from . import equipment_manager as equip_man
from . import game_manager as game_man
from . import level_manager as level_man
from . import level_pack_manager as lvl_pack_man
from . import npc_manager as npc_man
from . import roles_manager as role_man

CHAR_MANAGERS = [
    char_man,
    role_man,
    ability_man,
    equip_man,
]
GAME_MANAGERS = [game_man, level_man, lvl_pack_man, npc_man]

ALL_MANAGERS = CHAR_MANAGERS + GAME_MANAGERS


def build_manager_menu():
    manager_menu = Menu("Settings", "Configure the game character and game seetings.")
    char_menu = build_character_menu()
    game_menu = build_game_menu()

    manager_menu.add_item(char_menu.name, char_menu)
    manager_menu.add_item(game_menu.name, game_menu)

    return manager_menu


def build_character_menu():
    char_menu = Menu("Character Settings", "This is the menu to manage all character items.")
    for manager in CHAR_MANAGERS:
        sub_menu = Menu.build_menu(**manager.MENU)
        char_menu.add_item(sub_menu.name, sub_menu)
    return char_menu


def build_game_menu():
    game_menu = Menu("Game Settings", "Manage game and level settings.")
    for manager in GAME_MANAGERS:
        sub_menu = Menu.build_menu(**manager.MENU)
        game_menu.add_item(sub_menu.name, sub_menu)
    return game_menu


def load_data():
    # for manager in ALL_MANAGERS:
    for manager in CHAR_MANAGERS:
        manager.load_data()


def save_data():
    # for manager in ALL_MANAGERS:
    for manager in CHAR_MANAGERS:
        manager.export_data()
