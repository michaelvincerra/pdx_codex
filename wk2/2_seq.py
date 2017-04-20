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


Given two lists, return one list, with all of the items of the first list, and the second list.
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


temp/pdx_code/PythonFullStack/1_Python/2_Functional_Iteration/labs/list_practice/list_practice.py
 list_paractice
"""



def smoosh(bob, rob, reverse=False):
    result = bob + rob
    if reverse:
        result.reverse()
    return result






# compare first element of the two lists inside the tuple
# return true of the first two items that are equal

def compare_first_element(snip, snap):

    if snip[0] == snap[0]:
        return True
    else:
        return False

def compare_second_letter(zoo, zed):

    if zoo[1][0].casefold() == zed[1][0].casefold():    # casefold... sets it to case agnostic
        return True
    else:
        return False












# SOLUTION 3
# we use something as an variable that may modified later
# NOTE: A variable, result, must be created and then be recast as a 'list'
# 'list' reversed(something) casts the argument as a list so that it can be reversed.
def backwards(something):
     result = list(reversed(something))
     return result


# SOLUTION 2
# def backwards(something):
#    reverse_something = something[::-1]    # Alien Smiley - Four eyes


#SOLUTION 1
# def backwards(something):
#     something.reverse()
#     return something


def maximus(something):

    result = list()    # Create an empty list and build it.

    largest_num = max(something)    # Create a variable, and find the max value of the list something
    check_dig = str(largest_num)[0]    # Check_dig will cast largest digit as string, subscript it to first item 0.

    for item in something:   # Loop over the original parameter
        if check_dig in str(item):   # If the check_dig (largest_num) is in the item, cast as a string
            result.append(largest_num)    # append the list result with the largest_num
        else:
            result.append(item)    # else append by replacing the modified list, result, by replacing with original item
    return result


# item.startswith(largest_num):
# result.append(largest_num)

    #result = something.replace(largest_num)
        #something(:)
        #change other integers in something to
        #if i in something = str(largest_num)





# cast it into a string

