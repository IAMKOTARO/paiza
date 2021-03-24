N, M = map(int, input().split())
s = []
w = []
ans = []
for i in range(N):
    s.append(list(input()))
for i in range(M):
    w.append(input())
for word in w:
    for i, line in enumerate(s):
        if word[0] in line:
            index = [line.index(word[0])+1, i+1]
            flg = True
            # print(f'{word} -> {index}')
            for j, chr in enumerate(word[1:]):
                x = index[0]+j
                y = index[1]+j
                # print(f'{x} {y} {chr} {s[y][x]} {chr==s[y][x]}')
                if s[y][x] != chr:
                    break
            if flg:
                # print(f'{word} is {index}')
                ans.append(index)
                break
for a in ans:
    print(f'{a[0]} {a[1]}')
