from .base import BaseState

class Start(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SelectGameMode"

    def update(self):
        pass

    def get_event(self, event):
        if event == 'q':
            self.quit = True
        elif event != None:
            self.done = True


    def draw(self, screen):
        screen.clear()
        screen.addstr("Welcome to the Speed Typewriter")
        screen.addstr("\n Press any key to begin or q to quit")
        screen.refresh()

