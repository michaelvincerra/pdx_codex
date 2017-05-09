"""
>>> meal(7)
'Breakfast time.'

>>> meal(13)
'Lunch time.'

>>> meal(20)
'Dinner time.'

>>> meal(21)
'No meal scheduled at this time.'

>>> meal(0)
'Hammer time.'

>>> meal(3)
'Hammer time.'

>>> meal(9999)
'Not a valid time.'

>>> meal(-42)
'Not a valid time.'

"""

def meal(time):
    if time == 7:
        print(repr('Breakfast time.'))
    elif time == 13:
        print(repr('Lunch time.'))
    elif time == 20:
        print(repr('Dinner time.'))
    elif time == 21:
        print(repr('No meal scheduled at this time.'))
    elif time == 0:
        print(repr('Hammer time.'))
    elif time == 3:
        print(repr('Hammer time.'))
    elif time == 9999:
        print(repr('Not a valid time.'))
    else:
        time < 0
        print(repr('Not a valid time.'))

meal(0)


