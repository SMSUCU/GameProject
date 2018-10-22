import curses
import levels
import player
import text


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
height, width = stdscr.getmaxyx()
obstacle = ["Ж", "H", "I", "|", "/", "#"]
current_level = 0
mode = True
question_check = False
question_value = 0


def basic_player_generation():
    x = width // 2
    y = height - 8
    player.body(stdscr, y, x)
    return y, x


text.start(stdscr)
levels.entrance_level(stdscr, height, width)
border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
y, x = basic_player_generation()

while True:
    y, x, mode, current_level, old_level, question_value = player.movement(
        stdscr, height, width, obstacle, y, x, current_level)
    if question_value < 0:
        current_level = 0
        stdscr.clear()
        y, x = basic_player_generation()
    elif question_value == 0:
        question_check = False
    elif question_value == 5:
        question_check = True
    if mode == False:
        break
    if old_level == current_level:
        old_level = None
        stdscr.clear()
        y, x = basic_player_generation()
    if current_level == 0:
        levels.entrance_level(stdscr, height, width)
    if current_level in range(1, 5):
        levels.level(stdscr, height, width, question_check)
        levels.professor(height//2 - 3, width//2 - 2, stdscr)
    if current_level == 5:
        levels.level(stdscr, height, width, False)
    border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
    player.body(stdscr, y, x)
    stdscr.refresh
curses.endwin()
