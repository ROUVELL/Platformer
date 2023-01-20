import pygame as pg

from config import WIDTH, HEIGHT


class Drawing:
    def __init__(self, game):
        self._game = game
        self._sc = game.sc
        ########
        self._fps_font = pg.font.SysFont('calibri', 32)
        self._text_font = pg.font.SysFont('calibri', 24)

    def _bullets(self):
        [bullet.draw(self._sc) for bullet in self._game.world.bullets]

    def _world(self):
        self._game.world.draw(self._sc)

    def _player(self):
        self._game.hero.draw(self._sc)

    def _fps(self):
        fps = f'{self._game.clock.get_fps() : .1f}'
        self._sc.blit(self._fps_font.render(fps, True, 'white'), (0, 0))

    def _debug_info(self):
        bullets = self._game.hero.gun.curr_bullets
        text = f'Bullets: {bullets}'
        render = self._text_font.render(text, True, 'white')
        self._sc.blit(render, (WIDTH - 140, 0))

    def all(self):
        self._bullets()
        self._world()
        self._player()
        self._fps()
        self._debug_info()