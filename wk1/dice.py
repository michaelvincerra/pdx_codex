"""
Program should ask the user for the number of dice they want to roll
as well as the number of sides per die.

1. Open Atom
1. Create a new file and save it as `dice.py`
1. Follow along with your instructor
"""


import random

dice = input('How many dice?')
sides = input('How may sides?')
roll = random.randint(1, 6)

def dice():
    for i in range(int(dice)):
        print('Rolling dice.')
print('Roll', roll)


