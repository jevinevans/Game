"""
Programmer: Jevin Evans
Date: 1.13.2021
Description: The Roles class is to allow the characters to use abilities.
"""

import json
from typing import Any, Dict, List, Optional

from loguru import logger
from typing_extensions import Self

import funclg.utils.data_mgmt as db

from ..utils.types import ABILITY_TYPES, get_armor_type
from .abilities import Abilities

# logger.add("./logs/character/roles.log", rotation="1 MB", retention=5)


class Roles:
    """
    Creates a roles for a character
    """

    MAX_ABILITIES = 5
    DB_PREFIX = "ROLES"

    def __init__(
        self,
        name: str,
        description: str,
        armor_type: int,
        ability_types: Optional[List] = None,
        abilities: Optional[List[Abilities]] = None,
        **kwargs,
    ):  # pylint: disable=too-many-arguments
        self.name = name
        self.description = description
        self.armor_type = armor_type

        self.ability_types = (
            [a_type for a_type in ability_types if a_type in ABILITY_TYPES]
            if ability_types
            else ["None"]
        )
        self.abilities = self._validate_abilities(abilities) if abilities else []
        self._id = db.id_gen(self.DB_PREFIX, kwargs.get("_id"))
        # self.stats
        logger.debug(f"Created Role: {name}")

    def __str__(self):
        return f"Class: {self.name} | Class Type(s): {', '.join(self.ability_types)} | Armor Type: {get_armor_type(self.armor_type)} | Abilities: {len(self.abilities)}"

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    def add_power(self, ability: Abilities) -> bool:
        if ability.ability_type in self.ability_types:
            if len(self.abilities) < Roles.MAX_ABILITIES:
                self.abilities.append(ability.copy())
                logger.success(f"Added {ability.name} to {self.name}")
                return True
            logger.warning("Max abilities reached!")
            return False
        logger.warning(
            f"{ability.name}({ability.ability_type}) is not compatible with {self.name}({self.ability_types})"
        )
        return False

    def get_power(self, index: int):
        """Returns the wanted power"""
        if self.abilities and abs(index) < len(self.abilities):
            return self.abilities[index]
        logger.warning("There is no power in this slot.")
        return None

    def remove_power(self, index: int) -> bool:
        # Validation will be done at a higher level
        if self.abilities and index < len(self.abilities):
            old_ability = self.abilities.pop(index)
            del old_ability
            return True
        return False

    def details(self, indent: int = 0):
        desc = f"\n{' '*indent}Class: {self.name}"
        desc += f"\n{' '*indent}{'-'*(len(self.name)+7)}"
        desc += f"\n{' '*indent}Armor Type: {get_armor_type(self.armor_type)}"
        desc += f"\n{' '*indent}Description: {self.description}"
        desc += f"\n{' '*indent}Role Abilities:\n"
        if self.abilities:
            for ability in self.abilities:
                desc += ability.details(indent + 2)
                desc += "\n"
        else:
            desc += f"{' '*(indent+2)}No Abilities"
        return desc

    def export(self) -> Dict[str, Any]:
        logger.info(f"Exporting Role: {self.name}")
        exporter = self.__dict__.copy()
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

    def _validate_abilities(self, abilities: list) -> List[Abilities]:
        """
        Validates that abilities added are compatable
        """

        return [
            ability.copy() for ability in abilities if ability.ability_type in self.ability_types
        ]

    def copy(self) -> Self:
        """Returns a copy of the object"""
        return Roles(
            name=self.name,
            description=self.description,
            armor_type=self.armor_type,
            ability_types=self.ability_types,
            abilities=self.abilities,
            _id=self._id,
        )

    # def show_powers(): #TODO Define me
