def perevirka(a):
    if (a % 2 == 0):
        return True
    else:
        return False


def suma(a, b):
    if (a+b) % 2 == 0:
        return True
    else:
        return False


def parni(height, width, level, window):
    import random
    import buttons
    y, x = height//2 - 4, width//2 - 4
    number = random.randint(1, 1000)
    b = random.randint(1, 1000)
    if level == 1:
        window.addstr(y, x, 'Is ' + str(number) + ' a even number?   ')
        window.refresh()
        value = perevirka(number)
        player_value = buttons.buttons()
    elif level == 2:
        window.addstr(y, x, 'Is sum of ' + str(number) +
                      ' and ' + str(b) + ' an even number?')
        window.refresh()
        value = suma(number, b)
        player_value = buttons.buttons()
    if player_value == value:
        window.addstr(y, x, 'Correct. Press any key                      ')
        window.refresh()
        window.getkey()
        window.addstr(y, x, '                                     ')
        return True
    else:
        window.addstr(y, x, 'Wrong. Press any key                       ')
        window.refresh()
        window.getkey()
        window.addstr(y, x, '                                     ')
        return False
