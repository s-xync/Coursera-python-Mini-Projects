#http://www.codeskulptor.org/#user41_MSfe0fJbtuMYZ9w.py
"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append( (row, col) )

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append( (row, col) )

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # initialize
        grid_height = self.get_grid_height()
        grid_width = self.get_grid_width()
        visited = poc_grid.Grid(grid_height, grid_width)
        distance_field = [[grid_height*grid_width for _ in range(grid_width)]
                          for _ in range(grid_height)]
        boundary = poc_queue.Queue()
        entity_list = self._zombie_list if entity_type == ZOMBIE else self._human_list
        for entity in entity_list:
            boundary.enqueue(entity)
            visited.set_full(entity[0], entity[1])
            distance_field[entity[0]][entity[1]] = 0
        # search
        while boundary:
            current = boundary.dequeue()
            dist = distance_field[current[0]][current[1]]
            for neighbor in visited.four_neighbors(current[0], current[1]):
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    distance_field[neighbor[0]][neighbor[1]] = dist + 1
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        self._move_entities(zombie_distance_field, self._human_list, self.humans(), self.eight_neighbors, self._op_gt)

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        self._move_entities(human_distance_field, self._zombie_list, self.zombies(), self.four_neighbors, self._op_lt)

    def _move_entities(self, distance_field, entity_list, entities_gen, neighbors_func, op_comp):
        """
        helper function
        """
        for idx, entity in enumerate(entities_gen):
            candidate = entity
            dist = distance_field[entity[0]][entity[1]]
            neighbors = neighbors_func(entity[0], entity[1])
            random.shuffle(neighbors)
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    new_dist = distance_field[neighbor[0]][neighbor[1]]
                    if op_comp(new_dist, dist):
                        candidate = neighbor
                        dist = new_dist
            entity_list[idx] = candidate

    def _op_gt(self, dist1, dist2):
        """
        operator >
        """
        return dist1 > dist2

    def _op_lt(self, dist1, dist2):
        """
        operator <
        """
        return dist1 < dist2

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
