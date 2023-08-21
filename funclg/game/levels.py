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
        self.grid = self.generate_grid() # TODO: Consider if this should be private and only callable
        self.player_pos = (0,0)

    
    def coord_to_int(self, coordinate:set[int, int]):
        if coordinate[0] >= 0 and coordinate[0] < self.playable_size and coordinate[1] >= 0 and coordinate[1] < self.playable_size:
            return self.playable_size*coordinate[1] + coordinate[0]
        raise IndexError("Coordinate is out range")


    # TODO: Consider doing a precheck to make sure the running system can print the boundary characters, if not then use alternatives
    def generate_grid(self):

        # Build Grid
        temp_grid = [GameLevel.SPACE_SYMBOL for _ in range((self.playable_size)**2)]

        temp_grid[self.coord_to_int((0,self.playable_size-1))] = GameLevel.PLAYER_ICON

        half_way = int(round(self.playable_size/2,1)) # TODO: Decide whether to do a proper floor calculation or not
        temp_grid[self.coord_to_int((half_way,half_way))] = GameLevel.KEY_ICON

        temp_grid[self.coord_to_int((self.playable_size-1,0))] = GameLevel.BOSS_ICON

        return temp_grid
    
    def generate_difficulty(self):
        # TODO: I want to be able to make a decision if a block should be reward, enemy etc.
            # Should this automatically(randomly) completed before or done randomly as player progresses
            # How should the history of the space be preserved should it be tracked in another grid or should the slots be objects that track their status and use bools for status and visualization, and completion
        raise NotImplementedError
       
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

if __name__ == "__main__":
    new_level = GameLevel(game_settings={"level_size":7})
    new_level.print_grid()
    new_level.grid[new_level.coord_to_int(1,3)]