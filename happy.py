import random
import buttons
lst = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44,
       49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109,
       129, 130, 133, 139, 167, 176, 188, 190, 192, 193]
lst1 = list(range(201))
lst1.extend(lst)
number = random.choice(lst1)
print('Is', number, 'a happy number?')
if number in lst:
    value = True
else:
    value = False

player_value = buttons.buttons()
if player_value == value:
    print('Correct')
else:
    print('Wrong')

