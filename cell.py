import random

class Cell(object):

    PLAYER = 'player'
    OBJECTS = ['apple', 'pen', 'pineapple', 'jukebox']

    walls = {
        'north': False,
        'south': False,
        'east': False,
        'west': False
    }

    def __init__(self, walls=None):
        self.contains = []

        if walls is not None:
            self.walls = walls.copy()

        if random.randint(0, 20) == 5:
            self.add(self.OBJECTS[random.randint(0, len(self.OBJECTS) - 1)])            

    def add(self, value):
        self.contains.append(value)

    def remove(self, value):
        self.contains.pop(self.contains.index(value))

    def has(self, value):
        return value in self.contains

    def is_empty(self):
        return len(self.contains) == 0

    def get_objects(self):
        return [ o for o in self.contains if o != self.PLAYER ]

    def can_go(self, direction):
        if direction not in self.walls:
            return False
        return not self.walls[direction]