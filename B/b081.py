H, W = map(int, input().split())
table = []
for i in range(H):
    table.append(list(input()))
count = 0
for y in range(H):
    now_block_type = table[y][0]
    if table[y][0] == '#':
        count += 1
    for x in range(W):
        if table[y][x] != now_block_type:
            now_block_type = table[y][x]
            count += 1
        if y == 0:
            if table[y][x] == '#':
                count += 1
                if table[y+1][x] == '.':
                    count += 1
        elif y > 0 and y < H-1:
            if table[y][x] == '#':
                if table[y-1][x] == '.':
                    count += 1
                if table[y+1][x] == '.':
                    count += 1
        elif y == H-1:
            if table[y][x] == '#':
                count += 1
                if table[y-1][x] == '.':
                    count += 1
        if x == W-1:
            if table[y][x] == '#':
                count += 1
print(count)