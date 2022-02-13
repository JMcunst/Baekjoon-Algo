import heapq
from re import S

scovile = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    print(heap)
    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
        print(heap)

    return mix_cnt

solution(scovile, K)