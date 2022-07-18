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


class Equipment:
    """
    Defines the equipmet class for the game. Equipment can be weapons or armor pieces.
    """

    DB_PREFIX = "EQUIP"

    def __init__(
        self,
        name: str,
        modifier: Modifier,
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
        self.mod = modifier

        self._id = db.id_gen(kwargs.get("prefix", self.DB_PREFIX), kwargs.get("_id"))

        logger.debug(f"Created Equipment: {name}")

    def __str__(self) -> str:
        """
        Returns the name and level of the item
        """
        return f"{self.name} [{self.armor_type} {self.item_type}]"

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
            modifier=self.mod,
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
        weapon_type: int,
        description: str = "",
        armor_type: int = 0,
        modifiers: Optional[Dict[str, Dict]] = None,
        **kwargs,
    ):
        weapon_mod = Modifier(name=name + "_mod")
        if modifiers:
            weapon_mod.add_mod(m_type="adds", mods=modifiers.get("adds", {}))
            weapon_mod.add_mod(m_type="mults", mods=modifiers.get("mults", {}))
        else:
            weapon_mod.add_mod(m_type="adds", mods={"attack": 1, "energy": 1})

        super().__init__(
            name=name,
            description=description,
            item_type=4,
            armor_type=armor_type,
            modifier=weapon_mod,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
        )

        self.weapon_type = self._validate_weapon_type(weapon_type)

    @staticmethod
    def _validate_weapon_type(weapon_type: int):
        return weapon_type if abs(weapon_type) < len(uTypes.WEAPON_TYPES) else -1

    def get_weapon_type(self) -> str:
        return uTypes.get_weapon_type(self.weapon_type)

    def get_item_description(self) -> str:
        return uTypes.get_item_description(self.item_type, self.armor_type, self.weapon_type)

    def copy(self) -> Self:
        """Copies the current object"""
        return WeaponEquipment(
            name=self.name,
            weapon_type=self.weapon_type,
            description=self.description,
            armor_type=self.armor_type,
            modifiers=self.mod.get_mods(),
            _id=self._id,
        )


class BodyEquipment(Equipment):
    """
    Equipment Subclass specifically for armor items that are not weapons.
    """

    DB_PREFIX = "ARMOR"

    def __init__(
        self,
        name: str,
        modifiers: Optional[Dict[str, Dict]] = None,
        description: str = "",
        armor_type: int = 0,
        item_type: int = 0,
        **kwargs,
    ):
        """
        Modifiers should be a dictionary that has the possible properties {'adds':{}, 'mults':{}} that will be verified on Modifier creation
        """
        body_mod = Modifier(name=name + "_mod")
        if modifiers:
            body_mod.add_mod(m_type="adds", mods=modifiers.get("adds", {}))
            body_mod.add_mod(m_type="mults", mods=modifiers.get("mults", {}))
        else:
            body_mod.add_mod(m_type="adds", mods={"health": 1, "defense": 1})

        super().__init__(
            name=name,
            description=description,
            item_type=item_type,
            armor_type=armor_type,
            modifier=body_mod,
            _id=kwargs.get("_id"),
            prefix=self.DB_PREFIX,
        )

    def copy(self) -> Self:
        """Copies the current object"""
        return BodyEquipment(
            name=self.name,
            modifiers=self.mod.get_mods(),
            description=self.description,
            armor_type=self.armor_type,
            item_type=self.item_type,
            _id=self._id,
        )
