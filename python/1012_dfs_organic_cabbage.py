import sys
from sys import stdin
sys.setrecursionlimit(10000)

dx=[-1,0,1,0] # 좌  우 
dy=[0,1,0,-1] #   상  하

def dfs(x,y):
    field[x][y] = 0 # 방문한 배추는 0
    for i in range(4):
        nx = x + dx[i] #i=0 좌 , i=1 상, i=2 우 , i=3 하
        ny = y + dy[i]
        
        if (0 <= nx < var_y) and (0 <= ny < var_x):
            if field[nx][ny] == 1:
                dfs(nx, ny)

var_test_case = int(stdin.readline())
for _ in range(var_test_case):
    # 가로길이, 세로길이, 배추 개수
    var_x, var_y, var_cabbage = map(int, stdin.readline().split())
    # field = [[0]*var_x]*var_y # 연산자로 2차원 배열 초기화 (틀렸습니다)
    field = [[0]*var_x for _ in range(var_y)]
    var_cnt = 0

    # 배추 심기
    for _ in range(var_cabbage):
        ty,tx = map(int, stdin.readline().split())
        field[tx][ty] = 1
    # 벌레 수 정하기
    for i in range(var_y):
        for j in range(var_x):
            if field[i][j] > 0 :
                dfs(i,j)
                var_cnt += 1
    print(var_cnt)
