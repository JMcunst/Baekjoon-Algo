from sys import stdin

dx=[-1,0,1,0] # 좌 우 위 아래
dy=[0,1,0,-1] # 좌 우 위 아래

var_N,var_M = map(int, stdin.readline().split())
matrix = [list(stdin.readline()) for _ in range(var_N)]

queue = [[0, 0]]
matrix[0][0] = 1

def bfs(queue):
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < var_N and 0 <= ny < var_M and matrix[nx][ny] == "1":
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1

bfs(queue)
# 1 0 9 10 11 12
# 2 0 8 0  12 0
# 3 0 7 0  13 14
# 4 5 6 0  14 15

print(matrix[var_N - 1][var_M - 1])