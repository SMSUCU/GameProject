def test_all(height, width, window):
    import buttons
    import random
    import parni
    import happy
    import ulamfunc
    number = random.randint(1, 200)
    value = []
    y, x = height // 2 - 4, width // 2 - 4
    window.addstr(y, x, 'What type of number is ' + str(number) + '?')
    window.refresh()
    player_value = buttons.buttons5()
    if parni.perevirka(number):
        value.append(1)
    if number in happy.checkhappy():
        value.append(2)
    if number in ulamfunc.ulam_generator():
        value.append(3)
    if len(value) == 0:
        value.append(4)
    if player_value in value:
        window.addstr(y, x, 'Correct. Press any key                      ')
        window.refresh()
        window.getkey()
        return True
    else:
        window.addstr(y, x, 'Wrong. Press any key                       ')
        window.refresh()
        window.getkey()
        return False
