import pygame as pg

from utills import vec
from config import TILE_SIZE

_ = None
_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
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

        def collide(target: pg.Rect, offset: vec) -> vec:
            if not offset: return vec()
            # horizontal
            if target.move(offset.x, 0).collidelist(self.tiles) != -1:
                new_offset = vec(offset.x - 1 if offset.x > 0 else offset.x + 1, offset.y)
                return collide(target, new_offset)
            # vertical
            if target.move(0, offset.y).collidelist(self.tiles) != -1:
                new_offset = vec(offset.x, offset.y - 1 if offset.y > 0 else offset.y + 1)
                return collide(target, new_offset)
            return offset

        return collide(target, direction)

    def offset(self, offset: vec):
        [rect.move_ip(offset) for rect in self.tiles]
        [bullet.move(offset) for bullet in self.bullets]

    def update(self):
        [self.bullets.remove(bullet) for bullet in self.bullets if bullet.rect.collidelist(self.tiles) != -1]
        [bullet.update() for bullet in self.bullets]

    def draw(self, sc: pg.Surface):
        [pg.draw.rect(sc, 'gray', rect, 1) for rect in self.tiles]
        [bullet.draw(sc) for bullet in self.bullets]