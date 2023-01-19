import pygame as pg


class Drawing:
    def __init__(self, game):
        self.game = game
        self.sc = game.sc
        ########
        self.fps_font = pg.font.SysFont('calibri', 32)

    def world(self):
        self.game.world.draw(self.sc)

    def player(self):
        self.game.hero.draw(self.sc)

    def fps(self):
        fps = f'{self.game.clock.get_fps() : .1f}'
        self.sc.blit(self.fps_font.render(fps, True, 'white'), (0, 0))

    def all(self):
        self.world()
        self.player()
        self.fps()