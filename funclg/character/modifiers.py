"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the modifiers object that will be used for all stats
"""

from typing import Any, Dict, Optional, Union

# from loguru import logger
from ..utils.types import MOD_ADD_RANGE, MOD_MULT_RANGE, MODIFIER_TYPES


class Modifier:
    """
    These are used for to change stats along with being added to abilities to change stats

    Mod Example
        {
            id: {
                "add":{
                    "attack":-15,
                    "energy": 30,
                },
                "mult":{
                    "defense": 0.2,
                    "health": -0.1
                }
            }
        }

    """

    M_TYPES = ["adds", "mults"]

    def __init__(
        self,
        name: str,
        adds: Optional[Dict[str, Any]] = None,
        mults: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.adds = self._verify_mods(adds)
        self.mults = self._verify_mods(mults)

    def __str__(self):
        string = f"Modifier: {self.name}:\n"
        string += self._friendly_read(indent=2)

        return string

    def details(self, indent: int = 0):
        string = f"\n{' '*indent}{self.name}:\n"
        string += self._friendly_read(indent=indent + 2)

        return string

    @staticmethod
    def _verify_mods(mods):
        # TODO: Add check for percentage and add, and compare against the MOD_ADD_RANGE and MOD_MULT_RANGE
        verified = {}
        if mods:
            for stat in mods:
                if stat not in MODIFIER_TYPES:
                    continue
                verified[stat] = mods[stat]
        return verified

    def _add_mod(self, m_type: str, stat: str, effect: int):
        m_set = getattr(self, m_type)
        m_set[stat] = effect

    def add_mod(self, m_type: str, mods: Dict[str, int]):
        if m_type in self.M_TYPES and len(mods) >= 1:
            for stat, effect in self._verify_mods(mods).items():
                self._add_mod(m_type=m_type, stat=stat, effect=effect)

    def remove_mod(self, m_type: str, stat: str):
        if m_type in self.M_TYPES:
            m_dict = getattr(self, m_type)
            if stat in m_dict:
                del m_dict[stat]

    def get_mods(self):
        return {"adds": self.adds, "mults": self.mults}

    def export(self):
        return self.__dict__.copy()

    @staticmethod
    def _friendly_read_mod(effect: Union[int, float], percentage: bool = False):
        friendly = f"{effect*100}%" if percentage else str(effect)
        if effect > 0:
            friendly = "+" + friendly
        return " " + friendly

    def _friendly_read(self, indent: int = 0):
        stats = {}

        if self.adds:
            for stat, effect in self.adds.items():
                stats.setdefault(stat, []).append(self._friendly_read_mod(effect))
        if self.mults:
            for stat, effect in self.mults.items():
                stats.setdefault(stat, []).append(self._friendly_read_mod(effect, percentage=True))

        string = ""
        for stat, vals in stats.items():
            string += " " * indent + str(stat).capitalize() + ":"
            string += ",".join(val for val in vals)
            string += "\n"
        return string
