#--------------answer 1 백트래킹+최대힙 ---------------#
import heapq

T = int(input())


def dfs(field, sums, target):
    global maxNum, buff
    if sum(sums) > C:
        if maxNum < target - (sums[-1] ** 2):
            maxNum = target - (sums[-1] ** 2)
        return
    for i in range(len(field)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(field, sums + [field[i]], target + (field[i] ** 2))
            visited[i] = 0


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    for r in range(N):
        for c in range(N - M + 1):
            maxNum = 0
            if sum(arr[r][c:c + M]) <= C:#모든벌통의 꿀을 채취할 수 있는 경우
                for s in arr[r][c:c + M]:
                    maxNum += s ** 2
            else:  # C 미만의 벌통을 선택해야하는 경우
                visited = [0] * M
                dfs(arr[r][c:c + M], [], 0)
            heapq.heappush(heap, (-maxNum, r, c))  # 최대힙
    answer = []
    while heap:
        num, row, col = heapq.heappop(heap)
        if len(answer) == 2: break
        if len(answer) == 1 and answer[0][1] == row:
            if abs(answer[0][2] - col) <= M - 1:#두 일꾼의 벌통이 겹치는 경우
                continue
        answer.append((num, row, col))
    print(f'#{tc} {-answer[0][0] - answer[1][0]}')
#--------------answer 2 DFS 2번---------------------#
# T = int(input())
# def solve2(idx, a, summ, result):
#     if summ > c:
#         return
#     if idx == len(a) and summ <= c:
#         alst.append(result)
#         return
#     solve2(idx+1, a, summ+a[idx], result+a[idx]**2)
#     solve2(idx+1, a, summ, result)

# def solve(c1, c2):
#     arr1 = []
#     arr2 = []
#     money = 0
#     global alst
#     for j in range(m):
#         arr1.append(board[c1[0]][c1[1]+j])
#         arr2.append(board[c2[0]][c2[1]+j])
#     if sum(arr1) > c:
#         alst = []
#         solve2(0, arr1, 0, 0)
#         money += (max(alst))
#     else:
#         for a in arr1:
#             money += (a*a)

#     if sum(arr2) > c:
#         alst = []
#         solve2(0, arr2, 0, 0)
#         money += (max(alst))
#     else:
#         for a in arr2:
#             money += (a * a)
#     return money

# def combination(lst, num):
#     result = []
#     if num > len(lst):
#         return result
#     if num == 1:
#         for l in lst:
#             result.append([l])
#     elif num > 1:
#         for i in range(len(lst)-num+1):
#             for temp in combination(lst[i+1:], num-1):
#                 result.append([lst[i]]+temp)
#     return result

# for test_case in range(1, T+1):
#     n, m, c = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     c_lst = []
#     for i in range(n):
#         for j in range(n):
#             if j+(m-1) > n-1:
#                 break
#             c_lst.append([i, j])
#     answer = -1

#     for com in list(combination(c_lst, 2)):
#         if com[0][0] == com[1][0] and abs(com[0][1]-com[1][1]) < m:
#             continue
#         answer = max(answer, solve(com[0], com[1]))
#     print(f'#{test_case} {answer}')
# #-----------------answer 3 ------------------------#
# def comb(num, starting):
#     global max_get_honey, selected_honey_idxs

#     if num == 0:
#         amount = 0
#         value = 0
#         for j in range(len(selected_honey_idxs)):
#             amount += candidate_honey[selected_honey_idxs[j]]
#             value += candidate_honey[selected_honey_idxs[j]]**2
#         if amount <= C and max_get_honey < value:
#             max_get_honey = value
#     else:
#         for i in range(starting, M):
#             selected_honey_idxs[num-1] = i
#             comb(num-1, i+1)

# T = int(input())

# for tc in range(1, T+1):
#     N, M, C = map(int, input().split())
#     honey_map = [list(map(int, input().split())) for _ in range(N)]

#     total_value = 0
#     for r1 in range(N):
#         for c1 in range(N):
#             # 영역을 벗어나는 경우
#             if c1+M-1 >= N:
#                 continue
#             else:
#                 # 뭐가 최적인지 모르니 완전탐색을 해야함
#                 max_get_honey = 0
#                 candidate_honey = honey_map[r1][c1:c1+M]
#                 for i1 in range(1, M+1):
#                     selected_honey_idxs = [0] * i1
#                     comb(i1, 0)
#                 tmp_value1 = max_get_honey

#                 for r2 in range(r1, N):
#                     c2_starting = 0
#                     if r1 == r2:
#                         c2_starting = c1+M

#                     for c2 in range(c2_starting, N):
#                         if c2+M-1 >= N:
#                             continue
#                         else:
#                             max_get_honey = 0
#                             candidate_honey = honey_map[r2][c2:c2+M]
#                             for i2 in range(1, M+1):
#                                 selected_honey_idxs = [0] * i2
#                                 comb(i2, 0)
#                             tmp_value2 = max_get_honey

#                             if total_value < tmp_value1 + tmp_value2:
#                                 total_value = tmp_value1 + tmp_value2

#     print(f'#{tc} {total_value}')
#---------------------answer 4 실행시간 최소--------------------#
def cal(temp):
    ret=0
    for i in range(1,1<<m):
        tsum=0
        ttsum=0
        for j in range(0,m):
            if i&(1<<j):
                tsum+=temp[j]
                ttsum+=temp[j]**2
        if tsum<=c and ret<ttsum:
            ret=ttsum
    return ret

for t in range(1,int(input())+1):
    n,m,c=list(map(int, input().split()))
    b=[[*map(int,input().split())]for _ in'a'*n]

    d=[]
    for i in b:
        for j in range(n-m+1):
            d.append(cal(i[j:j+m]))
        for j in range(n-m+1,n):
            d.append(0)

    ans=0
    for i in range(len(d)-m):
        for j in range(i+m,len(d)):
            ans=max(ans,d[i]+d[j])
    print("#%i"%t,ans)