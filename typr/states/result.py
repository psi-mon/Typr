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
        screen.addstr("Result:")
        screen.addstr(1, 3, f"Total Typos: {self.persist.totalTypos()}")
        screen.addstr(2, 3, f"Number of perfect round {self.persist.perfectRounds()}")
        screen.addstr(3, 3, f"Average Accuracy {self.persist.averageAcc()}")
        screen.addstr(4, 3, f"Average Characters per Minute {self.persist.averageCPM()}")
        screen.addstr(5, 3, f"Average Words per Minute {self.persist.averageWPM()}")
        screen.addstr(6, 0, "Or Press q to quit")
        screen.refresh()
