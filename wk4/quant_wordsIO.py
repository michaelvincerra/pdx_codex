import re



def get_data(path):

    with open(path, 'r') as file:       # Context returns a file object; it can be a
        text = file.read()              # .read is a file method that returns the text object as a string.
        return text


def cleaner(raw: str) -> str:
    """
     Clean the list phrase so it's all lower case.

     >>> cleaner('test, llama.')
     'test llama'

    :param raw: str
    :return: str
    """
    small_txt = raw.lower()
    cleanest = re.sub(r"[.,']", '', small_txt)

    return cleanest


def quantify_words(path):
    phrase = get_data(path)

    cleaned = cleaner(phrase)          # Returns the value of the function called.
    split_ups = cleaned.split()

    word_count = dict()                 # Build an empty dict.
    for word in split_ups:              # For loop var in split_ups, loop:
        if word in word_count:          # If loop var occurs ...
            word_count[word] += 1
        else:
            word_count[word] = 1        # alternate: word_count.update({word: 1})
            continue

    for key, count in sorted(word_count.items()):  # items()  creates a list of tuples
        print(key, count)

path = '/Users/michaelevan/temp/pdx_code/PythonFullStack/1_Python/3_Applied_Python/labs/ari/books/jack_and_jill.txt'
quantify_words(path)


