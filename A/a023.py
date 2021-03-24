N = int(input())
d = list(map(int, input().split()))
count_max = 0
for i in range(N):
    count = 0
    holiday_count = 0
    workday＿count = 0
    flag = False
    for j in range(i, N):
        if d[j] == 1: # 平日
            workday＿count += 1
        elif d[j] == 0: # 休日
            holiday_count += 1

        if holiday_count >= 2:
            flag = True
            holiday_count = 0
            workday＿count = 0
        if workday＿count + holiday_count < 7:
            count += 1
        else:
            break
    if count > count_max and flag:
        count_max = count
print(count_max)
