from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

matrix = []
queue = deque()





var_M, var_N, var_H = map(int, stdin.readline().split())

for i in range(var_H):
    for j in range(var_N):
        matrix.append(list(map(int, stdin.readline().split())))