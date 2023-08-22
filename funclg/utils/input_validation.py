"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Centralized utility module to manage input validation (user choice, data cleaning, etc.)
"""

from string import ascii_letters, digits
from typing import Any, Dict, List, Optional, Union

import questionary
from questionary import ValidationError, Validator

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


def selection_validation(
    prompt: str,
    items: Union[List[Any], Dict[str, Any]],
    display_param: Optional[str] = "",
    return_param: Optional[str] = "",
):
    """
    Validates user selection choices

    :param prompt: The message displayed to the user
    :type prompt: str
    :param items: A Dict or List of items that the user selects from
    :type items: Union[List[Any], Dict[str, Any]]
    :param display_param: The value from a Dict the user wants displayed. If no value is sent then the index is used, defaults to ""
    :type display_param: Optional[str], optional
    :param return_param: The value from a Dict the user wants returned. If no value is selected it will return the Display param or index, defaults to ""
    :type return_param: Optional[str], optional
    :return: The item from the requested list
    :rtype: Any
    """

    # 4 Cases
    # 1) List - Needs to be converted into a string value for display
    # 2) Plain Dict - Will use the index key as the display and return value
    # 3) Dict + Display Param - Will display another key than the index key
    # 4) Dict + Display Param + Return Param - Will display another key than the index and return the specified return value
    selection_choices = []

    if isinstance(items, list):  # Case 1
        selection_choices = [questionary.Choice(title=str(x), value=x) for x in items]

    else:
        for index, data in items.items():  # Handles Case 2-4
            selection_choices.append(
                questionary.Choice(
                    title=data.get(display_param, index), value=data.get(return_param)
                )
            )

    return questionary.select(message=prompt, choices=selection_choices).ask()


def confirmation(prompt: str):
    """
    Provides a confirmation step for user actions

    :param prompt: The message displayed to the user
    :type prompt: str
    :return: Returns True or False based on user selection
    :rtype: bool
    """
    return questionary.confirm(prompt).ask()


class NumberValidation(Validator):
    """
    Validator class for user input, validates that the user sends a number.
    """

    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value", cursor_position=len(document.text)
            )
        if not document.text.isdigit():
            raise ValidationError(
                message="Please enter a valid number", cursor_position=len(document.text)
            )


def number_range_validation(min_val: int = 1, max_val: int = 100) -> int:
    """
    Validates user input of an integer is within the supplied range.

    :param min_val: The minimum (inclusive) number the user can enter, defaults to 1
    :type min_val: int
    :param max_val: The maximum (inclusive) number the user can enter, defaults to 100
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
