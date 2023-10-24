"""
The Play Game menu for the game module
"""

import questionary

import funclg.managers.character_manager as char_man

from . import game

# Game Se


def game_settings():
    """
    level_size - sets the grid size of the levels
    number_of_levels - sets the number of levels for the game
    difficulty - sets the number of rewards and enemies that will be on the board

    """

    print("Game Configuration")
    # Game settings form: level size, number of levels, and difficulty
    # game_setting = questionary.form(
    #     level_size = questionary.
    #     number_of_levels =
    #     difficulty =

    # ).ask()


def select_character():
    raise NotImplementedError


def game_setup():
    raise NotImplementedError

    # Set up Game Settings
    # Build Game
    # Build levels based on settings
    # Select Character


def game_start():
    raise NotImplementedError
    # Starts the game
