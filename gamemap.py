import random
from cell import Cell

class Win(Exception):
    pass

class GameMap(object):
    """
    Direction in the cells matrix is assumed as follow:

              north
                |
          west -X- east
                |
              south

    """
    AVAILABLE_DIRECTIONS = ('north', 'south', 'east', 'west')

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
        self.cells = [
            [
                Cell(walls={
                    "north": h == 0,
                    "south": h == height - 1,
                    "west": w == 0,
                    "east": w == width - 1
                })
                for w in range(width)
            ] for h in range(height)
        ]

        self.poke_a_hole()

        if player_position is not None:
            self.get_cell(player_position).add(Cell.PLAYER)

    def poke_a_hole(self):
        # listing all the cells with walls
        cells_with_a_wall = [ c for row in self.cells for c in row if True in c.walls.values() ]

        # pick one randomly
        cell_to_poke = cells_with_a_wall[random.randint(0, len(cells_with_a_wall) - 1)]

        # listing all the walls in the cell
        walls = [ direction for direction in self.AVAILABLE_DIRECTIONS if not cell_to_poke.can_go(direction) ]

        # pick one randomly
        direction = walls[random.randint(0, len(walls) - 1)]
        # print(['cheat for demo', walls, direction])

        # POKE!
        cell_to_poke.walls[direction] = False

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
            for w, cell in enumerate(row):
                if cell.has(value):
                    positions.append([w, h])
        return positions

    def is_inside(self, position):
        return (0 <= position[0] < len(self.cells[0])) and (0 <= position[1] < len(self.cells))

    def move(self, value, direction):
        old_position = self.get_position_of(value)
        if not self.get_cell(old_position).has(value):
            raise ValueError("Cannot move void")

        if not self.get_cell(old_position).can_go(direction):
            raise ValueError("You just hit a wall!")

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
            raise Win("Congrats!")

        self.get_cell(old_position).remove(value)
        self.get_cell(new_position).add(value)
