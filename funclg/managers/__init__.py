"""
These are a group of managers classes to allow users to manage the game and create objects
"""

from funclg.managers.abilities_manager import AbilitiesManager
from funclg.managers.character_manager import CharacterManager
from funclg.managers.equipment_manager import EquipmentManager
from funclg.managers.game_manager import GameManager
from funclg.managers.npc_manager import NPCManager
from funclg.managers.roles_manager import RolesManager
from funclg.utils.menu_funcs import Menu

CHAR_MANAGERS = [
    CharacterManager(),
    RolesManager(),
    AbilitiesManager(),
    EquipmentManager(),
]
GAME_MANAGERS = [GameManager(), NPCManager()]

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
        print(manager.name, manager.menu)
        sub_menu = Menu.build_menu(**manager.menu)
        char_menu.add_item(sub_menu.name, sub_menu)
    return char_menu


def build_game_menu():
    game_menu = Menu("Game Settings", "Manage game and level settings.")
    for manager in GAME_MANAGERS:
        sub_menu = Menu.build_menu(**manager.menu)
        game_menu.add_item(sub_menu.name, sub_menu)
    return game_menu


def load_data():
    for manager in ALL_MANAGERS:
        manager.load_data()


def save_data():
    for manager in ALL_MANAGERS:
        manager.export_data()
