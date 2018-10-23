def perevirka(a):
    '''(int) -> bool
    This function returns True if number a is even.
    Otherwise it returns False.
    >>> perevirka(4)
    True
    >>> perevirka(23)
    False
    '''
    if (a % 2 == 0):
        return True
    else:
        return False


def suma(a, b):
    '''(int, int) -> bool
    This function returns True if sum of a and b is even.
    Otherwise it returns False.
    >>> suma(9, 7)
    True
    >>> suma(3, 20)
    False
    '''
    if (a+b) % 2 == 0:
        return True
    else:
        return False


def parni(height, width, level, window):
    ''' (int, int, int, window) -> bool
    This function returns result of even numbers test.
    '''
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
