import heapq

## 시간초과 이슈가 있을 수 있으니, import sys, sys.stdin.readline()을 적극 활용할 것
n = int(input())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
        print('SAME LEN LEFT: ', leftHeap, ', SAME LEN RIGHT: ',rightHeap)
    else:
        heapq.heappush(rightHeap, num)
        print('LEFT: ', leftHeap, ', RIGHT: ',rightHeap)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        print('OUT LEFT: ', leftHeap, ', OUT RIGHT: ',rightHeap)
        rightValue = heapq.heappop(rightHeap)
        print('OUT LEFT: ', leftHeap, ', OUT RIGHT: ',rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)
        print('OUT RES LEFT: ', leftHeap, ', OUT RES RIGHT: ',rightHeap)

    print(-leftHeap[0])