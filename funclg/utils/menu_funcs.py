"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

from typing import Any, Dict, List

from funclg.utils.input_validation import choice_validation


# TODO: 20220822 - Create an issue to track the update/integration of questionary into the menu
class Menu:
    """Creates an interactive menu that can be used to create multiple connected menus"""

    def __init__(self, name: str, description: str, has_return: bool = True):
        self.name = name
        self.description = description
        self.menu_items = []

        self.has_return = has_return
        self.return_val = 1 if has_return else 0

    def add_item(self, name: str, action):
        self.menu_items.append({"name": name, "action": action})
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
            choice = choice_validation(len(self.menu_items) + 1)
        else:
            choice = choice_validation(len(self.menu_items))

        if choice == self.return_val:
            return

        action = self.menu_items[choice - 1]["action"]

        if isinstance(action, Menu):
            action.print_menu()
        else:
            action()

        self.print_menu()

    @staticmethod
    def build_menu(
        name: str, description: str, menu_items: List[Dict[str, Any]], has_return: bool = True
    ):
        new_menu = Menu(name, description, has_return)
        for item in menu_items:
            new_menu.add_item(**item)
        return new_menu
