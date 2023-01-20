from pygame.time import get_ticks


class Timer:
    def __init__(self, duration: int, *, state: bool = True, activate: bool = False):
        self.last_update = get_ticks()
        self.duration = duration
        ##########
        self.state = state   # True якщо час вийшов інакше False
        if activate: self.activate()

    def update(self):
        if not self.state:
            now = get_ticks()
            if now - self.last_update >= self.duration:
                self.state = True

    def activate(self):
        self.last_update = get_ticks()
        self.state = False

    def __bool__(self):
        return self.state
