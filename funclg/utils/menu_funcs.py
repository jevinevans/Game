"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Utility class used for data/database actions loading, saving, updating.
"""

from typing import Any, Dict, List

from funclg.utils.input_validation import selection_validation


class Menu:
    """Creates an interactive menu that can be used to create multiple connected menus"""

    def __init__(self, name: str, description: str, has_return: bool = True):
        self.name = name
        self.prompt = f"{name}: {description}"
        self.menu_items = {}
        self.has_return = has_return

    def add_item(self, title: str, value):
        self.menu_items[title] = value

    def print_menu(self):
        if self.has_return:
            self.menu_items["Go Back"] = None

        choice = selection_validation(prompt=self.prompt, items=list(self.menu_items.keys()))
        action = self.menu_items[choice]

        if isinstance(action, Menu):
            action.print_menu()
        elif action is None:
            return
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
