import curses
from curses import wrapper
from states.start import Start
from states.selectGameMode import SelectGameMode
from states.simpleTypr import SimpleTypr
from states.selectSTMode import SelectSTMode
from typr import Typr

states = {
    "Start": Start(),
    "SelectGameMode": SelectGameMode(),
    "SimpleTypr": SimpleTypr(),
    "SelectSTMode": SelectSTMode,
}


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    typr = Typr(stdscr, states, "Start")
    typr.run()


wrapper(main)
