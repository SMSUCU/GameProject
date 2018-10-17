import curses
import levels
import player


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
height, width = stdscr.getmaxyx()
obstacle = ["Ж", "H", "I"]
current_level = 0
mode = True


levels.entrance_level(stdscr, height, width)
border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
x = width//2
y = height - 8
player.body(stdscr, y, x)
while True:
    y, x, mode, current_level = player.movement(
        stdscr, height, width, obstacle, y, x, current_level)
    if mode == False:
        break
    if current_level == 0:
        levels.entrance_level(stdscr, height, width)
    border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
    player.body(stdscr, y, x)
    stdscr.refresh
curses.endwin()
