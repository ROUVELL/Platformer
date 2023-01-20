import pygame as pg

from utills import vec
from config import CAMERA_RECT


class Camera:
    def __init__(self, target, world):
        self._rect = pg.Rect(CAMERA_RECT)
        self._target = target
        self._world = world

    def _get_offset(self) -> vec:
        offset = vec()
        camera, player = self._rect, self._target.rect

        if camera.left > player.left:
            offset.x = camera.left - player.left
        elif camera.right < player.right:
            offset.x = camera.right - player.right
        if camera.top > player.top:
            offset.y = camera.top - player.top
        elif camera.bottom < player.bottom:
            offset.y = camera.bottom - player.bottom
        return offset

    def update(self):
        if not self._rect.contains(self._target.rect):
            offset = self._get_offset()

            self._target.move(offset)
            self._world.offset(offset)

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'orange', self._rect, 2)