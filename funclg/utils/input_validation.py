"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Centralized utility module to manage input validation (user choice, data cleaning, etc.)
"""

from string import ascii_letters, digits
from typing import Any, Dict, List


def choice_validation(max_choice: int) -> int:
    """
    Validates a numeric choice from 0 to [max].
    """
    while True:
        try:
            user_resp = int(input("CHOICE: "))

            if user_resp < 0 or user_resp > max_choice:
                raise ValueError()
        except ValueError:
            print(f"Invalid Answer: Please enter a number between 1 and {max_choice}")
            continue
        else:
            return user_resp


def remove_special_chars(value: str) -> str:
    """
    Removes special characters from a string.
    """
    safe_vals = ascii_letters + digits + "_" + " "
    return "".join(i for i in value if i in safe_vals)


def string_validation(prompt: str, value: str):
    """
    Filters string input to only specified safe characters
    """
    return remove_special_chars(input(f"{prompt}\nEnter {value}: "))


def list_choice_selection(items: List[Any]):
    """
    Provided a list of items will return an item from the list.
    """
    # TODO: Decide if the capitalize needs to stay here or not
    for index, item in enumerate(items, start=1):
        print(f"{index} --- {item.capitalize()}")
    return items[choice_validation(len(items)) - 1]


def char_manager_choice_selection(data: Dict[str, Any], show_param: str, return_param: str):
    """
    For data managers, reads the data dictionary, provides a list from the [show_param] and will return the [return_param] as selected.
    """
    items = [(_data[show_param], _data[return_param]) for _, _data in data.items()]
    for index, item in enumerate(items, start=1):
        print(f"{index} --- {item[0]}")
    return items[choice_validation(len(items)) - 1][1]


def yes_no_validation(prompt: str):
    """Provides a yes/no validation. Provide the prompt, the function will add [y|N] for you."""
    choice = ""
    while choice not in ["y", "Y", "N", "n"]:
        choice = remove_special_chars(input(prompt + " [y/N]:"))

    if choice in ["y", "Y"]:
        return True
    return False


def number_range_validation(min_val: int, max_val: int):
    """Provided a min and max value, this will validate a number in the selected range"""
    while True:
        try:
            user_resp = int(input(f"Choice number in range [{min_val} - {max_val}]: "))

            if user_resp < min_val or user_resp > max_val:
                raise ValueError("Out of Range")
        except ValueError:
            print(f"Invalid Answer: Please enter a number between {min_val} and {max_val}")
            continue
        else:
            return user_resp
