"""

#  Leave the line below alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

"""

def apply_to_all(data: list, n: int):    #

    result = []    # List building pattern to use for iterating over items

    for item in data:    # TODO: Write a listcomp of this function. [item for item in data if item != 0]
  
        product = item * n

        if product != 0:
            result.append(product)

    return result



apply_to_all([6, 5, 0, 3], 4)  # the first param is a LIST of ints; the second param is an int.
