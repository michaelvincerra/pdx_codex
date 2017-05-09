import random as rd

"""
- Event Loops
- User I/O
- Random Module
Print a welcome screen to the user.
1. use the random module's `random.choice()` to choose a prediction (or with your own clever logic).
1. Display the result of the 8 ball.
1. Ask the user if they want to play agian.
1. Say Goodbye on exit.
"""


def scelta():    # start() and start() are co-routines

    bizarro = rd.choice(['You shall be honored', 'Yes, indeed', 'Perhaps', 'Sometimes', 'If you apply yourself',
                         'Only on Tuesdays', 'Absolutely', 'Do birds fly?', 'Didn\'t your mother tell you?',
                         'Emperor Mao agrees', 'Let is be', 'Absolutely!', 'When you\'re wise',
                         'The President wills it so', 'On Mars only', 'After or before you die?',
                         'Wiser you should be!'])

    while True:
        scelta1 = input('Type your question. >>  ')

        if scelta1 != "":
            print(bizarro)
            return bizarro
        else:
            exit()


def start():
    yes_choices = ('Yes', 'Y', 'y')
    # no_choices = ['No', 'N']

    print('Welcome to the Magic 8 Ball')
    print('Where your future is our business')

    start_ans = input('Are you ready to begin? Y >>  ')

    if start_ans.casefold() in yes_choices:
        scelta()
    else:
        exit()

    answer = input('Do you want to play again? >>  ')

    if answer in yes_choices:
        start()
    else:
        exit()


start()
