from .base import BaseState
class ErrorScreen(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "Start"

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
        screen.addstr(3, 0, "Or Press q to quit")
