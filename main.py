import pygame as pg

from drawing import Drawing
from player import Player
from camera import Camera
from world import World

from utills import all_events, Timer
from config import *


class Game:
    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN, pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.restart_timer = Timer(10000)
        # self.dt = 0.0
        self.start()

    def start(self):
        self.world = World()
        self.hero = Player(self)
        self.camera = Camera(self.hero, self.world)
        self.draw = Drawing(self)

    def update(self):
        self.hero.update()
        self.camera.update()
        self.world.update()
        self.restart_timer.update()

    def run(self):
        while True:
            self.clock.tick(60)  # TODO: delta time
            [exit() for event in all_events(pg.KEYUP) if event.key == pg.K_ESCAPE]
            self.sc.fill((20, 20, 20))

            self.update()
            self.draw.all()
            # self.camera.draw(self.sc)

            pg.event.clear()
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()