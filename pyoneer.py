#!/usr/bin/env python

from gamemap import GameMap, AVAILABLE_DIRECTIONS, EMPTY, PLAYER

def play():
    # let's create a corridor map with the player dead in the top middle
    player_map = GameMap(3, 5, [1, 0])

    while True:
        player_position = player_map.get_position_of(PLAYER)

        direction = input("You're at ({position}), what would you like to do? ({directions})\n>> ".format(
            position=", ".join(map(str, player_position)),
            directions=", ".join(AVAILABLE_DIRECTIONS)
        ))

        if direction == '':
            print("Nothing heard!")
            continue

        direction = direction.lower()

        try:
            player_map.move(PLAYER, direction)
        except ValueError as e:
            print("/!\\ {0} /!\\".format(e))


if __name__ == '__main__':
    play()