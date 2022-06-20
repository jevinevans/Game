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


def build_main_menu():
    """Contructs the main menu for the game"""
    menu = Menu("Main Menu", "Please choice an option:", has_return=False)
    menu.add_item("Play", None)  # TODO: add play instance
    menu.add_item("Manage Game", build_manager_menu())
    menu.add_item("Exit", save_exit)
    return menu


MAIN_MENU = build_main_menu()

while True:
    # print_menu(MENU)
    MAIN_MENU.print_menu()
