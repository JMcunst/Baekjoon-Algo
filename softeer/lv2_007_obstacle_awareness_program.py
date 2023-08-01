import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    cnt = 1

    while q:
        r,c = q.popleft()

        for i in range(4):
            dr = r + dy[i] 
            dc = c + dx[i]

            if (0 <= dr < N and 0 <= dc < N) and graph[dr][dc] == 1 and not visited[dr][dc]:
                q.append([dr,dc])
                visited[dr][dc] = True
                cnt += 1

    return cnt


N = int(input())


graph = [list(map(int,input())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
result.sort()

for i in result:
    print(i)