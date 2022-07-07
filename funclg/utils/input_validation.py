"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: Centralized utility module to manage input validation (user choice, data cleaning, etc.)
"""

from typing import Any, List


def choice_validation(max_choice: int) -> int:
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
    return "".join(i for i in value if i.isalnum() or i.isspace())


def string_validation(value: str):
    return remove_special_chars(input(f"Enter {value}: "))


def list_choice_selection(items: List[Any]):
    for index, item in enumerate(items, start=1):
        print(f"{index} --- {item}")
    return items[choice_validation(len(items)) - 1]


def yes_no_validation(prompt: str):
    choice = ""
    while choice not in ["y", "Y", "N", "n"]:
        choice = input(prompt + " [y/N]:")

    if choice in ["y", "Y"]:
        return True
    return False


def number_range_validation(min_val: int, max_val: int):
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
