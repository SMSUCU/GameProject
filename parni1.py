def parni():
    import random

    a = random.randint(1, 4)
    b = random.randint(1, 4)
    print(a, b)

    def perevirka(a):
        if a % 2 != 0:
            return False
        else:
            return True

    def suma(a, b):
        if (a+b) % 2 == 0:
            return True
        else:
            return False
    return(perevirka(a), suma(a, b))
