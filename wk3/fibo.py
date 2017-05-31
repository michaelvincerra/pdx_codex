"""

>>> fibo(10)
[1, 1, 2, 3, 5, 8]

>>> fibo(20)
[1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[1, 1, 2, 3, 5, 8, 13, 21]


use a while sequence 
"""


def fibo(num: int):
    result = list()
    a, b = 0, 1
    while b < num:
        result.append(b)
        a, b = b, a + b
    print(result)


fibo(0)








# def fibo(num: int):
#     result = list()
#     a, b = 0, 1
#     while b < 10:
#         result.append(b)
#         a, b = b, a+b
#     print(result)
# fibo(0)
#
#
# def fibo(num: int):
#     result = list()
#     a, b = 0, 1
#     while b < 20:
#         result.append(b)
#         a, b = b, a+b
#     print(result)
# fibo(0)




