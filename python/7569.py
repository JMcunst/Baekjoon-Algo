from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        x, y, z = queue.popleft()
        visit[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 주변이 익지 않았고 방문하지 않았다면,
            if 0 <= nx < var_N and 0 <= ny < var_M and 0 <= nz < var_H and matrix[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:
                queue.append([nx, ny, nz]) # 큐에 넣고 ( 다음 while문에서 돌리기 위해)
                matrix[nz][nx][ny] = matrix[z][x][y] + 1 # 현재 값 + 1 을 인접칸의 값으로 한다.
                visit[nz][nx][ny] = 1

var_M, var_N, var_H = map(int, stdin.readline().split())
matrix = [[] for i in range(var_H)]
visit = [[[0 for i in range(var_M)] for i in range(var_N)] for i in range(var_H)]

for i in range(var_H):
    for j in range(var_N):
        matrix[i].append(list(map(int, stdin.readline().split())))

queue = deque()
for z in range(var_H):
    for x in range(var_N):
        for y in range(var_M):
            if matrix[z][x][y] == 1:
                queue.append([x, y, z])

bfs()

var_rtn = 0
bool_cant = False
for z in range(var_H):
    for x in range(var_N):
        for y in range(var_M):
            if matrix[z][x][y] == 0:
                bool_cant = True
            var_rtn = max(var_rtn, matrix[z][x][y])
if bool_cant == True:
    print(-1)
else:
    print(var_rtn - 1)