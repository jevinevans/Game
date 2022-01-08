"""   
Programmer: Jevin Evans
Date: 7.13.2021
Description: The Equipment class allows for creation of objects in the game to be used by 
    characters and placed inside of the armor or in other holders/storage containers inside 
    of the game.
"""

import json
from typing import Any, Dict, Optional

from ..utils import types as uTypes


class Equipment:
    def __init__(
        self,
        name: str = "",
        description: str = "",
        armorType: Optional[str] = None,
        itemType: Optional[str] = None,
        weaponType: Optional[str] = None,
        level: int = 0,
        abilityPoints: int = 0,
    ) -> None:
        """
        Creates an equipment item
        """

        self.name = name
        self.description = description
        self.armorType = armorType
        self.itemType = itemType
        self.weaponType = weaponType
        self.level = level
        self.abilityPoints = abilityPoints
        # self.stats = #STAT Object /may replace abiilty points with stats

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.level}]"

    def details(self) -> str:
        titleLen = 2 + len(self.name)
        desc = f"\n {self.name} \n{''.join(['-' for x in range(titleLen)])}"
        desc += f"\nLevel:{self.level:3d} | Ability Pts: {self.abilityPoints} "
        desc += "ATK" if self.get_item_type() == "Weapon" else "DEF"
        desc += f"\nType: {self.get_item_description()}"
        desc += f"\nDescription: {self.description}"
        return desc

    def print_to_file(self) -> None:
        with open(self.name + ".json", "w") as oFile:
            json.dump(self.export(), oFile)

    def export(self) -> Dict[str, Any]:
        # TODO: May have to change function when STATS object is integrated
        # Function will just need to call the export for each
        return self.__dict__

    def get_item_type(self) -> str:
        return uTypes.get_item_type(self.itemType)

    def get_armor_type(self) -> str:
        return uTypes.get_armor_type(self.armorType)

    def get_weapon_type(self) -> str:
        return uTypes.get_weapon_type(self.weaponType)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.itemType, self.armorType, self.weaponType)

    # TODO: Defined method
    # def getStats(self):
