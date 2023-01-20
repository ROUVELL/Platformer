from pygame.time import get_ticks


class Timer:
    def __init__(self, duration: int, *, state: bool = True, activate: bool = False):
        self._last_update = get_ticks()
        self._duration = duration
        ##########
        self._state = state   # True якщо час вийшов інакше False
        if activate: self.activate()

    def update(self):
        if not self._state:
            now = get_ticks()
            if now - self._last_update >= self._duration:
                self._state = True

    def activate(self):
        self._last_update = get_ticks()
        self._state = False

    def __bool__(self):
        return self._state
