"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The Armor class is made to store equipment itmes for a character.
"""

from typing import Dict, List, Optional, Union

from loguru import logger

from ..utils.types import ARMOR_TYPES, get_armor_type
from .equipment import Equipment, WeaponEquipment

logger.add("./logs/character/armor.log", rotation="1 MB", retention=5)


# TODO: Create Armor Stat
# - Create armor stat update function that will recal the whole thing instead of just removing one)
# - Will be a sum of the equipment stats, may or may not display the name and stats


class Armor:
    """
    Creates an armor object for a character
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        armor_type: int = 0,
        head: Equipment = None,
        chest: Equipment = None,
        back: Equipment = None,
        pants: Equipment = None,
        weapon: WeaponEquipment = None,
    ) -> None:
        self.armor_type = armor_type if abs(armor_type) < len(ARMOR_TYPES) else 0
        # self.stats = # Armor Stat Object
        self.head = self.validate_equipment(head)
        self.chest = self.validate_equipment(chest)
        self.back = self.validate_equipment(back)
        self.pants = self.validate_equipment(pants)
        self.weapon = self.validate_equipment(weapon)

    def validate_equipment(self, item: Optional[Equipment]) -> Union[Equipment, None]:
        """Validates that the equipment matches the armor class and returns a copy of the item to the slot"""
        if isinstance(item, Equipment):
            if item.armor_type == self.armor_type:
                logger.success(f"Equipped: {item}")
                return item.copy()
        logger.warning(f"{item} is not compatable with this armor.")
        return None

    def __str__(self) -> str:
        # Eventually add the stats to the class as well
        temp = f"{get_armor_type(self.armor_type)} Armor: <"
        temp += "H:1, " if self.head else "H:0, "
        temp += "C:1, " if self.chest else "C:0, "
        temp += "B:1, " if self.back else "B:0, "
        temp += "P:1, " if self.pants else "P:0, "
        temp += "W:1>" if self.weapon else "W:0>"
        return temp

    def _equip_head(self, item: Equipment):
        self.head = item

    def _equip_chest(self, item: Equipment):
        self.chest = item

    def _equip_back(self, item: Equipment):
        self.back = item

    def _equip_pants(self, item: Equipment):
        self.pants = item

    def _equip_weapon(self, item: WeaponEquipment):
        self.weapon = item

    def equip(self, item: Equipment) -> Union[Equipment, None]:
        if new_item := self.validate_equipment(item):
            if equip_func := getattr(self, "_equip_" + new_item.get_item_type().lower()):
                equip_func(new_item)
                logger.info(f"Equipped {new_item.name} to {new_item.get_item_type()}")
        # Add stats update process here

    def _dequip_head(self):
        temp = self.head
        self.head = None
        return temp

    def _dequip_chest(self):
        temp = self.chest
        self.chest = None
        return temp

    def _dequip_back(self):
        temp = self.back
        self.back = None
        return temp

    def _dequip_pants(self):
        temp = self.pants
        self.pants = None
        return temp

    def _dequip_weapon(self):
        temp = self.weapon
        self.weapon = None
        return temp

    def dequip(self, item_type: str) -> None:
        """
        Removes the currently equiped item in the current position and wil return an item if there is something already equiped.
        """

        if getattr(self, item_type.lower(), False):
            dequip_func = getattr(self, "_dequip_" + item_type.lower())
            del_item = dequip_func()
            logger.info(f"Equipped {del_item.name} to {del_item.get_item_type()}")
            del del_item
            # Add stats update process here
        logger.warning(f"{item_type} slot is empty.")

    def details(self, indent: int = 0) -> str:
        title = f"{' '*indent}Armor ({get_armor_type(self.armor_type)})"
        desc = f"\n{' '*indent}{title} \n{' '*indent}{'-'*(len(title)+2)}"
        desc += f"\n{' '*indent}Head: {self.head.__str__()}"
        desc += f"\n{' '*indent}Chest: {self.chest.__str__()}"
        desc += f"\n{' '*indent}Back: {self.back.__str__()}"
        desc += f"\n{' '*indent}Pants: {self.pants.__str__()}"
        desc += f"\n{' '*indent}Weapon: {self.weapon.__str__()}"
        return desc

    def get_equipment(self) -> List[Union[Equipment, None]]:
        """Returns the equipped armor"""
        return [self.head, self.chest, self.back, self.pants, self.weapon]

    def export(self) -> Dict:
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Equipment):
                exporter[key] = value.export()
        return exporter

    # def get_stats(self):
