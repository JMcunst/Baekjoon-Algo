import sys

N, M = list(map(int, sys.stdin.readline().split()))

places = [[] for _ in range(M)]

for i in range(N):
    tp = sys.stdin.readline().strip()
    for j in range(M):
        if tp[j] != '.' and tp[j] not in places[j]:
            places[j].append(tp[j])
max_l = -1
for pl in places:
    if len(pl) > max_l:
        max_l = len(pl)

print(max_l)