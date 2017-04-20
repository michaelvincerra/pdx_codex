"""
>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]

>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]

>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]

Given two `list`s and an `int` (three args), insert the elements of a list into the first list at the nth position.
"""

def punch_in(int1, int2, int3=None):
    pass



def double(int1, int2):

    result = []    # create an empty list

    for i in range(0, len(int1)):  # range(start, stop, [step]); range is an immutable seq type, not a function.
        result.append(int1[i] * int2[i])  # Using subscription, multiply each element together for length of elements
        if 0 in result:  # if 0 found in result
            result.remove(0)  # Remove the 0
            result.append(-1)  # Add the new -1 element in place of 0
    return result


    # for item in result:
    #     if item == 0:
    #         item = -1
    #     return result

    # if result == 0:
    #     result.append(-1)

    # result = int1[:] * int2[:]
    # if item in result == 0:
    #     item.replace(-1)
    # else:
    #     pass
    #
    # return result


def exclude_em(data, target=None):
    # KP: del a[wherever_it_is: wherever...+1]

    if not target:  # If target is None...Delete first two items in the list. (Definition by negation)
        del data[0:2]
    else:
        location = data.index(target)  # Set variable, from data get index where its value equals value of target
        # target is an int, not None.
        del data[location:location + 2]  # From data, delete the target as an index position, plus next two items
    return data
