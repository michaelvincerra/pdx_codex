"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

Write two functions `arb` and `stats` that satisfy the requirements of the doctests.

Instructions

Using the `*args` syntax, print back out each argument the function was invoked with.

Use the builtins `sum()`, `min()`, `max()` for the `stats` function.
"""


def arb(*arb):
    print('The {} args are: {}'.format(len(arb), arb))


def stats(*stats):
    print('Sum: {}'.format(sum(stats)))
    print('Max: {}'.format(max(stats)))
    print('Min: {}'.format(min(stats)))
    print('Avg: {}'.format(round(sum(stats) / len(stats))))
    print('Range: {}'.format((max(stats) - min(stats))))  # max - min.
    print('Entries: {}'.format(len(stats)))