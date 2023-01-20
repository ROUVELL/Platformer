import pygame as pg

from bullet import GlockBullet, Ak47Bullet
from utills import vec, all_events, Timer, current_pos
from config import CENTER


# Abstract class
class Weapon:
    def __init__(self, user, group: list, *, size: tuple[int, int],
                 shot_deley: int = 100, reload_time: int = 2000, name: str = 'Gun'):
        rect = pg.Rect((0, 0), size)
        rect.center = user.rect.center
        self.rect = rect
        self.user = user  # Той хто використовує зброю
        self._bullet_group = group  # група для патронів
        self.bullet = GlockBullet  # клас набоя яким будемо стріляти
        self.magazine_size = 30  # місткість магазину
        self.curr_bullets = 0  # поточна к-сть набоїв в магазині
        ##########
        self._shot_timer = Timer(shot_deley)  # таймер між вистрілами
        self._reload_timer = Timer(reload_time)  # таймер перезарядки
        self.reloading = False  # чи перезаряжаємо
        ##########
        self._name = pg.font.SysFont('calibri', 12).render(name, True, 'white')
        self._reloading_text = pg.font.SysFont('calibri', 36).render('Reloading', True, 'white')

    def _get_direction(self) -> vec:
        size = current_pos() - vec(self.rect.center)
        direction = vec(size.x / size.length(), size.y / size.length())
        return direction * 4

    def shot(self):
        if self._shot_timer and self._reload_timer:
            self.curr_bullets -= 1
            self._shot_timer.activate()
            self._bullet_group.append(self.bullet(self._bullet_group, vec(self.rect.center), self._get_direction()))

    def reload(self):
        # Якщо таймер не активований і ми не перезаряжаємось - починаємо перезарядку
        # Якщо таймер не активований і ми все ще перезаряєжаємось - значить перезарядку закінчено
        if not self._reload_timer: return
        if self.reloading:
            self.curr_bullets = self.magazine_size
            self.reloading = False
        else:
            self._reload_timer.activate()
            self.reloading = True

    def update(self):
        self._shot_timer.update()
        self._reload_timer.update()
        if self.reloading or not self.curr_bullets:
            self.reload()

    def draw(self, sc: pg.Surface):
        name_rect = self._name.get_rect()
        name_rect.centerx = self.rect.centerx
        name_rect.bottom = self.rect.top - 2

        pg.draw.rect(sc, 'green', self.rect, border_radius=3)
        if not self._reload_timer:
            rect = self._reloading_text.get_rect(center=CENTER)
            sc.blit(self._reloading_text, rect)
        # sc.blit(self.name, name_rect)


class Glock(Weapon):
    def __init__(self, user, group: list):
        super().__init__(user, group, size=(20, 15), shot_deley=300, reload_time=3000, name='Glock')
        self.magazine_size = 7


class Ak47(Weapon):
    def __init__(self, user, group: list):
        super().__init__(user, group, size=(30, 15), shot_deley=80, reload_time=2700, name='Ak-47')
        self.bullet = Ak47Bullet
