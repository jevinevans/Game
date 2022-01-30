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

    MAX_ABILITIES = 5

    def __init__(
        self,
        name: str,
        description: str,
        armor_type: int,
        class_types: Union[List, None],
        abilities: Union[List, None],
    ):  # pylint: disable=too-many-arguments
        self.name = name
        self.description = description
        self.armor_type = armor_type
        self.class_types = (
            [class_type for class_type in class_types if class_type in CLASS_TYPES]
            if class_types
            else "None"
        )
        self.abilities = self.validate_abilities(abilities) if abilities else []
        # TODO: self.stats

    def __str__(self):
        return f"Class: {self.name} | Class Type: {self.class_types} | Armor Type: {self.armor_type} | Abilities: {len(self.abilities)}"

    def add_power(self, ability: Abilities) -> int:
        if ability.class_type in self.class_types:
            if len(self.abilities) < Roles.MAX_ABILITIES:
                self.abilities.append(ability)
                logger.success(f"Added {ability.name} to {self.name}")
                return 0
            logger.warning("No open slot for an ability")
            return 5
        logger.error(
            f"{ability.name}({ability.class_type}) is not compatible with {self.name}({self.class_types})"
        )
        return 1

    # TODO: Complete use_power function
    # I think I am going to wait for stats integration because of how each power can effect the stats
    # def use_power(self, index:int):

    def remove_power(self, index: int):
        # Validation will be done at a higher level
        if self.abilities and index < len(self.abilities):
            old_ability = self.abilities.pop(index)
        del old_ability

    def get_powers(self):
        if len(self.abilities):
            for ability in self.abilities:
                print(ability)
        else:
            print("This role has no abilities")

    def details(self):
        desc = f"\n Class: {self.name} \n{''.join(['-' for x in range(len(self.name)+9)])}"
        desc += f"\nArmor Type: {self.armor_type}\nDescription: {self.description}\nAbilities:\n"
        for ability in self.abilities:
            desc += ability.details()
        return desc

    def export(self) -> Dict[str, Any]:
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Abilities):
                exporter[key] = value.export()
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
