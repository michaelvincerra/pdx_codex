"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""


# Write your code here.

def shrink(data: str) -> int:
    result = [int(char) for char in data]
    total = sum(result)

    print(result)


shrink('9')

