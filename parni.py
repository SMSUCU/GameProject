def parni():
    import random

    a = random.randint(1, 100000)
    b = random.randint(1, 100000)

    def perevirka(a):
        if (a % 2 == 0):
            return True
        else:
            return False

    def suma(a, b):
        if (a+b) % 2 == 0:
            return True
        else:
            return False

    return perevirka(a), suma(a, b)


print(parni())
