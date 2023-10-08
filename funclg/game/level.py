"""
Description: Defines the level creation process 
Developer: Jevin Evans
Date: 2.20.2023
"""

from math import floor

from loguru import logger

from funclg.utils.game_enums import AltIcons, GameAction, GamePiece, RegIcons


class GameLevel:
    """
    Generates the level grid for the game. Shows player, boss, key, and enemies.
    """

    ALT_ICONS = False
    MAX_SIZE = 16
    MIN_SIZE = 5
    DEFAULT_SIZE = 7

    def __init__(self, level_size: int):
        self.icons = AltIcons if GameLevel.ALT_ICONS else RegIcons

        self._validate_level_size(level_size)

        # Set Position Defaults
        half_way = floor(self.level_size / 2)

        self.player_pos = (0, self.level_size - 1)
        self.boss_pos = (half_way, half_way)
        self.key_pos = (self.level_size - 1, 0)
        self.enemy_pos = []

        self._level = self.generate_level()
        self.completed = False

    @property
    def level(self):
        return tuple(self._level)

    def _validate_level_size(self, level_size: int):
        """
        Validates that the provided user level size is in game parameters, if not sets to default size.

        :param level_size: The size of the level that should be created.
        :type level_size: int
        """
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
        """
        Converts (X,Y) coordinates to list array integer location.

        :param coordinate: The (X,Y) coordinates in the level.
        :type coordinate: set[int, int]
        :raises IndexError: Raises error for invalid coordinates that are not in the grid
        :return: The integer equivalent location in the list.
        :rtype: int
        """
        if (
            coordinate[0] >= 0
            and coordinate[0] < self.level_size
            and coordinate[1] >= 0
            and coordinate[1] < self.level_size
        ):
            return self.level_size * coordinate[1] + coordinate[0]
        raise IndexError("Coordinate is out range")

    def int_to_coord(self, location: int):
        """
        Converts an integer value to the (X,Y) coordinates in the level grid/

        :param location: An integer location in the list
        :type location: int
        :raises IndexError: Raises an error if the provided integer is not in the array.
        :return: The (X,Y) coordinates that coorespond in the grid.
        :rtype: tuple[int, int]
        """
        if location in range(self.level_size**2):
            x_cord = location // self.level_size
            y_cord = location % self.level_size
            return (x_cord, y_cord)
        raise IndexError("Location is out of range")

    def generate_level(self):
        """
        Generates the basic structure of a level. Adds the player, a key, and the boss.

        :return: The constructer level level with player, boss, and key icon.
        :rtype: List[str]
        """
        # Build level
        temp_level = [self.icons.SPACE.value for _ in range((self.level_size) ** 2)]
        temp_level[self.coord_to_int(self.player_pos)] = self.icons.PLAYER.value
        temp_level[self.coord_to_int(self.key_pos)] = self.icons.KEY.value
        temp_level[self.coord_to_int(self.boss_pos)] = self.icons.BOSS.value

        return temp_level

    def _reserved_coord_check(self, coords: tuple[int, int]):
        """
        Checks if the coord is a tracked reserved value. Specifically the player, key, boss, or existing enemy locations.

        :param coords: The (X,Y) coordinates that are being updated.
        :type coords: tuple[int, int]
        """
        reserved_pos = [self.player_pos, self.boss_pos, self.key_pos]
        reserved_pos += self.enemy_pos if self.enemy_pos is not None else reserved_pos
        if coords in reserved_pos:
            return True
        return False

    def _same_piece_check(self, game_piece: GamePiece, level_loc: int):
        """
        Checks if the game piece is already at the location.

        :param game_piece: The GamePiece that is being updated.
        :type game_piece: GamePiece
        :param level_loc: The list integer equivilant of the (X,Y) coordinates.
        :type level_loc: int
        :return: True if the pieces match, otherwise False.
        :rtype: bool
        """
        match game_piece:
            case GamePiece.ENEMY:
                return self._level[level_loc] == self.icons.ENEMY.value
            case GamePiece.KEY:
                return self._level[level_loc] == self.icons.KEY.value
            case GamePiece.BOSS:
                return self._level[level_loc] == self.icons.BOSS.value
            case GamePiece.PLAYER:
                return self._level[level_loc] == self.icons.PLAYER.value
            case _:
                return False

    def _validate_level_update_pos(
        self, game_piece: GamePiece, coords: tuple[int, int], level_loc: int
    ):
        """
        Validates if a location can be updated with the GamePiece. Checks if the new piece is being placed in an empty location, if the same type of piece is being updated in a location, and if the selected spot is a reserved location for a tracked GamePiece.

        :param game_piece: The GamePiece that is being updated.
        :type game_piece: GamePiece
        :param coords: The (X,Y) coordinates that are being updated.
        :type coords: tuple[int, int]
        :param level_loc: The array integer equivilant of the (X,Y) coordinates.
        :type level_loc: int
        :return: The True/False validation status
        :rtype: bool
        """
        if not self._level[level_loc] == self.icons.SPACE:
            # If not a space location, and
            if not self._same_piece_check(game_piece=game_piece, level_loc=level_loc):
                # Not the same piece, and
                if self._reserved_coord_check(coords=coords):
                    # A reserved location, returns not valid to make update
                    return False
        return True

    def update_level(self, game_piece: GamePiece, coords: tuple[int, int]):
        """
        Given a game piece and coordinates, the level will update the level board and return the GameAction that should be taken.

        :param game_piece: The GamePiece that is being updated.
        :type game_piece: GamePiece
        :param coords: The (X,Y) coordinates that are being updated.
        :type coords: tuple[int, int]
        :return: Returns the GameAction status based on the conditions of the change including: ready, error, combat, or win.
        :rtype: GameAction
        """
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
                    self._level[level_loc] = self.icons.ENEMY.value
                    if coords not in self.enemy_pos:
                        self.enemy_pos.append(coords)
                case GamePiece.KEY:
                    self._level[self.coord_to_int(self.key_pos)] = self.icons.SPACE.value
                    self.key_pos = coords
                    self._level[level_loc] = self.icons.KEY.value
                case GamePiece.BOSS:
                    self._level[self.coord_to_int(self.boss_pos)] = self.icons.SPACE.value
                    self.boss_pos = coords
                    self._level[level_loc] = self.icons.BOSS.value
                case GamePiece.PLAYER:
                    self._level[self.coord_to_int(self.player_pos)] = self.icons.SPACE.value
                    self.player_pos = coords
                    self._level[level_loc] = self.icons.PLAYER.value
                case _:
                    return GameAction.ERROR

            return GameAction.READY

        if game_piece is GamePiece.PLAYER:
            if self._level[level_loc] in [self.icons.ENEMY.value, self.icons.BOSS.value]:
                return GameAction.COMBAT

            if self._level[level_loc] == self.icons.KEY.value:
                self.completed = True
                return GameAction.WIN

        return GameAction.ERROR

    def display_level(self):
        """
        This function prints the level level and a boarder around it to the screen.
        """

        # Add Design Boundary
        header = (
            self.icons.TL_CORNER.value
            + self.icons.HORIZONTAL_EDGE.value * (self.level_size * 2 - 1)
            + self.icons.TR_CORNER.value
        )
        footer = (
            self.icons.BL_CORNER.value
            + self.icons.HORIZONTAL_EDGE.value * (self.level_size * 2 - 1)
            + self.icons.BR_CORNER.value
        )

        # Print level with Boundary
        print(header)
        for index in range(self.level_size):
            print(
                " ".join(
                    self._level[index * self.level_size : index * self.level_size + self.level_size]
                ).center(self.level_size * 2 + 1, self.icons.VERTICAL_EDGE.value)
            )
        print(footer)

    # def export_level():
    # def load_level():
