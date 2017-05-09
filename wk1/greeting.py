
def greeting():

    print('Welcome to the Mighty Age Predictor!')

    name = input('Please enter your name>> ')
    age = int(input('How old are you?>> ')) + 1    # cast the input as an int first; order of operations.


    print('Hello {}, next year, you will be: {}'.format(name, int(age)))

greeting()
