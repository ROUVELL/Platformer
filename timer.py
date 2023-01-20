from pygame.time import get_ticks


class Timer:
    def __init__(self, duration: int):
        self.last_update = get_ticks()
        self.duration = duration
        ##########
        self.state = False   # True якщо час вийшов інакше False

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
