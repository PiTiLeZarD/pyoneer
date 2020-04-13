"""
Direction in the cells matrix is assumed as follow:

          north
            |
      west -X- east
            |
          south

"""
AVAILABLE_DIRECTIONS = ('north', 'south', 'east', 'west')

EMPTY = 0
PLAYER = 1

class GameMap(object):

    def __init__(self, width, height, player_position=None):
        """
        Cells is a matrix as follows:

              <--- width --->
            [ [0, 0, 0, 0, 0],    ^
              [0, 0, 0, 0, 0],  height
              [0, 0, 0, 0, 0] ]   V

        Keep in mind: the first level is the height:
        cells[height][width] = cell
        """
        self.cells = [[EMPTY for h in range(width)] for w in range(height)]

        if player_position is not None:
            self.set_cell(player_position, PLAYER)

    def set_cell(self, position, value):
        self.cells[position[1]][position[0]] = value

    def get_cell(self, position):
        return self.cells[position[1]][position[0]]

    def get_position_of(self, value):
        positions = self.get_positions_of(value)
        if len(positions) != 1:
            raise ValueError("Expected to have a single positions and got {l}".format(l=len(positions)))
        return positions[0]

    def get_positions_of(self, value):
        positions = []
        for h, row in enumerate(self.cells):
            for w, v in enumerate(row):
                if v == value:
                    positions.append([w, h])
        return positions

    def is_inside(self, position):
        return (0 <= position[0] < len(self.cells[0])) and (0 <= position[1] < len(self.cells))

    def move(self, value, direction):
        old_position = self.get_position_of(value)
        if self.get_cell(old_position) == EMPTY:
            raise ValueError("Cannot move void")

        new_position = old_position.copy()

        if direction == 'north':
            new_position[1] = new_position[1] - 1
        elif direction == 'south':
            new_position[1] = new_position[1] + 1
        elif direction == 'west':
            new_position[0] = new_position[0] - 1
        elif direction == 'east':
            new_position[0] = new_position[0] + 1
        else:
            raise ValueError("Direction {direction} is not allowed".format(direction=direction))

        if not self.is_inside(new_position):
            raise ValueError("You cannot go outside the map")

        self.set_cell(old_position, EMPTY)
        self.set_cell(new_position, value)
