from ..core import typeThingProvider
from .base import BaseState
from ..core import gameProgress
import curses

class SimpleTypr(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "ResultScreen"
        self.current_text = []
        self.target_text = "This is something to write"

    def startup(self, persistent):
        self.persist:gameProgress = persistent
        self.target_text = self.persist.getText()
    def update(self):
        if "".join(self.current_text) == self.target_text:
            self.done = True

    def get_event(self, event):
        if ord(event) == 27:
            self.done = True


        if event in ("KET_BACKSPACE", '\b', "\x7f"):
            if len(self.current_text) > 0:
                self.current_text.pop()
        elif len(self.current_text) < len(self.target_text):
            self.current_text.append(event)

    def display_text(self, stdscr, target, current, wpm=0):
            stdscr.addstr(target)
            stdscr.addstr(1,0,f"WPM: {wpm}")
         
            for i, char in enumerate(current):
                correct_char = target[i]
                color = curses.color_pair(1)
                if char != correct_char:
                    color = curses.color_pair(2)

                stdscr.addstr(0, i, char, color)

    def draw(self, screen):
        screen.clear()
        self.display_text(screen, self.target_text, self.current_text)

        screen.refresh()
