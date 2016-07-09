#http://www.codeskulptor.org/#user41_gvxL5jmES7g64QL.py

"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
import time

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    myline = [item for item in line if item != 0] + [0]*line.count(0)
    return line if len(myline) < 2 else [2*myline[0]] + merge(myline[2:]) + [0] \
            if myline[0] == myline[1] else [myline[0]] + merge(myline[1:])

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._initial_tiles = {}
        self._initial_tiles[UP] = [(0,col) for col in range(grid_width)]
        self._initial_tiles[DOWN] = [(grid_height-1,col) for col in range(grid_width)]
        self._initial_tiles[LEFT] = [(row,0) for row in range(grid_height)]
        self._initial_tiles[RIGHT] = [(row,grid_width-1) for row in range(grid_height)]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for _ in range(self.get_grid_width())]
                           for _ in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join([str(row) for row in self._grid])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction in [UP,DOWN]:
            num_steps = self.get_grid_height()
        elif direction in [RIGHT, LEFT]:
            num_steps = self.get_grid_width()
        changed = False
        for cell in self._initial_tiles[direction]:
            tmp_list = self.traverse_grid(cell, OFFSETS[direction], num_steps)
            merged_list = merge(tmp_list)
            if merged_list != tmp_list:
                changed = True
            self.change_grid(cell, OFFSETS[direction], merged_list)
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_num = 2 if random.random() < 0.9 else 4
        empty_tiles = [(row, col) for row in range(self.get_grid_height())
                       for col in range(self.get_grid_width()) if self.get_tile(row,col) == 0]
        if len(empty_tiles) != 0:
            (row, col) = random.choice(empty_tiles)
            self.set_tile(row, col, new_num)
        else:
            print "Game over!"

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Helper function that return a line of grid
        """
        return [self._grid[start_cell[0] + step * direction[0]][start_cell[1] + step * direction[1]] for step in range(num_steps)]

    def change_grid(self, start_cell, direction, new_list):
        """
        Helper function that changes the value of row or colmun to new_list 
        """
        for step in range(len(new_list)):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid[row][col] = new_list[step]
            
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


