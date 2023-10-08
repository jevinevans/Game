"""
Description: This is to unit test Game Level
Developer: Jevin Evans
Data: 9/5/2023
"""

from unittest.mock import patch

import pytest

import funclg.game.level as game_level
from funclg.utils.game_enums import AltIcons, GameAction, GamePiece, RegIcons


def test_game_level_generation():
    test_level = game_level.GameLevel(6)

    assert test_level.boss_pos == (3, 3)
    assert test_level.player_pos == (0, 5)
    assert test_level.key_pos == (5, 0)

    assert test_level.level.count(test_level.icons.SPACE.value) == (6**2) - 3


def test_game_level_size_validation():
    # Valid
    test_level = game_level.GameLevel(6)
    assert test_level.level_size == 6
    assert len(test_level.level) == 6**2

    # Test Too Small
    test_level_small = game_level.GameLevel(1)
    assert test_level_small.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_small.level) == game_level.GameLevel.DEFAULT_SIZE**2

    # Test Too Large
    test_level_large = game_level.GameLevel(20)
    assert test_level_large.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_large.level) == game_level.GameLevel.DEFAULT_SIZE**2


def test_game_level_alt_icons():
    test_level = game_level.GameLevel(6)
    assert test_level.level[test_level.coord_to_int(test_level.boss_pos)] == RegIcons.BOSS.value

    game_level.GameLevel.ALT_ICONS = True
    test_alt_level = game_level.GameLevel(6)
    assert (
        test_alt_level.level[test_alt_level.coord_to_int(test_alt_level.boss_pos)]
        == AltIcons.BOSS.value
    )


def test_game_level_coord_to_int_index_error():
    test_level = game_level.GameLevel(6)

    with pytest.raises(IndexError):
        test_level.coord_to_int((6, 6))


def test_game_level_int_to_coord_index_error():
    test_level = game_level.GameLevel(6)

    with pytest.raises(IndexError):
        test_level.int_to_coord(100)

    assert test_level.int_to_coord(3) == (0, 3)


alt_level = ["+-----+", "|____K|", "|_____|", "|__B__|", "|_____|", "|P____|", "+-----+"]


@patch("builtins.print")
def test_game_level_alt_display(m_print):
    game_level.GameLevel.ALT_ICONS = True

    test_level = game_level.GameLevel(5)

    test_level.display_level()
    assert m_print.called_with(alt_level)


@patch("funclg.game.level.logger")
def test_game_level_update_level_game_error(m_log):
    # Bad Update Coordinate - Coordinate not on the board
    game_level.GameLevel.ALT_ICONS = False
    test_level = game_level.GameLevel(6)

    assert test_level.update_level(GamePiece.SPACE, (6, 0)) == GameAction.ERROR
    assert m_log.error.called_with("That location is not on the map silly...")

    # Succesful Update of Enemy = Ready | loc = (0,0)
    assert test_level.update_level(GamePiece.ENEMY, (0, 0)) == GameAction.READY
    assert test_level.level[0] == RegIcons.ENEMY.value

    # Succesful Update of Key = Ready | loc = (2,4)
    assert test_level.update_level(GamePiece.KEY, (2, 4)) == GameAction.READY
    assert test_level.key_pos == (2, 4)

    # Succesful Update of Boss = Ready | loc = (3,4)
    assert test_level.update_level(GamePiece.BOSS, (3, 4)) == GameAction.READY
    assert test_level.boss_pos == (3, 4)

    # Succesful Update of Player = Ready | loc = (1, 5)
    assert test_level.update_level(GamePiece.PLAYER, (1, 5)) == GameAction.READY
    assert test_level.player_pos == (1, 5)

    # Test Validation Method Flows
    # ----------------------------
    # Invalidation Test: Enemy Type, Not a Space, same piece = Ready
    assert test_level.update_level(GamePiece.ENEMY, (0, 0)) == GameAction.READY
    assert test_level.level.count(RegIcons.ENEMY.value) == 1

    # Invalidation Test: Key Type, Not a Space, same piece, Reserved location = Error
    assert test_level.update_level(GamePiece.KEY, test_level.player_pos) == GameAction.ERROR

    # Invalidation Test: Pass, Invalid Changeable Game Piece - Space = Error
    assert test_level.update_level(GamePiece.SPACE, (1, 1)) == GameAction.ERROR

    # Player moves to Enemy LOC = Combat
    assert test_level.update_level(GamePiece.PLAYER, (0, 0)) == GameAction.COMBAT

    # Player moves to Key LOC = Win
    assert test_level.update_level(GamePiece.PLAYER, test_level.key_pos) == GameAction.WIN

    assert len(test_level.enemy_pos) == 1
