from ..core import gameProgress
from .base import BaseState

class Result(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SelectSTMode"
        self.persist:gameProgress

    def update(self):
        pass

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if (
            event == "q"
        ):  ## todo acc event class and destinguise between input an other events
            self.done = True

    def draw(self, screen):
        screen.clear()
        screen.addstr("Result")
        screen.addstr(1, 3, f"Typos: {self.persist.totalTypos()}")
        screen.addstr(2, 3, "2. Vim Commands")
        screen.addstr(3, 0, "Or Press q to quit")
        screen.refresh()
