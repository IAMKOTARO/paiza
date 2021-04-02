import itertools
import collections


def calc_my_points(my_number:int, other_numbers:list) -> int:
    other_numbers_collection = collections.Counter(other_numbers)
    if other_numbers_collection[my_number] > 0:
        return 0
    else:
        point = 0
        for k, v in other_numbers_collection.items():
            if v == 1 and k > my_number:
                return 0
            point += k * v
        point += my_number
        return point
            

N, M = map(int, input().split())
input_lines = []
for i in range(N):
    input_lines.append(tuple(map(int, input().split())))
my_cards = list(itertools.permutations(range(1, M+1)))
max_my_point = 0
for cards in my_cards:
    my_point = 0
    for i in range(M):
        others = []
        for line in input_lines:
            others.append(line[i])
        my_point += calc_my_points(my_number=cards[i], other_numbers=others)
    if my_point > max_my_point:
        max_my_point = my_point
print(max_my_point)
