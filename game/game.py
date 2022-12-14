import pygame as pg
import sys
from .world import World
from .setting import TILE_SIZE


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(8, 8, self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((220, 220, 220))
        self.screen.blit(self.world.land_tile, (0, 0))

        for x in range(self.world.grid_lx):
            for y in range(self.world.grid_ly):

                #
                #               2D grid
                #

                #sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                #pg.draw.rect(self.screen, (0, 0, 255), rect, 2)

                render_pos = self.world.world[x][y]["render_pos"]
#
#               render grass tile with ineration(OUT-DATED)
#

              #  self.screen.blit(self.world.tiles["land"], (render_pos[0]+self.width/2, render_pos[1]+self.height/4))


#                   different tiles
#
                if self.world.world[x][y]["tile"]["name"] != "":
                    # tile = self.world.world[x][y]["tile"]
                    name_tile = self.world.world[x][y]["tile"]["name"]
                    offset = self.world.world[x][y]["tile"]["offset"]
                    self.screen.blit(self.world.tiles[name_tile], (
                        render_pos[0]+self.width/2,
                        render_pos[1]+self.height/4 - offset))


#
#                   2.5D grid
#
                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)

        pg.display.flip()
