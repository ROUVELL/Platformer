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
        self.on_ground = False  # чи стоїть ігрок на чомусь

    def movement(self):
        keys = pressed_keys()
        self.direction.x = 0

        if keys[pg.K_a]: self.direction.x = -self.speed
        if keys[pg.K_d]: self.direction.x = self.speed
        if keys[pg.K_SPACE] and self.on_dirty:
            self.direction.y = -JUMP_POWER
            self.on_ground = False

        if not self.on_ground:
            self.direction.y = min(self.direction.y + GRAVITY, MAX_VERTICAL_SPEED)
        else: self.direction.y = 0

        new_direction = self.game.world.check_collide(self._rect.copy(), self.direction)
        # print(self.direction)
        # print(self.on_ground)
        self.on_ground = True if new_direction == self.direction else False

        self.direction = new_direction
        self._rect.move_ip(self.direction)

    def update(self):
        self.movement()

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'red', self._rect, border_radius=3)
