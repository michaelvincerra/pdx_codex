"""
>>> together('knights', 'camelot')
k c
n a
i m
g e
h l
t o
s t

1. Use the zip() function!

1. Use the `range()` function!

1. Use the `enumerate()` function!

1. Use an Incrementing pattern `+=` with a `while` loop
"""

# Control flow statements

# to iterate over indices in a sequence, combine range() and len():
# this allows you to use range, only integers, by enclosing len, which returns the 'number' of items in list.
# assign i = list(a) to cast a as a list, or string.
# https://docs.python.org/3/tutorial/controlflow.html
# https://docs.python.org/3/reference/expressions.html #see 6..3.2 Subscriptions:
# "A subscription selects an item of a sequence (string, tuple or list) or mapping (dictionary) object:"
# while the len(a) value is 0-6, or 7 times, it is not shown, so the for loop iterates for 7 times


def together(a,b):
    i = list(a)
    for i in range(len(a)):
        print(a[i], b[i])


# for i, item, these are empty. enumerate x, equivalent to 'knights', thereby assigning it key values (0, 'K', 1, 'n', etc.)
# enumerate unpacks the item in tuple and assigns it key value indices.
# print statement prints the soda iteration of x first; then it prints the yoda iteration of y ; it does so for 7 times, or 0-6.

def together(x, y):
      for yoda, soda in enumerate(x):
          print(soda, y[yoda])


# iterate over zis and zat in the combined pair of x, y
# print zis and zat --on their shared indices
# zip(): Make an iterator that aggregates elements from each of the iterables.

def together(x,y):
    for zis, zat, in zip(x,y):
        print(zis, zat)





# iterate over the list to match the value pairs and then pair the items by index.
# create a counter to iterate over the variable  because def is together(a,b): 1 = 0
# while statement (i is variable set to 0; while True that i < than the length of a,
# print (a[i] ... superscript i.... AND print b[i] ... superscript i: UNTIL the length of a is exhausted
def together(a,b):
     i = 0
     while (i <len(a)):
         print(a[i], b[i])
         i += 1
#         #OR i = i + 1

