"""
Welcom message

set up and loading

menu
    - Play
        - if there is a character created, have load option on top
        - create character
        - Ask to create a new save world/ load world
    - Character managment
        - creating
        - edit
        - delete
    - settings
        - Manage Content
            - Equipment
            - Roles
            - Powers
            - Enemies
        - game settings (not sure yet)
            - difficulyy
            - number of levels?

"""
import os

from funclg.managers import build_manager_menu
from funclg.utils.data_mgmt import setup_data_path
from funclg.utils.menu_funcs import Menu, save_exit


def build_main_menu():
    """Contructs the main menu for the game"""
    menu = Menu("Main Menu", "Please choice an option:", has_return=False)
    menu.add_item("Play", None)  # TODO: add play instance
    menu.add_item("Manage Game", build_manager_menu())
    menu.add_item("Exit", save_exit)
    return menu


def game_set_up():
    # Set up data folder
    setup_data_path(os.path.dirname(__file__))
    return build_main_menu()


def main():
    main_menu = game_set_up()
    try:
        while True:
            main_menu.print_menu()

    except KeyboardInterrupt:
        print()
        save_exit()


if __name__ == "__main__":
    main()
