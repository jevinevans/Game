"""
Description: This defines the game object context manager that will be used for FUNCLG
Developer: Jevin Evans
Date: 2.20.2023
"""

#####
# THIS NEEDS TO BE A SINGLETON DESIGN
#####

# Context manager for the game
# Needs to build/load the levels/level packs, NPCs associated with them, and rewards
# User needs to provide a character they want to use, if no user exists they will need to create one first (needs to be done before game start)
# Need to create a level up process for the modifiers
# Counter until a boss appears
# Needs to have dialog for what the user is doing current stats


# Need to create an NPC generation process
# Need to create a level/stage generation process and define the parts of it. Should take a calculation of the characters stats and create a challenge.
# Consider building different play modes: main will be short 5-10 levs with a few enemies and a boss at the final level


class Game:
    """
    Defines the game manager for FUNCLG play.
    """

    START_MESSAGE = ""

    def __init__(self):
        # User selects or it is passed in an available player to play with
        #  If no character, initiate the building of a character
        # User selects level difficulty
        # Select the number of levels (minimum 5, maximum 20)
        # Randomly build the levels
        # Could spawn a boss every 5-10 level
        # Levels will generate
        raise NotImplementedError

    def start(self):
        # After the creation of init, this will start the game process and the actions that will happen
        # Could make use of the menus for actions to be taken
        raise NotImplementedError

    def save(self):
        # Need to be able to save game process and status, including level set up and remaining efforts
        raise NotImplementedError

    def generate_difficulty(self):
        # I want to be able to make a decision if a block should be reward, enemy etc.
        # Should this automatically(randomly) completed before or done randomly as player progresses
        # How should the history of the space be preserved should it be tracked in another grid or should the slots be objects that track their status and use bools for status and visualization, and completion
        raise NotImplementedError
