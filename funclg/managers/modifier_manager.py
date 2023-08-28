"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing modifiers.
"""
###
# May use the builder class
# - This needs to be able to read all of the available and accepted stats
# - allow the user/app to build out modifiers that can be used on abilities and equipment.
###
from random import randint
from typing import Any, Dict

from loguru import logger

from funclg.character.modifiers import Modifier
from funclg.utils.input_validation import (
    confirmation,
    number_range_validation,
    selection_validation,
)


def _gen_add_mod(mod_list: list, adds: Dict[str, Any], random: bool = False):
    if random:
        add_mod = mod_list.pop(randint(0, len(mod_list) - 1))
    else:
        add_mod = mod_list[0]
    add_value = randint(1, Modifier.MOD_ADD_RANGE)
    adds.setdefault(add_mod, add_value)
    return adds


def _gen_mult_mod(mod_list: list, mults: Dict[str, Any], random: bool = False):
    if random:
        mult_mod = mod_list.pop(randint(0, len(mod_list) - 1))
    else:
        mult_mod = mod_list[0]
    mult_value = randint(1, Modifier.MOD_MULT_RANGE)
    logger.debug(f"Mult Value: {mult_value}")
    while mult_value > 1:
        mult_value /= 100
    mult_value = round(mult_value, 2)

    mults.setdefault(mult_mod, mult_value)
    return mults


# TODO: Create/modify the build to allow for random creation
# Modifiers are specific to the item that they are attached to and do not need to have custom names. This manager needs to be updated to just create the adds and mults of a mod and return that dictionary to a calling function. Modifiers will not be directly custom created or tracked.
# TODO Convert method to be able to handle multiple types of modifier generations. May require creating sub methods for the different types, weapon, armor, and abilities
# Needs to provide the capability to decide which m_type should be used or both, also how many modifiers can be applied, or just simply random
def generate_modifier(item_type: str = "", pre_mods: Dict[str, Any] = None, random: bool = False):
    adds, mults = {}, {}
    pre_mods = pre_mods if pre_mods else {}

    mod_types = Modifier.MODIFIER_TYPES

    if item_type == "ability":
        mod_types = pre_mods["mods"].copy()
        if pre_mods["m_type"] == "adds":
            adds = _gen_add_mod(mod_types, adds, random)
        else:
            mults = _gen_mult_mod(mod_types, mults, random)

    else:
        if item_type == "armor":
            mod_types = ["health", "defense"]

        elif item_type == "weapon":
            mod_types = ["energy", "attack"]

        adds = _gen_add_mod(mod_types, adds)
        mults = _gen_mult_mod(mod_types, mults)

    logger.debug(f"MOD: adds: {adds}, mults: {mults}")
    return {"adds": adds, "mults": mults}


# TODO: 20221112 - Change function to be allow the user to define each attribute of the MOD type, for each type decide if wanted or not, if so which type (percetage or base) (positive or nega), return values.
def build_modifier(name: str):
    available_mods = Modifier.MODIFIER_TYPES.copy()
    adds, mults = {}, {}

    print("\nStarting Modifier Creation...\n")

    while True:
        mod_type = selection_validation("Select which stats you want to modify.", available_mods)

        if (
            selection_validation(
                "What type of change would you like to make", ["Base Change", "Percentage Change"]
            )
            == "Base Change"
        ):
            mod_val = number_range_validation(-Modifier.MOD_ADD_RANGE, Modifier.MOD_ADD_RANGE)

            print(f"You created modifier: {mod_type} {mod_val}")
            if confirmation("Confirm creation?"):
                adds[mod_type] = mod_val

        else:
            mod_val = number_range_validation(-Modifier.MOD_MULT_RANGE, Modifier.MOD_MULT_RANGE)
            while mod_val > 1:
                mod_val /= 100
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val*100}%")
            if confirmation("Confirm mod creation?"):
                mults[mod_type] = mod_val

        if confirmation("Would you like to add another modifier?"):
            available_mods.remove(mod_type)
        else:
            logger.debug("Constructing modifier...")
            break
    if confirmation(f"Validate Modifier: {name}\n\tAdds: {adds}\n\tMults: {mults}\n\r"):
        new_mod = Modifier(name=name, adds=adds, mults=mults)

        return new_mod
    return None
