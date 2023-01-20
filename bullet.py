import pygame as pg

from utills import vec, Timer
from config import AUTO_REMOVE_DELEY


# Abstract class
class Bullet:
    def __init__(self, group: list, pos: vec, size: vec, direction: vec, *, type_: str = 'rect', color: str = 'blue'):
        assert type_ in ['rect', 'cicle'], f'Unknown type of bullet: {type_}!'
        assert direction, 'Direction can`t be (0, 0)!'
        self.group = group
        self.pos = pos
        self.size = size
        self.direction = direction
        self.type_ = type_
        self.color = color
        # Таймер самознищення
        self.remove_timer = Timer(AUTO_REMOVE_DELEY, activate=True)

    @property
    def rect(self):
        return pg.Rect(self.pos, self.size)

    def move(self, offset: vec):
        self.pos += offset

    def update(self):
        self.remove_timer.update()
        if self.remove_timer: self.group.remove(self)
        self.move(self.direction)

    def draw(self, sc: pg.Surface):
        if self.type_ == 'rect':
            pg.draw.rect(sc, self.color, self.rect, border_radius=3)
        elif self.type_ == 'cicle':
            pg.draw.circle(sc, self.color, self.rect.center, self.size.x)


class GlockBullet(Bullet):
    def __init__(self, group: list, pos: vec, direction: vec):
        super().__init__(group, pos, vec(3, 3), direction, type_='cicle', color='orange')


class Ak47Bullet(Bullet):
    def __init__(self, group: list, pos: vec, direction: vec):
        super().__init__(group, pos, vec(4, 4), direction, type_='cicle', color='orange')
