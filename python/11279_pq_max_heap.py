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
        heapq.heappush(heap,[-num,num])  # -num 은 우선순위, num은 원소값