# With enumerate() we have a good way to loop over the characters in a string, while keeping track of indexes.

words = ['Zero', 'One', 'Two']

# Enumerate over a string.This is a good way to get indexes and chars from a string.
print('Built-in function enumerate() creates an index and its value')

for index, value in enumerate(words):
    print(f'Index: {index}, value: {value}')
print()
print('Alternately..')
for index, value in enumerate(words):
    print(index, value)
# Output

#
# 0 o
# 1 n
# 2 e