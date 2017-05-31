words = ['complete', 'absolute', 'positive']

def enumerator(data: str) -> str:
    result = list()
    for index, word in enumerate(words):
        result.append(word +'ly')
    print(result)

enumerator('word')