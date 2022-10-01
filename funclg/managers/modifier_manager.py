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

from loguru import logger

from funclg.character.modifiers import Modifier
from funclg.utils.input_validation import (
    list_choice_selection,
    number_range_validation,
    yes_no_validation,
)


# TODO: Create/modify the build to allow for random creation
# Modifiers are specific to the item that they are attached to and do not need to have custom names. This manager needs to be updated to just create the adds and mults of a mod and return that dictionary to a calling function. Modifiers will not be directly custom created or tracked.
# TODO Convert method to be able to handle multiple types of modifier generations. May require creating sub methods for the different types, weapon, armor, and abilities
# Needs to provide the capability to decide which m_type should be used or both, also how many modifiers can be applied, or just simply random
def generate_modifier(item_type: str = ""):
    adds, mults = {}, {}

    mod_types = ["attack", "energy", "health", "defense"]

    if item_type == "armor":
        mod_types = ["health", "defense"]

    elif item_type == "weapon":
        mod_types = ["energy", "attack"]

    add_mod = mod_types.pop(randint(0, len(mod_types)))
    add_value = randint(1, Modifier.MOD_ADD_RANGE)
    try:
        mult_mod = mod_types.pop(randint(0, len(mod_types)))
    except IndexError:
        mult_mod = mod_types.pop()

    mult_value = randint(1, Modifier.MOD_MULT_RANGE)

    while mult_value > 1:
        mult_value /= 100
    mult_value = round(mult_value, 2)

    adds.setdefault(add_mod, add_value)
    mults.setdefault(mult_mod, mult_value)

    return {"adds": adds, "mults": mults}


# TODO: Change function to be allow the user to define each attribute of the MOD type, for each type decide if wanted or not, if so which type (percetage or base) (positive or nega), return values.
def build_modifier(name: str):
    available_mods = Modifier.MODIFIER_TYPES.copy()
    adds, mults = {}, {}

    print("\nStarting Modifier Creation...\n")

    while True:
        print("Select which stats you want to modify.")
        mod_type = list_choice_selection(available_mods)

        if list_choice_selection(["Base Change", "Percentage Change"]) == "Base Change":
            mod_val = number_range_validation(-Modifier.MOD_ADD_RANGE, Modifier.MOD_ADD_RANGE)

            print(f"You created modifier: {mod_type} {mod_val}")
            if yes_no_validation("Confirm creation?"):
                adds[mod_type] = mod_val

        else:
            mod_val = number_range_validation(-Modifier.MOD_MULT_RANGE, Modifier.MOD_MULT_RANGE)
            while mod_val > 1:
                mod_val /= 100
            mod_val = round(mod_val, 2)

            print(f"You created modifier: {mod_type} {mod_val*100}%")
            if yes_no_validation("Confirm mod creation?"):
                mults[mod_type] = mod_val

        if yes_no_validation("Would you like to add another modifier?"):
            available_mods.remove(mod_type)
        else:
            logger.debug("Constructing modifier...")
            break

    if yes_no_validation(f"Validate Modifier: {name}\n\tAdds: {adds}\n\tMults: {mults}\n\r"):

        new_mod = Modifier(name=name, adds=adds, mults=mults)

        return new_mod
