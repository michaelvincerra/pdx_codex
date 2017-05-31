"""
>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> spell_out(a)
m
u
s
i
c

>>> spell_out(b)
17
28
42
31
12

>>> first_and_last(b)
17
12

>>> first_and_last(a)
m
c

"""


def spell_out(a):
    for item in a:
        print(item)

def spell_out(b):
    for item in b:
        print(item)

def first_and_last(b):
    for item in b:
        break
    print(b[0], b[-1], sep='\n')

def first_and_last(a):
    for item in a:
        break
    print(a[0], a[-1], sep='\n')

# def leper():
#     for i in range(0, len(a), 1):
#         print(b[i], a[i], sep='\n')

