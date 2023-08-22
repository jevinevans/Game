"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Centralized utility module to manage input validation (user choice, data cleaning, etc.)
"""

from string import ascii_letters, digits
from typing import Any, Dict, List

import questionary
from questionary import ValidationError, Validator


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


def confirmation(prompt: str):
    """Provides a yes/no validation. Provide the prompt, the function will add [y|N] for you."""
    return questionary.confirm(prompt).ask()


class NumberValidation(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value", cursor_position=len(document.text)
            )
        if not document.text.isdigit():
            raise ValidationError(
                message="Please enter a valid number", cursor_position=len(document.text)
            )


def number_range_validation(min_val: int, max_val: int) -> int:
    """
    Validates user input of an integer is within the supplied range.

    :param min_val: The minimum (inclusive) number the user can enter
    :type min_val: int
    :param max_val: The maximum (inclusive) number the user can enter
    :type max_val: int
    :return: The users entered response
    :rtype: int
    """
    print(f"Choice number in range [{min_val} - {max_val}]: ")
    user_resp = min_val - 1
    while user_resp < min_val or user_resp > max_val:
        user_resp = int(
            questionary.text(
                "Please enter a number:", validate=NumberValidation, validate_while_typing=False
            ).ask()
        )
    return user_resp
