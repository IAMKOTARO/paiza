def calc_fares(taxi_data:list, distance:int):
    if taxi_data[0] > distance:
        return taxi_data[1]
    else:
        remaining_distance = distance - taxi_data[0]
        result_fare = taxi_data[1] + taxi_data[3] * int(remaining_distance/taxi_data[2]+1)
        return result_fare


N, X = map(int, input().split())
min_fare = 5000 + 5000*100000 + 1
max_fare = 0
for i in range(N):
    taxi_data = list(map(int, input().split()))
    fare = calc_fares(taxi_data=taxi_data, distance=X)
    if fare > max_fare:
        max_fare = fare
    if fare < min_fare:
        min_fare = fare
print(min_fare, max_fare)
