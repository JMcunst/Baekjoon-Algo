# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# bfs, 백준 토마토 문제

from collections import deque

dx=[-1,0,1,0] # 좌  우 
dy=[0,1,0,-1] #   상  하

queue = deque()
								
def bfs(n, garden):
	while queue:
		x,y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if garden[nx][ny] == 0:
					garden[nx][ny] = garden[x][y] + 1
					queue.append([nx, ny])

def solution(n, garden):
	var_rtn  = -2
	
	for i in range(n):
		for j in range(n):
			if garden[i][j] == 1:
				queue.append([i,j]) # 익은토마토 좌표 찾아 큐에 넣기

	bfs(n, garden)
	
	for i in garden:
		for j in i:
			var_rtn = max(var_rtn, j)
			
	if var_rtn == -1:
		return 0
	else:
		return var_rtn - 1

n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

print("solution 함수의 반환 값은", ret2, "입니다.")