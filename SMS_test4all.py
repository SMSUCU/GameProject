import SMS_buttons
import random
import SMS_parni
import SMS_happy
import SMS_ulamfunc


def test_all(height, width, window):
    '''(int, int, window) -> bool
    This function returns result of test for all number types.
    '''
    number = random.randint(1, 100)
    value = []
    y, x = height // 2 - 4, width // 2 - 4
    window.addstr(y, x, 'What type of number is ' + str(number) + '?')
    window.refresh()
    player_value = SMS_buttons.buttons5()
    if SMS_parni.perevirka(number):
        value.append(1)
    if number in SMS_ulamfunc.ulam_generator():
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
