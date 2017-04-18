
"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

Return True if the first letter of the second element in each list is equal. (Case Insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


temp/pdx_code/PythonFullStack/1_Python/2_Functional_Iteration/labs/list_practice/list_practice.py
 list_paractice
"""

# SOLUTION 3
# we use something as an variable that may modified later
# NOTE: A variable, result, must be created and then be recast as a 'list'
# 'list' reversed(something) casts the argument as a list so that it can be reversed.
def backwards(something):
    result = list(reversed(something))
    return result


# SOLUTION 2
# def backwards(something):
    reverse_something = something[::-1]    # Alien Smiley - Four eyes


#SOLUTION 1
# def backwards(something):
#     something.reverse()
#     return something


def maximus(something):
    big_num = max(something)
    str(big_num),
# cast it into a string

    if startswith.big_num()