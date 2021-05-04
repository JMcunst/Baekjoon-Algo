from sys import stdin
from heapq import heappush, heappop
INF = 1e9

def dijkstra(var_start):
    list_shortest_dist = [INF] * (var_N + 1) # [INF, INF, INF, INF, INF, INF]
    list_shortest_dist[var_start] = 0
    heappush(heap, [0, var_start])
    while heap:                                                                                 
        pre_w, vtx_v = heappop(heap)                                                           
        for now_v, vtx_w in mat_table[vtx_v]:  #해당 vtx_v에 연결된 vertex들의 정보 꺼내옴        
            now_w = vtx_w + pre_w                                                              
            if now_w < list_shortest_dist[now_v]:
                list_shortest_dist[now_v] = now_w
                heappush(heap, [now_w, now_v])
    return list_shortest_dist

var_N,var_E = map(int, stdin.readline().split())    #  [            1         ], [          2           ], [           3          ], [            4         ]   
mat_table = [[] for i in range(var_N+1)]        # [[], [[2, 3], [3, 5], [4, 4]], [[1, 3], [3, 3], [4, 5]], [[2, 3], [4, 1], [1, 5]], [[3, 1], [2, 5], [1, 4]]]
heap = []

for _ in range(var_E):
    var_u,var_v,var_w = map(int, stdin.readline().split())
    mat_table[var_u].append([var_v,var_w])
    mat_table[var_v].append([var_u,var_w])

var_v1, var_v2 = map(int, stdin.readline().split())

ls_start = dijkstra(1)     # [INF, 0, 3, 5, 4]
ls_v1 = dijkstra(var_v1)   # [INF, 3, 0, 3, 4]
ls_v2 = dijkstra(var_v2)   # [INF, 5, 3, 0, 1]

shortest_dist = min(ls_start[var_v1] + ls_v1[var_v2] + ls_v2[var_N], ls_start[var_v2] + ls_v2[var_v1] + ls_v1[var_N])
print(shortest_dist if shortest_dist < INF else -1)