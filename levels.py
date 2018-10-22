def entrance_level(window, height, width):
    def tree(y, x):
        for stick in range(8):
            for i in range(5):
                window.addstr(y-stick, x+i, "I")
                highy = y-stick
        for leaves_length in range(10):
            for leaves_width in range(9):
                window.addstr(highy-leaves_length, x-2+leaves_width, "Ж")
        for leaves_length in range(8):
            for leaves_width in range(2):
                window.addstr(highy-1-leaves_length, x-4+leaves_width, "Ж")
            for leaves_width in range(2):
                window.addstr(highy-1-leaves_length, x+8-leaves_width, "Ж")
        for leaves_length in range(6):
            for leaves_width in range(2):
                window.addstr(highy-2-leaves_length, x+10-leaves_width, "Ж")
            for leaves_width in range(2):
                window.addstr(highy-2-leaves_length, x-6+leaves_width, "Ж")

    for y in range((height - 1)//2):
        for x in range(width - 1):
            window.addstr(y, x, "H")
    for y in range(12, (height - 1)//2):
        for x in range(86, 118):
            window.addstr(y, x, "🧱")
    tree(height - 9, 40)
    tree(height - 6, width - 50)
    tree(height - 8, width - 20)
    tree(height - 4, 15)


def level(window, height, width, question_check):
    for y in range(height - 1):
        for x in range(11):
            window.addstr(y, x, 'H')
        for x in range(width-11, width - 1):
            window.addstr(y, x, 'H')
    for x in range(11, width-11):
        for y in range(11):
            window.addstr(y, x, 'H')
        for y in range(height-5, height-1):
            window.addstr(y, x, 'H')
    for y in range(height-5, height-1):
        for x in range(86, 118):
            window.addstr(y, x, " ")
    if question_check == True:
        for y in range(11):
            for x in range(86, 118):
                window.addstr(y, x, "🧱")


def professor(y, x, window, level):
    if level == 1 or level == 4:
        window.addstr(y, x + 3, "###")
        window.addstr(y+1, x + 2, "#####")
    elif level == 2 or level == 5:
        window.addstr(y, x + 3, "///")
        window.addstr(y+1, x + 2, "/////")
    elif level == 3:
        window.addstr(y+1, x + 2, "/‾‾‾\\")
    window.addstr(y+2, x + 2, "|⦿△⦿|")
    if level == 2 or level == 4:
        window.addstr(y+3, x + 2, "| — |")
    elif level == 1 or level == 3 or level == 5:
        window.addstr(y+3, x + 2, "| ⏝ |")
    if level == 1 or level == 5:
        window.addstr(y+4, x + 2, "|_ _|")
    elif level == 2 or level == 3:
        window.addstr(y+4, x + 2, "|_W_|")
    elif level == 4:
        window.addstr(y+4, x + 2, "|@@@|")
    window.addstr(y+5, x + 3, "| |")
    window.addstr(y+6, x + 1, "/‾   ‾\\")
    window.addstr(y+7, x, "/   ∞   \\")
    window.addstr(y+8, x, "|  α Ω  |")
    window.addstr(y+9, x, "|   π   |")
    window.addstr(y+10, x, "|       |")
    window.addstr(y+11, x, "|       |")
    window.addstr(y+12, x, "|_______|")
