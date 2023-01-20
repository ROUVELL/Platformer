import pygame as pg

from utills import vec
from config import WIDTH, HEIGHT, CAMERA_RECT


class Camera:
    def __init__(self, target, world):
        l, t, r, b = CAMERA_RECT
        w, h = WIDTH - l - r, HEIGHT - t - b
        self.rect = pg.Rect(l, t, w, h)
        self.target = target
        self.world = world

    def get_offset(self) -> vec:
        ox = oy = 0
        camera, player = self.rect, self.target.rect

        if camera.left > player.left:
            ox = camera.left - player.left
        elif camera.right < player.right:
            ox = camera.right - player.right
        if camera.top > player.top:
            oy = camera.top - player.top
        elif camera.bottom < player.bottom:
            oy = camera.bottom - player.bottom
        return vec(ox, oy)

    def update(self):
        if not self.rect.contains(self.target.rect):
            offset = self.get_offset()

            self.target.move(offset)
            self.world.offset(offset)

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'orange', self.rect, 2)