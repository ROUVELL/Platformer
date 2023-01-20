import pygame as pg

from utills import vec, pressed_keys, pressed_mkeys, Timer

from weapon import Glock, Ak47
from config import *


class Player:
    def __init__(self, game, name: str = 'Player'):
        self.game = game
        self._name = pg.font.SysFont('arial', 14).render(name, True, 'white')
        self.rect = pg.Rect(PLAYER_POS, PLAYER_SIZE)
        #############
        self.gun = Ak47(self, self.game.world.bullets)
        self._jump_timer = Timer(JUMP_DELEY, activate=True)
        #############
        self.speed = PLAYER_SPEED  # швидкість ігрока
        self.direction = vec()     # напрям руху

    def move(self, direction: vec):
        self.rect.move_ip(direction)
        self.gun.rect.move_ip(direction)

    def _movement(self):
        self.direction.x = 0

        self._keyboard_control()

        self.direction.y = min(self.direction.y + GRAVITY, MAX_VERTICAL_SPEED)
        self.direction = self.game.world.check_collide(self.rect.copy(), self.direction)

        self.move(self.direction)

    def _keyboard_control(self):
        keys = pressed_keys()
        if keys[pg.K_a]: self.direction.x = -self.speed
        if keys[pg.K_d]: self.direction.x = self.speed
        if keys[pg.K_SPACE] and self._jump_timer:
            self._jump_timer.activate()
            self.direction.y = -JUMP_POWER
        if keys[pg.K_r]:
            self.gun.reload()

    def _mouse_control(self):
        mkeys = pressed_mkeys()
        if mkeys[0]: self.gun.shot()

    def update(self):
        self._jump_timer.update()
        self.gun.update()
        self._movement()
        self._mouse_control()

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'red', self.rect, border_radius=3)

        rect = self._name.get_rect()
        rect.centerx = self.rect.centerx
        rect.bottom = self.rect.top - 2
        sc.blit(self._name, rect)

        self.gun.draw(sc)
