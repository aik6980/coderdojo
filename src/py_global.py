from pygame.math import *

COLOR_WHITE = [255, 255, 255]
COLOR_BLACK = [0, 0, 0]
COLOR_RED = [255, 0, 0]

# pygame globals
SCREEN_SIZE = [640, 480]
MAIN_SURFACE = None

#our game global
PHYSIC_SIMULATION = None


def to_tuple_i32(a: Vector2):
    return (int(a.x), int(a.y))