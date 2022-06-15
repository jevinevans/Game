from typing import Any, Dict, Union
import sys
from funclg.utils.input_validation import choice_validation


def save_exit() -> None:
    "Fill in stuff"
    print("Saving and closing")
    sys.exit()


# TODO: add a description value to menus and have them printed out when called
# TODO: Need to add an ability to go back and not always start at the top menu
def print_menu(menu: Dict[str, Any]):
    print("MENU")
    for key, value in menu.items():
        print(f"{key}. --- {value['name']}")

    choice = choice_validation(len(menu))

    # Sub Menu
    if menu[choice].get("sub-menu", False):
        print_menu(menu[choice]["sub-menu"])

    # Function Action
    elif menu[choice].get("function", False):
        menu[choice]["function"]()

    # Return to previous menu
    elif menu[choice].get("return", False):
        return
    print_menu(menu)


class Menu():
    def __init__(self, name:str, description:str, has_return:bool=True):
        self.name = name
        self.description = description
        self.menu_items = []

        self.has_return = has_return
        self.return_val = 1 if has_return else 0
    
    def add_item(self, name:str, action):
        self.menu_items.append({"name":name, "action":action})
        if self.has_return:
            self.return_val += 1

    def print_menu(self):
        print(self.name)
        if self.description: 
            print(f"\t{self.description}")

        for index, value in enumerate(self.menu_items, start=1):
            print(f"{index}. --- {value['name']}")

        if self.has_return:
            print(f"{len(self.menu_items)+1}. --- Go Back")
            choice = choice_validation(len(self.menu_items)+1)
        else:
            choice = choice_validation(len(self.menu_items))

        if choice == self.return_val:
            return 
        
        action = self.menu_items[choice-1]['action']

        if isinstance(action, Menu):
            action.print_menu()
        else:
            action()
        
        self.print_menu()
        

    