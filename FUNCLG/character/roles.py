"""
Programmer: Jevin Evans
Date: 1.13.2021
Description: The Roles class is to allow the characters to use abilities.
"""

import json
from typing import Any, Dict, List, Union

from loguru import logger

from ..utils.types import CLASS_TYPES
from .abilities import Abilities


class Roles:
    """
    Creates a roles for a character
    """

    def __init__(
        self,
        name: str,
        description: str,
        armor_type: int,
        ability_groups: Union[List, None],
        abilities: Union[List, None],
    ):
        self.name = name
        self.description = description
        self.armor_type = armor_type
        self.class_types = self.validate_class_types(ability_groups)
        self.abilities = abilities if abilities else []
        # TODO: self.stats

    def __str__(self):
        return f"Class: {self.name} | Class Type: {self.class_types} | Armor Type: {self.armor_type} | Abilities: {len(self.abilities)}"

    # TODO: Complete add_power function
    def add_power():
        "COMPLETE ME"

    # TODO: Complete get_powers function
    def get_powers():
        "COMPLETE ME"

    # TODO: Complete use_power function
    def use_power():
        "COMPLETE ME"

    # TODO: Complete remove_power function
    def remove_power():
        "COMPLETE ME"

    def details(self):
        desc = f"\n Class: {self.name} \n{''.join(['-' for x in range(len(self.name)+9)])}"
        desc += f"\nArmor Type: {self.armor_type}\nDescription: {self.description}\nAbilities:\n"
        for ability in self.abilities:
            desc += ability.details()
        return desc

    def export(self) -> Dict[str, Any]:
        exporter = self.__dict__
        for key, index in exporter.items():
            if isinstance(index, Abilities):
                exporter[key] = index.export()
        return exporter

    def print_to_file(self) -> None:
        logger.info(f"Saving Role: {self.name}")
        with open(f"{self.name}.json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def validate_abilities(self, abilities: list):
        """
        Validates that abilities added are compatable
        """
        return [ability for ability in abilities if ability.class_type in self.class_types]

    @staticmethod
    def validate_class_types(ability_groups):
        return [ability for ability in ability_groups if ability in CLASS_TYPES]
