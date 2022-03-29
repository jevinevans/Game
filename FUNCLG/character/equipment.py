"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: The Equipment class allows for creation of objects in the game to be used by
    characters and placed inside of the armor or in other holders/storage containers inside
    of the game.
"""

import json
from typing import Any, Dict

from loguru import logger
from typing_extensions import Self

from ..utils import types as uTypes

logger.add("./logs/character/equipment.log", rotation="1 MB", retention=5)


class Equipment:
    """
    Defines the equipmet class for the game. Equipment can be weapons or armor pieces.
    """

    def __init__(
        self,
        name: str = "",
        description: str = "",
        item_type: int = 0,
        armor_type: int = 0,
        weapon_type: int = -1,
        level: int = 0,
        damage: int = 0,
    ) -> None:
        """
        Creates an equipment item
        """

        self.name = name
        self.description = description
        self.item_type = item_type
        self.armor_type = armor_type
        self.weapon_type = weapon_type
        self.level = level
        self.damage = damage
        # self.stats = #STAT Object /may replace abiilty points with stats
        logger.debug(f"Created Equipment: {name}")

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.level}]"

    # TODO: add indention factor
    def details(self) -> str:
        desc = f"\n{self.name}\n{''.join(['-' for x in range(len(self.name))])}"
        desc += f"\nLevel:{self.level:3d}\nAbility Pts: {self.damage} "
        desc += "ATK" if self.get_item_type() == "Weapon" else "DEF"
        desc += f"\nType: {self.get_item_description()}"
        desc += f"\nDescription: {self.description}"
        return desc

    def print_to_file(self) -> None:
        logger.info(f"Saving Equipment: {self.name}")
        with open(self.name + ".json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def export(self) -> Dict[str, Any]:
        # TODO: May have to change function when STATS object is integrated
        # Function will just need to call the export for each
        logger.info(f"Exporting Equipment: {self.name}")
        return self.__dict__

    def get_item_type(self) -> str:
        return uTypes.get_item_type(self.item_type)

    def get_armor_type(self) -> str:
        return uTypes.get_armor_type(self.armor_type)

    def get_weapon_type(self) -> str:
        return uTypes.get_weapon_type(self.weapon_type)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type, self.weapon_type)

    # TODO: Look to see if this is the best way to copy an object and if there is a better way to send all of the attributes (it may be * or **)
    def copy(self) -> Self:
        """Copies the current object"""
        return Equipment(
            self.name,
            self.description,
            self.item_type,
            self.armor_type,
            self.weapon_type,
            self.level,
            self.damage,
        )

    # TODO: Defined method
    # def get_stats(self):
