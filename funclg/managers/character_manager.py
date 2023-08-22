"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing characters.
"""
from typing import List, Union

from loguru import logger

import funclg.managers.abilities_manager as ab_man
import funclg.managers.equipment_manager as eq_man
import funclg.managers.roles_manager as role_man
import funclg.utils.data_mgmt as db
from funclg.character.armor import Armor
from funclg.character.character import Character
from funclg.utils.input_validation import (
    confirmation,
    selection_validation,
    string_validation,
)
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES

CHARACTER_DATA = {"filename": "characters.json", "data": {}, "objects": {}}


def _update_char_role(data: dict, new_data: dict):
    char_role_abilities = []
    logger.debug(data["role"])
    for _ability in data["role"].get("abilities", []):
        char_role_abilities.append(ab_man.Abilities(**_ability))
    new_data["role"]["abilities"] = char_role_abilities
    new_data["role_instance"] = role_man.Roles(**new_data["role"])
    del new_data["role"]
    return new_data


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

    new_data["armor_instance"] = Armor(
        armor_type=new_data["armor"].get("armor_type"),
        head=new_data["armor"].get("head", None),
        chest=new_data["armor"].get("chest", None),
        back=new_data["armor"].get("back", None),
        pants=new_data["armor"].get("pants", None),
        weapon=new_data["armor"].get("weapon", None),
    )
    del new_data["armor"]
    return new_data


def update_data():
    db.update_data(CHARACTER_DATA)
    for _id, data in CHARACTER_DATA["data"].items():
        if _id not in CHARACTER_DATA["objects"]:
            new_data = data.copy()

            if data.get("role"):
                new_data = _update_char_role(data, new_data)

            if data.get("armor"):
                new_data = _update_char_armor(data, new_data)

            CHARACTER_DATA["objects"][_id] = Character(**new_data)


def export_data():
    for _id, data in CHARACTER_DATA["objects"].items():
        CHARACTER_DATA["data"][_id] = data.export()

    db.update_data(CHARACTER_DATA)


def _pick_char_armor_equipment(
    armor_type: str, armor_type_int: int
) -> List[Union[eq_man.BodyEquipment, eq_man.WeaponEquipment, None]]:
    # Show all availabile equipment
    available_equipment = eq_man.filter_equipment_by_armor_type(armor_type_int)
    print(available_equipment)
    selected_equipment = {}

    # Go through each item type and select or skip
    # TODO: 2023.06.17 - Add the option to skip
    for item_type in ITEM_TYPES:
        if available_equipment[item_type]:
            print(f"Please choose a {item_type} to equip:")
            sel_item_name = selection_validation(
                [item.name for item in available_equipment[item_type].values()] + ["Skip"]
            )
            logger.debug(f"Selected {sel_item_name} from {available_equipment[item_type]}")
            if sel_item_name == "Skip":
                print(f"Skipping {item_type} selection...")
                continue
            sel_item = [
                item
                for item in available_equipment[item_type].values()
                if item.name == sel_item_name
            ][0]
            if confirmation(f"Do you want equip {sel_item}?"):
                selected_equipment[item_type.lower()] = sel_item.copy()
            else:
                selected_equipment[item_type.lower()] = None
        else:
            print(f"There are not any {armor_type} {item_type} items, continuing...\n")
    # TODO: 2023.06.17 - Confirm at the end, can ask to restart or move forward

    return selected_equipment


def build_character():
    """Dialog for building a new character"""

    # Basic Traits
    print("\nStarting Character Creation")
    char_name = string_validation("What would you like to name your character", "Name")

    # Choose Armor Type and Role
    print(
        f"Choose an available armor type for {char_name}. The armor type determines what role your character can have."
    )
    sorted_roles = role_man.sort_roles_by_armor_type()

    if not sorted_roles:
        logger.warning(
            "There are no roles to assign to your character. Please create a role before creating a character"
        )
        return

    for armor_type, a_roles in sorted_roles.items():
        print(f"{armor_type}:")
        for _a_role in a_roles:
            print(f"\n\t- {_a_role}")

    char_armor_type = selection_validation(list(sorted_roles.keys()))
    char_armor_type_int = ARMOR_TYPES.index(char_armor_type)

    print(f"Which role would you like for {char_name}:")
    char_role_name = selection_validation([role.name for role in sorted_roles[char_armor_type]])
    char_role = [role for role in sorted_roles[char_armor_type] if role.name == char_role_name][
        0
    ].copy()

    char_armor = None
    if confirmation(f"Do you want to add equipment to your character: '{char_name.capitalize()}'?"):
        char_equipment = _pick_char_armor_equipment(char_armor_type, char_armor_type_int)
        char_armor = Armor(armor_type=char_armor_type_int, **char_equipment)
    else:
        char_armor = Armor(armor_type=char_armor_type_int)

    new_character = Character(
        name=char_name,
        armor_type=char_armor_type_int,
        armor_instance=char_armor,
        role_instance=char_role,
    )

    if confirmation(f"You created:\n{new_character.details()}\nSave new character?"):
        CHARACTER_DATA["data"][new_character.id] = new_character.export()
        update_data()
        print(f"{new_character.name} has been saved!!!")
        return

    print(f"Oh well..., I guess we'll just kill {new_character.name}")
    del new_character


def select_character():
    if CHARACTER_DATA["data"]:
        return selection_validation(
            "Please select a character", CHARACTER_DATA["data"], "name", "_id"
        )
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
        if confirmation(f"Do you want to delete \"{del_character['name']}\"?"):
            print(f"Deleteing {del_character['name']}")
            del CHARACTER_DATA["data"][del_character_id]
            del CHARACTER_DATA["objects"][del_character_id]
            update_data()
            return
        print("Keeping all characters alive...")
        return
    logger.warning("There are currently no character to delete.")


MENU = {
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
