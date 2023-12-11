"""
Description: This defines the game object context manager that will be used for FUNCLG
Developer: Jevin Evans
Date: 11.27.2023
"""

# Context manager for the game
# Needs to build/load the levels/level packs, NPCs associated with them, and rewards
# User needs to provide a character they want to use, if no user exists they will need to create one first (needs to be done before game start)
# Need to create a level up process for the modifiers
# Counter until a boss appears
# Needs to have dialog for what the user is doing current stats


import questionary

# Need to create an NPC generation process
# Need to create a level/stage generation process and define the parts of it. Should take a calculation of the characters stats and create a challenge.
# Consider building different play modes: main will be short 5-10 levs with a few enemies and a boss at the final level
from loguru import logger

import funclg.managers.character_manager as char_man
import funclg.managers.level_manager as lvl_man
import funclg.managers.level_pack_manager as lvl_pack_man
from funclg.utils import game_enums
from funclg.utils.input_validation import number_range_validation, selection_validation

from .level import GameLevel


class Game:
    """
    Defines the game manager for FUNCLG play.
    """

    START_MESSAGE = ""

    def __init__(self):
        # Select Character
        # If no character, warn that a character needs to be created before game start. Either start character creation or prompt warning and return to main menu.
        # If character, using char_man.select character choose the character that will be used for the game
        self.character = char_man.get_character()
        if not self.character:
            raise game_enums.GameError("No Character provided to initiate game")

        self.levels = self._level_set_up()
        # 1. Set up Game Settings
        # Use game pack or random levels
        # Number of levels (with in range)[default 10], size of levels ([5, 20]), level difficulty (easy(-1-4%), medium(4-7%), hard(7-10%))
        # Where difficuly is the stat percentage increase for NPCs (will constantly be tweaked for optimization)
        # Build Levels and Enemies
        # Take character stats, use difficulty to decide what stat ranges enemies will have
        # Use max difficulty range to build boss
        # Generate x enemies based on the level size (5x5 = 5 enemies) + 1 Boss
        # Create levels and place tokens in randomized locations
        # Generate a level reward (based on number of levels try to create an item of each type that is compatible with current player)

        raise NotImplementedError

    def process_input(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def run(self):
        # After the creation of init, this will start the game process and the actions that will happen
        # Could make use of the menus for actions to be taken
        raise NotImplementedError

    def save(self):
        # Need to be able to save game process and status, including level set up and remaining efforts
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def _level_set_up(self):
        if "Level Pack" == selection_validation(
            "Choose level type", ["Level Pack", "Random Level"]
        ):
            return lvl_pack_man.get_level_pack()
        else:
            answers = questionary.form(
                number_of_levels=number_range_validation(
                    min_val=1,
                    max_val=10,
                    default=3,
                    prompt="How many levels would you like to play:",
                ),
                level_size=number_range_validation(
                    min_val=GameLevel.MIN_SIZE,
                    max_val=GameLevel.MAX_SIZE,
                    default=GameLevel.DEFAULT_SIZE,
                    prompt="Please select level grid size:",
                ),
                difficulty=selection_validation(
                    "Please choose level difficulty:", ["Easy", "Normal", "Hard"]
                ),
            ).ask()
            return self._random_level_gen(**answers)

    def _random_level_gen(self, number_of_levels, level_size, difficulty):
        """
        level_size - sets the grid size of the levels
        number_of_levels - sets the number of levels for the game
        difficulty - sets the number of rewards and enemies that will be on the board

        """

        # Use game pack or random levels
        # Number of levels (with in range)[default 10], size of levels ([5, 20]), level difficulty (easy(-1-4%), medium(4-7%), hard(7-10%))
        # Where difficuly is the stat percentage increase for NPCs (will constantly be tweaked for optimization)

        # Game settings form: level size, number of levels, and difficulty
        raise NotImplementedError

    def _generate_difficulty(self):
        # I want to be able to make a decision if a block should be reward, enemy etc.
        # Should this automatically(randomly) completed before or done randomly as player progresses
        # How should the history of the space be preserved should it be tracked in another grid or should the slots be objects that track their status and use bools for status and visualization, and completion
        raise NotImplementedError
