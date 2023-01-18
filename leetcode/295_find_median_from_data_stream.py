# Input : addNum(num)
# Output : findMedian

# Heap & Priority Queue , smallHeap(MaxHeap) & largeHeap(MinHeap)
import heapq

small = []
large = []

def addNum(num):
    heapq.heappush(small, -1 * num)

    # make sure every num small is <= every num in large
    if (small and large and (-1 * small[0] > large[0])):
        val = -1 * heapq.heappop(small)
        heapq.heappush(large, val)

    # uneven size?
    if len(small) > len(large) + 1:
        val = -1 * heapq.heappop(small)
        heapq.heappush(large, val)
    if len(small) > len(small) + 1:
        val = heapq.heappop(large)
        heapq.heappush(small, -1 * val)


def findMedian():
    if len(small) > len(large): # Odd 
        return small[0]
    if len(large) > len(small):
        return large[0]

    return (-1 * small[0] + large[0]) / 2

addNum(1)
addNum(2)
res = findMedian()
print(res)
addNum(3)
res2 = findMedian()
print(res2)