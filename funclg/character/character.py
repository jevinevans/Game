"""
Programmer: Jevin Evans
Date: 6.11.2022
Description: The character that will be used. The character will have a role, abilities, and armor.
"""

from typing import Any, Dict, Optional

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

    def __init__(
        self,
        name: str,
        armor_type: int,
        armor_instance: Optional[Armor] = None,
        role_instance: Optional[Roles] = None,
    ):
        """
        Creates a new character with an armor set and role
        """
        self.name = name
        self.armor_type = armor_type if armor_type else 0

        self._set_up_armor(armor_instance)
        self._set_up_role(role_instance)

    def _set_up_armor(self, armor_instance: Optional[Armor] = None) -> None:
        if armor_instance and armor_instance.armor_type == self.armor_type:
            self.armor = armor_instance
        else:
            self.armor = Armor(self.armor_type)

    def _set_up_role(self, roles_instance: Optional[Roles] = None) -> None:
        if roles_instance and roles_instance.armor_type == self.armor_type:
            self.role = roles_instance
        else:
            self.role = Roles("Basic", "A basic character role", self.armor_type)

    def __str__(self) -> str:
        string = f"  {self.name}  \n"
        string += "-" * (len(self.name) + 4)
        string += f"\n Class: {self.role.name}"
        string += f"\n Armor: {self.armor}"

        return string

    def export(self) -> Dict[str, Any]:
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Armor):
                exporter[key] = value.export()
            if isinstance(value, Roles):
                exporter[key] = value.export()
        return exporter

    # def details(self, indent:int = 0) -> str:
    # TODO: Define details,
    # Add armor details and roles details

    def equip(self, item: Equipment) -> None:
        """Calls the armor equip function"""
        self.armor.equip(item)

    def dequip(self, item_type: str) -> None:
        """Calls the armor dequip function"""
        self.armor.dequip(item_type)

    # def use_power(self):
    # def add_power????
    # def get_stats(self):
