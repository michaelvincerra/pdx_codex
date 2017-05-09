"""
Save your solution as `practice/wall-painting.py`.

All our friends are re-painting one wall of their rooms.
They want us to figure out how much it's going to cost.
Assume one gallon of paint covers 400 square feet.

Ask the user for:

1. Width of the wall
1. Height of the wall
1. How much a gallon of paint costs

Figure out then print how much it will cost to paint the wall with one coat.
"""

one_gall = 400          # 400 square feet

def wall_painting():

    width = int(input('Enter width of wall>> '))
    height = int(input('Enter height of wall>> '))
    cost = int(input('Enter cost of gallon of paint>> '))

    sqft_area = width * height    # if one_gall = 400, then
    coverage = sqft_area / one_gall
    calc = round(cost * coverage)

    if coverage < one_gall:
        print(f'To paint a wall of {sqft_area} square feet, it will cost {cost} dollars.')
    else:
        print(f'To paint a wall of {sqft_area} square feet, it will cost {calc} dollars.')


wall_painting()
