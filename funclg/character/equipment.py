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

import funclg.utils.data_mgmt as db

from ..utils import types as uTypes
from .stats import Stats

# logger.add("./logs/character/equipment.log", rotation="1 MB", retention=5)
# pylint: disable=duplicate-code


class Equipment:
    """
    Defines the equipmet class for the game. Equipment can be weapons or armor pieces.
    """

    DB_PREFIX = "EQUIP"

    def __init__(
        self,
        name: str,
        stats: Stats,
        description: str = "",
        item_type: int = 0,
        armor_type: int = 0,
        **kwargs,
    ):
        """
        Creates an equipment item
        """

        self.name = name
        self.description = description
        self.item_type = item_type
        self.armor_type = armor_type
        self.stats = stats
        self.level = kwargs.get("level", 1)

        self._id = db.id_gen(kwargs.get("prefix", self.DB_PREFIX), kwargs.get("_id"))

        logger.debug(f"Created Equipment: {name}")

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [lvl {self.level}] [{uTypes.ITEM_TYPES[self.item_type]}]"

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def power(self):
        return self.stats.power

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    def details(self, indent: int = 0) -> str:
        desc = f"\n{' '*indent}{self.name} [lvl {self.level}]"
        desc += f"\n{' '*indent}{'-'*(len(self.name) + 7 + len(str(self.level)))}"
        desc += f"\n{' '*indent}Type: {self.get_item_description()}"
        desc += f"\n{' '*indent}Description: {self.description}\n"
        desc += self.stats.details(indent)
        return desc

    def print_to_file(self) -> None:
        logger.info(f"Saving Equipment: {self.name}")
        with open(self.name + ".json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def export(self):
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Stats):
                exporter[key] = value.export()
        return exporter

    def get_item_type(self) -> str:
        return uTypes.get_item_type(self.item_type)

    def get_armor_type(self) -> str:
        return uTypes.get_armor_type(self.armor_type)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type)

    def get_stats(self):
        return self.stats.get_stats()

    def copy(self) -> Self:
        """Copies the current object"""
        return Equipment(
            name=self.name,
            description=self.description,
            item_type=self.item_type,
            armor_type=self.armor_type,
            stats=self.stats.copy(),
            _id=self._id,
            level=self.level,
        )

    def level_up(self):
        self.level += 1
        self.stats.level_up()

    def to_mod(self):
        return self.stats.to_mod(self.name)


class WeaponEquipment(Equipment):
    """
    Equipment Subclass for Weapons. Has a specific stat item and determines the type of weapon
    """

    DB_PREFIX = "WEAPON"
    BASE_STATS = {"attack": 5, "health": 1, "energy": 5, "defense": 1}

    def __init__(
        self,
        name: str,
        weapon_type: str,
        description: str = "",
        armor_type: int = 1,
        stats: Dict[str, Any] = None,
        **kwargs,
    ):
        new_stat = {}
        if stats:
            new_stat = Stats(**stats)
        else:
            new_stat = Stats(attributes=WeaponEquipment.BASE_STATS)

        self.weapon_type = self._validate_weapon_type(weapon_type)
        armor_type = (
            armor_type
            if armor_type == uTypes.WEAPON_TYPES[self.weapon_type]
            else uTypes.WEAPON_TYPES[self.weapon_type]
        )

        super().__init__(
            name=name,
            description=description,
            item_type=4,
            armor_type=armor_type,
            stats=new_stat,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
            level=kwargs.get("level", 1),
        )

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [lvl {self.level}] [{self.weapon_type} {uTypes.ITEM_TYPES[self.item_type]}]"

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.weapon_type} {self.item_type}]"

    @staticmethod
    def _validate_weapon_type(weapon_type: str):
        return weapon_type if weapon_type in uTypes.WEAPON_TYPES else "Unknown"

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type, self.weapon_type)

    def copy(self) -> Self:
        """Copies the current object"""
        return WeaponEquipment(
            name=self.name,
            weapon_type=self.weapon_type,
            description=self.description,
            armor_type=self.armor_type,
            stats=self.stats.copy(),
            _id=self.id,
            level=self.level,
        )

    def export(self):
        logger.debug(f"Exporting Weapon: {self.name}")
        return super().export()


class BodyEquipment(Equipment):
    """
    Equipment Subclass specifically for armor items that are not weapons.
    """

    DB_PREFIX = "ARMOR"
    BASE_STATS = {"attack": 1, "health": 5, "energy": 1, "defense": 5}

    def __init__(
        self,
        name: str,
        item_type: int,
        armor_type: int,
        description: str = "",
        stats: Dict[str, Any] = None,
        **kwargs,
    ):
        """
        Modifiers should be a dictionary that has the possible properties {'base':{}, 'percentage':{}} that will be verified on Modifier creation
        """
        new_stat = {}
        if stats:
            new_stat = Stats(**stats)
        else:
            new_stat = Stats(attributes=BodyEquipment.BASE_STATS)

        super().__init__(
            name=name,
            description=description,
            item_type=item_type,
            armor_type=armor_type,
            stats=new_stat,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
            level=kwargs.get("level", 1),
        )

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [lvl {self.level}] [{uTypes.ARMOR_TYPES[self.armor_type]} {uTypes.ITEM_TYPES[self.item_type]}]"

    def copy(self) -> Self:
        """Copies the current object"""
        return BodyEquipment(
            name=self.name,
            stats=self.stats.copy(),
            description=self.description,
            armor_type=self.armor_type,
            item_type=self.item_type,
            _id=self.id,
            level=self.level,
        )

    def export(self):
        logger.debug(f"Exporting Armor: {self.name}")
        return super().export()
