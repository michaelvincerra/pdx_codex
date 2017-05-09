"""
>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'



Here are the rules for the FizzBuzz problem:

Given the length of the output of numbers from 1 - n:

If a number is divisible by 3, append "Fizz" to a list.
If a number is divisible by 5, append "Buzz" to that same list.
If a number is divisible by both 3 and 5, append "FizzBuzz" to the list.
If a number meets none of theese rules, just append the string of the number.

Append each value to a list starting with 1, and ending at `n` and return the resulting list.

"""
def joined_buzz(stop):

    results = []    # build an empty list, inside the scope of function

    item = 1    # set a counter

    while item < (stop + 1):

        if item % 15 == 0:
            results.append('FizzBuzz')

        elif item % 5 == 0:
            results.append('Buzz')

        elif item % 3 == 0:
            results.append('Fizz')
        else:
            results.append(str(item))

        item += 1

    return ' '.join(results)



def fizz_buzz(stop):

    results = []    # build an empty list, inside the scope of function

    item = 1    # set a counter

    while item < (stop + 1):

        if item % 15 == 0:
            results.append('FizzBuzz')

        elif item % 5 == 0:
            results.append('Buzz')

        elif item % 3 == 0:
            results.append('Fizz')
        else:
            results.append(str(item))

        item += 1

    return results










#
# def fizz_buzz(stop):
#
#     results = list()                 # Build an empty list, inside the scope of function.
#
#     for item in range(1, stop+1):    # Start, Stop, Step (Non-Inclusive).
#
#         if item % 15 == 0:
#             msg = 'FizzBuzz'
#
#         elif item % 5 == 0:
#             msg = 'Buzz'
#
#         elif item % 3 == 0:
#             msg = 'Fizz'
#
#         else:
#             msg = str(item)
#
#         results.append(msg)
#
#     return results
#
# def fizz_buzz(stop):
#
#     results = list()  # Build an empty list, inside the scope of function.
#
#     for item in range(1, stop + 1):  # Start, Stop, Step (Non-Inclusive).
#
#         msg = str()
#
#         if item % 3 == 0:
#             msg += 'Fizz'
#
#         if item % 5 == 0:
#             msg += 'Buzz'
#
#         else:
#             msg = str(item)
#
#         results.append(msg)
#
#     return results
#



        # fizz_buzz(results)

#
# x =[ 1, 2, 3, 4]
# i = 0
# # while (i is less than the length of x do this:
# while (i < len(x)):
# 	#because the length of x = 4, print must loop 4 times and print each item before exiting
# 	print (x[i])
# 	i = i +1