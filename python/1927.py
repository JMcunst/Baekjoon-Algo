import heapq
from sys import stdin

var_N = int(stdin.readline())
heap = []

#Max Heap
for _ in range(var_N):
    x = int(stdin.readline())

    if x != 0:                        #heap에 자연수 x값 넣기
        heapq.heappush(heap, x)
    else:                               #x에 0을 넣었을 경우
        if heap:                        #heap이 비어있지 않았다면,
            print(heapq.heappop(heap))   # heap 인덱스 1번, 젤 앞의 원소
        else:
            print(0)