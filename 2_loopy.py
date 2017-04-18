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

#
#
#

def together(a, b):
     for i, item in enumerate(a):
         print(item, b[i])


# iterate over the list to match the value pairs and then pair the items by index.

# create a counter to iterate over the variable  because def is together(a,b): 1 = 0
# while statement (i is variable set to 0; while True that i < than the length of a,
# print (a[i] ... superscript i.... AND print b[i] ... superscript i: UNTIL the length of a is exhausted
#

def together(a,b):
    i = 0
    while (i <len(a)):
        print(a[i], b[i])
        i += 1
        #OR i = i + 1



"""
def together(a, b):
        result = list(zip(ppl, plc))
        print(result)

while i < len(plc):
pass
"""









"""
def together(a, b):
    for i, item in enumerate(plc):
        list(zip(plc, ppl))

    for i in range(0, len(plc), 1):
        pass

        # range
        # while
"""