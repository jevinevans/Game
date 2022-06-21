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
from funclg.managers import build_manager_menu
from funclg.utils.menu_funcs import Menu, save_exit
from funclg.utils.data_mgmt import setup_data_path
import os

MAIN_MENU = ''


def build_main_menu():
    """Contructs the main menu for the game"""
    menu = Menu("Main Menu", "Please choice an option:", has_return=False)
    menu.add_item("Play", None)  # TODO: add play instance
    menu.add_item("Manage Game", build_manager_menu())
    menu.add_item("Exit", save_exit)
    return menu

def game_set_up():
    global MAIN_MENU

    # Set up data folder
    setup_data_path(os.path.dirname(__file__))
    MAIN_MENU = build_main_menu()
    


def main():
    game_set_up()
    try:
        while True:
            # print_menu(MENU)
            MAIN_MENU.print_menu()
    except KeyboardInterrupt:
        print()
        save_exit()

if __name__ == "__main__":
    main()