import pygame as pg

from config import WIDTH, HEIGHT


class Drawing:
    def __init__(self, game):
        self.game = game
        self.sc = game.sc
        ########
        self.fps_font = pg.font.SysFont('calibri', 32)
        self.text_font = pg.font.SysFont('calibri', 24)

    def bullets(self):
        [bullet.draw(self.sc) for bullet in self.game.world.bullets]

    def world(self):
        self.game.world.draw(self.sc)

    def player(self):
        self.game.hero.draw(self.sc)

    def fps(self):
        fps = f'{self.game.clock.get_fps() : .1f}'
        self.sc.blit(self.fps_font.render(fps, True, 'white'), (0, 0))

    def debug_info(self):
        bullets = len(self.game.world.bullets)
        text = f'Bullets: {bullets}'
        render = self.text_font.render(text, True, 'white')
        self.sc.blit(render, (WIDTH - 140, 0))

    def all(self):
        self.bullets()
        self.world()
        self.player()
        self.fps()
        self.debug_info()