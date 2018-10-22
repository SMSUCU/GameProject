def movement(window, height, width, obstacle, y, x, level):
    import curses
    import parni
    import happy
    import ulamfunc
    import test4all
    key = window.getch()
    old_level = None
    question_check = 1
    for area in range(5):
        for len in range(6):
            window.addch(y + len, x + area, ' ')
    if key == ord('w') or key == curses.KEY_UP:
        y -= 1
        if chr(window.inch(y, x)) in obstacle or y == 1:
            y += 1
        if chr(window.inch(y, x)) == "_":
            question_check = 0
            while question_check in range(0, 5):
                if level == 1:
                    trash, answer = parni.parni(
                        height, width, level, window)
                elif level == 2:
                    trash, answer = parni.parni(
                        height, width, level, window)
                elif level == 3:
                    trash, answer = happy.happy_test(height, width, window)
                elif level == 4:
                    trash, answer = ulamfunc.ulam_test(height, width, window)
                if answer == True:
                    question_check += 1
                elif answer == False:
                    question_check -= 1
            y += 2
    if key == ord('s') or key == curses.KEY_DOWN:
        y += 1
        if y == height - 7:
            y -= 1
        elif chr(window.inch(y + 6, x)) in obstacle:
            y -= 1
    if key == ord('d') or key == curses.KEY_RIGHT:
        x += 1
        if chr(window.inch(y, x + 4)) in obstacle or x == width - 5:
            x -= 1
    if key == ord('a') or key == curses.KEY_LEFT:
        x -= 1
        if chr(window.inch(y, x)) in obstacle or x == 1:
            x += 1
    if key == ord('q'):
        return y, x, False, level, old_level, None
    if chr(window.inch(y, x)) == '🧱':
        level += 1
        old_level = level
        return y, x, True, level, old_level, 0
    return y, x, True, level, old_level, question_check


def body(window, y, x):
    window.addstr(y, x+1, "_П_")
    window.addstr(y+1, x+2, "@")
    window.addstr(y+2, x, "--|--")
    window.addstr(y+3, x+2, "|")
    window.addstr(y+4, x+1, "| |")
    window.addstr(y+5, x+1, "| |")
