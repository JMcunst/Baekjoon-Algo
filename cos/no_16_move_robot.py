# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(commands):
	answer = []
	x = 0
	y = 0
	
	list_commands = list(commands)
	
	for i in list_commands:
		if i == 'L':
			x -= 1
		elif i == 'R':
			x += 1
		elif i == 'U':
				y += 1
		else:
				y -= 1
	
	answer.append(x)
	answer.append(y)
	
	return answer

commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")