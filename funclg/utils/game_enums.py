from enum import Enum, auto


class GameAction(Enum):
    READY = auto()
    COMBAT = auto()
    WIN = auto()
    DIE = auto()
    ERROR = auto()


class GamePiece(Enum):
    SPACE = auto()
    PLAYER = auto()
    ENEMY = auto()
    KEY = auto()
    BOSS = auto()


# TODO: 20230827 - Future: Consider allowing user to define their own boundary characters or just multiple custom packs or options the end user can choose from. Change to a structured format that is loaded in a specific order and then multiples can be chosen from.
class RegIcons(Enum):
    SPACE = "\u25A0"

    # BOUNDARY ICONS
    HORIZONTAL_EDGE = "\u2550"
    VERTICAL_EDGE = "\u2551"
    TL_CORNER = "\u2554"
    TR_CORNER = "\u2557"
    BL_CORNER = "\u255A"
    BR_CORNER = "\u255D"

    # PLAYER/TOKEN ICONS
    PLAYER = "\u25CA"
    KEY = "\u2625"
    BOSS = "\u265A"
    ENEMY = "\u265F"


class AltIcons(Enum):
    SPACE = "_"

    # BOUNDARY ICONS
    HORIZONTAL_EDGE = "-"
    VERTICAL_EDGE = "|"
    TL_CORNER = "+"
    TR_CORNER = "+"
    BL_CORNER = "+"
    BR_CORNER = "+"

    # PLAYER/TOKEN ICONS
    PLAYER = "P"
    KEY = "K"
    BOSS = "B"
    ENEMY = "E"
