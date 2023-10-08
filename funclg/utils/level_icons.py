from dataclasses import dataclass


@dataclass
class level_icons:
    NAME: str  # Icon Set name
    SPACE: str

    # BOUNDARY ICONS
    HORIZONTAL_EDGE: str
    VERTICAL_EDGE: str
    TL_CORNER: str
    TR_CORNER: str
    BL_CORNER: str
    BR_CORNER: str

    # PLAYER/TOKEN ICONS
    PLAYER: str
    KEY: str
    BOSS: str
    ENEMY: str

    def __str__(self):
        board_icons = [
            self.SPACE,
            self.TL_CORNER,
            self.HORIZONTAL_EDGE,
            self.VERTICAL_EDGE,
            self.BR_CORNER,
        ]
        char_icons = [self.PLAYER, self.KEY, self.ENEMY, self.BOSS]
        return f"{self.NAME.capitalize()} = Board:{(board_icons)} | Char:{char_icons}"

    def __repr__(self) -> str:
        return self.__str__()
