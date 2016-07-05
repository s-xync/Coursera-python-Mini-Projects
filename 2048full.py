"""
Clone of 2048 game.
"""
import poc_2048_gui
import random
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
    result = [0] * len(line)
    merged = False

    if len(line) < 2:
        return line

    for indexi in range(0, len(line)):
        if line[indexi] != 0:
            
            for indexl in range(0, len(result)):
               
                if result[indexl] == 0:
                    result[indexl] = line[indexi]
                    merged = False
                    break
                
                elif result[indexl + 1] == 0:
                    
                    if result[indexl] == line[indexi] and merged == False:
                        result[indexl] = result[indexl] + line[indexi]
                        merged = True
                        break
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        
        
        self.grid_value=dict()
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        for indexi in range(self.grid_height):
            for indexl in range(self.grid_width):
                self.grid_value[indexi,indexl]=0
        self.new_tile()
        self.new_tile()
        
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string=""
        for indexi in range(self.grid_height):
            for indexl in range(self.grid_width):
                string+=str(self.grid_value[indexi,indexl])
            string+='\n'
        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved=False
        if direction==UP:
            for indexi in range(self.grid_width):
                valuelist=[]
                for indexl in range(self.grid_height):
                    valuelist.append(self.grid_value[(indexl,indexi)])
                listmerged = merge(valuelist)
                if listmerged != valuelist:
                    moved=True
                for indexl in range(self.grid_height):
                    self.grid_value[(indexl,indexi)] = listmerged[indexl]
        elif direction==DOWN:
            for indexi in range(self.grid_width):
                valuelist=[]
                for indexl in range(self.grid_height):
                    valuelist.append(self.grid_value[(indexl,indexi)])
                valuelist.reverse()    
                listmerged = merge(valuelist)
                
                if listmerged != valuelist:
                    moved=True
                listmerged.reverse()
                for indexl in range(self.grid_height):
                    self.set_tile(indexl,indexi,listmerged[indexl])
        elif direction==LEFT:
            for indexi in range(self.grid_height):
                valuelist=[]
                for indexl in range(self.grid_width):
                    valuelist.append(self.grid_value[(indexi,indexl)])
                listmerged=merge(valuelist)
                if listmerged != valuelist:
                    moved=True
                for indexl in range(self.grid_width):
                    self.set_tile(indexi,indexl,listmerged[indexl])
        elif direction==RIGHT:
            for indexi in range(self.grid_height):
                valuelist=[]
                for indexl in range(self.grid_width):
                    valuelist.append(self.grid_value[(indexi,indexl)])
                valuelist.reverse()
                listmerged=merge(valuelist)
                
                if listmerged != valuelist:
                    moved=True
                listmerged.reverse()
                for indexl in range(self.grid_width):
                    self.set_tile(indexi,indexl,listmerged[indexl])
        if moved==True:
            self.new_tile()
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        nonelist=list()
        for index in self.grid_value:
            if self.grid_value[index]==0:
                nonelist.append(index)
        poschosen = random.choice(nonelist)
        self.grid_value[poschosen]=random.choice([2,2,2,2,2,2,2,2,2,4])

        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid_value[(row,col)]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """ 
             
        return self.grid_value[(row,col)]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
