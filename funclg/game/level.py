"""
Description: Defines the level creation process 
Developer: Jevin Evans
Date: 2.20.2023
"""

# TODO: 20230905 -  Clean up
# Needs to be able to create levels based on provide information and possible keep some statistics about what occured at the level
# Levels should be level based structures 5x5 or 7x7 or odd number level less than 10x10 to hold user, enemies, and boss and rewards
"""
Level Creation Process/Steps:
    User's character stats are provided for calculating power of enemies
    Generates the appropriate level
    - for odd NxN level, there should be N rewards and 2N enemies
"""

# Should include the monsters on the level, the rewards, and the experience that can be earned
#  Need to create a way to randomly generate appropriate rewards for the current users stats
# Levels/stages can be enemy or random awards
# Create a util that will generate npcs based on the current characters stats so that it is challenging but allows them to win
# Needs to be semi efficient, might consider specifying specific types of mobs


from loguru import logger

from funclg.utils.game_enums import AltIcons, GameAction, GamePiece, RegIcons


class GameLevel:
    ALT_ICONS = False
    MAX_SIZE = 16
    MIN_SIZE = 5
    DEFAULT_SIZE = 7

    def __init__(self, level_size: int):
        self.ICONS = AltIcons if GameLevel.ALT_ICONS else RegIcons

        self._validate_level_size(level_size)

        # Set Position Defaults
        half_way = int(
            round(self.level_size / 2, 1)
        )  # TODO: 202308 - Decide whether to do a proper floor calculation or not

        self.player_pos = (0, self.level_size - 1)
        self.boss_pos = (half_way, half_way)
        self.key_pos = (self.level_size - 1, 0)
        # TODO: 20230904 - Should enemy positions be tracked too...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # TODO: 20230904 - Create tests

        # TODO: 202308 - Consider if this should be private and only callable
        self._level = self.generate_level()
        self.completed = False

    @property
    def level(self):
        return tuple(self._level)

    def _validate_level_size(self, level_size: int):
        level_size = int(level_size)
        match level_size:
            case _ if level_size < self.MIN_SIZE:
                logger.warning("That's a really small level, let's get you a better map instead")
                self.level_size = self.DEFAULT_SIZE
            case _ if level_size > self.MAX_SIZE:
                logger.warning("This level is waaay to big, let's get you a better map instead")
                self.level_size = self.DEFAULT_SIZE
            case _:
                self.level_size = level_size

    def coord_to_int(self, coordinate: set[int, int]):
        if (
            coordinate[0] >= 0
            and coordinate[0] < self.level_size
            and coordinate[1] >= 0
            and coordinate[1] < self.level_size
        ):
            return self.level_size * coordinate[1] + coordinate[0]
        raise IndexError("Coordinate is out range")

    def int_to_coord(self, location: int):
        if location in range(self.level_size**2):
            x_cord = location // self.level_size
            y_cord = location % self.level_size
            return (x_cord, y_cord)
        raise IndexError("Location is out of range")

    def generate_level(self):
        """
        _summary_

        :return: The constructer level level with player, boss, and key icon.
        :rtype: List[str]
        """
        # Build level
        temp_level = [self.ICONS.SPACE.value for _ in range((self.level_size) ** 2)]
        temp_level[self.coord_to_int(self.player_pos)] = self.ICONS.PLAYER.value
        temp_level[self.coord_to_int(self.key_pos)] = self.ICONS.KEY.value
        temp_level[self.coord_to_int(self.boss_pos)] = self.ICONS.BOSS.value

        return temp_level

    def _reserved_coord_check(self, coords: tuple[int, int]):
        """
        Checks if the coord is currently a reserved value

        :param coords: _description_
        :type coords: tuple[int, int]
        """
        if coords in [self.player_pos, self.boss_pos, self.key_pos]:
            return True
        return False

    def _same_piece_check(self, game_piece: GamePiece, level_loc: int):
        """
        Checks if the game piece is already at the location

        :param game_piece: _description_
        :type game_piece: GamePiece
        :param level_loc: _description_
        :type level_loc: int
        :return: _description_
        :rtype: _type_
        """
        match game_piece:
            case GamePiece.ENEMY:
                return self._level[level_loc] == self.ICONS.ENEMY.value
            case GamePiece.KEY:
                return self._level[level_loc] == self.ICONS.KEY.value
            case GamePiece.BOSS:
                return self._level[level_loc] == self.ICONS.BOSS.value
            case GamePiece.PLAYER:
                return self._level[level_loc] == self.ICONS.PLAYER.value
            case _:
                return False

    def _validate_level_update_pos(
        self, game_piece: GamePiece, coords: tuple[int, int], level_loc: int
    ):
        if not self._level[level_loc] == self.ICONS.SPACE:
            if not self._same_piece_check(game_piece=game_piece, level_loc=level_loc):
                if self._reserved_coord_check(coords=coords):
                    return False
        return True

    def update_level(self, game_piece: GamePiece, coords: tuple[int, int]):
        # This function will take an object (player/enemy or reward/equipment) and add/remove it to the playable level
        # This function should also be used to update the placement of the main character
        try:
            level_loc = self.coord_to_int(coords)
        except IndexError:
            logger.error("That location is not on the map silly....")
            return GameAction.ERROR

        if self._validate_level_update_pos(
            game_piece=game_piece, coords=coords, level_loc=level_loc
        ):
            match game_piece:
                case GamePiece.ENEMY:
                    self._level[level_loc] = self.ICONS.ENEMY.value
                case GamePiece.KEY:
                    self._level[self.coord_to_int(self.key_pos)] = self.ICONS.SPACE.value
                    self.key_pos = coords
                    self._level[level_loc] = self.ICONS.KEY.value
                case GamePiece.BOSS:
                    self._level[self.coord_to_int(self.boss_pos)] = self.ICONS.SPACE.value
                    self.boss_pos = coords
                    self._level[level_loc] = self.ICONS.BOSS.value
                case GamePiece.PLAYER:
                    self._level[self.coord_to_int(self.player_pos)] = self.ICONS.SPACE.value
                    self.player_pos = coords
                    self._level[level_loc] = self.ICONS.PLAYER.value

            return GameAction.READY

        if game_piece is GamePiece.PLAYER:
            if self._level[level_loc] is self.ICONS.ENEMY | self.ICONS.BOSS:
                return GameAction.COMBAT

            if self._level[level_loc] is self.ICONS.KEY:
                self.completed = True
                return GameAction.WIN

        return GameAction.ERROR

    def display_level(self):
        """
        This function prints the level level and a boarder around it to the screen.
        """
        # Add Design Boundary
        header = (
            self.ICONS.TL_CORNER.value
            + self.ICONS.HORIZONTAL_EDGE.value * (self.level_size * 2 - 1)
            + self.ICONS.TR_CORNER.value
        )
        footer = (
            self.ICONS.BL_CORNER.value
            + self.ICONS.HORIZONTAL_EDGE.value * (self.level_size * 2 - 1)
            + self.ICONS.BR_CORNER.value
        )

        # Print level with Boundary
        print(header)
        for index in range(self.level_size):
            print(
                " ".join(
                    self._level[index * self.level_size : index * self.level_size + self.level_size]
                ).center(self.level_size * 2 + 1, self.ICONS.VERTICAL_EDGE.value)
            )
        print(footer)

    # def export_level():
    # def load_level():
