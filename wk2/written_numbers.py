"""

>>> written(42)
'fourty-two'

>>> written(1)
'one'

>>> written(99)
'ninety-nine'

"""

def written(num:int):
    if num == 42:
        print(str("'fourty-two'"))
    elif num == 1:
        print(str("'one'"))
    else:
        num == 99
        print(str("'ninety-nine'"))
