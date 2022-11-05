"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing roles.
"""

from loguru import logger

import funclg.managers.abilities_manager as ab_man
import funclg.utils.data_mgmt as db
from funclg.character.roles import Roles
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    string_validation,
    yes_no_validation,
)
from funclg.utils.types import ABILITY_TYPES, ARMOR_TYPES

ROLES_DATA = {"filename": "roles.json", "data": {}, "objects": {}}


def update_data():
    # TODO: On edit, needs to update all values
    db.update_data(ROLES_DATA)
    for _id, data in ROLES_DATA["data"].items():
        if _id not in ROLES_DATA["objects"]:
            ROLES_DATA["objects"][_id] = Roles(**data)


def export_data():
    for _id, data in ROLES_DATA["objects"].items():
        ROLES_DATA["data"][_id] = data.export()

    db.update_data(ROLES_DATA)


def _select_ability_types():
    """Allows the user to select the ability types they want to add to the role"""
    a_types = []
    available_types = ABILITY_TYPES.copy()

    while True:
        print(
            "Lets add some ability types to your role!\n\nWhat ability type(s) would you like this class to have?"
        )
        # TODO: Add description print out
        for _a_type, data in available_types.items():
            print(f"{_a_type}\n\tAvailable Mods: {', '.join(data['mods'])}")

        a_type = list_choice_selection(list(available_types.keys()))
        a_types.append(a_type)

        print(f"Current Ability Types: {' '.join(a_types)}")
        if yes_no_validation("Would you like to add another type?"):
            del available_types[a_type]
            continue
        break

    if not a_types:
        a_types = ["None"]
    return a_types


def _select_role_abilities(a_types: list):
    """"""

    def display_abilities():
        print(f"You can choose abilities from the following types: {', '.join(a_types)}")

        for _atype in available_abilities:
            print(f"{_atype}:")
            for _ability in available_abilities[_atype]:
                print(f"\t{_ability}")

        print("Select ability type:")
        a_choice = list_choice_selection(list(available_abilities.keys()))
        if available_abilities[a_choice]:
            print("Select ability to add:")
            new_ability_name = list_choice_selection(
                [a.name for a in available_abilities[a_choice]]
            )

            new_ability = [a for a in available_abilities[a_choice] if a.name == new_ability_name][
                0
            ]

            if yes_no_validation(f"Do you want to add {new_ability.name} to this role?"):
                # Remove added ability from available options and return
                available_abilities[new_ability.ability_type].remove(new_ability)
                return new_ability
            return None
        print(f"\nThere are no more {a_choice} abilities available.\n")
        return None

    print(
        "Now lets add some abilities!\n\nYou can add 5 abilities max, which would you like to add (see available below)?"
    )

    role_abilities = []
    available_abilities = ab_man.filter_abilities_by_types(a_types)

    # Show available abilities created, filtered by the ability types selcted
    while len(role_abilities) < 5:
        new_ability = display_abilities()
        if new_ability:
            role_abilities.append(new_ability)

        print("This role currently have the following abilities:")
        for ability in role_abilities:
            print(f"\n\t- {ability}")
        print(f"\nYou can still add more {5-len(role_abilities)} abilities.")

        if not yes_no_validation("Would you like to add another ability?"):
            break

    # TODO: Future: consider option to create a new one
    return role_abilities


def build_role():
    """Dialog for building a new character role"""

    print("\nStarting Role Creation")
    role_name = string_validation("What would you like to name this new Role?", "Name")
    role_desc = string_validation(f"How would you describe {role_name}?", "Description")
    print(f"What type of armor would you like to make the {role_name}?")
    armor_type = list_choice_selection(ARMOR_TYPES[:-1])

    a_types = _select_ability_types()

    r_abilities = _select_role_abilities(a_types)

    new_role = Roles(
        name=role_name,
        description=role_desc,
        armor_type=armor_type,
        ability_types=a_types,
        abilities=r_abilities,
    )

    if yes_no_validation(f"You created:\n{new_role.details()}\nSave new role?"):
        ROLES_DATA["data"][new_role.id] = new_role.export()
        update_data()
        print(f"{new_role.name} has been saved!!!")
    print("Oh well..., no roles to add to this awesome adventure!!!")
    del new_role


# def edit_role():
#     """
#     Allows the user to add or remove abilities from a role
#     """


def select_role():
    if ROLES_DATA["data"]:
        role_id = char_manager_choice_selection(ROLES_DATA["data"], "name", "_id")
        return ROLES_DATA["data"][role_id]
    logger.warning("There are no roles available.")
    return None


def show_role():
    show_role_id = select_role()
    if show_role_id:
        _show_role = ROLES_DATA["objects"][show_role_id]
        print(_show_role.details())
        return
    logger.warning("There are no roles available to show.")


def delete_role():
    del_role_id = select_role()
    if del_role_id:
        del_role = ROLES_DATA["data"][del_role_id]
        if yes_no_validation(f"Do you want to delete \"{del_role['name']}\"?"):
            print(f"Deleteing {del_role['name']}")
            del ROLES_DATA["data"][del_role_id]
            del ROLES_DATA["objects"][del_role_id]
            update_data()
            return
        print("Keeping all roles in the vault...")
        return
    logger.warning("There are no roles to delete.")


ROLES_MENU = {
    "name": "Manage Roles",
    "description": "This is the menu to manage character roles/classes. Build a class and the attributes to go with it.",
    "menu_items": [
        {"name": "New Role", "action": build_role},
        # {"name": "Edit Role", "action": edit_role},
        {"name": "View Role Details", "action": show_role},
        {"name": "Delete Role", "action": delete_role},
    ],
}

db.load_data(ROLES_DATA)
for _id, _data in ROLES_DATA["data"].items():
    ROLES_DATA["objects"][_id] = Roles(**_data)
