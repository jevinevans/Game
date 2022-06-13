from typing import Any, Dict


def save_exit() -> None:
    "Fill in stuff"
    print("Saving and closing")
    exit()


def print_menu(menu: Dict[str, Any]):
    print("MENU")
    for key, value in menu.items():
        print(f"{key}. --- {value['name']}")

    choice = -1
    while choice < 0 or choice > len(menu):
        choice = int(input("CHOICE: "))
    choice = str(choice)

    # Sub Menu
    if menu[choice].get("sub-menu", False):
        print_menu(menu[choice]["sub-menu"])

    # Function Action
    elif menu[choice].get("function", False):
        menu[choice]["function"]()
