"""
>>> which_case('this_test_text')
'snake_case.'

>>> which_case('this_is_snake_case')
'snake_case.'

>>> which_case('ThisIsCamelCase')
'CamelCase.'


"""

def which_case(words):
    print('Python uses two types of naming for variables and files.')
    print('ThisIsCamelCase')
    print('this_is_snake_case')
    print('Snake or camel? Which case are you?')

    words = str(input('Enter a file name using one of the above conventions: >> '))
    # words.replace(' ', '')

    for word in words:
        if '_' in words:
            print('That\'s snake_case. So_slithery_smooth!')
        elif word.istitle() and ' ' not in words:
            print('That\'s CamelCase. GoOnASafari!')            # elif user_inp.title() in user_inp:
        else:
            print('That\'s neither. Thanks for playing. Ciao!')
        break
which_case('Words_Are')
