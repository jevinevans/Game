"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

import json
from typing import Any, Dict, List, Optional

from loguru import logger

from ..utils.types import STAT_TYPES


"""Mod Example

{
    id: {
        "add":{
            "ATK":-15,
            "MP": 30,
        },
        "mult":{
            "DEF": 0.2,
            "HP": -0.1
        }
    }
}

"""
class Modifier:
    
class Stats:
    """
    This class defines the basic stat class structure for all objects
    """
    def __init__(self, HP:int, MP:int, ATK:int, DEF:int, mods:Optional[Dict[str, Any]]):
        # Base Stats
        self._HP = HP
        self._MP = MP
        # Modified Stats
        self.HP = HP  
        self.MP = MP
        self.ATK = ATK
        self.DEF = DEF
        # Modifiers for Boosting and changing stats
        self.modifiers = {}
        if mods:
            for id, mod in mods.items():
                self.modifiers[id] = self._verify_modifier(mod)

    def add_modifier(self, id:str, mod:Dict[str, Any]):
        """
        This funciton modifies the base stats of a stat positively or negatively
        """
        self.modifiers[id] = self._verify_modifier(mod)


    def remove_modifier(self, id:str):
        if id in self.modifiers:
            del self.modifiers[id]

    @staticmethod
    def _verify_modifier(mod):
        # check stat is valid, mod type, and that if mult then the effect is a percentage
        
        for m_type in ["add", "mult"]:
            for stat, effect in mod.setdefault(m_type, {}).items():
                if stat not in STAT_TYPES:
                    del mod[m_type][stat]
                elif m_type == "mult" and effect > 1.0:
                    while effect > 1.0:
                        effect /= 10
                    mod[m_type][stat] = effect

        return mod
        

    def get_stat(self, stat):
        base = getattr(self, stat, 0)
        multiplier = 1

        for _, mod in self.modifiers:
            base += mod['add'].get(stat, default=0)
            multiplier += mod['mult'].get(stat, default=0)

        return base*multiplier
    
    def export(self) -> Dict [str, Any]:
        logger.info(f"Exporting Stats")
        return self.__dict__


class Character_Stats(Stats):
    def __init__(self, HP:int, MP:int, ATK:int, DEF:int):
        super().__init__(HP, MP, ATK, DEF)
        
        self.alive = True
        # TODO: Figure out what other stats are needed
        

    