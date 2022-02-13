from sys import stdin

dx=[-1,0,1,0] # 좌 우 위 아래
dy=[0,1,0,-1] # 좌 우 위 아래
var_cnt = 0

var_N = int(stdin.readline())
matrix = [list(stdin.readline()) for _ in range(var_N)]
apt=[]

def dfs(x,y):
    global var_cnt
    matrix[x][y] = '0' #방문한 곳은 0으로
    var_cnt += 1
    for i in range(4):
        nx = x + dx[i] #i=0 좌 , i=1 상, i=2 우 , i=3 하
        ny = y + dy[i]
        if nx < 0 or nx >= var_N or ny < 0 or ny >=var_N: # 단지 범위 초과
            continue
        if matrix[nx][ny] == '1': # 인접한 단지 있다면, 
            dfs(nx,ny)

for i in range(var_N):
    for j in range(var_N):
        if matrix[i][j] == '1': # 아파트가 있다면, 
            var_cnt= 0 # 모임 아파트 개수
            dfs(i,j)
            apt.append(var_cnt)

print(len(apt)) # 3
apt.sort() # 7 8 9 
for i in apt:
    print(i)