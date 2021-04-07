import heapq
from sys import stdin

left, right = [],[]
n = int(stdin.readline())

for _ in range(n):
    num = int(stdin.readline())     # 수빈이가 정수를 하나씩 외칠때마다 수빈이가 말한 수 중에서 중간값을 말해야 한다.
    if len(left) == len(right):     # (홀수)중간값 말하기
        heapq.heappush(left,(-num,num))     #left(최대힙)에 정수를 넣는다. 배열 젤 앞에 최댓값이 들어감.
    else:                           # (짝수)중간에 있는 두수 중 작은 수 말하기
        heapq.heappush(right, (num,num))    #right(최소힙)에 정수를 넣는다. 배열 젤 앞에 최솟값이 들어감.

    if right and left[0][1] > right[0][1]:
        var_left = heapq.heappop(left)[1]
        var_right = heapq.heappop(right)[1]
        heapq.heappush(right, (var_left, var_left)) #left max와 right min 비교, left max >? right min과 교체
        heapq.heappush(left, (-var_right, var_right))

    print(left[0][1])

    # left       right       result     heapq total
    #  1                       1         1
    #  1           5           1         1 5 
    #  2 1         5           2         1 2 5
    #  2 1         5 10        2         1 2 5 10
    #  2 1 -99     5 10        2         -99 1 2 5 10
    #  2 1 -99     5 7 10      2         -99 1 2 5 7 10
    #  5 2 1 -99   5 7 10      5         -99 1 2 5 5 7 10