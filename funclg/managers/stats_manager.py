"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing modifiers.
"""

from random import randint
from typing import Any, Dict

from loguru import logger

from funclg.character.modifiers import Modifier
from funclg.character.stats import Stats
from funclg.utils.input_validation import (
    confirmation,
    number_range_validation,
    selection_validation,
)


def _gen_base_mod(mod_list: list, base: Dict[str, Any], random: bool = False):
    if random:
        base_mod = mod_list.pop(randint(0, len(mod_list) - 1))
    else:
        base_mod = mod_list[0]
    base_value = randint(1, Modifier.MOD_BASE_RANGE)
    base.setdefault(base_mod, base_value)
    return base


def _gen_percentage_mod(mod_list: list, percentages: Dict[str, Any], random: bool = False):
    if random:
        percentage_mod = mod_list.pop(randint(0, len(mod_list) - 1))
    else:
        percentage_mod = mod_list[0]
    percentage_value = randint(1, Modifier.MOD_PERCENTAGE_RANGE)
    logger.debug(f"Mult Value: {percentage_value}")
    while percentage_value > 1:
        percentage_value /= 100
    percentage_value = round(percentage_value, 2)

    percentages.setdefault(percentage_mod, percentage_value)
    return percentages


# Notes for change
# Create/modify the build to allow for random creation
# Modifiers are specific to the item that they are attached to and do not need to have custom names. This manager needs to be updated to just create the base and percentages of a mod and return that dictionary to a calling function. Modifiers will not be directly custom created or tracked.
# Convert method to be able to handle multiple types of modifier generations. May require creating sub methods for the different types, weapon, armor, and abilities
# Needs to provide the capability to decide which m_type should be used or both, also how many modifiers can be applied, or just simply random
# 2023.10.24 - May need/want to combine with below method or create a handler that will call manual or automatic and just have one call
def generate_modifier(item_type: str = "", pre_mods: Dict[str, Any] = None, random: bool = False):
    base, percentage = {}, {}
    pre_mods = pre_mods if pre_mods else {}

    mod_types = Modifier.MODIFIER_TYPES

    if item_type == "ability":
        mod_types = pre_mods["mods"].copy()
        if pre_mods["m_type"] == "base":
            base = _gen_base_mod(mod_types, base, random)
        else:
            percentage = _gen_percentage_mod(mod_types, percentage, random)

    else:
        if item_type == "armor":
            mod_types = ["health", "defense"]

        elif item_type == "weapon":
            mod_types = ["energy", "attack"]

        base = _gen_base_mod(mod_types, base)
        percentage = _gen_percentage_mod(mod_types, percentage)

    logger.debug(f"MOD: base: {base}, percentage: {percentage}")
    return {"base": base, "percentage": percentage}


# 20221112 - Change function to be allow the user to define each attribute of the MOD type, for each type decide if wanted or not, if so which type (percetage or base) (positive or nega), return values.
# 2023.10.24 - May need/want to combine with above method or create a handler that will call manual or automatic and just have one call
def build_modifier(name: str):
    available_mods = Modifier.MODIFIER_TYPES.copy()
    base, percentage = {}, {}

    print("\nStarting Modifier Creation...\n")

    while True:
        mod_type = selection_validation("Select which stats you want to modify.", available_mods)

        if (
            selection_validation(
                "What type of change would you like to make", ["Base Change", "Percentage Change"]
            )
            == "Base Change"
        ):
            mod_val = number_range_validation(-Modifier.MOD_BASE_RANGE, Modifier.MOD_BASE_RANGE)

            print(f"You created modifier: {mod_type} {mod_val}")
            if confirmation("Confirm creation?"):
                base[mod_type] = mod_val

        else:
            mod_val = number_range_validation(
                -Modifier.MOD_PERCENTAGE_RANGE, Modifier.MOD_PERCENTAGE_RANGE
            )
            while mod_val > 1:
                mod_val /= 100
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val*100}%")
            if confirmation("Confirm mod creation?"):
                percentage[mod_type] = mod_val

        if confirmation("Would you like to add another modifier?"):
            available_mods.remove(mod_type)
        else:
            logger.debug("Constructing modifier...")
            break
    if confirmation(f"Validate Modifier: {name}\n\tBase: {base}\n\tPercentage: {percentage}\n\r"):
        new_mod = Modifier(name=name, base=base, percentage=percentage)

        return new_mod
    return None


def build_stats():
    print("\nStarting Stats Creation...\n")
    print(
        f"Stats are made up of 4 attributes {', '.join(Stats.BASE_ATTRIBUTES)} with a base value of {Stats.STAT_DEFAULT}."
    )

    attributes = {_attr: Stats.STAT_DEFAULT for _attr in Stats.BASE_ATTRIBUTES}

    while True:
        print("Current Attributes:")
        for _a, _v in attributes.items():
            print(f"{_a}: {_v}")

        attr_choice = selection_validation(
            "Which stat would you like to customize", list(attributes)
        )

        print(
            f"What would you like to set {attr_choice.capitalize()} to ({Stats.STAT_DEFAULT} <= x <= {Modifier.MOD_BASE_RANGE})?"
        )
        attr_value = number_range_validation(Stats.STAT_DEFAULT, Modifier.MOD_BASE_RANGE)

        if confirmation(f"Confirm updating {attr_choice} to {attr_value}?"):
            attributes.update({attr_choice: attr_value})

        if not confirmation("Do you want to change another stat?"):
            logger.debug("Building Stats")
            break

    return {"attributes": attributes}
