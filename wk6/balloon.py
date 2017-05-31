'''

>>> inflator([1,5,6,2,6,7], 500)
False

>>> inflator([1,5,6,2,6,7,20,45,20,23], 1500)
False

>>> inflator([1,5,6,2,6,7,20,45,20,23], 10000)
True

>>> inflator([1,5,6,2,6,7], 2000)
True

>>> inflator([1,5,6,2,6,7], 3000)
False

'''





def inflator(sec:list, size: int) -> bool:

    psi = 42
    total = int(sum(sec))

    # for item in sec:
    product = psi * total

    if product > size or product <= size/2:
        return False
    elif product < size:
        return True


# int(sum(my_list[0])
#
inflator([1,5,6,2,6,7], 500)


# def apply_to_all(data: list, n: int):    #
#
#     result = []    # List building pattern to use for iterating over items
#
#     for item in data:    # TODO: Write a listcomp of this function. [item for item in data if item != 0]
#
#         product = item * n
#
#         if product != 0:
#             result.append(product)
#
#     return result
