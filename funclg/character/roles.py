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
from .stats import Stats

# logger.add("./logs/character/roles.log", rotation="1 MB", retention=5)


class Roles:
    # pylint: disable=too-many-instance-attributes

    """
    Creates a roles for a character
    """

    MAX_ABILITIES = 5
    DB_PREFIX = "ROLES"
    BASE_STATS = {"attack": 5, "health": 5, "energy": 5, "defense": 5}

    def __init__(
        self,
        name: str,
        description: str,
        armor_type: int,
        ability_types: Optional[List] = None,
        abilities: Optional[List[Abilities]] = None,
        stats: Dict[str, Any] = None,
        **kwargs,
    ):  # pylint: disable=too-many-arguments, too-many-instance-attributes
        self.name = name
        self.description = description
        self.armor_type = armor_type

        self.ability_types = (
            [a_type for a_type in ability_types if a_type in ABILITY_TYPES]
            if ability_types
            else ["Basic"]
        )
        self.abilities = self._validate_abilities(abilities) if abilities else []
        self._id = db.id_gen(self.DB_PREFIX, kwargs.get("_id"))
        self.stats = Stats(**stats) if stats else Stats(attributes=Roles.BASE_STATS)
        self.level = kwargs.get("level", 1)
        logger.debug(f"Created Role: {name}")

    def __str__(self):
        return f"Class: {self.name} [lvl {self.level}] | Type(s): {', '.join(self.ability_types)} | {get_armor_type(self.armor_type)} Armor | Abilities: {len(self.abilities)}"

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def power(self):
        return self.stats.power

    def add_ability(self, ability: Abilities) -> bool:
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

    def get_ability(self, index: int):
        """Returns the wanted power"""
        if self.abilities and abs(index) < len(self.abilities):
            return self.abilities[index]
        logger.warning("There is no power in this slot.")
        return None

    def remove_ability(self, index: int) -> bool:
        # Validation will be done at a higher level
        if self.abilities and index < len(self.abilities):
            old_ability = self.abilities.pop(index)
            del old_ability
            return True
        return False

    def details(self, indent: int = 0):
        desc = f"\n{' '*indent}Class: {self.name} [lvl {self.level}]"
        desc += f"\n{' '*indent}{'-'*(len(self.name)+14+len(str(self.level)))}"
        desc += f"\n{' '*indent}Armor Type: {get_armor_type(self.armor_type)}"
        desc += f"\n{' '*indent}Description: {self.description}\n"
        desc += self.stats.details(indent) + "\n"
        desc += f"\n{' '*indent}Role Abilities:\n"
        if self.abilities:
            for ability in self.abilities:
                desc += ability.details(indent + 2)
                desc += "\n"
        else:
            desc += f"{' '*(indent+2)}No Abilities\n"

        return desc

    def export(self) -> Dict[str, Any]:
        logger.debug(f"Exporting Role: {self.name}")
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if key == "abilities" and len(value) > 0:
                for index, ability in enumerate(value):
                    if isinstance(ability, Abilities):
                        value[index] = ability.export()
            if isinstance(value, Stats):
                exporter[key] = value.export()
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

    def get_stats(self):
        return self.stats.get_stats()

    def copy(self) -> Self:
        """Returns a copy of the object"""
        return Roles(
            name=self.name,
            description=self.description,
            armor_type=self.armor_type,
            ability_types=self.ability_types,
            abilities=self.abilities,
            _id=self._id,
            stats=self.stats.copy(),
            level=self.level,
        )

    def level_up(self):
        self.level += 1
        self.stats.level_up()
        if self.abilities:
            for ability in self.abilities:
                ability.level_up()

    def to_mod(self):
        return self.stats.to_mod(self.name)
