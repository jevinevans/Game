"""
Description: This is to unit test Game Level
Developer: Jevin Evans
Data: 9/5/2023
"""

from unittest.mock import patch

import pytest

import funclg.game.level as game_level


def test_game_level_generation():
    test_level = game_level.GameLevel(6)

    assert test_level.boss_pos == (3, 3)
    assert test_level.player_pos == (0, 5)
    assert test_level.key_pos == (5, 0)

    assert test_level.level.count(test_level.ICONS) == (6**2) - 3


@patch.object("funclg.game.level.GameLevel", "generate_level")
def test_game_level_size_validation(m_generate_lvl):
    # Valid
    test_level = game_level.GameLevel(6)
    assert test_level.level_size == 6
    assert len(test_level.level) == 6**2

    # Test Too Small
    test_level_small = game_level.GameLevel(1)
    assert test_level_small.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_small) == game_level.GameLevel.DEFAULT_SIZE**2

    # Test Too Large
    test_level_large = game_level.GameLevel(20)
    assert test_level_large.level_size == game_level.GameLevel.DEFAULT_SIZE
    assert len(test_level_large) == game_level.GameLevel.DEFAULT_SIZE**2
