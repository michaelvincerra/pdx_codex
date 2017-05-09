"""
Create a program asks for a _single_ English word and translates it to **Pig Latin**.
It prints out the input word and the resulting translation like the example below.

1. If the first letter is a consonant, move it to the end.
1. Add "ay" to the end of that.
1. If the first letter is a vowel, just ad "yay" to the end.

> Word? hat
>
> hat in Pig Latin is athay
>
> Word? apple
>
> apple in Pig Latin is appleyay

"""

def pig_latin(data: str):


    print('Pig Latin Translator now loading...')

    user_inp = str(input('Enter a word>> '))
    word = user_inp.casefold()
    first = word[0]                         # slice identifies what is first char
    vowels = ['a','e','i','o','u']

    if first in vowels:                     #
        print(word + 'yay')
    else:
        print(word[1:] + word[0] + 'ay')    # slice: start at the 1th position of 'word', then add the 0th char + 'ay'


pig_latin('word')