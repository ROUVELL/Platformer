import pygame as pg

from utills import vec


# Abstract class
class Bullet:
    def __init__(self, pos: vec, size: vec, direction: vec, *, type_: str, color: str | tuple[int, int, int]):
        assert type_ in ['rect', 'cicle'], f'Unknown type of bullet: {type_}!'
        assert direction, 'Direction can`t be (0, 0)!'
        self.pos = pos
        self.size = size
        self.direction = direction
        self.type_ = type_
        self.color = color

    @property
    def rect(self):
        return pg.Rect(self.pos, self.size)

    def move(self, offset: vec):
        self.pos += offset

    def update(self):
        self.move(self.direction)

    def draw(self, sc: pg.Surface):
        if self.type_ == 'rect':
            pg.draw.rect(sc, self.color, self.rect, border_radius=3)
        elif self.type_ == 'cicle':
            pg.draw.circle(sc, self.color, self.rect.center, self.size.x)


class PistolBullet(Bullet):
    def __init__(self, pos: vec, direction: vec):
        super().__init__(pos, vec(4, 4), direction, type_='cicle', color='orange')
