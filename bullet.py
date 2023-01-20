import pygame as pg

from utills import vec, Timer
from config import AUTO_REMOVE_DELEY


# Abstract class
class __Bullet:
    def __init__(self, group: list, pos: vec, size: vec, direction: vec, *, color: str = 'orange'):
        assert direction, 'Direction can`t be (0, 0)!'
        self._group = group
        self._pos = pos
        self._size = size
        self._direction = direction
        self._color = color
        # Таймер самознищення
        self._remove_timer = Timer(AUTO_REMOVE_DELEY, activate=True)

    @property
    def rect(self) -> pg.Rect:
        return pg.Rect(self._pos, self._size)

    def move(self, offset: vec):
        self._pos += offset

    def update(self):
        self._remove_timer.update()
        if self._remove_timer: self._group.remove(self)
        self.move(self._direction)

    def draw(self, sc: pg.Surface):
        pg.draw.circle(sc, self._color, self.rect.center, self._size.x)


class GlockBullet(__Bullet):
    def __init__(self, group: list, pos: vec, direction: vec):
        super().__init__(group, pos, vec(3, 3), direction)


class Ak47Bullet(__Bullet):
    def __init__(self, group: list, pos: vec, direction: vec):
        super().__init__(group, pos, vec(4, 4), direction)
