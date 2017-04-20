flowers = ['Flytrap', 'Orchid', 'Rose', 'Daisy']
smells = ['Carion', 'Awful', 'Sweet', 'Lavender']

for flower in flowers:
    print(flower)

# increment by one '1'
for i in range(0, len(flowers), 1):
    print(flowers[i], smells[i])


result = enumerate(smells)
# You have a list and you want to give each thing a nyumber? use enumerate
# Enumerate: Give each element in a single list a number, key

print(list(result))

a, b = 1, 2

(a, b, c, d) = (1, 2, True, None)

print(a, b, c, d)



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

#counter/ increment

def countingflowers():
    counter = 0
    while counter < len(flowers):
        print (flowers[counter], smells[counter])
        counter += 1
print (countingflowers)






