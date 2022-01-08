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
        a_type: str,
        effect: int,
        description: str,
    ) -> None:
        self.name = name
        self.ability_type = a_type if a_type in ABILITY_TYPES else "None"
        self.effect_type = get_ability_effect_type(a_type)
        self.effect = effect  # TODO: Will become stats, and a specific sub class that will be more focused for armor
        self.description = description
        # Validation will be done during creation

    def __str__(self):
        sign = "-" if self.effect_type == "Damage" else "+"
        return f"{self.name} ({self.ability_type}): {sign}{self.effect}"

    def details(self):
        sign = "-" if self.effect_type == "Damage" else "+"
        desc = f"\n{self.name}\n{''.join(['-' for x in range(len(self.name))])}"
        desc += f"\nDescription: {self.description}"
        desc += f"\nType: {self.ability_type} ({self.effect_type})"
        desc += f"\nEffect: {sign}{self.effect}"

    def export(self) -> Dict[str, Any]:
        return self.__dict__

    def print_to_file(self) -> None:
        logger.info(f"Saving {self.name} to {self.name}.json")
        with open(f"{self.name}.json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)
