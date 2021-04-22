from sys import stdin
from collections import deque

def bfs(queue):
    while(queue):
        var_x, var_dept = queue[0][0], queue[0][1]
        if var_x == var_K:
            break
        queue.popleft()
        visit[var_x] = 1
        if var_x - 1 >= 0 and visit[var_x - 1] == 0:
            queue.append([var_x - 1, var_dept + 1])
        if var_x + 1 <= 100000 and visit[var_x + 1] == 0:
            queue.append([var_x + 1, var_dept + 1])
        if var_x * 2 <= 100000 and visit[var_x * 2] == 0:
            queue.append([var_x * 2, var_dept + 1])

var_N,var_K = map(int, stdin.readline().split())
visit = [0 for i in range(100001)]

queue = deque()
queue.append([var_N, 0])

bfs(queue)

print(queue[0][1])