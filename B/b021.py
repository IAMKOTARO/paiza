def to_plural(word:str):
    if word[-1] in ['s', 'o', 'x']:
        return word + 'es'
    elif word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word[-1] == 'f':
        return word[:-1] + 'ves'
    elif word[-2:] == 'fe':
        return word[:-2] + 'ves'
    elif word[-1] == 'y' and word[-2] not in ['a', 'i', 'u', 'e', 'o']:
        return word[:-1] + 'ies'
    else:
        return word + 's'


N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
for word in words:
    plural_word = to_plural(word=word)
    print(plural_word)