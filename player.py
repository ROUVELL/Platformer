import pygame as pg

from utills import vec, pressed_keys
from config import *


class Player:
    def __init__(self, game):
        self.game = game
        self._rect = pg.Rect(PLAYER_POS, PLAYER_SIZE)
        #############
        self.speed = PLAYER_SPEED  # швидкість ігрока
        self.direction = vec()     # напрям руху
        #############
        self.on_dirty = False  # чи стоїть ігрок на чомусь

    def movement(self):
        keys = pressed_keys()
        self.direction.x = 0

        if keys[pg.K_a]: self.direction.x = -self.speed
        if keys[pg.K_d]: self.direction.x = self.speed

        if not self.on_dirty:
            self.direction.y = min(self.direction.y + GRAVITY, MAX_VERTICAL_SPEED)

        # print(self.direction)
        offset = self.game.world.check_collide(self._rect.copy(), self.direction)

        self.on_dirty = False if offset.y else True

        self._rect.move_ip(offset)

    def update(self):
        self.movement()

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'red', self._rect, border_radius=3)
