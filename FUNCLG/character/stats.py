"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional

from loguru import logger

from ..utils.types import STAT_TYPES


class Modifier:
    """
    These are used for to change stats along with being added to abilities to change stats

    Mod Example
        {
            id: {
                "add":{
                    "attack":-15,
                    "mana": 30,
                },
                "mult":{
                    "defense": 0.2,
                    "health": -0.1
                }
            }
        }

    """
    def __init__(self, name: str, adds: Optional[Dict[str, Any]], mults: Optional[Dict[str, Any]]):
        self.name = name
        self.add = self._verify_mods(adds)
        self.mult = self._verify_mods(mults)

    @staticmethod
    def _verify_mods(mod):
        for stat in mod:
            if stat not in STAT_TYPES:
                del mod[stat]
        return mod

    def add_mod(self, m_type: str, stat: str, effect: int):
        if stat in STAT_TYPES:
            getattr(self, m_type).append({stat: effect})

    def remove_mod(self, m_type: str, stat: str):
        if m_dict := getattr(self, m_type):
            if stat in m_dict:
                del m_dict[stat]

    def get_stats(self):
        return {"add": self.add, "mult": self.mult}

    def export(self):
        return self.__dict__

# TODO: Possibly create a subclass tempMod. This would be the result of an attack and would expire after a number of turns and be removed after the combat, instance is over


class Stats:
    """
    This class defines the basic stat class structure for all objects
    """

    # TODO: Create a more abstract load based on STAT_TYPES
    def __init__(
        self, health: int, mana: int, attack: int, defense: int, mods: Optional[List[Modifier]]
    ): # pylint: disable=too-many-arguments
        # Base Stats
        self._health = health
        self._mana = mana
        # Modified Stats
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        # Modifiers for Boosting and changing stats
        self.modifiers = {}
        if mods:
            for mod in mods:
                self.modifiers[mod.name] = mod.get_stats()

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
            base += mod["add"].get(stat, default=0)
            multiplier += mod["mult"].get(stat, default=0)

        return base * multiplier

    def export(self) -> Dict[str, Any]:
        logger.info("Exporting Stats")
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter

    def reset(self):
        self.health = self._health
        self.mana = self._mana
        
        for name in self.modifiers:
            self.remove_modifier(name)


# TODO: Do I need a specific character stat or do I just need the basic parts?
# class Character_Stats(Stats):
#     def __init__(self, health:int, mana:int, attack:int, defense:int):
#         super().__init__(health, mana, attack, DEF)
#         self.alive = True
