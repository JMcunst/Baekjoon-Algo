from sys import stdin
from heapq import heappush, heappop
INF = 1e7

def dijkstra(var_start):
    list_shortest_dist[var_start] = 0
    heappush(heap, [0, var_start])
    while heap:                                                                                 # [[0, 1]]
        pre_w, vtx_v = heappop(heap)                                                            # [[2, 2], [3, 3]]
        for now_v, vtx_w in mat_table[vtx_v]:  #해당 vtx_v에 연결된 vertex들의 정보 꺼내옴        # [[3, 3], [7, 4]]
            now_w = vtx_w + pre_w                                                               # [[7, 4]]
            if now_w < list_shortest_dist[now_v]:
                list_shortest_dist[now_v] = now_w
                heappush(heap, [now_w, now_v])

var_V,var_E = map(int, stdin.readline().split())
var_start = int(stdin.readline())
mat_table = [[] for i in range(var_V+1)]     # [[], [], [], []] => [[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]
list_shortest_dist = [INF] * (var_V + 1) # [10000000.0, 10000000.0, 10000000.0, 10000000.0, 10000000.0, 10000000.0]
heap = []

for _ in range(var_E):
    var_u,var_v,var_w = map(int, stdin.readline().split())
    mat_table[var_u].append([var_v,var_w])

dijkstra(var_start)

for i in list_shortest_dist[1:]:
    print(i if i != INF else "INF")