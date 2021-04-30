from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()





var_M, var_N, var_H = map(int, stdin.readline().split())
matrix = [[] for i in range(var_H)]
isTrue = False
st = False

for i in range(var_H):
    for j in range(var_N):
        matrix[i].append(list(map(int, stdin.readline().split())))


visit = [[[0 for i in range(var_M)] for i in range(var_N)] for i in range(var_H)]

