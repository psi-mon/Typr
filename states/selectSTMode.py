
from .base import BaseState

class SelectSTMode(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SimpleTypr"

    def update(self):
        pass


    def get_event(self, event):
        if (
            event == "q"
        ):  ## todo acc event class and destinguise between input an other events
            self.quit = True
        elif event == "1":
            self.done = True
        elif event == "2":
            self.done = True

    def draw(self, screen):
        screen.clear()
        screen.addstr("Select your mode")
        screen.addstr("1. Local storage")
        screen.addstr("2. Something else")
        screen.refresh()

