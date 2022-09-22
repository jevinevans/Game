"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing equipment.
"""

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import ITEM_TYPES, ARMOR_TYPES, WEAPON_TYPES
from funclg.utils.input_validation import (
    char_manager_choice_selection,
    list_choice_selection,
    yes_no_validation,
)

EQUIPMENT_DATA = {"filename": "equipment.json", "data": {}, "objects": {}}


def update_data():
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



# TODO design these to be just the creation function
def _new_weapon():
    print("What kind of Weapon would you like to create?")
    list_choice_selection("")
    raise NotImplementedError


def _new_body_armor():
    print("TODO: Build New Body Armor Section")
    raise NotImplementedError


def build_equipment():
    """ Dialog for building new equipment"""

    print("\nStarting Equipmet Creation:\n\nWhat type of equipment would you like to create:")
    equip_type = list_choice_selection(["Body Armor", "Weapon"])
    new_equipment = None

    if equip_type == "Body Armor":
        new_equipment = _new_body_armor()
    else:
        new_equipment = _new_weapon()

    if yes_no_validation(f"You created:\n{new_equipment.details()}\nSave new {equip_type}?"):
        EQUIPMENT_DATA["data"][new_equipment.id] = new_equipment.export()
        update_data()


def select_equipment():
    if EQUIPMENT_DATA["data"]:
        equip_list = {}
        print("Which type of equipment would you like to select:")
        if list_choice_selection(["Weapons", "Armor"]) == "Weapons":
            equip_list = {
                _id: data for _id, data in EQUIPMENT_DATA["data"].items() if data["item_type"] == 4
            }
        else:
            equip_list = {
                _id: data for _id, data in EQUIPMENT_DATA["data"].items() if data["item_type"] != 4
            }
        return char_manager_choice_selection(equip_list, "name", "_id")
    logger.warning("There are is no equipment available.")
    return None


def show_equipment():
    show_equip_id = select_equipment()
    if show_equip_id:
        show_equip = EQUIPMENT_DATA["objects"][show_equip_id]
        print(show_equip.details())


# def edit_equipment():
#     print("TODO: Build Edit Equipment Section")
#     raise NotImplementedError


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
    logger.warning("There are currently no equipment to delete.")


EQUIPMENT_MENU = {
    "name": "Manage Equipment",
    "description": "This the menu to create armor and weapons for characters to use.",
    "menu_items": [
        {"name": "New Equipment", "action": build_equipment},
        {"name": "View Modifier Details", "action": show_equipment},
        # {"name": "Edit Equipment", "action": edit_equipment},
        {"name": "Delete Equipment", "action": delete_equipment},
    ],
}

EQUIPMENT_DATA = db.load_data(EQUIPMENT_DATA)

for _id, _data in EQUIPMENT_DATA["data"].items():
    if _data["item_type"] == 4:
        EQUIPMENT_DATA["objects"][_id] = WeaponEquipment(**_data)
    else:
        EQUIPMENT_DATA["objects"][_id] = BodyEquipment(**_data)
