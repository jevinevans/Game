"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: This defines the stats object that will be used for all character classes
"""

from typing import Any, Dict, List, Optional, Union

from loguru import logger

from .modifiers import Modifier

# TODO: 2023.10.10 - Decide if stats and modifiers should round to whole numbers


class Stats:
    """
    This class defines the basic stat class structure for all objects
    """

    BASE_ATTRIBUTES = ["health", "attack", "defense", "energy"]

    def __init__(
        self,
        attributes: Optional[Dict[str, Any]] = None,
        modifiers: Optional[List[Modifier]] = None,
        default: Optional[int] = 1,
    ):
        for attr in Stats.BASE_ATTRIBUTES:
            setattr(self, attr, default)

        self._validate_attributes(attributes)

        # Modifiers for changing stats
        self.mods = {}
        if modifiers:
            for mod in modifiers:
                if self._validate_mod(mod):
                    self.mods[mod.name] = mod.get_mods()

        # Calculates objects
        self._power = 0
        self._cal_power()

    def _validate_attributes(self, attributes: Union[Dict[str, Any], None]):
        """
        Validates that provided attributes are valid. Used for loading existing attributes.

        :param attributes: Dictionary of attributes that are not the default value
        :type attributes: Union[Dict[str,Any], None]
        """
        if attributes:
            for attribute, value in attributes.items():
                if attribute in Stats.BASE_ATTRIBUTES:
                    setattr(self, attribute, value)
                else:
                    logger.error(f"{attribute} is not a valid stats attribute")

    def _cal_power(self):
        power = 0
        for attr in Stats.BASE_ATTRIBUTES:
            power += self.get_stat(attr)
        self._power = power

    @property
    def power(self):
        return self._power

    def __str__(self):
        stats = "\nStats\n" + "-" * 5
        for attr in Stats.BASE_ATTRIBUTES:
            stats += f"\n{attr.capitalize()}: {self.get_stat(attr)}"
        return stats

    def details(self, indent: int = 0):
        stats = f"\n{' '*indent}Stats [{self.power}]\n{' '*indent}"
        stats += "-" * (8 + len(str(self.power)))
        for attr in Stats.BASE_ATTRIBUTES:
            stats += f"\n{' '*(indent+2)}{attr.capitalize()} [{getattr(self, attr)}]: {self.get_stat(attr)}"
        return stats

    def _validate_mod(self, mod: Modifier):
        """
        Checks for duplicate mods being applied to stat
        """
        # TODO: 2023.10.10 - Consider if this will be valid during combat as an enemy may attack twice and the mod should be added but the effect may need to be combined.
        return not mod.name in self.mods

    def add_mod(self, mod: Modifier):
        """
        This funciton modifies the base stats of a stat positively or negatively
        """
        if self._validate_mod(mod):
            self.mods[mod.name] = mod.get_mods()
        else:
            logger.warning(f"Modifier: {mod.name} is not valid for this stat")
            return

    def remove_mod(self, name: str):
        if name in self.mods:
            del self.mods[name]
            return
        logger.error(f"This stat does not have the '{name}' modifier.")

    def get_stat(self, stat: str) -> Union[int, float, None]:
        base = getattr(self, stat, None)

        if not base:
            return base

        multiplier = 1

        for _, mod in self.mods.items():
            base += mod["adds"].get(stat, 0)
            multiplier += mod["mults"].get(stat, 0)

        return round(base * multiplier, 2)

    def get_stats(self) -> Dict[str, Any]:
        """Returns current stats of object with applied mods"""
        stats = {}
        for attr in Stats.BASE_ATTRIBUTES:
            stats[attr] = self.get_stat(attr)
        return stats

    def export(self) -> Dict[str, Any]:
        logger.debug("Exporting Stats")
        return self.__dict__.copy()

    # TODO: 2023.10.10 - Test if the removal of a mod deletes the original object
    def clear_mods(self):
        for mod in self.mods:
            self.remove_mod(mod)
        logger.debug("All mods cleared from stat")

    def level_up(self, upgrade: int = 1):
        for attribute in Stats.BASE_ATTRIBUTES:
            base_attr = getattr(self, attribute)
            base_attr += upgrade
        self._cal_power()

    def to_mod(self, name: str):
        """
        Converts the current stats values into a Modifier that can be added to another stat.

        :param name: The name of the object the stat belongs to.
        :type name: str
        :return: The generated modifier for the stat.
        :rtype: funclg.character.modifiers.Modifier
        """
        return Modifier(name=name, adds=self.get_stats())

    # TODO: 2023.10.10 - Define eq, lt, gt, lte, gte, neq, etc.
    # TODO: 2023.10.10 - Consider add and sub track
