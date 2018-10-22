def ulam_generator(chyslo):
    ''' (int) -> list
    This function returns a list of ulam numbers in sequence (chyslo)
    >>> ulam_generator(30)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138]
    >>> ulam_generator(15)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53]
    '''
    ulam = [1, 2]
    for i in range(chyslo):
        lst = []
        for each in ulam:
            for every in ulam:
                if each != every:
                    lst.append(each + every)
        while True:
            a = min(lst)
            if lst.count(a) == 2 and ulam.count(a) < 1:
                ulam.append(a)
                break
            else:
                for i in range(lst.count(a)):
                    lst.remove(a)
    return ulam


def ulam_test(height, width, window):
    import random
    y, x = height//2 - 4, width//2 - 4
    lst = ulam_generator(100)
    lst1 = list(range(201))
    lst1.extend(lst)
    number = random.choice(lst1)
    window.addstr(y, x, 'Is ' + str(number) + ' a Ulam number?')
    window.refresh()
    if number in lst:
        value = True
    else:
        value = False

    player_value = buttons.buttons()
    if player_value == value:
        window.addstr(y, x, 'Correct. Press any key               ')
        window.refresh()
        window.getkey()
        return number, True
    else:
        window.addstr(y, x, 'Wrong. Press any key                 ')
        window.refresh()
        window.getkey()
        return number, False
