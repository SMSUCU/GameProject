def test_all():
    import random
    import parni
    import happy
    import ulamfunc
    a = random.randint(1, 100)
    if perevirka(a) == True:
        value = 1
    if happy() == True:
        value = 2
    if ulamfunc() == True:
        value = 3
    return value == player_value
