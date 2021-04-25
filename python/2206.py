from sys import stdin
from collections import deque

dx=[-1,0,1,0] # 좌 우 위 아래
dy=[0,1,0,-1] # 좌 우 위 아래

def bfs():
    q.append([0, 0, 0])
    mat_visit[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < var_N and 0 <= ny < var_M:
                if mat_before[nx][ny] == 0 and mat_visit[nx][ny][z] == -1:
                    mat_visit[nx][ny][z] = mat_visit[x][y][z] + 1
                    q.append([nx, ny, z])
                elif z == 0 and mat_before[nx][ny] == 1 and mat_visit[nx][ny][z+1] == -1:
                    mat_visit[nx][ny][z+1] = mat_visit[x][y][z] + 1
                    q.append([nx, ny, z+1])

var_N,var_M = map(int, stdin.readline().split())
mat_before = [list(map(int, input())) for _ in range(var_N)]
mat_visit = [[[-1]*2 for _ in range(var_M)] for _ in range(var_N)]
q = deque()

bfs()

var_rtn_1, var_rtn_2 = mat_visit[var_N-1][var_M-1][0], mat_visit[var_N-1][var_M-1][1]
if var_rtn_1 == -1 and var_rtn_2 != -1:
    print(var_rtn_2)
elif var_rtn_1 != -1 and var_rtn_2 == -1:
    print(var_rtn_1)
else:
    print(min(var_rtn_1, var_rtn_2))

