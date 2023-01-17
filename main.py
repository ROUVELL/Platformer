import pygame as pg

from player import Player
from world import World

from utills import all_events
from config import *


class Game:
    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN, pg.NOFRAME)
        self.clock = pg.time.Clock()
        ##########
        self.hero = Player(self)
        self.world = World()

    def run(self):
        while True:
            self.clock.tick(60)
            [exit() for event in all_events(pg.KEYUP) if event.key == pg.K_ESCAPE]
            self.sc.fill((20, 20, 20))

            self.hero.update()
            self.world.draw(self.sc)
            self.hero.draw(self.sc)

            pg.event.clear()
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()