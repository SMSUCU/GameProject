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
