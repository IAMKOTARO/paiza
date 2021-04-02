M, N, K = map(int, input().split())
input_lines = []
for i in range(K):
    input_lines.append(int(input()))
candidates = [0]*M
voters = N
for a in input_lines:
    now_candidate = a-1
    candidates[a-1] += 1
    for idx, c in enumerate(candidates):
        if c:
            candidates[idx] -= 1
            candidates[a-1] += 1
    voters -= 1
max_indexes = [i+1 for i, v in enumerate(candidates) if v == max(candidates)]
for i in max_indexes:
    print(i)