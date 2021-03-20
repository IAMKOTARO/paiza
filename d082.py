N, M = map(int, input().split())
schedule = []
for i in range(N):
    schedule.append(input())

max_days = 0
for i, s1 in enumerate(schedule):
    count = 0
    M_count = M
    for s2 in schedule[i+1:]:
        if s2 == 'off':
            count += 1
        elif M_count <= 0:
            break
        elif s2 == 'work':
            M_count -= 1
            count += 1
    if count > max_days:
        max_days = count
print(max_days)
