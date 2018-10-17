import curses


def start(window):
    window.addstr('''Our game was made to teach you some math.
    Don't worry you wont be bored... at least to much)
    To start press any key''')
    window.getkey()
    window.clear()
    window.addstr('''Firstly, Happy Numbers
    A happy number is defined by the following process: Starting with any positive integer,
    replace the number by the sum of the square of its digits in base-ten,
    and repeat the process until the number either equals 1 (where it will stay),
    or it loops endlessly in a cycle that does not include 1.
    Those numbers for which this process ends in 1 are happy numbers,
    while those that do not end in 1 are unhappy numbers (or sad numbers).

    For example, 19 is happy, as the associated sequence is:

    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1

    The first few terms are
    1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109,
    129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262,
    263, 280, 291, 293, 301...

    ''')
    window.getkey()
    window.clear()
    window.addstr('''Secondly, Ulam Numbers
    The standard Ulam sequence (the (1, 2)-Ulam sequence) starts with U1 = 1 and U2 = 2.
    Then for n > 2, Un is defined to be the smallest integer that is the sum
    of two distinct earlier terms in exactly one way and larger than all earlier terms.
    As a consequence of the definition, 3 is an Ulam number (1+2); and 4 is an Ulam number (1+3).
    Here 2+2 is not a second representation of 4, because the previous terms must be distinct.
    The integer 5 is not an Ulam number, because 5 = 1 + 4 = 2 + 3.

    The first few terms are
    1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97,
    99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219,
    221, 236, 238, 241, 243, 253, 258, 260, 273, 282...
    ''')
    window.getkey()
    window.clear()
    window.addstr('''And the last one, Even Numbers
    An even number is an integer which is "evenly divisible" by two. This means that if the integer is divided by 2,
    it yields no remainder.''')
    window.getkey()
    window.clear()
    window.addstr('''Let's start our game)
    You can move with arrows or WASD. Go ahead to your goal. To exit press 'Q'
    Good luck)''')
    window.getkey()
    window.clear()
    window.addstr('''Oh wise hero, since your early childhood your dream was to become a member of order.
    And now you are close to your dream. Only five test in Labirintum stands between you and becoming part of order.
    Now you are ready to make last step to your goal...''')
    window.getkey()
    window.clear()
