"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional

from loguru import logger

from .modifiers import Modifier

# from typing_extensions import Self


class Stats:
    """
    This class defines the basic stat class structure for all objects
    """

    # TODO: Create a more abstract load based on STAT_TYPES
    def __init__(
        self,
        attributes: Dict[str, int],
        mods: Optional[List[Modifier]] = None,
    ):
        for key, value in attributes.items():
            setattr(self, key, value)

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

    def get_stats(self):
        """Returns all user stats, process each stat the object has...?"""
        # Override in sub class
        pass

    def export(self) -> Dict[str, Any]:
        logger.info("Exporting Stats")
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter


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
