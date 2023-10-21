"""
Programmer: Jevin Evans
Date: 12.5.2021
Description: This defines Abilities object used for the roles class
"""

import json
from typing import Any, Dict, Optional

from loguru import logger
from typing_extensions import Self

import funclg.utils.data_mgmt as db

from ..utils.types import ABILITY_TYPES
from .modifiers import Modifier

# logger.add("./logs/character/abilities.log", rotation="1 MB", retention=5)
# pylint: disable=duplicate-code

# TODO: add energy cost attribute


class Abilities:
    """
    Defines character/monster abilities
    """

    DB_PREFIX = "ABILITY"

    def __init__(
        self,
        name: str,
        ability_type: str,
        description: str,
        mod: Optional[Dict[str, Dict]] = None,
        **kwargs,
    ):
        self.name = name
        self.description = description
        self.ability_type = ability_type if ability_type in ABILITY_TYPES else "Basic"
        self._target = ABILITY_TYPES[self.ability_type]["target"]

        # Set Ability Modifier effects
        self.mod = Modifier(name=name)
        val_mod = self._validate_mods(mod)
        self.mod.add_mod(ABILITY_TYPES[self.ability_type]["m_type"], val_mod)

        self._id = db.id_gen(self.DB_PREFIX, kwargs.get("_id"))
        self.level = kwargs.get("level", 1)

        logger.debug(f"Created Ability: {name}")

    def _validate_mods(self, modifier: Optional[Dict[str, Dict]] = None):
        m_type = ABILITY_TYPES[self.ability_type]["m_type"]
        if modifier:
            # Check if the right m_type is provided
            if mod := modifier.get(m_type, {}):
                pass_check = True
                for key in mod.keys():
                    pass_check &= key in ABILITY_TYPES[self.ability_type]["mods"]
                    logger.debug(
                        f"Mod Checks: {key} in {ABILITY_TYPES[self.ability_type]['mods']} {key in ABILITY_TYPES[self.ability_type]['mods']}"
                    )
                    if self._target == "enemy":
                        mod[key] = mod[key] if mod[key] < 0 else mod[key] * -1
                if pass_check:
                    return mod

            logger.warning("Provided mod was not compatable with selected ability.")
        logger.warning("Using default modifier value.")
        if self.ability_type == "Basic":
            return {}
        m_value = 1 if m_type == "adds" else 0.01
        return {"health": m_value}

    def __str__(self):
        string = f"{self.name} ({self.ability_type})"
        if self.mod.adds or self.mod.mults:
            string += f" - {self.mod}"
        return string

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    def details(self, indent: int = 0):
        desc = f"\n{' '*indent}{self.name} [lvl {self.level}]\n{' '*indent}"
        desc += "-" * (len(self.name) + 7 + len(str(self.level)))
        desc += f"\n{' '*indent}Description: {self.description}"
        desc += f"\n{' '*indent}Ability Type: {self.ability_type}"
        desc += f"\n{' '*indent}Target: {self._target.capitalize()}"
        desc += self.mod.details(indent + 2)
        return desc

    def export(self) -> Dict[str, Any]:
        logger.debug(f"Exporting Ability: {self.name}")
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter

    def print_to_file(self) -> None:
        logger.info(f"Saving Ability: {self.name}")
        with open(f"{self.name}.json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def copy(self) -> Self:
        """Returns a copy of the object"""
        return Abilities(
            name=self.name,
            ability_type=self.ability_type,
            mod=self.mod.export(),
            description=self.description,
            _id=self._id,
            level=self.level,
        )

    def level_up(self):
        self.level += 1
        self.mod.level_up()

    # TODO def use()
