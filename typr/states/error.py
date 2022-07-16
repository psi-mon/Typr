from .base import BaseState
class ErrorScreen(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SelectSTMode"

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
        screen.addstr("There was an error")
        screen.addstr(2, 0, "Press q to go back to Selection Menu")
