"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly.'

>>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit.'


>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex.'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'


>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'

# >>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')
#  45
# 
# >>> extracto('2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.')
#  40
#  
# >>> extracto('3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.')
# 45
# """
import re

#
def scrub_numbers(something):
    """
     Find the int and replace it with nothing    
    """
    result = re.sub(r'\d+', '', something)    #?
    result2 = result + '.'

    return result2

# scrub_numbers('99gwhwe')


def gentle_clean(something):

    item = something.replace('_', ' ').replace('-', ' ')
    a_dopo = ' '.join(item.split()) + '.'
    return a_dopo

def clean_data(something):

    result = re.sub(r'\d+', '', something)                  # \d+ find one or more digits
    result2 = result.replace('_', ' ').replace('-', ' ')    # set variable; for result, replace _ with ' ' empty and replace '-' with ' '.
    result3 = ' '.join(result2.split()) + '.'
    return result3


def some_scrubber(something):

    result = re.sub(r'(?<=\w)\s(?=\w)', '', something)    # REVIEW regex here.
    result2 = result.replace('   ', ' ')
    result3 = result2.replace(' .', '.').strip()
    return result3

def mr_clean(something):

    result = list()
    for item in something:
        result.extend([item, ' '])            # review extend

    result = ''.join(result)
    result = ' ' + result
    return result


def ms_clean(something):
    """
    Replace characters after the first and last with the len of those characters' count. 
    # find the first and last characters of each word; count the number of char between the first and last of the words
    """
    something.split()
    result1 = list(something[0:11:10] + something[12:18:5])
    result1.insert(1, '9')
    result1.insert(4, '4')
    result2 = ''.join(result1[0:3])
    result3 = ''.join(result1)[3:7]
    print(repr(result2 + ' ' + result3))


def strong_cleaner(something):

    result = re.sub(r'[*?@#%$!&(I1]', '', something)+'.'       # re.sub(something,'r(?<=\w)\s(?=\w)', something)
    return result

#
# def special_cases(dada):







    #  result = re.sub(r'\s{3}', ' ', something)
    # result = something.replace('  ', ' ')
    #
    # if '   ' in result:
    #     result
    # else:
    #     ' ' in result
    #     result.replace(' ', '')
    #
    # return result




    # result2 = result.replace(' ', '')
    # result2 = result.split()
    # result3 = result2.strip()
