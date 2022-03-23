"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional, Union

from loguru import logger
from typing_extensions import Self

from ..utils.types import STAT_TYPES
from .modifiers import Modifier

class Stats:
    """
    This class defines the basic stat class structure for all objects
    """

    # TODO: Create a more abstract load based on STAT_TYPES
    def __init__(
        self,
        health: int,
        energy: int,
        attack: int,
        defense: int,
        mods: Optional[List[Modifier]] = None,
    ):  # pylint: disable=too-many-arguments
        self.health = health
        self.energy = energy
        self.attack = attack
        self.defense = defense

        # Modifiers for changing stats
        self.modifiers = {}
        if mods:
            for mod in mods:
                self.modifiers[mod.name] = mod.get_mods()

    def add_modifier(self, name: str, mod: Modifier):
        """
        This funciton modifies the base stats of a stat positively or negatively
        """
        self.modifiers[name] = mod

    def remove_modifier(self, name: str):
        if name in self.modifiers:
            del self.modifiers[name]

    def get_stat(self, stat):
        base = getattr(self, stat, 0)
        multiplier = 1

        for _, mod in self.modifiers:
            base += mod["adds"].get(stat, default=0)
            multiplier += mod["mults"].get(stat, default=0)

        return base * multiplier

    def export(self) -> Dict[str, Any]:
        logger.info("Exporting Stats")
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter

# TODO: Consider creating a Equipment stats class that will pull the info for item, weapon, armor types and include all other base stats


class Character_Stats(Stats):
    def __init__(self, health:int, energy:int, attack:int, defense:int):
        super().__init__(health, energy, attack, defense)
        self.alive = True # TODO: Does this attribute need to be here

        # Base Health and energy
        self._health = health
        self._energy = energy

    def reset(self):
        self.health = self._health
        self.energy = self._energy

        for name in self.modifiers:
            self.remove_modifier(name)
