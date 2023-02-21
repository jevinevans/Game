"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing equipment.
"""

from loguru import logger

import funclg.managers.modifier_manager as mod_man
import funclg.utils.data_mgmt as db
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    string_validation,
    yes_no_validation,
)
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, WEAPON_TYPES

EQUIPMENT_DATA = {"filename": "equipment.json", "data": {}, "objects": {}}


def update_data():
    # TODO: On edit, needs to update all values
    db.update_data(EQUIPMENT_DATA)

    for _id, data in EQUIPMENT_DATA["data"].items():

        if _id not in EQUIPMENT_DATA["objects"]:
            if data["item_type"] == 4:
                EQUIPMENT_DATA["objects"][_id] = WeaponEquipment(**data)
            else:
                EQUIPMENT_DATA["objects"][_id] = BodyEquipment(**data)


def export_data():
    for _id, data in EQUIPMENT_DATA["objects"].items():
        EQUIPMENT_DATA["data"][_id] = data.export()

    db.update_data(EQUIPMENT_DATA)


def _new_weapon():
    print("What kind of Weapon would you like to create?")
    weapon_type = list_choice_selection(list(WEAPON_TYPES)[:-1])
    weapon_name = string_validation(f"What would you like to name this new {weapon_type}?", "Name")
    weapon_desc = string_validation(f"How would you describe {weapon_name}?", "Description")

    print("Generating mods for this weapon...")
    weapon_mod = mod_man.generate_modifier("weapon")

    return WeaponEquipment(
        name=weapon_name,
        weapon_type=weapon_type,
        description=weapon_desc,
        mod=weapon_mod,
    )

def update_data():
    db.update_data(EQUIPMENT_DATA)

def _new_body_armor():
    print("What type of Armor would you like to create?")
    item_type = list_choice_selection(ITEM_TYPES[:-1])
    print(f"What type of armor would you like to make the {item_type}?")
    armor_type = list_choice_selection(ARMOR_TYPES)
    item_name = string_validation(
        f"What would you like to name this new {armor_type} {item_type}?", "Name"
    )
    item_desc = string_validation(f"How would you describe {item_name}?", "Description")

    print(f"Generating mods for this {item_type}...")
    item_mod = mod_man.generate_modifier("armor")

    return BodyEquipment(
        name=item_name,
        mod=item_mod,
        description=item_desc,
        armor_type=ARMOR_TYPES.index(armor_type),
        item_type=ITEM_TYPES.index(item_type),
    )

def export_data():
    for _id, data in EQUIPMENT_DATA["objects"].items():
        EQUIPMENT_DATA["data"][_id] = data.export()

    db.update_data(EQUIPMENT_DATA)


def build_equipment():
    """Dialog for building new equipment"""

    print("\nStarting Equipmet Creation:\n\nWhat type of equipment would you like to create:")
    equip_type = list_choice_selection(["Body Armor", "Weapon"])
    new_equipment = None

    if equip_type == "Armor":
        new_equipment = _new_body_armor()
    else:
        new_equipment = _new_weapon()

    if yes_no_validation(f"You created:\n{new_equipment.details()}\nSave new {equip_type}?"):
        EQUIPMENT_DATA["data"][new_equipment.id] = new_equipment.export()
        update_data()
        print(f"{new_equipment.name} has been saved!!!")
        return

    print(f"No new {equip_type.lower()}, oh well...")
    del new_equipment


<<<<<<< HEAD
=======
<<<<<<< HEAD
    print("\nStarting Equipmet Creation:\n\nWhat type of equipment would you like to create:")
    equip_type = list_choice_selection(["Body Armor", "Weapon"])
    new_equipment = None
=======
>>>>>>> ccd0204... completed character manager
def filter_equipment_by_armor_type(armor_type: int):
    filtered_equipment = {}

    for index, item_type in enumerate(ITEM_TYPES):
        filtered_equipment[item_type] = {
            equipment.id: equipment
            for equipment in EQUIPMENT_DATA["objects"].values()
            if equipment.armor_type == armor_type and equipment.item_type == index
        }

    return filtered_equipment
<<<<<<< HEAD

=======
>>>>>>> 2d0e567... completed character manager
>>>>>>> ccd0204... completed character manager


def select_equipment():
    if EQUIPMENT_DATA["data"]:
        equip_list = {}
        print("Which type of equipment would you like to select:")
        choice = list_choice_selection(["Weapons", "Armor"])
        if choice == "Armor":
            equip_list = {
                _id: data for _id, data in EQUIPMENT_DATA["data"].items() if data["item_type"] != 4
            }
        else:
            equip_list = {
                _id: data for _id, data in EQUIPMENT_DATA["data"].items() if data["item_type"] == 4
            }
        return char_manager_choice_selection(equip_list, "name", "_id")
    logger.warning("There are is no equipment available.")
    return None


def show_equipment():
    show_equip_id = select_equipment()
    if show_equip_id:
        show_equip = EQUIPMENT_DATA["objects"][show_equip_id]
        print(show_equip.details())
        return
    logger.warning("There are no equipment items to show.")

    if yes_no_validation(f"You created:\n{new_equipment.details()}\nSave new {equip_type}?"):
        EQUIPMENT_DATA["data"][new_equipment.id] = new_equipment.export()
        update_data()


def delete_equipment():
    del_equip_id = select_equipment()
    if del_equip_id:
        del_equip = EQUIPMENT_DATA["data"][del_equip_id]
        if yes_no_validation(f"Do you want to delete \"{del_equip['name']}\"?"):
            print(f"Deleteing {del_equip['name']}")
            del EQUIPMENT_DATA["data"][del_equip_id]
            del EQUIPMENT_DATA["objects"][del_equip_id]
            update_data()
            return
        print("Keeing all equipment in the vault...")
        return
    logger.warning("There are currently no equipment to delete.")


<<<<<<< HEAD
MENU = {
=======
<<<<<<< HEAD

EQUIPMENT_MENU = {
=======
MENU = {
>>>>>>> 2d0e567... completed character manager
>>>>>>> ccd0204... completed character manager
    "name": "Manage Equipment",
    "description": "This the menu to create armor and weapons for characters to use.",
    "menu_items": [
        {"name": "New Equipment", "action": build_equipment},
        {"name": "View Equipment Details", "action": show_equipment},
        # {"name": "Edit Equipment", "action": edit_equipment},
        {"name": "Delete Equipment", "action": delete_equipment},
    ],
}

db.load_data(EQUIPMENT_DATA)
update_data()
