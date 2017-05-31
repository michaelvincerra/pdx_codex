"""

>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!


##### Instructions

1. Slice off the last digit.  That is the **check digit**.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
7. If that matches the check digit, the whole card number is valid.

"""


def validate(account_number):
    check_dig = account_number.pop()
    rev_num = account_number[::-1]

    result = list()                         # build an empty list.
    for index, num in enumerate(rev_num):   # tuple unpacking
        if index % 2 == 0:                  # if index value is 'even', or divisible by 2.
            doubled = num * 2               # double each even value of 'num' as it iterates over list
            if doubled > 9:                 # if doubled value (result) is greater than 9
                doubled = doubled - 9       # take that doubled value and subtract 9
        else:                               # else
            doubled = num                   # append the original number to the result list (leaky loop problem)

        result.append(doubled)              # finally append result, the list, with the doubled after transformations

    # total = sum(result)
    stringy = int(str(sum(result))[1])      # sum the above result, cast as string, at 1th pos., now cast as integer.

    if stringy == check_dig:                # with stringy, as int, and compare w check_dig, if match;
        print('Valid!')                     # print 'Valid!'
    elif stringy != check_dig:              # with stringy, as int, and compare w check_dig, if NO match;
        print('Invalid!')                   # print 'Invalid!'

    # if stringy[1] != check_dig:
    #     print('Invalid!')
    # elif stringy[1] == check_dig:
    #     print('Valid!')

    # index = 0
    # result = list()         # build an empty list.
    # while index < len(rev_num):
    #     num = rev_num[index]
    #     if index % 2 == 0:
    #         doubled = num * 2   # must be assigned a new name so as not to override the loop variable.
    #
    #         if doubled > 9:
    #             doubled = doubled - 9
    #
    #     result.append(doubled)
    #     index += 1
    #


validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])    # validate function by passing integers as params
