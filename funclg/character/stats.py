"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional

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
        extra_attributes: Optional[Dict[str, int]] = None,
        modifiers: Optional[List[Modifier]] = None,
    ):
        # Initializes level in case the call stat does not
        self.level = 0

        for attr in Stats.BASE_ATTR:
            setattr(self, attr, 0)

        # Adds the individual stat
        if extra_attributes:
            for key, value in extra_attributes.items():
                setattr(self, key, value)

        # Modifiers for changing stats
        self.mods = {}
        if modifiers:
            for mod in modifiers:
                if self._validate_mod(mod):
                    self.mods[mod.name] = mod.get_mods()

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

    # TODO: check for attribute in class first
    def get_stat(self, stat: str):
        base = getattr(self, stat, None)

        if not base:
            return base

        multiplier = 1

        for _, mod in self.mods.items():
            base += mod["adds"].get(stat, 0)
            multiplier += mod["mults"].get(stat, 0)

        return base * multiplier

    def get_stats(self):
        """Returns all user stats, process each stat the object has...?"""
        stats = {}
        for attr in [attr for attr in self.__dict__ if attr not in Stats.PRINT_IGNORES]:
            if attr == "level":
                stats[attr] = self.level
            else:
                stats[attr] = self.get_stat(attr)
        return stats

    def export(self) -> Dict[str, Any]:
        logger.info("Exporting Stats")
        return self.__dict__


# TODO: Consider if level/level up is a common function for all stats and can be added to base class

# For each subclass define a set of stats and if no information is passed in just initiate to a base value

# TODO: Create an equipment class
"""
This class will have the stats for piece of equipment

Stats [Health, Energy, Defense, Attack]
"""


# TODO: Create an abilities class
"""
While mostly modifiers, this stat will have the cost of an ability
Stats [Energy Cost]

Need to add a function to get the modifiers that will take effect on usage
"""

# TODO: Create an armor stat
"""
The armor stat subclass will have a slot for each individual weapon slot and aggregate those stats so that it is easier changed. In the armor class on equip and dequip the stats can be updated.

[Health, Energy, Defense, Attack]

The armor may get a base stat possibly???
"""

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
