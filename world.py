import pygame as pg

from utills import vec
from config import TILE_SIZE

_ = None
_map = [
    [_, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, 1, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, 1, _, _, _, _, _, 1, 1, _, _, _, _, _, _, _, 1],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class World:
    def __init__(self):
        self.tiles = []
        self.bullets = []
        self._parse_map()

    def _parse_map(self):
        for y, row in enumerate(_map):
            for x, item in enumerate(row):
                if item:
                    self.tiles.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def check_collide(self, target: pg.Rect, direction: vec) -> vec:
        def horizontal_collide(target: pg.Rect, ox: float) -> float:
            if not int(ox): return ox
            if target.move(ox, 0).collidelist(self.tiles) != -1:
                new_ox = ox - 1 if ox > 0 else ox + 1
                return horizontal_collide(target, new_ox)
            return ox

        def vertical_collide(target: pg.Rect, oy: float) -> float:
            if not int(oy): return oy
            if target.move(0, oy).collidelist(self.tiles) != -1:
                new_oy = oy - 1 if oy > 0 else oy + 1
                return vertical_collide(target, new_oy)
            return oy

        ox = horizontal_collide(target, direction.x)
        oy = vertical_collide(target, direction.y)

        return vec(ox, oy)

    def offset(self, offset: vec):
        [rect.move_ip(offset) for rect in self.tiles]
        [bullet.move(offset) for bullet in self.bullets]

    def update(self):
        [self.bullets.remove(bullet) for bullet in self.bullets if bullet.rect.collidelist(self.tiles) != -1]
        [bullet.update() for bullet in self.bullets]

    def draw(self, sc: pg.Surface):
        [pg.draw.rect(sc, 'gray', rect, 1) for rect in self.tiles]