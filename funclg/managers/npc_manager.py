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
from funclg.managers.character_manager import CharacterManager
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES
from funclg.managers.manager import BaseManager, SingletonMeta


class NPCManager(BaseManager, metaclass=SingletonMeta):
    """
    A manager class for maintain non-playable characters/NPCs
    """

    def __init__(self):
        """Initialize the NPCManager."""
        super().__init__(name="NPCs", filename="npcs.json")
        self.menu["menu_items"] = [
            {"title": "Create new NPC", "value": self.create_npc},
            {"title": "Show NPC(s)", "value": self.show_npc},
            {"title": "Remove NPC(s)", "value": self.delete_npc},
        ]
        logger.debug("NPCManager initialized.")
        self.load_data()
        logger.debug(f"NPCManager data loaded {len(self.data)} NPCs.")

    def update_data(self):
        for _id, data in self.data.items():
            if _id not in self.objects:
                new_data = data.copy()

                if data.get("role"):
                    new_data = CharacterManager()._update_char_role(data, new_data)

                if data.get("armor"):
                    new_data = CharacterManager()._update_char_armor(data, new_data)

                self.objects[_id] = NonPlayableCharacter(**new_data)
        super().update_data()

    def export_data(self):
        for _id, data in self.objects.items():
            self.data[_id] = data.export()

        super().export_data()

    def create_npc(self):
        raise NotImplementedError

    def select_npc(self):
        if self.data:
            return self.get_selection("Please select an NPC", self.data, "name", "_id")
        logger.warning("There are no NPCs available.")
        return None

    def show_npc(self):
        npc_id = self.select_npc()
        if npc_id:
            npc = self.objects[npc_id]
            print(npc.details())
            return
        logger.warning("There are no NPCs to show.")

    def get_npc(self):
        if self.objects:
            return self.objects.get(self.select_npc(), None)
        logger.warning("There are no NPCs to choose.")
        return None

    def delete_npc(self):
        npc_id = self.select_npc()
        if npc_id:
            npc = self.data[npc_id]
            if self.get_confirmation(f"Do you want to delete\"{npc['name']}\"?"):
                print(f"Deleteing {npc['name']}")
                del self.data[npc_id]
                del self.objects[npc_id]
                self.update_data()
                return
            print("Keeping the monsters at bay...")
            return
        logger.warning("There are not any NPCs at the moment.")
