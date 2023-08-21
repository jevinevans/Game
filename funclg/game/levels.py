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

class GameLevel():

    # BOARD ICONS
    SPACE_SYMBOL = '\U000025A0'
    VISITED_SPACE_SYMBOL = '\U000025A6'
    HORIZONTAL_BOUND_SYMBOL= '\U00002550' 
    VERTICAL_BOUND_SYMBOL= '\U00002551' 
    CORNER_BOUND_SYMBOLS = ['\U00002554','\U00002557','\U0000255A','\U0000255D'] # Top Left, Top Right, Bottom Left, Bottom Right
    
    # ITEMS 
    PLAYER_ICON = '\U000025CA'
    KEY_ICON = '\U00002625'
    BOSS_ICON = '\U00002620'

    
    def __init__(self, game_settings:dict):
        self.playable_size = game_settings['level_size']
        self.grid = self.generate_grid(self.playable_size) # TODO: Consider if this should be private and only callable

    # TODO: Consider doing a precheck to make sure the running system can print the boundary characters, if not then use alternatives
    @staticmethod
    def generate_grid(grid_size:int=5):

        # Build Grid
        temp_grid = [GameLevel.SPACE_SYMBOL for _ in range((grid_size)**2)]

        temp_grid[grid_size*(grid_size-1)] = GameLevel.PLAYER_ICON

        half_way = int(round(grid_size/2,1)) # TODO: Decide whether to do a proper floor calculation or not
        temp_grid[grid_size*half_way+half_way] = GameLevel.KEY_ICON

        temp_grid[grid_size-1] = GameLevel.BOSS_ICON

        return temp_grid
       
    def update_grid(self):
        # This function will take an object (player/enemy or reward/equipment) and add/remove it to the playable level
        # This function should also be used to update the placement of the main character 
        raise NotImplementedError

    def print_grid(self):

        # Add Design Boundary
        header = GameLevel.CORNER_BOUND_SYMBOLS[0] +GameLevel.HORIZONTAL_BOUND_SYMBOL*self.playable_size + GameLevel.CORNER_BOUND_SYMBOLS[1]
        footer = GameLevel.CORNER_BOUND_SYMBOLS[2] +GameLevel.HORIZONTAL_BOUND_SYMBOL*self.playable_size+GameLevel.CORNER_BOUND_SYMBOLS[3]
        
        # Print Grid with Boundary
        print(header)
        for index in range(self.playable_size):
            print(''.join(self.grid[index*self.playable_size:index*self.playable_size+self.playable_size]).center(self.playable_size+2, GameLevel.VERTICAL_BOUND_SYMBOL))
        print(footer)

    def select_monsters():
        raise NotImplementedError   