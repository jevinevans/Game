"""
Programmer: Jevin Evans
Date: 6.11.2022
Description: The character that will be used. The character will have a role, abilities, and armor.
"""

from typing import Any, Dict, Optional

import funclg.utils.data_mgmt as db

from .abilities import Abilities
from .armor import Armor
from .equipment import Equipment
from .roles import Roles

# from loguru import logger

# """
# Object Needs:
# - name
# - armor type - needed for compatability of role and armor
# - gender - (M/F/etc.) - For the future
# - role object - unless provided, start with basic role, no name and basic abilities
# - armor object - unless provided, the user starts with a blank armor and maybe basic armor?

# - validation method
# - ways to access role and object items
# - add a class
# - add equipment
# """


class Character:
    """
    The playable character for the game
    """

    # TODO: Update initialization process so that the role decides the armor type for the character and then all armor and equips will validate for the role

    DB_PREFIX = "CHARS"

    def __init__(
        self,
        name: str,
        armor_type: int,
        armor_instance: Optional[Armor] = None,
        role_instance: Optional[Roles] = None,
        **kwargs,
    ):
        """
        Creates a new character with an armor set and role
        """
        self.name = name
        self.armor_type = armor_type if armor_type else 0 # TODO: Consider changing to -1, but requires many changes to the ARMOR class for allowing None
        self.inventory = kwargs.get("inventory", [])

        self._set_up_armor(armor_instance)
        self._set_up_role(role_instance)
        self._id = db.id_gen(self.DB_PREFIX, kwargs.get("_id"))

    def _set_up_armor(self, armor_instance: Optional[Armor] = None) -> None:
        if armor_instance and armor_instance.armor_type == self.armor_type:
            self.armor = armor_instance
        else:
            self.armor = Armor(self.armor_type)

    def _set_up_role(self, roles_instance: Optional[Roles] = None) -> None:
        if roles_instance and roles_instance.armor_type == self.armor_type:
            self.role = roles_instance
        else:
            self.role = Roles("NPC", "A non-playable character", self.armor_type)

    def __str__(self) -> str:
        string = f"  {self.name}  \n"
        string += "-" * (len(self.name) + 4)
        string += f"\n Class: {self.role.name}"
        string += f"\n Armor: {self.armor}"

        return string

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    def export(self) -> Dict[str, Any]:
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Armor):
                exporter[key] = value.export()
            if isinstance(value, Roles):
                exporter[key] = value.export()
        return exporter

    def details(self, indent: int = 0) -> str:
        desc = f"{self.name}\n"
        desc += "-" * (len(self.name))
        desc += "\n" + self.role.details(indent + 2)
        desc += "\n" + self.armor.details(indent + 2)
        return desc

    def equip(self, item: Equipment) -> None:
        """Calls the armor equip function"""
        self.armor.equip(item)

    def dequip(self, item_type: str) -> None:
        """Calls the armor dequip function"""
        if item := self.armor.dequip(item_type) is not None:
            self.inventory.append(item)

    def show_inventory(self):
        print("\nInventory:")
        print("\n  - ".join(self.inventory))

    def add_power(self, ability: Abilities) -> bool:
        return self.role.add_power(ability)

    # def use_power(self): TODO

    # def get_stats(self): TODO
