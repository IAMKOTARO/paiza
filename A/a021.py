def is_independent_point(table, x, y):
    if table[x+1][y+1] == '.'
        and table[x-1][y-1] == '.'
        and table[x+1][y-1] == '.'
        and table[x-1][y+1] == '.':
        return True
    else:
        return False


H, W = map(int, input().split())
table = []
flag_table = []
for i in range(H):
    line = list(input())
    table.append(line)
    flag_table.append([False for j in range(len(line))])
area = 0
around_length = 0
for i in range(H):
    for j in range(W):
        if table[i][j] == '#':
            if not is_independent_point(table, i, j):
                area += 1
                
        elif table[i][j] == '.':

            flag_table[i][j] = True