"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]


Write a function to return a list of integers indicating the index of each letter occourance in a given test string.


--------------------

##### Instructions

Use a _list building pattern_ to gather each letters location.
use the full parametric syntax of `str.index()`.

# cast a string as an integer 

"""


# def locate(target, word):
#
#     results = list()
#
#     for i in word:    # i is the STORED VALUE at that index
#
#         if str(i) == word.index(target):  # item.index(0)
#             results.append(i)
#         return results

def locate(target, word):

    results = list()                # Method: Build an empty list
    index = 0                       # GET the INDEX in scope; create a counter
    for char in word:               # 'char' is loop variable--is empty at first: char is an assignment that accepts input in future
        if char == target:          # if the 'char' == target: whatever that
            results.append(index)   #
        index += 1
    return results




    # results = list()
    #
    # for index, char in enumerate(word):   # two items imply: for index in word; and for char in word
    #      if char == target:               # this is the same as: a, b = 1, 2.
    #         results.append(index)
    # return results




        # print(results)

# locate(yada, yoda)

# def locate(target, word):
#
#     for index,char in enumerate(word):
#         if char == target:
#             return index
