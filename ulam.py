def ulam_generator(chyslo):
    ''' (int) -> list
    This function returns a list of ulam numbers in sequence (chyslo)
    >>> ulam_generator(30)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138]
    >>> ulam_generator(15)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53]
    '''
    ulam = [1,2]
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
