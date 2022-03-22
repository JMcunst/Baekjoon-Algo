# 구현
# INF = 1000000001

# def solution(n, v):
#     answer = -1
#     mx = v[0]
#     midx = -1
#     for i,val in enumerate(v):
#         if mx < val:
#             mx = val
#             midx = i
    
#     if midx == n-1:
#         return answer
#     else:
#         mn = INF
#         for idx in range(midx+1, n):
#             if mn > v[idx]:
#                 mn = v[idx]

#     return v[midx] - mn

# 시간초과 40점
def solution(n, v):
    bnf = [[-1]*n for _ in range(n)]

    for selidx in range(n):
        for buyidx in range(selidx+1, n):
            bnf[selidx][buyidx] = v[selidx] - v[buyidx]
    return max(map(max, bnf))