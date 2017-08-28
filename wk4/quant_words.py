"""
Write a function that quanitifies word occourances in a given string.

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
a 2
black 1
can 1
fellow 1
friend 1
is 1
jack 1
kill 1
of 1
red 2
touching 2
yellow 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a (European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european) 1
11 1
24 1
a 1  
about 1
airspeed 1
concluded 1
end 1
hour 1
in 1
is 1
it's 1
meters 1
miles 1
of 1
or 1
per 2
second 1
swallow 1
that 1
the 2
unladen 1
velocity 1
"""
import re



def cleaner(raw: str) -> str:
    """
     Clean the list phrase so it's all lower case.
     
     >>> cleaner('test, llama.')
     'test llama'
    
    :param raw: str
    :return: str 
    """
    small_txt = raw.lower()
    cleanest = re.sub(r"[.,']",'', small_txt)

    return cleanest


def quantify_words(phrase):

    cleaned = cleaner(phrase)       # Returns the value of the function called.
    split_ups = cleaned.split()

    word_count = dict()             # Build an empty dict.

    for word in split_ups:          # For loop var in split_ups, loop:
        if word in word_count:      # If loop var occurs ...
            word_count[word] += 1
        else:
            word_count[word] = 1    # alternate: word_count.update({word: 1})
            continue
                                    # ord() use to order the word_count

    for key, count in sorted(word_count.items()):    # items()  creates a list of tuple
        print(key,count)

        # return result


