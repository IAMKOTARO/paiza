n, T = input().split()
T = list(T)
S = input()

output = ''
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for s in S:
    if s == ' ':
        output += ' '
    else:
        decorded_char = s
        for i in range(int(n)):
            decorded_char = alphabets[T.index(decorded_char)]
        output += decorded_char
print(output)
