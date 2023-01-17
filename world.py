import pygame as pg

from utills import vec
from config import TILE_SIZE

_ = None
_map = [
    [_, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _],
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
    [_, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _]
]


class World:
    def __init__(self):
        self.tiles = []
        self._parse_map()

    def _parse_map(self):
        for y, row in enumerate(_map):
            for x, item in enumerate(row):
                if item:
                    self.tiles.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def check_collide(self, target: pg.Rect, direction: vec) -> vec:
        indexes = target.move(direction).collidelistall(self.tiles)
        colliders = [self.tiles[i] for i in indexes]
        offset = vec()
        vo, ho = direction


        if not colliders: return direction
        if len(colliders) == 1: return vec(direction.x, 0)
        if len(colliders) == 2:
            rect1, rect2 = colliders

        if rect1.centerx == rect2.centerx:
            # пересікли зліва
            if abs(target.centerx - rect1.right) < abs(target.centerx - rect1.left):
                offset.x = direction.x - (rect1.right - target.left)
            # пересікли зправа
            else: offset.x = direction.x - (target.right - rect1.left)
        # два горизонтально
        elif rect1.centery == rect2.centery:
            # пересікли зверху
            if abs(target.centery - rect1.bottom) < abs(target.centery - rect1.top):
                offset.y = direction.y - (rect1.bottom - target.top)
            # пересікли знизу
            else: offset.y = direction.y - (target.bottom - rect1.top)
        # один вище другий нижче
        else:
            pass

        return offset


    def update(self):
        pass

    def draw(self, sc: pg.Surface):
        [pg.draw.rect(sc, 'green', rect, 1) for rect in self.tiles]