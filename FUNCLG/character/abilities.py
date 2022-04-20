"""
Programmer: Jevin Evans
Date: 12.5.2021
Description: This defines Abilities object used for the roles class
"""

import json
from typing import Any, Dict

from loguru import logger
from typing_extensions import Self

from ..utils.types import DAMAGE_TYPES, get_ability_effect_type

# logger.add("./logs/character/abilities.log", rotation="1 MB", retention=5)


class Abilities:
    """
    Defines character/monster abilities
    """

    def __init__(
        self,
        name: str,
        damage_type: str,
        effect: int,
        description: str,
    ) -> None:
        self.name = name
        self.damage_type = damage_type if damage_type in DAMAGE_TYPES else "None"
        self.ability_group, effect_type = get_ability_effect_type(self.damage_type)
        self.effect = (
            effect * effect_type
        )  # TODO: Will become stats, and a specific sub class that will be more focused for armor
        self.description = description
        logger.debug(f"Created Ability: {name}")

    def __str__(self):
        return f"{self.name} ({self.damage_type}): {self.effect}"

    def details(self, indent: int = 0):
        desc = f"\n{' '*indent}{self.name}\n{' '*indent}{''.join(['-' for x in range(len(self.name))])}"
        desc += f"\n{' '*indent}Description: {self.description}"
        desc += f"\n{' '*indent}Type: {self.damage_type} ({self.ability_group})"
        desc += f"\n{' '*indent}Effect: {self.effect}"
        return desc

    def export(self) -> Dict[str, Any]:
        logger.info(f"Exporting Ability: {self.name}")
        return self.__dict__.copy()

    def print_to_file(self) -> None:
        logger.info(f"Saving Ability: {self.name}")
        with open(f"{self.name}.json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def copy(self) -> Self:
        """Returns a copy of the object"""
        return Abilities(self.name, self.damage_type, abs(self.effect), self.description)

    # TODO: Define what happens when using a power. Damage and effect on which stat
    # def use()
