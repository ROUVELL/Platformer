import pygame as pg

from bullet import Bullet, PistolBullet
from utills import vec, all_events, Timer, current_pos


# Abstract class
class Weapon:
    def __init__(self, user, group: list, size: tuple[int, int], shot_deley: int = 100, name: str = 'Gun'):
        rect = pg.Rect((0, 0), size)
        rect.center = user.rect.center
        self.rect = rect
        self.user = user
        self.bullet_group = group
        ##########
        self.shot_pos = vec(self.rect.right, self.rect.top)  # Позиція де з'являється пуля
        self.shot_timer = Timer(shot_deley)
        ##########
        self.name = pg.font.SysFont('calibri', 12).render(name, True, 'white')

    def shot(self):
        if self.shot_timer.state:
            self.shot_timer.activate()
            self.bullet_group.append(Bullet(self.bullet_group, self.shot_pos, vec(12, 5), vec(5, 0), type_='rect', color='blue'))

    def update(self):
        self.shot_timer.update()
        self.shot_pos = vec(self.rect.right, self.rect.top)

    def draw(self, sc: pg.Surface):
        name_rect = self.name.get_rect()
        name_rect.centerx = self.rect.centerx
        name_rect.bottom = self.rect.top - 2

        pg.draw.rect(sc, 'green', self.rect, border_radius=3)
        # sc.blit(self.name, name_rect)


class Pistol(Weapon):
    def __init__(self, user, group: list):
        super().__init__(user, group, (20, 15), 3, 'Pistol')

    def shot(self):
        if self.shot_timer.state:
            self.shot_timer.activate()
            size = vec(current_pos()) - self.shot_pos
            direction = vec(size.x / size.length(), size.y / size.length())
            direction *= 4
            self.bullet_group.append(PistolBullet(self.bullet_group, self.shot_pos, direction))
