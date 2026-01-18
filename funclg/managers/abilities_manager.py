"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing abilities.
"""

from loguru import logger

import funclg.managers.stats_manager as stats_man
from funclg.character.abilities import Abilities
from funclg.utils.types import ABILITY_TYPES
from funclg.managers.manager import BaseManager, SingletonMeta


class AbilitiesManager(BaseManager, metaclass=SingletonMeta):
    """
    A manager class for creating, updating, and removing abilities.
    """

    def __init__(self):
        """Initialize the AbilitiesManager."""
        super().__init__(name="Abilities", filename="abilities.json")
        self.menu["menu_items"] = [
            {"title": "Add New Ability", "value": self.build_ability},
            # {"title": "Edit Ability", "value": self.edit_ability},
            {"title": "View Ability Details", "value": self.show_ability},
            {"title": "Delete Ability", "value": self.delete_ability},
        ]
        logger.debug("AbilitiesManager initialized.")
        self.load_data()
        logger.debug(f"AbilitiesManager data loaded {len(self.data)} abilities.")

    def update_data(self):
        for _id, data in self.data.items():
            if _id not in self.objects:
                self.objects[_id] = Abilities(**data)
        super().update_data()

    def export_data(self):
        for _id, data in self.objects.items():
            self.data[_id] = data.export()

        super().export_data()

    def build_ability(self):
        print("\nStarting Ability Creation...\n\nWhat type of ability would you like to create")

        for _a_type, data in ABILITY_TYPES.items():
            print(f"{_a_type}\n\tAvailable Mods: {', '.join(data['mods'])}")

        ability_type = self.get_selection("Choose from the above", list(ABILITY_TYPES.keys()))
        ability_name = self.get_string(
            f"What would you like to name this new {ability_type}?", "Name"
        )
        ability_desc = self.get_string(f"How would you describe {ability_name}?", "Description")
        print("Generating mods for this weapon...")
        ability_mod = stats_man.generate_modifier("ability", ABILITY_TYPES[ability_type], True)

        new_ability = Abilities(
            name=ability_name, ability_type=ability_type, description=ability_desc, mod=ability_mod
        )

        if self.get_confirmation(f"You created:\n{new_ability.details()}\nSave new ability?"):
            self.data[new_ability.id] = new_ability.export()
            self.update_data()
            print(f"{new_ability.name} has been saved!!!")
            return
        print("Guess no new ability for you to use, oh well...")
        del new_ability

    def select_ability(self):
        if self.data:
            return self.get_selection("Please choose an ability", self.data, "name", "_id")
        logger.warning("There are no abilities available.")
        return None

    def filter_abilities_by_types(self, a_types: list):
        filtered_abilities = {}
        for a_type in a_types:
            filtered_abilities[a_type] = [
                ability for ability in self.objects.values() if ability.ability_type == a_type
            ]
        return filtered_abilities

    def show_ability(self):
        show_ability_id = self.select_ability()
        logger.debug(f"Selected ability ID: {show_ability_id}")
        if show_ability_id:
            logger.debug(f"Showing ability with ID: {show_ability_id}")
            _show_ability = self.objects[show_ability_id]
            print(_show_ability.details())
            return
        logger.warning("There are no abilities to show.")

    def delete_ability(self):
        del_ability_id = self.select_ability()
        if del_ability_id:
            del_ability = self.data[del_ability_id]
            if self.get_confirmation(f"Do you want to delete \"{del_ability['name']}\"?"):
                print(f"Deleting {del_ability['name']}")
                del self.data[del_ability_id]
                del self.objects[del_ability_id]
                self.update_data()
                return
            print("Keeping all abilities in the vault...")
            return
        logger.warning("There are no abilities to delete.")
