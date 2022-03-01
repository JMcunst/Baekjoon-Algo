# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 3차 4번

def solution(s1, s2):
	print(s1[:2:-1])
	print('-------------')
	answer = 0
	
	for i in range(len(s1)):
		print(s1[0:i], '===', s2[-i:])
		if s1[0:i] == s2[-i:]:
			answer = i
			break
			
	for i in range(len(s2)):
		if s2[0:i] == s1[-i:]:
			if answer < i:
				answer = i
				break
	
	return len(s1)+len(s2)-answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")