"""
Description: The manages level creation, statisitcs, and creation of enemies/rewards.
Developer: Jevin Evans
Date: 10.8.2023
"""

# import questionary
# from loguru import logger


# TODO: 20231008 - Decide if this should be its own module, where it should be and what it should do.

"""
This should manage level settings:

- User prefered Level size range within permanent range
    low, high ( MIN < low < high < MAX)
- Difficulty settings
    - increases number of enemys or percentage difference
- Level Symbols selection
"""

# TODO: 20230905 -  Clean up
# Needs to be able to create levels based on provide information and possible keep some statistics about what occured at the level
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
