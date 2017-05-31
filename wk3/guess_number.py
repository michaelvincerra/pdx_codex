
""" 
1. Display a welcome screen to the user.
1. The Computer chooses a random number between 1 and 2 billion.
1. After the computer chooses a number, the human attempts to guess the computer's secret number in as few guesses as possible. The human:

    - Guessses a number
    - The computer will respond with a message 'too high!' or 'too low!'
    - Repeat until the human guesses the exact number correctly.


1. score is kept like golf: lower is better!import random
"""

import random

answer = random.randint(1000000000, 2000000000)
# print(answer)

def guesser():

    welcome_display()

    guess = int(input('Guess the number:>> '))

    if guess < answer:
        print("Try higher")
        guesser()
    elif guess > answer:
        print("Try lower")
        guesser()
    else:
        guess == answer
        print('You win!!!')


def welcome_display():
        message = f'''  
                Welcome to 'Guess the Number', the only binary 
                search game in the multiverse you cannot trick.
                Guess the number between 1000000000 and 2000000000. 
                Enter the number you think the computer holds. 
                Keep trying until you find the answer. 
                '''

        print(message)

guesser()