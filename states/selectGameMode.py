from .base import BaseState


class SelectGameMode(BaseState):
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
            self.next_state = "VimCommands"
            self.done = True

    def draw(self, screen):
        screen.clear()
        screen.addstr("Please Select one Game Mode")
        screen.addstr(1, 3, "1. Simple Type Mode")
        screen.addstr(2, 3, "2. Vim Commands")
        screen.addstr(3, 0, "Or Press q to quit")
        screen.refresh()
