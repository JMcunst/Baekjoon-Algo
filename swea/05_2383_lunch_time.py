#------------answer1-------------#
# T = int(input())+1
# for tc in range(1,T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for i in range(N)]

#     queue = []
#     e = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 queue.append([i, j])
#             if arr[i][j] > 1:
#                 e.append([i, j, arr[i][j]])
#     D = []

#     for j in queue:
#         a = []
#         for i in e:
#             dis = abs(i[0] - j[0]) + abs(i[1] - j[1]) + 1
#             a.append(dis + i[2])
#         print('AA::',a)
#         D.append(a)
#     print('DDD::',D)
#     res = []
#     r1 = 0
#     r2 = 0
#     m_i = 0
#     for i in D:
#         if i[0] < i[1]:
#             r1 += 1
#             res.append([i[0], 1, m_i])
#         else:
#             r2 += 1
#             res.append([i[1], 2, m_i])
#         m_i += 1
#     res.sort()
#     print('RES::',res)
#     for i in res:
#         if r1 > 3:
#             i[0] = min(i[0] + e[0][2], D[i[2]][1])
#             r1 -= 1
#         if r2 > 3:
#             i[0] = min(i[0] + e[1][2], D[i[2]][0])
#             r2 -= 1
#     r = 0
#     for i in res:
#         r = max(i[0], r)
#     print("#{} {}".format(tc,r))
#------------------answer2---------------------#
from itertools import combinations
from collections import deque

# 두 그룹으로 나누어 내려가는 시간 계산
def go_for_lunch(people, stairs):
    print('GO_FOR_LUNCH')
    # 계단까지 도착하는 시간
    s = []

    for person in people:
        s.append(abs(person[0]-stairs[0]) + abs(person[1]-stairs[1]))
    
    s = deque(sorted(s))

    # 계단을 내려가서 도착할 시간
    e = deque()

    time = 0
    curr = 0

    while s:
        time += 1

        # 이동을 완료했을 경우
        while e and e[0] == time:
            e.popleft()
            curr -= 1

        while s[0] < time:
            print('s[0]:', s[0], ', time:', time)
            # 계단 이동
            if curr < 3:
                s.popleft()
                if not s:
                    time += grid[stairs[0]][stairs[1]]
                    break

                e.append(time+grid[stairs[0]][stairs[1]])
                curr += 1
            else:
                break
        
    return time


T = int(input())

for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                people.append((i, j))
            elif grid[i][j] >= 2:
                stairs.append((i, j))
    # print('PEOPLE:',people)
    # print('COMBI:', list(combinations(people, N)))
    total = float('inf')
    for n in range(N):
        for people1 in combinations(people, n):
            # print('PEOPLE1:', people1)
            people2 = list(set(people) - set(people1))
            # print('PEOPLE2:', people2)
            time = max(go_for_lunch(people1, stairs[0]), go_for_lunch(people2, stairs[1]))
            total = min(total, time)
    
    print('#{} {}'.format(t, total))