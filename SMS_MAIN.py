import curses
import SMS_levels
import SMS_player
import SMS_text


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
height, width = stdscr.getmaxyx()
obstacle = ["Ж", "H", "I", "|", "/", "#"]
current_level = 0
win = False
mode = True
question_check = False
question_value = 0


def basic_player_generation():
    x = width // 2
    y = height - 8
    SMS_player.body(stdscr, y, x)
    return y, x


SMS_text.start(stdscr)
SMS_levels.entrance_level(stdscr, height, width)
border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
y, x = basic_player_generation()

while True:
    y, x, mode, current_level, old_level, question_value = SMS_player.movement(
        stdscr, height, width, obstacle, y, x, current_level)
    if question_value != None:
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
        SMS_levels.entrance_level(stdscr, height, width)
    if current_level in range(1, 5):
        SMS_levels.level(stdscr, height, width, question_check)
        SMS_levels.professor(height//2 - 3, width//2 -
                             2, stdscr, current_level)
    if current_level == 5:
        SMS_levels.level(stdscr, height, width, False)
        SMS_levels.professor(height//2 - 3, width//2 -
                             2, stdscr, current_level)
        if question_check == True:
            SMS_levels.professor(height//2 - 1, width//2 - 12, stdscr, 1)
            SMS_levels.professor(height//2 - 1, width//2 + 7, stdscr, 2)
            SMS_levels.professor(height//2 + 1, width//2 - 23, stdscr, 3)
            SMS_levels.professor(height//2 + 1, width//2 + 18, stdscr, 4)
            win = True
            break
    border = stdscr.border(0, 0, 0, 0, 0, 0, 0, 0)
    SMS_player.body(stdscr, y, x)
    stdscr.refresh
if win:
    SMS_text.end_game(height, width, stdscr)
curses.endwin()
