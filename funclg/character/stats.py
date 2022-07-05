"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional, Union

from loguru import logger

from .modifiers import Modifier


class Stats:
    """
    This class defines the basic stat class structure for all objects
    """

    PRINT_IGNORES = ["mods"]
    BASE_ATTR = ["health", "energy", "attack", "defense"]

    def __init__(
        self,
        attributes: Optional[Dict[str, Any]] = None,
        modifiers: Optional[List[Modifier]] = None,
        default: Optional[int] = 0,
    ):
        """
        Creates a stat object, if no attributes provided then the BASE_ATTRs are set to a default value
        """
        # Initializes level in case the call stat does not
        self.level = 0

        for attr in Stats.BASE_ATTR:
            setattr(self, attr, default)

        # Adds the individual stat
        if attributes:
            for key, value in attributes.items():
                setattr(self, key, value)

        # Modifiers for changing stats
        self.mods = {}
        if modifiers:
            for mod in modifiers:
                if self._validate_mod(mod):
                    self.mods[mod.name] = mod.get_mods()

    def __str__(self):
        return self.details()

    def details(self, indent: int = 0):
        stats = f"\n{' '*indent}Stats\n{' '*indent}"
        stats += "-" * 5
        if self.level:
            stats += f"\n{' '*indent}Level: {self.level}"
        ignores = Stats.PRINT_IGNORES
        ignores.append("level")
        for attr in [attr for attr in self.__dict__ if attr not in ignores]:
            stats += f"\n{' '*indent}{attr.capitalize()}: {self.get_stat(attr)}"
        return stats

    def _validate_mod(self, mod: Modifier):
        """
        Checks for duplicate mods being applied to stat
        """
        return not mod.name in self.mods

    def add_mod(self, mod: Modifier):
        """
        This funciton modifies the base stats of a stat positively or negatively
        """
        if self._validate_mod(mod):
            self.mods[mod.name] = mod.get_mods()
        else:
            logger.warning(f"Modifier: {mod.name} is not valid for this stat")
            return

    def remove_mod(self, name: str):
        if name in self.mods:
            del self.mods[name]
            return
        logger.error(f"This stat does not have the '{name}' modifier.")

    def get_stat(self, stat: str) -> Union[int, float, None]:
        base = getattr(self, stat, None)

        if not base:
            return base

        multiplier = 1

        for _, mod in self.mods.items():
            base += mod["adds"].get(stat, 0)
            multiplier += mod["mults"].get(stat, 0)

        return round(base * multiplier, 2)

    def get_stats(self) -> Dict[str, Any]:
        """Returns all user stats, process each stat the object has...?"""
        stats = {}
        for attr in [attr for attr in self.__dict__ if attr not in Stats.PRINT_IGNORES]:
            stats[attr] = self.get_stat(attr)
        stats["level"] = self.level
        return stats

    def export(self) -> Dict[str, Any]:
        logger.info("Exporting Stats")
        return self.__dict__.copy()

    # def level_up(self):


# TODO: Create a role stat class
"""
This stat will have a base stats for a users roles and any boosts

[Health, Energy, Attack]
"""


# TODO: Build Character stats
"""
This will probably take a armor and roles stat and aggregate the information for the character info

- may need an update function to get information from the other stats, this will either be on the stat or the character class, probably on the character class

[Health (max), health (current), energy (max), energy (current), defense, attack, alive status,]

- need to create a reset method to return the health and energy back to max
"""
