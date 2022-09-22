"""
Programmer: Jevin Evans
Date: 6.11.2022
Description: The character that will be used. The character will have a role, abilities, and armor.
"""

from typing import Any, Dict, Optional

from loguru import logger

import funclg.utils.data_mgmt as db
from funclg.character.armor import Armor
from funclg.character.equipment import Equipment
from funclg.character.roles import Roles
from funclg.character.stats import Stats


class Character:
    """
    Base character unit of the game.

    :return: Returns a character object
    :rtype: Character
    """

    # TODO: Update initialization process so that the role decides the armor type for the character and then all armor and equips will validate for the role

    DB_PREFIX = "CHARS"
    BASE_STATS = {"attack": 5, "health": 5, "energy": 5, "defense": 5}

    def __init__(
        self,
        name: str,
        armor_instance: Optional[Armor] = None,
        role_instance: Optional[Roles] = None,
        stats: Optional[Stats] = None,
        **kwargs,
    ):
        """
        Creates a new character with an armor set and role
        """
        self.name = name
        self.level = kwargs.get("level", 1)
        self.stats = stats if stats else Stats(attributes=Character.BASE_STATS)
        self._set_up_role(role_instance)
        self._set_up_armor(armor_instance)
        self._update_stats()
        self._id = db.id_gen(self.DB_PREFIX, kwargs.get("_id"))

    def _set_up_role(self, roles_instance: Optional[Roles] = None) -> None:
        if roles_instance:
            self.role = roles_instance
            self.armor_type = roles_instance.armor_type
        else:
            self.armor_type = 0
            self.role = Roles("NPC", "A non-playable character", self.armor_type)

    def _set_up_armor(self, armor_instance: Optional[Armor] = None) -> None:
        if armor_instance and armor_instance.armor_type == self.armor_type:
            self.armor = armor_instance
        else:
            self.armor = Armor(self.armor_type)

    def _update_stats(self):
        self.stats.add_mod(self.role.to_mod())
        self.stats.add_mod(self.armor.to_mod())

    def __str__(self) -> str:
        string = f"{self.name} [lvl {self.level}]\n"
        string += "-" * (len(self.name) + 7 + len(str(self.level)))
        string += f"\n Class: {self.role.name}"
        string += f"\n Armor: {self.armor}"

        return string

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def id(self):  # pylint: disable=C0103
        return self._id

    @property
    def power(self):
        return self.stats.power

    def export(self) -> Dict[str, Any]:
        logger.debug(f"Exporting Character: {self.name}")
        exporter = self.__dict__.copy()
        for key, value in exporter.items():
            if isinstance(value, Armor):
                exporter[key] = value.export()
            if isinstance(value, Roles):
                exporter[key] = value.export()
            if isinstance(value, Stats):
                tmp_stat = Stats(**value.copy())
                tmp_stat.remove_mod("armor")
                tmp_stat.remove_mod(self.role.name)
                exporter[key] = tmp_stat.export()
        return exporter

    def details(self, indent: int = 0) -> str:
        desc = f"{self.name} [lvl {self.level}]\n"
        desc += "-" * (len(self.name) + 7 + len(str(self.level)))
        desc += "\n" + self.stats.details(indent)
        desc += "\n" + self.role.details(indent + 2)
        desc += self.armor.details(indent + 2)
        desc += "\n"
        return desc

    def equip(self, item: Equipment) -> None:
        """Calls the armor equip function"""
        self.armor.equip(item)
        self._update_stats()

    def dequip(self, item_type: str) -> None | Equipment:
        """Calls the armor dequip function"""
        item = self.armor.dequip(item_type)
        self._update_stats()
        return item

    # def use_ability(self):
    # def level_up(self):


class Player(Character):
    """
    The playable character that an end-user will use to play the game:

    :param Character: _description_
    :type Character: _type_
    """

    def __init__(
        self,
        name: str,
        armor_instance: Optional[Armor] = None,
        role_instance: Optional[Roles] = None,
        **kwargs,
    ):
        super().__init__(
            name=name, armor_instance=armor_instance, role_instance=role_instance, **kwargs
        )

        self.inventory = kwargs.get("inventory", [])

    def show_inventory(self):
        print("\nInventory:")
        print("\n  - ".join(self.inventory))

    def dequip(self, item_type: str) -> None:
        """Calls the armor dequip function"""
        if item := super().dequip(item_type) is not None:
            self.inventory.append(item)


class NonPlayableCharacter(Character):
    """
    A non playable character that is used for player combat
    """

    def __init__(
        self,
        name: str,
        armor_instance: Optional[Armor] = None,
        role_instance: Optional[Roles] = None,
        **kwargs,
    ):
        super().__init__(
            name=name, armor_instance=armor_instance, role_instance=role_instance, **kwargs
        )
        self.npc = True
