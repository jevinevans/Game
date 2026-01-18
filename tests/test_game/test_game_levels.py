"""
Description: This is to unit test Game Level
Developer: Jevin Evans
Data: 9/5/2023
"""

from unittest.mock import call, patch

import pytest

import funclg.game.level as game_level
from funclg.managers.game_manager import GameManager
from funclg.utils.game_enums import GameAction, GamePiece

@pytest.fixture
def game_man():
    return GameManager()

@pytest.fixture
def game_icons(game_man):
    game_man.load_data()
    return {
        "reg": game_man.objects["level_icons"]["Set 1"],
        "alt": game_man.objects["level_icons"]["Set 2"],
    }


def test_game_level_generation(game_icons):
    test_level = game_level.GameLevel(6, game_icons["reg"])

    assert test_level.boss_pos == (3, 3)
    assert test_level.player_pos == (0, 5)
    assert test_level.key_pos == (5, 0)

    assert test_level.level.count(test_level.icons.space) == (6**2) - 3


def test_game_level_size_validation(game_icons):
    # Valid
    test_level = game_level.GameLevel(6, game_icons["reg"])
    assert test_level.level_size == 6
    assert len(test_level.level) == 6**2

    # Test Too Small
    test_level_small = game_level.GameLevel(1, game_icons["reg"])
    assert test_level_small.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_small.level) == game_level.GameLevel.DEFAULT_SIZE**2

    # Test Too Large
    test_level_large = game_level.GameLevel(20, game_icons["reg"])
    assert test_level_large.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_large.level) == game_level.GameLevel.DEFAULT_SIZE**2


def test_game_level_alt_icons(game_icons):
    test_level = game_level.GameLevel(6, game_icons["reg"])
    assert test_level.level[test_level.coord_to_int(test_level.boss_pos)] == game_icons["reg"].boss

    test_alt_level = game_level.GameLevel(6, game_icons["alt"])
    assert (
        test_alt_level.level[test_alt_level.coord_to_int(test_alt_level.boss_pos)]
        == game_icons["alt"].boss
    )


def test_game_level_coord_to_int_index_error(game_icons):
    test_level = game_level.GameLevel(6, game_icons["reg"])

    with pytest.raises(IndexError):
        test_level.coord_to_int((6, 6))


def test_game_level_int_to_coord_index_error(game_icons):
    test_level = game_level.GameLevel(6, game_icons["reg"])

    with pytest.raises(IndexError):
        test_level.int_to_coord(100)

    assert test_level.int_to_coord(3) == (0, 3)


@patch("builtins.print")
def test_game_level_alt_display(m_print, game_icons):
    alt_level = [
        call("\u2554" + "\u2550" * 9 + "\u2557"),
        call("\u2551" + "\u25a0 " * 4 + "\u2625" + "\u2551"),
        call("\u2551" + "\u25a0 " * 4 + "\u25a0" + "\u2551"),
        call("\u2551" + "\u25a0 " * 2 + "\u265a " + "\u25a0 " + "\u25a0" + "\u2551"),
        call("\u2551" + "\u25a0 " * 4 + "\u25a0" + "\u2551"),
        call("\u2551" + "\u25ca " + "\u25a0 " * 3 + "\u25a0" + "\u2551"),
        call("\u255a" + "\u2550" * 9 + "\u255d"),
    ]
    test_level = game_level.GameLevel(5, game_icons["alt"])

    test_level.display_level()
    m_print.assert_has_calls(alt_level)


@patch("funclg.game.level.logger")
def test_game_level_update_level_game_error(m_log, game_icons):
    # Bad Update Coordinate - Coordinate not on the board
    test_level = game_level.GameLevel(6, game_icons["reg"])

    assert test_level.update_level(GamePiece.SPACE, (6, 0)) == GameAction.ERROR
    m_log.error.assert_called_with("That location is not on the map silly...")

    # Succesful Update of Enemy = Ready | loc = (0,0)
    assert test_level.update_level(GamePiece.ENEMY, (0, 0)) == GameAction.READY
    assert test_level.level[0] == game_icons["reg"].enemy

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
    # Validation Test: Enemy Type, Not a Space, same piece = Ready
    assert test_level.update_level(GamePiece.ENEMY, (0, 0)) == GameAction.READY
    assert test_level.level.count(game_icons["reg"].enemy) == 1

    # Validation Test: Key Type, Not a Space, same piece, Reserved location = Error
    assert test_level.update_level(GamePiece.KEY, test_level.player_pos) == GameAction.ERROR

    # Validation Test: Pass, Invalid Changeable Game Piece - Space = Error
    assert test_level.update_level(GamePiece.SPACE, (1, 1)) == GameAction.ERROR

    # Validation Test: Pass, same piece boss = Ready
    assert test_level.update_level(GamePiece.BOSS, test_level.boss_pos) == GameAction.READY

    # Player moves to Enemy LOC = Combat
    assert test_level.update_level(GamePiece.PLAYER, (0, 0)) == GameAction.COMBAT

    # Player moves to Key LOC = Win
    assert test_level.update_level(GamePiece.PLAYER, test_level.key_pos) == GameAction.WIN

    assert len(test_level.enemy_pos) == 1
