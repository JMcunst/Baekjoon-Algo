from sys import stdin
from heapq import heappush, heappop
INF = 1e7

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])  # 시작 노드 최단 경로 0
    shortest_weight = [INF for i in range(point_count + 1)]  # 최단거리 값, 무한으로 초기화
    shortest_weight[start] = 0
    while heap:
        pre_weight, now_node = heappop(heap)
        for now_edge, now_weight in list_s[now_node]:
            weight = pre_weight + now_weight
            if shortest_weight[now_edge] > weight:
                shortest_weight[now_edge] = weight
                heappush(heap, [weight, now_edge])
    return shortest_weight

testcase_count = int(stdin.readline())

for _ in range(testcase_count):
    point_count, load_count, candidate_count = map(int, stdin.readline().split()) # n:교차로, m:도로, t:목적지후보
    var_start, point_one, point_two = map(int, stdin.readline().split()) # s:예술가출발, g:지점1 h:지점2
    list_s = [[] for i in range(point_count + 1)]
    list_dest = []
    for _ in range(load_count):
        from_a, to_b, load_weight = map(int, stdin.readline().split()) # a와 b사이에 길이 d의 양방향 도로
        list_s[from_a].append([to_b, load_weight])
        list_s[to_b].append([from_a, load_weight])
    for _ in range(candidate_count):
        list_dest.append(int(stdin.readline())) # t개의 목적지 후보들, 서로 다른 위치며, 모두 s가 아니다.
    start_ = dijkstra(var_start)
    point_one_ = dijkstra(point_one)
    point_two_ = dijkstra(point_two)

    results = []
    for l in list_dest:
        if start_[point_one] + point_one_[point_two] + point_two_[l] == start_[l] or start_[point_two] + point_two_[point_one] + point_one_[l] == start_[l]:
            results.append(l)
    results.sort()
    for f in results:
        print(f, end=' ')
    print()