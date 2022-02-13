from sys import stdin
from heapq import heappush, heappop

var_N = int(stdin.readline())  # 1 <= N <= 100000

cards = []

for _ in range(var_N):
    heappush(cards, int(stdin.readline()))

if var_N == 1: 
    print(0)
else:
    rtn_sum = 0
    while len(cards) > 1: 
        min_fst = heappop(cards) 
        min_sec = heappop(cards) 
        rtn_sum += min_fst + min_sec 
        heappush(cards, min_fst + min_sec)
    
    print(rtn_sum)

# 출력 초과
# from sys import stdin

# var_N = int(stdin.readline())  # 1 <= N <= 100000
# cards = []
# rtn_sum = 0

# for _ in range(var_N):
#     cards.append(int(stdin.readline()))

# cards.sort()

# min_sum = cards[0] + cards[1]
# rtn_sum = min_sum

# if var_N == 1:
#     print(0)
# else:
#     for i in range(var_N-2):
#         rtn_sum = rtn_sum*2 + cards[i+2]
#     print(rtn_sum)

# 메모리 초과
# import sys

# var_N = int(sys.stdin.readline())
# cards = []
# for _ in range(var_N):
#     cards.append(int(sys.stdin.readline()))

# cards.sort()

# rtn_sum = 0
# if var_N == 1:
#     print(0)
# else:
#     for i in range(var_N-1):
#         rtn_sum += cards[i] + cards[i+1]
#         cards[i+1] = rtn_sum
#     print(rtn_sum)