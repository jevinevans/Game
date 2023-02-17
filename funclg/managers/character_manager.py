"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing characters.
"""
from loguru import logger

import funclg.managers.abilities_manager as ab_man
import funclg.managers.equipment_manager as eq_man
import funclg.managers.roles_manager as role_man
import funclg.utils.data_mgmt as db
from funclg.character.armor import Armor
from funclg.character.character import Character
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    string_validation,
    yes_no_validation,
)
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES

CHARACTER_DATA = {"filename": "characters.json", "data": {}, "objects": {}}


def _update_char_role(data: dict, new_data: dict):
    char_role_abilities = []
    for _ability in data["role"].get("abilities", []):
        char_role_abilities.append(ab_man.Abilities(**_ability))
    new_data["role"]["abilities"] = char_role_abilities
    new_data["role_instance"] = role_man.Roles(**new_data["role"])
    del new_data["role"]


def _update_char_armor(data: dict, new_data: dict):
    for item_type in ITEM_TYPES:
        if new_data["armor"][item_type.lower()]:
            if new_data["armor"][item_type.lower()]["item_type"] == 4:
                new_data["armor"][item_type.lower()] = eq_man.WeaponEquipment(
                    **data["armor"][item_type.lower()]
                )
            else:
                new_data["armor"][item_type.lower()] = eq_man.BodyEquipment(
                    **data["armor"][item_type.lower()]
                )
    new_data["armor_instance"] = Armor(**new_data["armor"])
    del new_data["armor"]


def update_data():
    db.update_data(CHARACTER_DATA)
    for _id, data in CHARACTER_DATA["data"].items():
        if _id not in CHARACTER_DATA["objects"]:
            new_data = data.copy()

            if data.get("role"):
                _update_char_role(data, new_data)

            if data.get("armor"):
                _update_char_armor(data, new_data)

            CHARACTER_DATA["objects"][_id] = Character(**new_data)


def export_data():
    for _id, data in CHARACTER_DATA["objects"].items():
        CHARACTER_DATA["data"][_id] = data.export()

    db.update_data(CHARACTER_DATA)


def _pick_char_armor_equipment(armor_type: str) -> list:
    armor_type = ARMOR_TYPES.index(armor_type)

    raise NotImplementedError


def build_character():
    """Dialog for building a new character"""

    # Basic Traits
    print("\nStarting Character Creation")
    char_name = string_validation("What would you like to name your character", "Name")

    # Choose Armor Type and Role
    print(
        f"Choose an armor type for {char_name}. The armor type determines what role your character can have."
    )
    sorted_roles = role_man.sort_roles_by_armor_type()
    for armor_type, a_roles in sorted_roles.items():
        print(f"{armor_type}:")
        print("\n\t- ".join(a_roles))

    char_armor_type = list_choice_selection(ARMOR_TYPES[:-1])

    print(f"Which role would you like for {char_name}:")
    char_role = list_choice_selection([role.name for role in sorted_roles[char_armor_type]])

    if yes_no_validation(f"Do you want to add equipment to {char_name}?"):

        char_equipment = _pick_char_armor_equipment(char_armor_type)

    # Ask if they want to build an armor
    # Yes, build armor method - select equipment that is compatible with the armor type

    # Confirm and build, update

    raise NotImplementedError


# def edit_character():
#     print("TODO: Build Edit Character Section")
#     raise NotImplementedError


def select_character():
    if CHARACTER_DATA["data"]:
        return char_manager_choice_selection(CHARACTER_DATA["data"], "name", "_id")
    logger.warning("There are no roles available.")
    return None


def show_character():
    show_character_id = select_character()
    if show_character_id:
        _show_character = CHARACTER_DATA["objects"][show_character_id]
        print(_show_character.details())
        return
    logger.warning("There are no characters available to show.")


def delete_character():
    del_character_id = select_character()
    if del_character_id:
        del_character = CHARACTER_DATA["data"][del_character_id]
        if yes_no_validation(f"Do you want to delete \"{del_character['name']}\"?"):
            print(f"Deleteing {del_character['name']}")
            del CHARACTER_DATA["data"][del_character_id]
            del CHARACTER_DATA["object"][del_character_id]
            update_data()
            return
        print("Keeping all characters alive...")
        return
    logger.warning("There are currently no character to delete.")


CHARACTER_MENU = {
    "name": "Manage Characters",
    "description": "This is the menu to create characters to use in game.",
    "menu_items": [
        {"name": "New Character", "action": build_character},
        # {"name": "Edit Character", "action": edit_character},
        {"name": "Show Character", "action": show_character},
        {"name": "Delete Character", "action": delete_character},
    ],
}

db.load_data(CHARACTER_DATA)
update_data()
