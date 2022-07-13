
from .base import BaseState
from ..core import gameProgress
from ..core import TypeType
from ..core import typeThingProvider

class SelectSTMode(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SimpleTypr"
        self.persist = None

    def update(self):
        pass

    def startup(self, persistent):
        pass

    def get_event(self, event):
        if (
            event == "q"
        ):  ## todo acc event class and destinguise between input an other events
            self.quit = True
        elif event == "1":
            self.done = True
        elif event == "2":
            self.persist = gameProgress(typeThingProvider(TypeType.EN))
            self.done = True

    def draw(self, screen):
        screen.clear()
        screen.addstr("Select your mode")
        screen.addstr(1,3,"1. Local storage")
        screen.addstr(2,3,"2. English")
        screen.addstr(3,3,"3. German")
        screen.addstr(4,3,"4. Python")
        screen.addstr(5,3,"5. Typescript")
        screen.addstr(6,3,"6. C#")
        screen.addstr(7,3,"7. Single Characters")
        screen.addstr(8,3,"8. Numbers")
        screen.addstr(9, 0, "Or Press q to quit")
        screen.refresh()

