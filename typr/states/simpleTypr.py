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
        try:
          self.target_text = self.persist.getText() # todo try except block and transition to error screen
          self.current_text = []
          self.next_state = "SimpleTypr"
          self.current_typo = False
        except:
            self.next_state = "ErrorScreen"
            self.done = True

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
            if self.persist.isGameOver():
                self.next_state = "ResultScreen"
            self.done = True

        if event in ("KET_BACKSPACE", '\b', "\x7f"):
            if len(self.current_text) > 0:
                self.current_text.pop()
        elif len(self.current_text) < len(self.target_text):
            self.current_text.append(event)

    def display_text(self, stdscr, target, current, wpm=0):
            stdscr.addstr(target)
            stdscr.addstr(3,0,f"Rounds: {self.persist.currentProg()}")
            stdscr.addstr(4,0,f"Press ESC to skip")

         
            line = 0
            row = 0
            rowOffset = 0
            for i, char in enumerate(current):
                correct_char = target[i]
                color = curses.color_pair(1)
                if char != correct_char:
                    color = curses.color_pair(2)

                row = i - rowOffset
                # addstr is responsive and adds a new line when there is no room left
                # so when there is an exception we assume that we overflow and continue
                # at the next line
                try:
                  stdscr.addstr(line, row, char, color)
                except:
                    line +=1
                    rowOffset = i
                    stdscr.addstr(line, 0, char, color)


    def draw(self, screen):
        screen.clear()
        self.display_text(screen, self.target_text, self.current_text)

        screen.refresh()
