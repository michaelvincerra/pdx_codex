"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""


# ZIP: Combine two lists whose length is EQUAL
# Goal: I need to loop over multiple iterables
#Prob: How can I get the index in scope (of current iteration)??


# COMMENT
#
#
def display_indexes(a):
    for index, item in enumerate(a):
        print(item, index)


# COMMENT
# i and item share the same index; therefore,
#result = list(zip(a, b))
# enumerates a list with each thing having a number; generates a list of tuples
#

def parallel(a, b):
    for i, item in enumerate(a):
        print(item, b[i])




# COMMENT
#
#

def leper():
    for i in range(0, len(a), 1):
        print(b[i], a[i], sep='\n')


""""- LESSON EX -----

flowers = ['Flytrap', 'Orchid', 'Rose', 'Daisy']
smells = ['Carion', 'Awful', 'Sweet', 'Lavender']

for index, element in enumerate(flowers):
    print(index, element)



for x in enumerate(flowers):
    print(x)

list(zip(smells, flowers))
print(list)


for smell, flower in zip(smells, flower):
    print(smell, flower)

"""
