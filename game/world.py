
import pygame as pg
from .setting import TILE_SIZE


class World:

    def __init__(self, grid_l_x, grid_l_y, witdh, height):
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = witdh
        self.height = height

        self.world = self.cree_world()

    def cree_world(self):
        world = []

        for grid_x in range(self.grid_lx):
            world.append([])
            for grid_y in range(self.grid_ly):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)
        return world

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x*TILE_SIZE, grid_y*TILE_SIZE),
            (grid_x*TILE_SIZE+TILE_SIZE, grid_y*TILE_SIZE),
            (grid_x*TILE_SIZE+TILE_SIZE, grid_y*TILE_SIZE+TILE_SIZE),
            (grid_x*TILE_SIZE, grid_y*TILE_SIZE+TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        output = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly
        }

        return output

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y
