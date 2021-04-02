import numpy as np
from itertools import combinations


def split(array):
    n_group1 = len(array) // 2
    g1 = list(combinations(array, n_group1))
    g2 = [tuple(set(array).difference(x)) for x in g1]
    pairs = set((x, y) if x < y else (y, x) for x, y in zip(g1, g2))
    pairs = list(pairs)
    return pairs


N, K = map(int, input().split())
count = 0
rewards = [a+1 for a in range(2*N)]
for reward_set in split(rewards):
    A_reward, B_reward = reward_set
    A_reward, B_reward = np.array(list(A_reward)), np.array(list(B_reward))
    if sum(np.abs(A_reward-B_reward)) <= K:
        count += 1
print(2 * count)