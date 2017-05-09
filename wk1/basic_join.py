"""
>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'

  - Implement a solution that employs a dictionary
  - Write an additional doctest and execute it
Write a function that convert two input strings into kebab-case sting output.

str.join()`
"""


def link(nonno, nonna):

    # cast items in the list as a string.
    container = [str(nonno), str(nonna)]    # set a variable;  cast two data types as strings

    nonni = '-'.join(container)    # set a new variable to join those two elements with a '-'

    return nonni

# ''.join()
