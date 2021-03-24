import math

N, M = map(int, input().split())
a = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    s, e = map(int, input().split())
    sum = 0.0
    for j in range(s-1, e):
        sum += a[j]
    avg = sum/(e-s+1)
    if avg < M:
        for j in range(s-1, e):
            a[j] += math.ceil(M-avg)
print(' '.join([str(s) for s in a]))