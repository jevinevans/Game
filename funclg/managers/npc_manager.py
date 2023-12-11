"""
Description: A manager class for maintain non-playable characters/NPCs
Developer: Jevin Evans
Data: 12.7.2023
"""

from loguru import logger

import funclg.managers.abilities_manager
import funclg.managers.equipment_manager
import funclg.managers.roles_manager
import funclg.utils.data_mgmt as db
from funclg.character.armor import Armor
from funclg.character.character import NonPlayableCharacter
from funclg.managers.character_manager import _update_char_armor, _update_char_role
from funclg.utils.input_validation import (
    confirmation,
    selection_validation,
    string_validation,
)
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES

NPC_DATA = {"filename": "npcs.json", "data": {}, "objects": {}}


def load_data():
    db.load_data(NPC_DATA)
    update_data()


def update_data():
    db.update_data(NPC_DATA)
    for _id, data in NPC_DATA["data"].items():
        if _id not in NPC_DATA["objects"]:
            new_data = data.copy()

            if data.get("role"):
                new_data = _update_char_role(data, new_data)

            if data.get("armor"):
                new_data = _update_char_armor(data, new_data)

            NPC_DATA["objects"][_id] = NonPlayableCharacter(**new_data)


def export_data():
    for _id, data in NPC_DATA["objects"].items():
        NPC_DATA["data"][_id] = data.export()

    db.update_data(NPC_DATA)


def create_npc():
    raise NotImplementedError


def select_npc():
    if NPC_DATA["data"]:
        return selection_validation("Please select an NPC", NPC_DATA["data"], "name", "_id")
    logger.warning("There are no NPCs available.")
    return None


def show_npc():
    npc_id = select_npc()
    if npc_id:
        npc = NPC_DATA["objects"][npc_id]
        print(npc.details())
        return
    logger.warning("There are no NPCs to show.")


def get_npc():
    if NPC_DATA["objects"]:
        return NPC_DATA["objects"].get(select_npc(), None)
    logger.warning("There are no NPCs to choose.")
    return None


def delete_npc():
    npc_id = select_npc()
    if npc_id:
        npc = NPC_DATA["data"][npc_id]
        if confirmation(f"Do you want to delete\"{npc['name']}\"?"):
            print(f"Deleteing {npc['name']}")
            del NPC_DATA["data"][npc_id]
            del NPC_DATA["objects"][npc_id]
            update_data()
            return
        print("Keeping the monsters at bay...")
        return
    logger.warning("There are not any NPCs at the moment.")


MENU = {
    "name": "NPC Manager",
    "description": "Create and manage NPC enemies in the game.",
    "menu_items": [
        {"title": "Create new NPC", "value": create_npc},
        {"title": "Show NPC(s)", "value": show_npc},
        {"title": "Remove NPC(s)", "value": delete_npc},
    ],
}
