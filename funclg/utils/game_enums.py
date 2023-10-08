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
