"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(names, 5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with(names, 'S')    # here the 'S' is hardcoded; below you can set a variable.
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""
def long_names(names, abba):
    result = [name for name in names if len(name) > abba]    # names is a list
    return result


def starts_with(names, str1):
    result = [name for name in names if name.startswith(str1)]
    return result

def last_names(people):
    result = [peep[1] for peep in people]
    return result


def smoosh(people):
    result = [item for person in people for item in person]
            # output  #assign   #
    return result





    result= enumerate(people)

    result2 = [peep for peep in result1]

    return result2



# #     [thing  for thing in people if thing startswith.... ]
