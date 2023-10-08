from dataclasses import dataclass


@dataclass
class level_icons:
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
        top = f"{self.TL_CORNER}" + self.HORIZONTAL_EDGE * 5 + f"{self.TR_CORNER}"
        btm = f"{self.BL_CORNER}" + self.HORIZONTAL_EDGE * 5 + f"{self.BR_CORNER}"

        char_icons = "".join(
            [
                self.VERTICAL_EDGE,
                self.PLAYER,
                self.KEY,
                self.SPACE,
                self.ENEMY,
                self.BOSS,
                self.VERTICAL_EDGE,
            ]
        )
        return f"\n{top}\n{char_icons}\n{btm}"

    def __repr__(self) -> str:
        return self.__str__()
