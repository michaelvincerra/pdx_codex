## Enumerates creates a list of tuples

words = ['complete', 'absolute', 'positive']

def enumerator(words: str) -> str:
    result = list()
    for index, word in enumerate(words):
        result.append(word + 'ly')
    print(result)

enumerator(words)