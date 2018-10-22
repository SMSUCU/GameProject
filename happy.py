def happy_test(height, width, window):
    import random
    import buttons
    # lst = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44,
    #        49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109,
    #        129, 130, 133, 139, 167, 176, 188, 190, 192, 193]

    def checkhappy(rnge):
        '''
        int -> list
        This function checks if a number is a happy one or a sad and adds it to a list

        >>> checkhappy(201)
        [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193]

        '''
        lst = []
        for num in range(1, rnge + 1):
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

    y, x = height//2 - 4, width//2 - 4
    lst = checkhappy(201)
    lst1 = list(range(201))
    lst1.extend(lst)
    number = random.choice(lst1)
    window.addstr(y, x, 'Is ' + str(number) + ' a happy number?')
    window.refresh()
    if number in lst:
        value = True
    else:
        value = False

    player_value = buttons.buttons()
    if player_value == value:
        window.addstr(y, x, 'Correct. Press any key                ')
        window.refresh()
        window.getkey()
        return number, True
    else:
        window.addstr(y, x, 'Wrong. Press any key                    ')
        window.refresh()
        window.getkey()
        return number, False
