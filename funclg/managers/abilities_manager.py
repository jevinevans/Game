"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing abilities.
"""

from loguru import logger

import funclg.managers.modifier_manager as mod_man
import funclg.utils.data_mgmt as db
from funclg.character.abilities import Abilities
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    string_validation,
    yes_no_validation,
)
from funclg.utils.types import ABILITY_TYPES

ABILITIES_DATA = {"filename": "abilities.json", "data": {}, "objects": {}}


def update_data():
    db.update_data(ABILITIES_DATA)

    for _id, data in ABILITIES_DATA["data"].items():
        if _id not in ABILITIES_DATA["objects"]:
            ABILITIES_DATA["objects"][_id] = Abilities(**data)


def export_data():
    for _id, data in ABILITIES_DATA["objects"].items():
        ABILITIES_DATA["data"][_id] = data.export()

    db.update_data(ABILITIES_DATA)


# TODO: need to add a condition to not return so that there is not lose data
# TODO: Need to update so that if a new role is created and the user wants to create a new ability the selected ability types can be passed in only used
def build_ability():
    print("\nStarting Ability Creation...\n\nWhat type of ability would you like to create")

    # TODO: Add description print out
    for _a_type, data in ABILITY_TYPES.items():
        print(f"{_a_type}\n\tAvailable Mods: {', '.join(data['mods'])}")

    ability_type = list_choice_selection(list(ABILITY_TYPES.keys()))
    ability_name = string_validation(
        f"What would you like to name this new {ability_type}?", "Name"
    )
    ability_desc = string_validation(f"How would you describe {ability_name}?", "Description")

    # TODO: Need to be able to chose the mod for the ability they want
    print("Generating mods for this weapon...")
    ability_mod = mod_man.generate_modifier("ability", ABILITY_TYPES[ability_type], True)

    new_ability = Abilities(
        name=ability_name, ability_type=ability_type, description=ability_desc, mod=ability_mod
    )

    if yes_no_validation(f"You created:\n{new_ability.details()}\nSave new ability?"):
        ABILITIES_DATA["data"][new_ability.id] = new_ability.export()
        update_data()
        print(f"{new_ability.name} has been saved!!!")
        return
    print("Guess no new ability for you to use, oh well...")
    del new_ability


def select_ability():
    if ABILITIES_DATA["data"]:
        return char_manager_choice_selection(ABILITIES_DATA["data"], "name", "_id")
    logger.warning("There are no abilities available.")
    return None


def filter_abilities_by_types(a_types: list):

    _abilities = [
        ability.copy()
        for _, ability in ABILITIES_DATA["objects"].items()
        if ability.ability_type in a_types
    ]

    filtered_abilities = {a: [] for a in a_types}

    for ability in _abilities:
        filtered_abilities[ability.ability_type].append(ability)

    return filtered_abilities


def show_ability():
    show_ability_id = select_ability()
    if show_ability_id:
        _show_ability = ABILITIES_DATA["objects"][show_ability_id]
        print(_show_ability.details())
        return
    logger.warning("There are no abilities to show.")


def delete_ability():
    del_ability_id = select_ability()
    if del_ability_id:
        del_ability = ABILITIES_DATA["data"][del_ability_id]
        if yes_no_validation(f"Do you want to delete \"{del_ability['name']}\"?"):
            print(f"Deleteing {del_ability['name']}")
            del ABILITIES_DATA["data"][del_ability_id]
            del ABILITIES_DATA["objects"][del_ability_id]
            update_data()
            return
        print("Keeping all abilities in the vault...")
        return
    logger.warning("There are no abilities to delete.")


ABILITY_MENU = {
    "name": "Manage Abilities",
    "description": "This is the menu to create abilities to add to Roles for characters to use.",
    "menu_items": [
        {"name": "Add New Ability", "action": build_ability},
        # {"name": "Edit Ability", "action": edit_ability},
        {"name": "View Ability Details", "action": show_ability},
        {"name": "Delete Ability", "action": delete_ability},
    ],
}

db.load_data(ABILITIES_DATA)
for _id, _data in ABILITIES_DATA["data"].items():
    ABILITIES_DATA["objects"][_id] = Abilities(**_data)
