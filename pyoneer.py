#!/usr/bin/env python

from cell import Cell
from gamemap import GameMap

def play():
    # let's create a corridor map with the player dead in the top middle
    player_map = GameMap(4, 6, [0, 0])

    while True:
        player_position = player_map.get_position_of(Cell.PLAYER)
        cell = player_map.get_cell(player_position)

        objects = cell.get_objects()
        objects = "\nYou're seeing: {objects}".format(objects=", ".join(objects)) if len(objects) > 0 else ""

        direction = input("You're currently at ({position}) {objects} \nWhat would you like to do? ({directions})\n>> ".format(
            position=", ".join(map(str, player_position)),
            objects=objects,
            directions=", ".join(GameMap.AVAILABLE_DIRECTIONS)
        ))

        if direction == '':
            print("Nothing heard!")
            continue

        direction = direction.lower()

        try:
            player_map.move(Cell.PLAYER, direction)
        except ValueError as e:
            print("/!\\ {0} /!\\".format(e))


if __name__ == '__main__':
    play()