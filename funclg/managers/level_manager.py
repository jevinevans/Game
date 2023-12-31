"""
Description: The manages level creation, statisitcs, and creation of enemies/rewards.
Developer: Jevin Evans
Date: 10.8.2023
"""

# from loguru import logger

LEVEL_DATA = {"filename": "game_levels.json", "data": {}, "objects": {}}


def load_data():
    raise NotImplementedError


def update_data():
    raise NotImplementedError


def export_data():
    raise NotImplementedError


def create_level():
    raise NotImplementedError


def show_levels():
    raise NotImplementedError


def delete_level():
    raise NotImplementedError


MENU = {
    "name": "Levels Manager",
    "description": "Create and manage level settings.",
    "menu_items": [
        {"title": "Create New Level", "value": create_level},
        {"title": "Show Level(s)", "value": show_levels},
        {"title": "Delete Level", "value": delete_level},
    ],
}
# Allow user to build a level board

# This should manage level settings:

# - User prefered Level size range within permanent range
#     low, high ( MIN < low < high < MAX)
# - Difficulty settings
#     - increases number of enemys or percentage difference
# - Level Symbols selection


# Needs to be able to create levels based on provide information and possible keep some statistics about what occured at the level

# Level Creation Process/Steps:
#     User's character stats are provided for calculating power of enemies
#     Generates the appropriate level
#     - for odd NxN level, there should be N rewards and 2N enemies


# Should include the monsters on the level, the rewards, and the experience that can be earned
#  Need to create a way to randomly generate appropriate rewards for the current users stats
# Levels/stages can be enemy or random awards
# Create a util that will generate npcs based on the current characters stats so that it is challenging but allows them to win
# Needs to be semi efficient, might consider specifying specific types of mobs
