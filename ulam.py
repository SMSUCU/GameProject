def ulam():
    import random
    lst = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26,
    28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77,
    82, 87, 97, 99, 102, 106, 114, 126, 131, 138,
    145, 148]
    lst2 = list(range(151))
    lst2.extend(lst)
    a = random.choice(lst2)
    print(a)
    def perevirka(a):
        if a in lst:
            return True
        else:
            return False
    return(perevirka(a))
print(ulam())
