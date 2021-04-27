from sys import stdin
from collections import deque
import pprint

dx=[-1,0,1,0] # 좌 우 
dy=[0,1,0,-1] # 위 아래

def bfs():
    queue.append([0, 0, 0])
    mat_visit[0][0][0] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < var_N and 0 <= ny < var_M:
                if mat_before[nx][ny] == 0 and mat_visit[nx][ny][z] == -1:  # 좌우위아래 길이고, 방문한적이 없다면,
                    mat_visit[nx][ny][z] = mat_visit[x][y][z] + 1
                    queue.append([nx, ny, z])
                    #print(queue)
                elif z == 0 and mat_before[nx][ny] == 1 and mat_visit[nx][ny][z+1] == -1: # z==0:뚫은적이 없고, 좌우위아래벽이고, 방문한적이 없다면,
                    mat_visit[nx][ny][z+1] = mat_visit[x][y][z] + 1
                    queue.append([nx, ny, z+1])
                    #print(queue)

var_N,var_M = map(int, stdin.readline().split())
mat_before = [list(map(int, input())) for _ in range(var_N)]
#mat_before = [list(map(int, stdin.readline().split())) for _ in range(var_N)]   -> why?
mat_visit = [[[-1]*2 for _ in range(var_M)] for _ in range(var_N)]
queue = deque()
#pprint.pprint(mat_visit)
bfs()
print(mat_visit[0][2][0], mat_visit[0][2][1])
#pprint.pprint(mat_visit)
var_rtn_1, var_rtn_2 = mat_visit[var_N-1][var_M-1][0], mat_visit[var_N-1][var_M-1][1]
if var_rtn_1 == -1 and var_rtn_2 != -1:
    print(var_rtn_2)
elif var_rtn_1 != -1 and var_rtn_2 == -1:
    print(var_rtn_1)
else:
    print(min(var_rtn_1, var_rtn_2))