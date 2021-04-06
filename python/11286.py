import heapq
from sys import stdin

var_N = int(stdin.readline())
heap = []

for _ in range(var_N):
    num = int(stdin.readline())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])   # heap 인덱스 1번, 젤 앞의 원소
        else:
            print("0")
    else:
        heapq.heappush(heap,(abs(num), num))  # abs(num)을 보고 heap을 정렬하므로, 정렬은 절댓값으로, 원래값은 그대로 들어가고.