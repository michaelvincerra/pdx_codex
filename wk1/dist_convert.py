"""
Write a function to convert between `mi`, `km`, `ft`, and `m`.

--------------------
##### Instructions

Ask the user for a distance, then the units of that distance, then the target units.
Then print out the conversion as below.

```
> Enter a distance:
> 100
> Enter units:
> mi
> Enter target units:
> km
> 100 mi is 160.93440000000115 km
```

Support converting between `mi`, `km`, `ft`, and `m`.

"""

print('This is a distance converter >> ')
print('Unit of Measurement is abbreviated: UOM'),

dist = input('Enter a distance>> ')
uom = input('Enter original UOM: ft (feet), mi (miles), km (kilometers, m (meters)>> ').casefold()
targ = input('Enter target UOM: ft (feet), mi (miles), km (kilometers, m (meters)>> ').casefold()


# feet to miles:        5280 ft = 1 mile
# feet to kilometers:   1 ft = 0.0003048 kilometer
# feet to meters        3 ft = 1 m

# km to feet            1 km = 3281 ft
# km to miles           1 km = 0.62 miles
# km to meters          1 km = 1000 m

# meters to feet        1 m = 3.28 ft
# meters to miles       1 m = 0.00062 m
# meters to kilometers  1 m = 0.001 km
# TODO refactor with error catching


def converter():
    if uom == 'ft' and targ == 'mi':
        print(round(int(dist) / 5280), 'mi')

    elif uom == 'ft' and targ == 'km':
        print(round(int(dist) * .000348), 'km')

    elif uom == 'ft' and targ == 'm':
        print(int(dist) * .3048, 'm')


    elif uom == 'km' and targ == 'ft':
        print(round(int(dist) * 3281), 'ft')

    elif uom == 'km' and targ == 'mi':
        print(int(dist) * 0.62, 'mi')

    elif uom == 'km' and targ == 'm':
        print(int(dist) * 1000, 'm')


    elif uom == 'm' and targ == 'ft':
        print(round(int(dist) * 3.28), 'ft')

    elif uom == 'm' and targ == 'mi':
        print(round(int(dist)* 0.00062), 'mi')

    elif uom == 'm' and targ == 'km':
        print(round(int(dist) * 0.001), 'km')


    elif uom == 'mi' and targ == 'ft':
        print(round(int(dist) * 5280), 'ft')

    elif uom == 'mi' and targ == 'm':
        print(int(dist) * 1609, 'm')

    elif uom == 'mi' and targ == 'km':
        print(round(int(dist) * 1.6), 'km')

    else:
        print('Enter a valid UOM. Start over.')

converter()

