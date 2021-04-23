from sys import stdin

dx=[-1,0,1,0] # 좌 우 위 아래
dy=[0,1,0,-1] # 좌 우 위 아래

var_N,var_M = map(int, stdin.readline().split())
matrix = [list(stdin.readline()) for _ in range(var_N)]