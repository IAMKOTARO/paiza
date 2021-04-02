# def dfs(G, start, Visited=None):
#     if Visited is None:
#         Visited = list()
#     Visited.append(start)
#     print(start, Visited, G[start-1])
#     for u in G[start-1]:
#         if u in Visited:
#             continue    # next for loop
#         dfs(G, u, Visited)


N, M = map(int, input().split())
E = []
for i in range(M):
    E.append(tuple(map(int, input().split())))
V = []
for i in range(N):
    v_temp = []
    for e in E:
        if i+1 in e and e[~e.index(i+1)] not in v_temp:
            v_temp.append(e[~e.index(i+1)])
    V.append(v_temp)
# print(V)
# dfs(G=V, start=1)
for i in range(N):
    # print(V[i], len(V[i]), int(N/2))
    if len(V[i]) < int(N/2):
        print('No')
        enit(0)
print('Yes')