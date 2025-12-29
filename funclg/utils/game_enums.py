"""
Description: Defines enum and common needed Game structures
Developer: Jevin Evans
Date: 10.8.2023
"""

from dataclasses import dataclass
from enum import Enum, auto


class GameAction(Enum):
    """
    Defines game status and states.
    """

    READY = auto()
    COMBAT = auto()
    WIN = auto()
    DIE = auto()
    ERROR = auto()
    PAUSED = auto()


class GamePiece(Enum):
    """
    Used to identify Game pieces in the game system.
    """

    SPACE = auto()
    PLAYER = auto()
    ENEMY = auto()
    KEY = auto()
    BOSS = auto()


@dataclass
class LevelIcons:  # pylint: disable=too-many-instance-attributes
    """
    Defines level icon structure used for design and display.
    """

    space: str

    # Boundary Icons
    horizontal_edge: str
    vertical_edge: str
    tl_corner: str
    tr_corner: str
    bl_corner: str
    br_corner: str

    # PLAYER/TOKEN ICONS
    player: str
    key: str
    boss: str
    enemy: str

    def __str__(self):
        top = f"{self.tl_corner}" + self.horizontal_edge * 5 + f"{self.tr_corner}"
        btm = f"{self.bl_corner}" + self.horizontal_edge * 5 + f"{self.br_corner}"

        char_icons = "".join(
            [
                self.vertical_edge,
                self.player,
                self.key,
                self.space,
                self.enemy,
                self.boss,
                self.vertical_edge,
            ]
        )
        return f"\n{top}\n{char_icons}\n{btm}"


class GameError(Exception):
    pass
