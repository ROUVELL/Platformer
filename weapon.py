import pygame as pg


from utills import vec, all_events, Timer


class Bullet:
    def __init__(self, pos: vec, direction: vec):
        self.rect = pg.Rect(pos, (12, 5))
        self.direction = direction

    def update(self):
        self.rect.move_ip(self.direction)

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, 'blue', self.rect, border_radius=3)


# Abstract class
class Weapon:
    SHOT_EVENT = pg.USEREVENT + 1

    def __init__(self, user, group: list, rect: pg.Rect, shot_deley: int = 100, name: str = 'Gun'):
        self.rect = rect
        self.user = user
        self.bullet_group = group
        ##########
        self.shot_pos = vec(self.rect.right, self.rect.top)  # Позиція де з'являється пуля
        self.shot_timer = Timer(shot_deley)
        ##########
        self.name = pg.font.SysFont('calibri', 12).render(name, True, 'white')

    def shot(self, direction: vec):
        if self.shot_timer.state:

            pg.time.set_timer(self.SHOT_EVENT, self.shot_time_deley, 1)
            self.bullet_group.append(Bullet(self.shot_pos, direction))

    def update(self):
        self.shot_pos = vec(self.rect.right, self.rect.top)
        if self.is_shot:
            if all_events(self.SHOT_EVENT):
                self.is_shot = False

    def draw(self, sc: pg.Surface):
        name_rect = self.name.get_rect()
        name_rect.centerx = self.rect.centerx
        name_rect.bottom = self.rect.top - 2

        pg.draw.rect(sc, 'green', self.rect, border_radius=3)
        sc.blit(self.name, name_rect)


class Pistol(Weapon):
    def __init__(self, user, group: list):
        topleft = (user.rect.right, user.rect.top + 5)
        rect = pg.Rect(topleft, (20, 15))
        super().__init__(user, group, rect, 100, 'Pistol')
