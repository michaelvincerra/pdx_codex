"""
>>> func("required argument")
required argument

>>> func("required argument", 1, 2, '3')
required argument
(1, 2, '3')

>>> func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")
required argument
(1, 2, '3')
{'keyword2': 'foo', 'keyword1': 4}

"""

def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        print(args)

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.
        print(kwargs)

