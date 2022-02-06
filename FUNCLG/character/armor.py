"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The Armor class is made to store equipment itmes for a character.
"""

import json
from typing import Dict, List, Union

from loguru import logger

from ..utils.types import ARMOR_TYPES, ITEM_TYPES, get_armor_type
from .equipment import Equipment


class Armor:
    """
    Creates an armor object for a character
    """

    def __init__(
        self,
        armor_type: int = 0,
        head: Equipment = None,
        chest: Equipment = None,
        back: Equipment = None,
        pants: Equipment = None,
        weapon: Equipment = None,
    ) -> None:
        self.armor_type = armor_type if armor_type <= len(ARMOR_TYPES) and armor_type >= 0 else 0
        # self.stats = #TODO: Stat Object
        # Requires that the equipment is the same armor time
        # TODO: Create a validation method
        self.head = head if head is not None and head.armor_type == self.armor_type else None
        self.chest = chest if chest is not None and chest.armor_type == self.armor_type else None
        self.back = back if back is not None and back.armor_type == self.armor_type else None
        self.pants = pants if pants is not None and pants.armor_type == self.armor_type else None
        self.weapon = (
            weapon if weapon is not None and weapon.armor_type == self.armor_type else None
        )

    def validate_equipment(self, item: Equipment) -> Union[Equipment, None]:
        """Validates that the equipment matches the armor class and returns a copy of the item to the slot"""
        if item.armor_type == self.armor_type:
            logger.success(f"Equipped: {item}")
            return item
        logger.error(
            f"{item.name}({get_armor_type(item.armor_type)}) is not compatable with {get_armor_type(self.armor_type)}."
        )
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

    def equip(self, item: Equipment) -> Union[Equipment, None]:
        temp = None
        if item is not None and item.armor_type == self.armor_type:
            if item.get_item_type() == "Head":
                self.head, temp = item, self.head
            elif item.get_item_type() == "Chest":
                self.chest, temp = item, self.chest
            elif item.get_item_type() == "Back":
                self.back, temp = item, self.back
            elif item.get_item_type() == "Pants":
                self.pants, temp = item, self.pants
            elif item.get_item_type() == "Weapon":
                self.weapon, temp = item, self.weapon
            print(f"Equipped: {item}")
        else:
            print(f"\n{item}, is not compatable with this armor")
            return item
        # Returns previously equiped item, if there was one
        if isinstance(temp, Equipment):
            return temp

    # TODO: Consider return a status and the item, for faster check
    def dequip(self, item) -> Union[None, Equipment]:
        """
        Removes the currently equiped item in the current position and wil return an item if there is something already equiped.
        """
        temp = None
        item_type = ""
        if isinstance(item, int):
            # If the user sends the item type value
            if item < 0 or item >= len(ITEM_TYPES):
                print(f"Failed to Dequip: {item}")
                return
            item_type = ITEM_TYPES[item]
        elif isinstance(item, str):
            # If the user sends the name of the value
            item_type = item.capitalize()
            if item_type not in ITEM_TYPES:
                print(f"Failed to Dequip: {item}")
                return
        # elif isinstance(item, Equipment):
        #     # Future for if the user selects the item to unequip may send item may remove all together
        #     item_type = item.getItem_type()
        else:
            print(f"Failed to Dequip: {item}")
            return

        if item_type == "Head":
            temp, self.head = self.head, None
        elif item_type == "Chest":
            temp, self.chest = self.chest, None
        elif item_type == "Back":
            temp, self.back = self.back, None
        elif item_type == "Pants":
            temp, self.pants = self.pants, None
        elif item_type == "Weapon":
            temp, self.weapon = self.weapon, None

        print(f"Dequipped: {temp}")
        return temp

    # TODO: Add indention factor
    def details(self) -> str:
        title = f"Armor ({get_armor_type(self.armor_type)})"
        desc = f"\n {title} \n{''.join(['-' for x in range(len(title)+2)])}"
        desc += f"\nHead: {self.head.__str__()}"
        desc += f"\nChest: {self.chest.__str__()}"
        desc += f"\nBack: {self.back.__str__()}"
        desc += f"\nPants: {self.pants.__str__()}"
        desc += f"\nWeapon: {self.weapon.__str__()}\n"
        return desc

    def get_equipment(self) -> List[Union[Equipment, None]]:
        """Returns the equipped armor"""
        return [self.head, self.chest, self.back, self.pants, self.weapon]

    def print_to_file(self) -> None:
        with open(f"Armor_{id(self)}.json", "w", encoding="utf-8") as out_file:
            logger.info(f"Saving Armor: {out_file.name}")
            json.dump(self.export(), out_file)

    def export(self) -> Dict:
        exporter = self.__dict__
        for key, value in exporter.items():
            if isinstance(value, Equipment):
                exporter[key] = value.export()
        return exporter

    # TODO: Need to create an import function that is static to the method
    #  @staticmethod
    #  def import()
    # TODO: Need to create a define stats for armor
    # def get_stats(self):
    # Will be a sum of the equipment stats, may or may not display the name and stats
