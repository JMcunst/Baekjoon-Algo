from sys import stdin
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(var_x,var_y,var_tx,var_ty):
    queue = deque()
    queue.append([var_x,var_y])
    mat_field[var_x][var_y] = 1
    while(queue):
        var_nx, var_ny = queue.popleft()            # deque 왼쪽 값 읽고 삭제
        if var_tx == var_nx and var_ty == var_ny:
            print(mat_field[var_tx][var_ty]-1)
            break
        
        for i in range(8):
            nx = var_nx + dx[i]
            ny = var_ny + dy[i]
            if 0<=nx<var_N and 0<=ny<var_N and mat_field[nx][ny] == 0:
                queue.append([nx,ny])
                mat_field[nx][ny] = mat_field[var_nx][var_ny] + 1

var_T = int(stdin.readline())

for _ in range(var_T):
    var_N = int(stdin.readline())
    var_x,var_y = map(int, stdin.readline().split())
    var_tx,var_ty = map(int, stdin.readline().split())
    mat_field = [[0] * var_N for i in range(var_N)]
    bfs(var_x,var_y,var_tx,var_ty)
    