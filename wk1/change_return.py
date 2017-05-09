"""
>>> make_change(94)
3 quarters
1 dimes
1 nickles
4 pennies

>>> make_change(75)
3 quarters

>>> make_change(42)
1 quarters
1 dimes
1 nickles
2 pennies



Some supermarkets have automatic change dispensers.

*   Ask for the amount of change to dispense _in cents_.
    Assume that the amount input will be less than 100 cents.

*   Calculate the number of quarters necessary first.

*   Then calculate the number of dimes, nickels, and pennies.
    If you do it in that order, you will minimize the number of coins.

This is easiest done by updating a _running total_ of number of cents left to be put into coins.

Also remember that the `//` operator divides and removes any remainder.


x  = sum of the remainder of the division. Or: x = 100 // 25. x = 4

The % (modulo) operator yields the remainder from the division of the first argument by the second argument. 

quarters  = 94 // 3
 q => 3

rem = 94 - (q * 25)

dimes = rem // 10

rem = rem - (dimes * 10)

etc. 

"""


def make_change():

    cents = int(input('Enter the amount of change to be dispensed:>>  '))
    rem = cents
    # print(cents)

    while rem < 100:

        quarters = round(cents // 25)
        print(quarters, 'quarters')
        rem = rem - quarters * 25

        dimes = round(rem // 10)
        print(dimes, 'dimes')
        rem = rem - dimes * 10

        nickels = round(rem // 5)
        print(nickels, 'nickels')
        rem = rem - nickels * 5

        print(rem, 'pennies')
        break


make_change()


#     dimes =
#
#
#
#
# def make_change(cents: int):
#
#     cents = int(input('Enter the amount of change to be dispensed:>>  '))
#
#     rem = [0]
#
#     if cents // 25:
#         rem = round(cents / 25)
#         print(rem, 'quarters')
#     if rem // 10:
#         rem = round(rem / 10)
#         print(rem, 'dimes')
#     if rem // 5:
#         rem = round(rem / 5)
#         print(rem, 'nickels')
#     if rem < 5:
#         print(rem, 'pennies')

#     rem1 = round(cents // 25)
#     print(rem1, 'quarters')
#
#     rem2 = round(rem1 // 10)
#     print(rem2, 'dimes')
#
#     rem3 = round(rem2 % 5)
#     print(rem3, 'nickels')
#
#     rem4 = round(rem3 < 5)
#     print(rem4, 'pennies')
#
# make_change(0)


# def make_change(cents: int):
#     quarters = int(cents // 25)
#     print(quarters)
#     dimes = int(cents % 25 // 10)  # the remainder after the quarters are taken out
#     # print(dimes)
#     nickels = int(cents % 25 % 10 // 5)
#     # print(nickels)
#     pennies = int(cents % 5)
#     # print(pennies)
#
    # rem = int(0)
#
#     while rem < 100:

#
#
#
#
#     else:
#         pass
#     if cents % 25 // 10:
#         print(str(dimes) + ' dimes')
#     else:
#         pass
#     if cents % 25 % 10 // 5:
#         print(str(nickels) + ' nickels')
#     else:
#         pass
#     if pennies % 5:
#         print(str(pennies) + ' pennies')
#     else:
#         pass
#
#
# make_change(0)
#
#
# #
#
#     if cents // 25:
#         print(str(quarters)+' quarters')
#     else:
#         pass
#     if cents % 25 // 10:
#         print(str(dimes)+' dimes')
#     else:
#         pass
#     if cents % 25 % 10 // 5:
#         print(str(nickels)+' nickels')
#     else:
#         pass
#     if pennies % 5:
#         print(str(pennies)+' pennies')
#     else:
#         pass
#
# make_change(0)
