H, W, N = map(int, input().split())
table = []
table.append(['.']*W)
for i in range(H):
    table.append(['.'] + input().split() + ['.'])
table.append(['.']*W)
input_lines = []
for i in range(N):
    input_lines.append(list(map(int, input().split())))
for line in input_lines:
    y1, x1, y2, x2 = line
    if table[y1][x1] == table[y2][x2]:
        if y1 == y2 or x1 == x2:
            print('yes')
        else:
            if (abs(y1-y2)+abs(x1-x2)) == 1:
                print('yes')
            else:
                print('no')
    else:
        print('no')