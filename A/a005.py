a, b, n = map(int, input().split())
pins = list(map(int, input().replace('G', '0').split()))
score = []
i = 0
while i < n-1:
    pin_sum = pins[i] + pins[i+1]
    if pins[i] == b:
        if i == n-3:
            score.append(pin_sum + pins[i+2] + pins[i+1] + pins[i+2])
        else:
            score.append(pin_sum + pins[i+2])
        i -= 1
    elif pin_sum == b:
        if i == n-3:
            score.append(pin_sum + 2 * pins[i+2])
        else:
            score.append(pin_sum + pins[i+2])
    else:
        score.append(pin_sum)
    i += 2
print(score)
print(sum(score))