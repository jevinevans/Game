"""
Programmer: Jevin Evans
Date: 1.13.2021
Description: The Roles class is to allow the characters to use abilities.
"""

import json
from typing import Any, Dict, List, Union

from loguru import logger

from ..utils.types import CLASS_TYPES, get_armor_type
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
        abilities: Union[List, None] = None,
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
        return f"Class: {self.name} | Class Type: {self.class_types} | Armor Type: {get_armor_type(self.armor_type)} | Abilities: {len(self.abilities)}"

    # TODO: add check/validation for duplicates
    def add_power(self, ability: Abilities) -> int:
        if ability.class_type in self.class_types:
            if len(self.abilities) < Roles.MAX_ABILITIES:
                self.abilities.append(ability)
                logger.success(f"Added {ability.name} to {self.name}")
                return 0
            logger.warning("Max abilities reached!")
            return 3
        logger.error(
            f"{ability.name}({ability.class_type}) is not compatible with {self.name}({self.class_types})"
        )
        return 1

    def get_power(self, index: int):
        """Returns the wanted power"""
        if self.abilities and (index < len(self.abilities) or index >= -1):
            return self.abilities[index]
        return None

    def remove_power(self, index: int) -> bool:
        # Validation will be done at a higher level
        if self.abilities and (index < len(self.abilities) or index >= -1):
            old_ability = self.abilities.pop(index)
            del old_ability
            return True
        return False

    # TODO add indention factor
    def details(self):
        desc = f"\n Class: {self.name} \n{''.join(['-' for x in range(len(self.name)+9)])}"
        desc += f"\nArmor Type: {get_armor_type(self.armor_type)}\nDescription: {self.description}\n\nAbilities:\n"
        for ability in self.abilities:
            desc += "\t"
            desc += ability.details()
            desc += "\n"
        return desc

    def export(self) -> Dict[str, Any]:
        exporter = self.__dict__
        for key, value in exporter.items():
            if key == "abilities" and len(value) > 0:
                for index, ability in enumerate(value):
                    if isinstance(ability, Abilities):
                        value[index] = ability.export()
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
