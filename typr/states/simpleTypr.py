from ..core import typeThingProvider
from .base import BaseState
from ..core import gameProgress
import curses

class SimpleTypr(BaseState):
    def __init__(self):
        super().__init__()
        self.next_state = "SimpleTypr"
        self.current_text = []
        self.target_text = "This is something to write"
        self.current_typo = False


    def startup(self, persistent):
        self.persist:gameProgress = persistent
        self.target_text = self.persist.getText() # todo try except block and transition to error screen
        self.current_text = []
        self.next_state = "SimpleTypr"
        self.current_typo = False

    def update(self):
        if "".join(self.current_text) == self.target_text:
            if self.persist.isGameOver():
                self.next_state = "ResultScreen"
            self.done = True
            # add typo to the stats
        if self.hasTypo(self.current_text, self.target_text) and not self.current_typo:
            self.current_typo = True
            self.persist.addTypo(1)
        elif not self.hasTypo(self.current_text, self.target_text):
            self.current_typo = False 



    def hasTypo(self, current, target)->bool:
        for i, char in enumerate(current):
            correct_char = target[i]
            if char != correct_char:
                return True
        return False 

    def get_event(self, event):
        if ord(event) == 27:
            self.done = True # todo: handle this as a sip => rounds++

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
