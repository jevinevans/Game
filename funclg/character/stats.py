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
    STAT_DEFAULT = 1

    # TODO: 2023.10.15 - define a base stat max
    def __init__(
        self,
        attributes: Optional[Dict[str, Any]] = None,
        modifiers: Optional[List[Modifier]] = None,
    ):
        for attr in Stats.BASE_ATTRIBUTES:
            setattr(self, attr, Stats.STAT_DEFAULT)

        self._validate_attributes(attributes)

        # Modifiers for changing stats
        # TODO: 2023.10.17 - Create copies of each mod
        self.mods = {}
        if modifiers:
            for mod in modifiers:
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
                    if value >= Stats.STAT_DEFAULT:
                        setattr(self, attribute, value)
                    else:
                        logger.error(f"{value} is below default")
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

    def add_mod(self, mod: Modifier):
        """
        This funciton modifies the base stats of a stat positively or negatively, and can be updated
        """
        self.mods[mod.name] = mod.get_mods()

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

    def get_stats(self, base_only=False) -> Dict[str, Any]:
        """Returns current stats with mods"""
        stats = {}
        for attr in Stats.BASE_ATTRIBUTES:
            if base_only:
                stats[attr] = getattr(self, attr)
            else:
                stats[attr] = self.get_stat(attr)
        return stats

    def export(self) -> Dict[str, Any]:
        logger.debug("Exporting Stats")
        return {"attributes": self.get_stats(base_only=True), "modifiers": self.mods}

    # TODO: 2023.10.10 - Test if the removal of a mod deletes the original object
    def clear_mods(self):
        mod_keys = list(self.mods.keys())
        for mod in mod_keys:
            self.remove_mod(mod)
        logger.debug("All mods cleared from stat")

    def level_up(self, levels: int = 1):
        for attribute in Stats.BASE_ATTRIBUTES:
            setattr(self, attribute, getattr(self, attribute) + levels)
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

    # TODO: 2023.10.18 - Needs to return a new Stats object and should be loaded as a Stats item in equipment similar to other Characer module copies.
    # Requires a change in *[Equipment] modules.
    def copy(self):
        mods_list = []
        if self.mods:
            for name, mods in self.mods.items():
                mods_list.append(
                    Modifier(name=name, adds=mods.get("adds", {}), mults=mods.get("mults", {}))
                )
        return {"attributes": self.get_stats(base_only=True), "modifiers": mods_list}

    def __eq__(self, __value: object) -> bool:
        return self.power == __value.power

    def __lt__(self, other) -> bool:
        return self.power < other.power

    def __le__(self, other) -> bool:
        return self.power <= other.power

    def __gt__(self, other) -> bool:
        return self.power > other.power

    def __ge__(self, other) -> bool:
        return self.power >= other.power

    def __ne__(self, other) -> bool:
        return self.power != other.power
