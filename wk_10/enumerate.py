# import random
#
# random_bits = 0
# for i in range(64):
#     if randint(0,1):
#         random_bits |= 1 << i
#
#     print(random_bits)


#
#
#

flavor_list = ['vanilla', 'chocolate', 'strawberry', 'pecan']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

print()
print('Range Used Below')
print()

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))
print()
print('Enumerate Used Below')
print()
#
#


for i, flavor in enumerate(flavor_list):    # for i (index #), and item in the enumerated list (flavor_list), assign #'s
    print('%d: %s' % (i + 1, flavor))

print()
print('Enumerate Used Starting at 1')
print()

for i, flavor in enumerate(flavor_list, 1):    # for i (index #), and item in the enumerated list (flavor_list), assign #'s
    print('%d: %s' % (i + 1, flavor))

# enumerate provides concise syntax for looping over an iterator and getting the index of each item form the iterator as you go.
# Prefer enumerate over range.
#  You can specify a starting number, parameter, to specify number from which to start (0 is default).