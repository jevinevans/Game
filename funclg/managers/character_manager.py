"""
Description: A manager class for creating, updating, and removing characters.
Developer: Jevin Evans
Date: 6.19.2022
"""

from typing import List, Union

from loguru import logger

from funclg.managers.manager import BaseManager, SingletonMeta
from funclg.managers.equipment_manager import EquipmentManager
from funclg.managers.roles_manager import RolesManager
from funclg.character.armor import Armor
from funclg.character.character import Player
from funclg.character.abilities import Abilities
from funclg.character.roles import Roles
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES


class CharacterManager(BaseManager, metaclass=SingletonMeta):
    """
    A manager class for creating, updating, and removing characters.
    """

    def __init__(self):
        """Initialize the CharacterManager."""
        super().__init__(name="Characters", filename="characters.json")
        self.menu["menu_items"] = [
            {"title": "New Character", "value": self.build_character},
            # {"title": "Edit Character", "value": self.edit_character},
            {"title": "Show Character", "value": self.show_character},
            {"title": "Delete Character", "value": self.delete_character},
        ]
        logger.debug("CharacterManager initialized.")
        self.load_data()
        logger.debug(f"CharacterManager data loaded {len(self.data)} characters.")

    def _update_char_role(self, data: dict, new_data: dict):
        char_role_abilities = []
        logger.debug(data["role"])
        for _ability in data["role"].get("abilities", []):
            char_role_abilities.append(Abilities(**_ability))
        new_data["role"]["abilities"] = char_role_abilities
        new_data["role_instance"] = Roles(**new_data["role"])
        del new_data["role"]
        return new_data

    def _update_char_armor(self, data: dict, new_data: dict):
        for item_type in ITEM_TYPES:
            if new_data["armor"][item_type.lower()]:
                if new_data["armor"][item_type.lower()]["item_type"] == 4:
                    new_data["armor"][item_type.lower()] = WeaponEquipment(
                        **data["armor"][item_type.lower()]
                    )
                else:
                    new_data["armor"][item_type.lower()] = BodyEquipment(
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

    def update_data(self):
        for _id, data in self.data.items():
            if _id not in self.objects:
                new_data = data.copy()

                if data.get("role"):
                    new_data = self._update_char_role(data, new_data)

                if data.get("armor"):
                    new_data = self._update_char_armor(data, new_data)

                self.objects[_id] = Player(**new_data)

        super().update_data()

    def export_data(self):
        for _id, data in self.objects.items():
            self.data[_id] = data.export()

        super().export_data()

    def _pick_char_armor_equipment(
        self, armor_type: str, armor_type_int: int
    ) -> List[Union[BodyEquipment, WeaponEquipment, None]]:
        # Show all availabile equipment
        available_equipment = EquipmentManager().filter_equipment_by_armor_type(armor_type_int)
        print(available_equipment)
        selected_equipment = {}

        # Go through each item type and select or skip
        for item_type in ITEM_TYPES:
            logger.debug(f"{item_type} has {len(available_equipment[item_type])} available items")
            if available_equipment[item_type]:
                logger.debug(f"{item_type} True")
                sel_item_name = self.get_selection(
                    f"Please choose a {item_type} to equip:",
                    [item.name for item in available_equipment[item_type].values()] + ["Skip"],
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
                if self.get_confirmation(f"Do you want equip {sel_item}?"):
                    selected_equipment[item_type.lower()] = sel_item.copy()
                else:
                    selected_equipment[item_type.lower()] = None
            else:
                print(f"There are not any {armor_type} {item_type} items, continuing...\n")
                logger.debug(f"There are not any {armor_type} {item_type} items, continuing...\n")

        return selected_equipment

    def build_character(self):
        """Dialog for building a new character"""

        # Basic Traits
        print("\nStarting Character Creation")
        char_name = self.get_string("What would you like to name your character", "Name")

        # Choose Armor Type and Role
        print(
            f"Choose an available armor type for {char_name}. The armor type determines what role your character can have."
        )
        sorted_roles = RolesManager().sort_roles_by_armor_type()

        if not sorted_roles:
            logger.warning(
                "There are no roles to assign to your character. Please create a role before creating a character"
            )
            return

        for armor_type, a_roles in sorted_roles.items():
            print(f"{armor_type}:")
            for _a_role in a_roles:
                print(f"\n\t- {_a_role}")

        char_armor_type = self.get_selection(
            "Which armor type would you like", list(sorted_roles.keys())
        )
        char_armor_type_int = ARMOR_TYPES.index(char_armor_type)

        char_role_name = self.get_selection(
            f"Which role would you like for {char_name}:",
            [role.name for role in sorted_roles[char_armor_type]],
        )
        char_role = [role for role in sorted_roles[char_armor_type] if role.name == char_role_name][
            0
        ].copy()

        char_armor = None
        if self.get_confirmation(
            f"Do you want to add equipment to your character: '{char_name.capitalize()}'?"
        ):
            char_equipment = self._pick_char_armor_equipment(char_armor_type, char_armor_type_int)
            char_armor = Armor(armor_type=char_armor_type_int, **char_equipment)
        else:
            char_armor = Armor(armor_type=char_armor_type_int)

        new_character = Player(
            name=char_name,
            armor_type=char_armor_type_int,
            armor_instance=char_armor,
            role_instance=char_role,
        )

        if self.get_confirmation(f"You created:\n{new_character.details()}\nSave new character?"):
            self.data[new_character.id] = new_character.export()
            self.update_data()
            print(f"{new_character.name} has been saved!!!")
            return

        print(f"Oh well..., I guess we'll just kill {new_character.name}")
        del new_character

    def select_character(self):
        if self.data:
            return self.get_selection("Please select a character", self.data, "name", "_id")
        logger.warning("There are no characters available.")
        return None

    def get_character(self):
        if self.objects:
            return self.objects.get(self.select_character(), None)
        logger.warning("There are no characters available to choose.")
        return None

    def show_character(self):
        show_character_id = self.select_character()
        if show_character_id:
            _show_character = self.objects[show_character_id]
            print(_show_character.details())
            return
        logger.warning("There are no characters available to show.")

    def delete_character(self):
        del_character_id = self.select_character()
        if del_character_id:
            del_character = self.data[del_character_id]
            if self.get_confirmation(f"Do you want to delete \"{del_character['name']}\"?"):
                print(f"Deleting {del_character['name']}")
                del self.data[del_character_id]
                del self.objects[del_character_id]
                self.update_data()
                return
            print("Keeping all characters alive...")
            return
        logger.warning("There are currently no character to delete.")
