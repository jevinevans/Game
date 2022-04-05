"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: The Equipment class allows for creation of objects in the game to be used by
    characters and placed inside of the armor or in other holders/storage containers inside
    of the game.
"""

import json
from typing import Any, Dict, Optional, Union

from loguru import logger
from typing_extensions import Self

from ..utils import types as uTypes
from .modifiers import Modifier

logger.add("./logs/character/equipment.log", rotation="1 MB", retention=5)


# TODO: May split into body equipment and weapons, that way
# TODO: Remove damage and level because they will be a part of the equipment stat
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
    ) -> None:
        """
        Creates an equipment item
        """

        self.name = name
        self.description = description
        self.item_type = item_type
        self.armor_type = armor_type
        # self.stats = #STAT Object /may replace abiilty points with stats
        logger.debug(f"Created Equipment: {name}")

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.armor_type} {self.item_type}]"

    # TODO: add indention factor
    # TODO: add stats info for details
    def details(self, indent: int = 0) -> str:
        desc = f"\n{' '*indent}{self.name}"
        desc += f"\n{' '*indent}{'-'*len(self.name)}"
        desc += f"\n{' '*indent}Type: {self.get_item_description()}"
        desc += f"\n{' '*indent}nDescription: {self.description}"
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

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type)

    # TODO: Look to see if this is the best way to copy an object and if there is a better way to send all of the attributes (it may be * or **)
    def copy(self) -> Self:
        """Copies the current object"""
        return Equipment(
            self.name,
            self.description,
            self.item_type,
            self.armor_type,
        )


# TODO: WeaponEquipment: Define functions [details, export, getstats]
class WeaponEquipment(Equipment):
    """
    Equipment Subclass for Weapons. Has a specific stat item and determines the type of weapon
    """

    def __init__(self, name: str, weapon_type: int, description: str = "", armor_type: int = 0):
        super().__init__(name=name, description=description, item_type=4, armor_type=armor_type)

        self.weapon_type = weapon_type
        # TODO: self.stats  =  Create and add weapon stats that way they can be buffed or debuffed during battle

    def get_weapon_type(self) -> str:
        return uTypes.get_weapon_type(self.weapon_type)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type, self.weapon_type)

    # def details(self) -> str:
    #     desc = super().details()
    #     desc += f"{' '*indent} ....
    # Add stats info
    #     self.stats.details()
    #     return desc

    def copy(self) -> Self:
        """Copies the current object"""
        return WeaponEquipment(
            self.name,
            self.weapon_type,
            self.description,
            self.armor_type,
        )

    # def get_stats(self):
    # def export(self):


# TODO: BodyEquipment: Define functions [details, export, get_mods]
class BodyEquipment(Equipment):
    """
    Equipment Subclass specifically for armor items that are not weapons.
    """

    def __init__(
        self,
        name: str,
        modifiers: Optional[Dict[str, Union[int, float]]] = None,
        description: str = "",
        armor_type: int = 0,
        item_type: int = 0,
    ):
        """
        Modifiers should be a dictionary that has the possible properties {'adds':{}, 'mults':{}} that will be verified on Modifier creation
        """
        super().__init__(name=name, description=description, item_type=item_type, armor_type=armor_type)

        self.mods = Modifier(name=self.name)
        if modifiers:
            self.mods.add_mods(m_type="adds", mods=modifiers.get("adds", {}))
            self.mods.add_mods(m_type="mults", mods=modifiers.get("mults", {}))

    def get_mods(self) -> str:
        return self.mods.get_mods()

    # def details(self) -> str:
    #     desc = super().details()
    #     desc += f"{' '*indent} ....
    # Add mod info
    #     self.stats.details()
    #     return desc

    def copy(self) -> Self:
        """Copies the current object"""
        return BodyEquipment(
            self.name,
            self.mods,
            self.description,
            self.armor_type,
            self.item_type,
        )

    # def get_mods(self):

    def export(self):
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter
