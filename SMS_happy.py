import random
import SMS_buttons


def checkhappy():
    '''
    None -> list
    This function checks if a number is a happy one or a sad and adds it to a list
    '''
    lst = []
    for num in range(1, 101):
        result = 0
        number = num
        while True:
            for digit in str(number):
                result += int(digit) ** 2
            number = result
            result = 0
            if number == 1 or number == 4:
                break

        if number == 1:
            lst.append(num)
    return lst


def happy_test(height, width, window):
    '''
    (int, int, window) -> bool

    This function generates a number for player to choose whether it is happy one or not 
    Then it checks if players choice is correct and returns the result
    '''
    y, x = height//2 - 4, width//2 - 4
    lst = checkhappy()
    lst1 = list(range(101))
    lst1.extend(lst)
    number = random.choice(lst1)
    window.addstr(y, x, 'Is ' + str(number) + ' a happy number?')
    window.refresh()
    if number in lst:
        value = True
    else:
        value = False

    player_value = SMS_buttons.buttons()
    if player_value == value:
        window.addstr(y, x, 'Correct. Press any key                ')
        window.refresh()
        window.getkey()
        window.addstr(y, x, '                                     ')
        return True
    else:
        window.addstr(y, x, 'Wrong. Press any key                    ')
        window.refresh()
        window.getkey()
        window.addstr(y, x, '                                     ')
        return False
