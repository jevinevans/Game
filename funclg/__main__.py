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
from funclg.utils.menu_funcs import *

# TODO: Auto generate this

MENU = {
    "1": {"name": "Play", "sub-menu": {}},
    "2": {"name": "Manage Game", "sub-menu": build_manager_menu()},
    "3": {"name": "Exit", "function": save_exit},
}

while True:
    print_menu(MENU)
