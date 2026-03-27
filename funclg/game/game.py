"""
Description: Defines the base game actions
Developer: Jevin Evans
Date: 1.17.2026
"""

import random

import questionary

from funclg.game.combat import update_combat
from funclg.game.models import GameState, LevelState
from funclg.game.movement import update_exploration
from funclg.game.ui import render
from funclg.managers.character_manager import CharacterManager
from funclg.managers.game_manager import GameManager
from funclg.utils.game_enums import GameAction
from funclg.utils.input_validation import number_range_validation


def game_set_up() -> LevelState:
    """
    Creates a new game level state.

    :return: Returns a new level state
    :rtype: LevelState
    """
    answers = questionary.form(
        number_of_levels=number_range_validation(
            min_val=1,
            max_val=10,
            default=3,
            prompt="How many levels would you like to play:",
        ),
        level_size=number_range_validation(
            min_val=LevelState.MIN_SIZE,
            max_val=LevelState.MAX_SIZE,
            default=LevelState.DEFAULT_SIZE,
            prompt="Please select level grid size:",
        ),
        game_icon_set=GameManager().select_level_icons(),
        # difficulty=selection_validation(
        #     "Please choose level difficulty:", ["Easy", "Normal", "Hard"]
        # ),
        player=CharacterManager().select_character(),
    ).ask()

    return GameState(
        player=answers["player"],
        level=LevelState(level_size=answers["level_size"], level_icons=answers["game_icon_set"]),
    )


def update_game(state: GameState, intent: str) -> GameState:
    if state.mode == GameAction.EXPLORE:
        return update_exploration(state, intent)
    elif state.mode == GameAction.COMBAT:
        return update_combat(state, intent)
    else:
        return state


def get_player_intent(state: GameState) -> str:
    if state.mode == GameAction.EXPLORE:
        return input("\nMove (WASD) or 'q' to quit: ").strip()
    elif state.mode == GameAction.COMBAT:
        return input("Action (1/2/3): ").strip()
    else:
        return ""


def run_game() -> None:
    random.seed()
    state = game_set_up()

    while True:
        render(state)
        if state.mode in [GameAction.GAME_OVER, GameAction.WIN, GameAction.LOSE]:
            break
        intent = get_player_intent(state)
        state = update_game(state, intent)

    # Final render to show game over message
    render(state)
