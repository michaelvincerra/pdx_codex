"""

>>> combine(7, 4)
11
>>> combine(42)
42
  
>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney", "Massimiliano")
'Massimiliano'

# >>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle", "Massimiliano" )
# 'Massimiliano'
# 
# >>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""

def combine(num1=0, num2=0):    # sets the defaults
    return num1 + num2
    # print('{}'.format(sum(combine)))
    # print('{}'.format(combine))

def combine_many(*args):    # *args creates a 'tuple' called args. That is callable as: return sum(args) below
    return sum(args)

#
# def return_len(word):
#    return len(word)
#
# max(word, key=return_len)

def helper(word):
    return len(word)


def choose_longest(*args):
    return max(args, key=helper)



