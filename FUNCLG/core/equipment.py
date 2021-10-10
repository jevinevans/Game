#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/13/2021                                                                 #
#   Program: Equipment Class                                                        #
#   Description: The Equipment class allows for creation of objects in the game     #
#       to be used by characters and placed inside of the armor or in other         #
#       holders/storage containers inside of the game.                              #
#####################################################################################

import json
from typing import Any, Dict, Union

from ..utils import types as uTypes


class Equipment:
    def __init__(
        self,
        name: str = "",
        description: str = "",
        armorType: Union[str, None] = None,
        itemType: Union[str, None] = None,
        weaponType: Union[str, None] = None,
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
        desc += "ATK" if self.getItemType() == "Weapon" else "DEF"
        desc += f"\nType: {self.getItemDescription()}"
        desc += f"\nDescription: {self.description}"
        return desc

    def printToFile(self) -> None:
        with open(self.name + ".json", "w") as oFile:
            json.dump(self.export(), oFile)

    def export(self) -> Dict[str, Any]:
        # TODO: May have to change function when STATS object is integrated
        # Function will just need to call the export for each
        return self.__dict__

    def getItemType(self) -> str:
        return uTypes.getItemType(self.itemType)

    def getArmorType(self) -> str:
        return uTypes.getArmorType(self.armorType)

    def getWeaponType(self) -> str:
        return uTypes.getWeaponType(self.weaponType)

    def getItemDescription(self) -> str:
        return uTypes.getItemDescription(self.itemType, self.armorType, self.weaponType)

    # def getStats(self):
    # TODO: Defined method
