# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(grid):
	print(grid)
	answer = 0
	cnt = 1
	for i in range(4):
		for j in range(4):
			for k in range(j + 1, 4, 2):
				print('--------cnt:',cnt,'-----------')
				print('i:',i, ' j:',j, ' k:',k)
				print('A:',grid[i][j],' B:', grid[j][k], ' C:',grid[i][j], ' D:', grid[k][i])
				answer = max(answer, max(grid[i][j] + grid[j][k], grid[i][j] + grid[k][i]))
				cnt += 1
	return answer

grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)

print("solution 함수의 반환 값은", ret, "입니다.")