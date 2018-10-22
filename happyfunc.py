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
