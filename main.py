import curses
from curses import wrapper
from typr.states import Start
from typr.states import SelectGameMode
from typr.states import SimpleTypr
from typr.states import SelectSTMode
from typr.states import Result
from typr.states import ErrorScreen
from typr.core import Typr

states = {
    "Start": Start(),
    "SelectGameMode": SelectGameMode(),
    "SimpleTypr": SimpleTypr(),
    "SelectSTMode": SelectSTMode(),
    "ResultScreen": Result(),
    "ErrorScreen" : ErrorScreen()
}


import requests
def testfu():
    r = requests.get('https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/cc7f584b962ff1d86e5f07777878e017d0ddeae5/tools/challenge-editor/api/server.ts')
    code = r.content
    lines = code.splitlines()
    print(r.status_code)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)
    typr = Typr(stdscr, states, "Start")
    typr.run()


testfu()
wrapper(main)
