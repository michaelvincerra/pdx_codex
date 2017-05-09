"""
>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

Problem: Show that two strings contain the same letters, in whatever order they appear
         Remove the spaces if present. 
"""
import string


# wrd2 = string.ascii_lowercase()





def anagram(wrd1, wrd2):

    wrd1 = sorted(wrd1.replace('.', '').replace(' ', '').casefold())  #

    wrd2 = sorted(wrd2.replace('.', '').replace(' ', '').casefold())

    if wrd1 == wrd2:
        return True
    else:
        return False

    anagram(wrd1, wrd2)





#def palindrome(word):
#     word = str(word)    # data cleaning
#     hux = word.replace(',', '').casefold().replace(' ', '')    # data cleaning
#
#     if hux == hux[::-1]:    # place the variable above , as a second method use this: rev = hux[::-1]
#         return True
#     else:
#         return False
#
# palindrome('hux')