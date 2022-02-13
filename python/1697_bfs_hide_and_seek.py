from sys import stdin
from collections import deque

def bfs(queue):
    while(queue):
        var_x, var_sec = queue[0][0], queue[0][1]
        if var_x == var_K:
            break
        queue.popleft()                             # deque 왼쪽 값 읽고 삭제
        visit[var_x] = 1                            # 해당 x 값 방문 인증
        if var_x - 1 >= 0 and visit[var_x - 1] == 0:        # 해당 x 값의 좌측, -1
            queue.append([var_x - 1, var_sec + 1])
            #print(queue)
        if var_x + 1 <= 100000 and visit[var_x + 1] == 0:   # 해당 x 값의 우측, +1
            queue.append([var_x + 1, var_sec + 1])
            #print(queue)
        if var_x * 2 <= 100000 and visit[var_x * 2] == 0:   # 해당 x 값의 우측, *2
            queue.append([var_x * 2, var_sec + 1])
            #print(queue)

var_N,var_K = map(int, stdin.readline().split())
visit = [0 for i in range(100001)]

queue = deque()
queue.append([var_N, 0])

bfs(queue)

print(queue[0][1])