from enum import Enum


class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 4
    NONE = 8

class File(Enum):

    FILE = 0
    IMAGE = 1
    PDF = 2
