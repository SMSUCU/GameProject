<<<<<<< HEAD
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
=======
def sumulam():
    import random
    ulamlist = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26,
        28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77,
        82, 87, 97, 99, 102, 106, 114, 126, 131, 138,
        145, 148]
    summ = random.randint(1, 80), random.randint(1,80)
    sumlist = []
    sumlist.append(summ[0])
    sumlist.append(summ[1])
    print(sumlist)
    if sumlist[0] + sumlist[1] in ulamlist:
        return True
    else:
        return False
print(sumulam())

>>>>>>> a9a5922d586b151657bfa7872cf4d3a0d468aac2
