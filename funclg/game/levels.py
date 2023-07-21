"""
Description: Defines the level creation process 
Developer: Jevin Evans
Date: 2.20.2023
"""

# Needs to be able to create levels based on provide information and possible keep some statistics about what occured at the level
    # Levels should be grid based structures 5x5 or 7x7 or odd number grid less than 10x10 to hold user, enemies, and boss and rewards
"""
Level Creation Process/Steps:
    User's character stats are provided for calculating power of enemies
    Generates the appropriate grid
    - for odd NxN grid, there should be N rewards and 2N enemies
"""

# Should include the monsters on the level, the rewards, and the experience that can be earned
    #  Need to create a way to randomly generate appropriate rewards for the current users stats
# Levels/stages can be enemy or random awards 
    # Create a util that will generate npcs based on the current characters stats so that it is challenging but allows them to win
    # Needs to be semi efficient, might consider specifying specific types of mobs

# TODO: Create a level manager

class game_levels():
    def __init__():
        raise NotImplementedError

    def generate_grid():
        raise NotImplementedError

    def select_rewards():
        raise NotImplementedError

    def select_monsters():
        raise NotImplementedError   