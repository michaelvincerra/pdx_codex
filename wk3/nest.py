"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest(letters)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""



def denest(letters):



    result = [item for letter in letters for item in letter]

    return result

    denest(letters)

