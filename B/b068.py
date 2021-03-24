def split_choco(line:list):
    line_len = len(line)
    A_sum = 0
    A_count = 0
    B_sum = 0
    while True:
        if A_sum <= B_sum:
            A_sum += line.pop(0)
            A_count += 1
        else:
            B_sum += line.pop()
        if not line:
            if A_sum == B_sum:
                return 'A'*A_count + 'B'*(line_len-A_count)
            else:
                return 'No'


H, W = map(int, input().split())
lines = []
output = 'Yes\n'
for i in range(H):
    lines.append(list(map(int, input().split())))
for line in lines:
    result = split_choco(line=line)
    if result == 'No':
        print('No')
        exit(0)
    else:
        output += f'{result}\n'
print(output[:-1])
