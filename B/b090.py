N, K = map(int, input().split())
parties = []
for i in range(N):
    parties.append(int(input()))
giseki_count = [0]*len(parties)
paties_temp = parties.copy()
for i in range(K):
    max_value = max(paties_temp)
    max_index = paties_temp.index(max_value)
    giseki_count[max_index] += 1
    paties_temp[max_index] = int(parties[max_index]/(giseki_count[max_index]+1))
for s in giseki_count:
    print(s)
