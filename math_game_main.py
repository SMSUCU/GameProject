import curses


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
height, width = stdscr.getmaxyx()


def tree(y, x):
    for stick in range(8):
        for i in range(5):
            stdscr.addstr(y-stick, x+i, "I")
            highy = y-stick
    for leaves_length in range(10):
        for leaves_width in range(9):
            stdscr.addstr(highy-leaves_length, x-2+leaves_width, "Ж")
    for leaves_length in range(8):
        for leaves_width in range(2):
            stdscr.addstr(highy-1-leaves_length, x-4+leaves_width, "Ж")
        for leaves_width in range(2):
            stdscr.addstr(highy-1-leaves_length, x+8-leaves_width, "Ж")
    for leaves_length in range(6):
        for leaves_width in range(2):
            stdscr.addstr(highy-2-leaves_length, x+10-leaves_width, "Ж")
        for leaves_width in range(2):
            stdscr.addstr(highy-2-leaves_length, x-6+leaves_width, "Ж")


def entrance_level():
    for y in range((height - 1)//2):
        for x in range((width - 1)//3):
            stdscr.addch(y, x, ord('a'))
        for x in range((width - 1)//3):
            stdscr.addch(y, (width - x - 1), ord('a'))
    tree(height - 9, 40)
    tree(height - 6, width - 50)
    tree(height - 8, width - 20)
    tree(height - 4, 15)


def movement(y, x):
    key = stdscr.getch()
    for area in range(5):
        for len in range(6):
            stdscr.addch(y + len, x + area, ' ')
    if key == ord('w') or key == curses.KEY_UP:
        y -= 1
    if key == ord('s') or key == curses.KEY_DOWN:
        y += 1
    if key == ord('d') or key == curses.KEY_RIGHT:
        x += 1
    if key == ord('a') or key == curses.KEY_LEFT:
        x -= 1
    if key == ord('q'):
        return y, x, False
    player(y, x)
    stdscr.refresh()
    return y, x, True


def player(y, x):
    stdscr.addstr(y, x+1, "_П_")
    stdscr.addstr(y+1, x+2, "@")
    stdscr.addstr(y+2, x, "--|--")
    stdscr.addstr(y+3, x, "  |  ")
    stdscr.addstr(y+4, x+1, "| |")
    stdscr.addstr(y+5, x+1, "| |")


entrance_level()
mode = True
x = width//2
y = height - 8
player(y, x)
while True:
    y, x, mode = movement(y, x)
    if mode == False:
        break
    entrance_level()
    player(y, x)
    stdscr.refresh
curses.endwin()
