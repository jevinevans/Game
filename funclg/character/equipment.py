"""
Programmer: Jevin Evans
Date: 7.13.2021
Description: The Equipment class allows for creation of objects in the game to be used by
    characters and placed inside of the armor or in other holders/storage containers inside
    of the game.
"""

import json
from typing import Dict, Optional

from loguru import logger
from typing_extensions import Self

import funclg.utils.data_mgmt as db

from ..utils import types as uTypes
from .modifiers import Modifier

# logger.add("./logs/character/equipment.log", rotation="1 MB", retention=5)
# pylint: disable=duplicate-code

# TODO: Change equipment display methods


class Equipment:
    """
    Defines the equipmet class for the game. Equipment can be weapons or armor pieces.
    """

    DB_PREFIX = "EQUIP"

    def __init__(
        self,
        name: str,
        mod: Modifier,
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
        self.mod = mod

        self._id = db.id_gen(kwargs.get("prefix", self.DB_PREFIX), kwargs.get("_id"))

        logger.debug(f"Created Equipment: {name}")

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.item_type}]"

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def id(self):
        return self._id

    def details(self, indent: int = 0) -> str:
        desc = f"\n{' '*indent}{self.name}"
        desc += f"\n{' '*indent}{'-'*len(self.name)}"
        desc += f"\n{' '*indent}Type: {self.get_item_description()}"
        desc += f"\n{' '*indent}Description: {self.description}"
        desc += f"\n\n{' '*indent}Modifier(s):"
        desc += self.mod.details(indent + 2)
        return desc

    def print_to_file(self) -> None:
        logger.info(f"Saving Equipment: {self.name}")
        with open(self.name + ".json", "w", encoding="utf-8") as out_file:
            json.dump(self.export(), out_file)

    def export(self):
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Modifier):
                exporter[key] = value.export()
        return exporter

    def get_item_type(self) -> str:
        return uTypes.get_item_type(self.item_type)

    def get_armor_type(self) -> str:
        return uTypes.get_armor_type(self.armor_type)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type)

    def get_mods(self):
        return self.mod.get_mods()

    def copy(self) -> Self:
        """Copies the current object"""
        return Equipment(
            name=self.name,
            description=self.description,
            item_type=self.item_type,
            armor_type=self.armor_type,
            mod=self.mod,
            _id=self._id,
        )


class WeaponEquipment(Equipment):
    """
    Equipment Subclass for Weapons. Has a specific stat item and determines the type of weapon
    """

    DB_PREFIX = "WEAPON"

    def __init__(
        self,
        name: str,
        weapon_type: str,
        description: str = "",
        mod: Optional[Dict[str, Dict]] = None,
        armor_type: int = 1,
        **kwargs,
    ):
        weapon_mod = Modifier(name=name)
        if mod:
            weapon_mod.add_mod(m_type="adds", mods=mod.get("adds", {}))
            weapon_mod.add_mod(m_type="mults", mods=mod.get("mults", {}))
        else:
            weapon_mod.add_mod(m_type="adds", mods={"attack": 1, "energy": 1})

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
            mod=weapon_mod,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
        )

    # TODO: Change equipment display methods
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
            mod=self.mod.get_mods(),
            _id=self.id,
        )

    # TODO: Override details to include the weapon type


class BodyEquipment(Equipment):
    """
    Equipment Subclass specifically for armor items that are not weapons.
    """

    DB_PREFIX = "ARMOR"

    def __init__(
        self,
        name: str,
        mod: Optional[Dict[str, Dict]] = None,
        description: str = "",
        armor_type: int = 0,
        item_type: int = 0,
        **kwargs,
    ):
        """
        Modifiers should be a dictionary that has the possible properties {'adds':{}, 'mults':{}} that will be verified on Modifier creation
        """
        body_mod = Modifier(name=name)
        if mod:
            body_mod.add_mod(m_type="adds", mods=mod.get("adds", {}))
            body_mod.add_mod(m_type="mults", mods=mod.get("mults", {}))
        else:
            body_mod.add_mod(m_type="adds", mods={"health": 1, "defense": 1})

        super().__init__(
            name=name,
            description=description,
            item_type=item_type,
            armor_type=armor_type,
            mod=body_mod,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
        )

    # TODO: Change equipment display methods
    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.armor_type} {self.item_type}]"

    def copy(self) -> Self:
        """Copies the current object"""
        return BodyEquipment(
            name=self.name,
            mod=self.mod.get_mods(),
            description=self.description,
            armor_type=self.armor_type,
            item_type=self.item_type,
            _id=self.id,
        )
