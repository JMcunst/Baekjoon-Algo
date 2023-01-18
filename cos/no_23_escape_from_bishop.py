# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 3차 3번

def solution(bishops):
	answer = 0
	
	dxy = [[1,1],[1,-1],[-1,1],[-1,-1]]
	
	field = [[0] * 8 for _ in range(8)]
	
	for bis in bishops:
		x = ord(bis[0])-65
		y = int(bis[1])-1
		field[x][y] = 1
		
		for dx, dy in dxy: # 4번 간다.
			nx , ny = x, y

			while True:
				nx += dx
				ny += dy
				if nx >=8 or nx < 0 or ny >=8 or ny <0:
					break
				if field[nx][ny] == 0:
					field[nx][ny] = 1
				
	for i in range(8):
		for j in range(8):
			if not field[i][j]:
				answer += 1
	return answer

bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")