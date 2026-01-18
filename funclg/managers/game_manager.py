"""
Description: Manages game setttings
Developer: Jevin Evans
Date: 10.8.2023
"""

from typing import Any

from loguru import logger

from funclg.utils.game_enums import LevelIcons
from funclg.managers.manager import BaseManager, SingletonMeta


class GameManager(BaseManager, metaclass=SingletonMeta):
    """
    A manager class for game settings.
    """

    def __init__(self):
        """Initialize the GameManager."""
        super().__init__(name="Game Settings", filename="game_settings.json")
        self.menu["menu_items"] = [
            {"title": "Select Level Icons", "value": self.select_level_icons},
        ]
        logger.debug("GameManager initialized.")
        self.load_data()
        logger.debug("GameManager data loaded.")

    def update_data(self):
        # Will load many different types of data
        self._load_level_icons(self.data["level_icons"])

    def export_data(self):
        raise NotImplementedError

    def _load_level_icons(self, icon_data: dict[str, Any]):
        icons_sets = {}

        for name, icon_set in icon_data.items():
            icons_sets[name] = LevelIcons(**icon_set)

        self.objects["level_icons"] = icons_sets

    def select_level_icons(self):
        if icons := self.objects["level_icons"]:
            print(
                "Below are the game icon styles in a mini grid surrounding the icons for the player, key, space, enemy, and boss (respectively):"
            )
            for name, icon in icons.items():
                print(name, icon, "\n")

            choice = self.get_selection(
                "Which level icon set would you like to use for your levels?", list(icons)
            )
            return icons[choice]
        logger.error("There are no level icons loaded.")
        raise SystemError("No level icons loaded.")
