# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(num):
	answer = num + 1
	digit = 1
	print(answer)
	while answer // digit % 10 == 0:
		tmp = answer // digit
		print('Condition:',tmp, digit)
		answer += digit
		digit *= 10
		print('Middle_Answer:',answer)
	return answer

num = 9949999;
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")