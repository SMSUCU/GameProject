def happy_number():
    import random
    lst = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44,
           49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109,
           129, 130, 133, 139, 167, 176, 188, 190, 192, 193]
    lst1 = list(range(201))
    lst1.extend(lst)
    number = random.choice(lst1)
    print(number)

    def ifhappy(number):
        if number in lst:
            return True
        if number not in lst:
            return False
    return ifhappy(number)
print(happy_number())
