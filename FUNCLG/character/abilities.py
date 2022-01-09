"""
Programmer: Jevin Evans
Date: 12.5.2021
Description: This defines the Roles and Abilities class
"""

import json
from typing import Any, Dict

from loguru import logger

from ..utils.types import ABILITY_TYPES, get_ability_effect_type


class Abilities:
    """
    Defines character/monster abilities
    """

    def __init__(
        self,
        name: str,
        ability_type: str,
        effect: int,
        description: str,
    ) -> None:
        self.name = name
        self.ability_type = ability_type if ability_type in ABILITY_TYPES else "None"
        self.ability_group, effect_type = get_ability_effect_type(self.ability_type)
        self.effect = (
            effect * effect_type
        )  # TODO: Will become stats, and a specific sub class that will be more focused for armor
        self.description = description
        # TODO: Validation will be done during creation

    def __str__(self):
        return f"{self.name} ({self.ability_type}): {self.effect}"

    def details(self):
        desc = f"\n{self.name}\n{''.join(['-' for x in range(len(self.name))])}"
        desc += f"\nDescription: {self.description}"
        desc += f"\nType: {self.ability_type} ({self.ability_group})"
        desc += f"\nEffect: {self.effect}"
        return desc

    def export(self) -> Dict[str, Any]:
        return self.__dict__

    def print_to_file(self) -> None:
        logger.info(f"Saving {self.name} to {self.name}.json")
        with open(f"{self.name}.json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)
