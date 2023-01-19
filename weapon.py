import pygame as pg


class Weapon:
    def __init__(self, user):
        self.user = user
        ##########
        self.name = pg.font.SysFont('calibri', 12).render('Gun', True, 'white')

    def draw(self, sc: pg.Surface):
        user_rect = self.user.rect.copy()
        gun_rect = pg.Rect(user_rect.right, user_rect.top + 8, 20, 20)
        name_rect = self.name.get_rect()
        name_rect.centerx = gun_rect.centerx
        name_rect.bottom = gun_rect.top - 2

        pg.draw.rect(sc, 'green', gun_rect, border_radius=3)
        sc.blit(self.name, name_rect)
