import curses
from curses import wrapper
from typr.states import Start
from typr.states import SelectGameMode
from typr.states import SimpleTypr
from typr.states import SelectSTMode
from typr.core import Typr

states = {
    "Start": Start(),
    "SelectGameMode": SelectGameMode(),
    "SimpleTypr": SimpleTypr(),
    "SelectSTMode": SelectSTMode(),
}


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    typr = Typr(stdscr, states, "Start")
    typr.run()


wrapper(main)
