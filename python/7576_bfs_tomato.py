from sys import stdin
from collections import deque

var_M, var_N = map(int, stdin.readline().split())
matrix = []
queue = deque()
var_rtn  = -2

dx=[-1,0,1,0] # 좌  우 
dy=[0,1,0,-1] #   상  하

for i in range(var_N):
    matrix.append(list(map(int, stdin.readline().split())))

def bfs():
    while queue: # 익은 토마토 만큼
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < var_N and 0 <= ny < var_M and matrix[nx][ny] == 0: # 익지 않은 토마토면
                matrix[nx][ny] = matrix[x][y] + 1   # 익은 토마토로 변경
                queue.append([nx, ny])              # 다음 익은 토마토 좌표
# 익은 토마토 찾기
for i in range(var_N):
    for j in range(var_M):
        if matrix[i][j] == 1:
            queue.append([i, j]) # 익은토마토 좌표 찾아 큐에 넣기

bfs()

bool_cant = False
for i in matrix: # [9,8,7,6,5,4] , [8,7,6,5,4,3], [7,6,5,4,3,2], [6,5,4,3,2,1]
    for j in i:
        if j == 0: # 토마토가 모두 익지 못하는 상황
            bool_cant = True
        var_rtn  = max(var_rtn , j) # 최대값이 1일경우, 모두 익어있음. 

if bool_cant == True: # 전부 익지 못한다면,
    print(-1)
elif var_rtn  == -1:  # 애초에 다 익었다면
    print(0)
else:                 # 다 익기 위해 걸리는 날 수
    print(var_rtn  - 1)
# [9, 8, 7, 6, 5, 4] [0, 0, 0, 0, 0, 0]
# [8, 7, 6, 5, 4, 3] [0, 0, 0, 0, 0, 0]
# [7, 6, 5, 4, 3, 2] [0, 0, 0, 0, 0, 0]
# [6, 5, 4, 3, 2, 1] [0, 0, 0, 0, 0, 1]

# [0, -1, 7, 6, 5, 4] [0, -1, 0, 0, 0, 0]
# [-1, 7, 6, 5, 4, 3] [-1, 0, 0, 0, 0, 0]
# [7,  6, 5, 4, 3, 2] [0,  0, 0, 0, 0, 0]
# [6,  5, 4, 3, 2, 1] [0,  0, 0, 0, 0, 1]

# [1, -1, 7, 6, 5, 4] [1, -1, 0, 0,  0, 0] 
# [2, -1, 6, 5, 4, 3] [0, -1, 0, 0,  0, 0]
# [3,  4, 5, 6,-1, 2] [0,  0, 0, 0, -1, 0]
# [4,  5, 6, 7,-1, 1] [0,  0, 0, 0, -1, 1]

# [-1,  1,  2,  3, 4] [-1, 1, 0,  0, 0]
# [15, -1, -1, -1, 5] [ 0, 1,-1, -1, 0]
# [14, -1, -1, -1, 6] [ 0, 1,-1, -1, 0]
# [13, -1, -1, -1, 7] [ 0, 1,-1, -1, 0]
# [12, 11, 10,  9, 8] [ 0, 0, 0,  0, 0]

# [ 1, -1] [ 1, -1]
# [-1,  1] [-1,  1]