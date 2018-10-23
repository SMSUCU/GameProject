def test_all():
    import buttons5
    import random
    import parni
    import happy
    import ulam
    i = random.randint(1, 4)
    if i == 1:
        a = random.randint(1, 100)
        if parni.perevirka(a) == True:
            value = 1
    elif i == 2:
        a, bools == happy.happy_test()
        if bools == True:
            value = 2

    elif ulamfunc() == True:
        value = 3
    else:
        value = None
    print(a)
    print('What kind of number is', a, '?')
    return value == buttons5.buttons()

    if player_value == value:
        print('Correct')
    else:
        print('Wrong')
test_all()
