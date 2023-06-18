"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The Armor class is made to store equipment itmes for a character.
"""

from typing import Dict, List, Union

from loguru import logger

from funclg.character.equipment import BodyEquipment, Equipment, WeaponEquipment
from funclg.character.stats import Stats
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, get_armor_type

# logger.add("./logs/character/armor.log", rotation="1 MB", retention=5)


class Armor:
    """
    Creates an armor object for a character
    """

    BASE_STATS = {"attack": 1, "health": 1, "energy": 1, "defense": 1}

    def __init__(  # pylint: disable=too-many-arguments
        self,
        armor_type: int = 0,
        head: BodyEquipment = None,
        chest: BodyEquipment = None,
        back: BodyEquipment = None,
        pants: BodyEquipment = None,
        weapon: WeaponEquipment = None,
    ):
        self.armor_type = armor_type if abs(armor_type) < len(ARMOR_TYPES) else 0
        self.stats = self._stats_setup(armor_type)
        # Base armor stat will have base attributes set to armor_type * 10 [10, 20, 30]

        # TODO: 20230617 - Change to setter/getters to protect equipment from being directly modified

        self.head = self._validate_equipment(head, 0)
        self.chest = self._validate_equipment(chest, 1)
        self.back = self._validate_equipment(back, 2)
        self.pants = self._validate_equipment(pants, 3)
        self.weapon = self._validate_equipment(weapon, 4)

    def _stats_setup(self, armor_type: int = 0):
        stat_default = Armor.BASE_STATS.copy()
        for attr in stat_default:
            stat_default[attr] *= (armor_type + 1) * 10
        return Stats(attributes=stat_default)

    def _update_armor_mods(self, item):
        """Validates that the equipment matches the armor class and returns a copy of the item to the slot"""
        self.stats.add_mod(item.to_mod())
        return item.copy()

    def _validate_equipment(
        self, item: Union[BodyEquipment, None], item_type: int
    ) -> Union[BodyEquipment, None]:
        if isinstance(item, (BodyEquipment, WeaponEquipment)):
            if item.armor_type == self.armor_type:
                if item.item_type == item_type:
                    return self._update_armor_mods(item)
                logger.warning(f"{item} can not be assigned to this slot.")
                return None
            logger.warning(f"{item} incompatable with this armor.")
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

    def _equip_head(self, item: BodyEquipment):
        if new_item := self._validate_equipment(item, 0):
            self.head = new_item
            return True
        return False

    def _equip_chest(self, item: BodyEquipment):
        if new_item := self._validate_equipment(item, 1):
            self.chest = new_item
            return True
        return False

    def _equip_back(self, item: BodyEquipment):
        if new_item := self._validate_equipment(item, 2):
            self.back = new_item
            return True
        return False

    def _equip_pants(self, item: BodyEquipment):
        if new_item := self._validate_equipment(item, 3):
            self.pants = new_item
            return True
        return False

    def _equip_weapon(self, item: WeaponEquipment):
        if new_item := self._validate_equipment(item, 4):
            self.weapon = new_item
            return True
        return False

    def equip(self, item: Equipment):
        if item:
            equip_func = getattr(self, "_equip_" + item.get_item_type().lower(), None)
            if equip_func:
                if equip_func(item):
                    self.stats.add_mod(item.to_mod())
                    logger.info(f"Equipped {item.name} to {item.get_item_type()}")
            else:
                logger.warning(f"{item} is not compatible with this armor")
                return
        logger.error("No item was provided to equip")

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
            ret_item = dequip_func()
            self.stats.remove_mod(ret_item.name)
            logger.info(f"Dequipped {ret_item.name} from {ret_item.get_item_type()}")
            return ret_item
        logger.warning("There is no item to remove.")
        return None
   
    def details(self, indent:int=0) -> str:
        title = f"{get_armor_type(self.armor_type)} Armor"
        desc = f"\n{' '*indent}{title}\n{' '*indent}{'-'*len(title)}"
        desc += self.stats.details(indent=indent + 2) + "\n"

        for _item_type in ITEM_TYPES:
            desc += self._details_check_none(indent, _item_type) + "\n"
        return desc
    
    def _details_check_none(self, indent:int, _item_type:str) -> str:
        desc = f"\n{' '*(indent+2)}{_item_type}: "

        if _item:=getattr(self, _item_type.lower(), False):
            return desc + _item.details(indent+4)
        return desc + "None"


    def _details_check_none(self, indent: int, _item_type: str) -> str:
        desc = f"\n{' '*(indent+2)}{_item_type}: "

        if getattr(self, _item_type.lower(), False):
            return desc + getattr(self, _item_type.lower()).details(indent + 4)
        return desc + "None"

    def get_equipment(self) -> List[Union[Equipment, None]]:
        """Returns the equipped armor"""
        return [self.head, self.chest, self.back, self.pants, self.weapon]

    def export(self) -> Dict:
        logger.debug("Exporting Equipment")
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Equipment):
                exporter[key] = value.export()
            if isinstance(value, Stats):
                continue
        exporter.pop("stats")
        return exporter

    def get_stats(self):
        """Armor Call method for the stats object"""
        return self.stats.get_stats()

    def level_up(self):
        if self.head:
            self.head.level_up()
        if self.chest:
            self.chest.level_up()
        if self.back:
            self.back.level_up()
        if self.pants:
            self.pants.level_up()
        if self.weapon:
            self.weapon.level_up()

    def to_mod(self):
        return self.stats.to_mod("armor")
