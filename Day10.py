with open("Day10.txt", "r") as file:
    lines = file.readlines()
    file.seek(0)
    content = file.read()

pipe_length = 1

from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

