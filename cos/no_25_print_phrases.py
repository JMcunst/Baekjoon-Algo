# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(phrases, second):
	answer = ''
	length = 14

	step = second // length
	loc = second % length
	print(step, loc)
	if step % 2 == 0: # 나타날 때
		if loc == 0:
			answer = '______________'
		else:
			for _ in range(length - loc):
				answer += '_'
			for i in range(loc):
				answer += phrases[i]
		print(answer)
	else: # 사라질 때
		if loc == 0:
			answer = phrases
		else:
			for i in range(length - loc):
				answer += phrases[i+loc]
			for _ in range(loc):
				answer += '_'

	return answer

phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")

phrases = "happy-birthday"
second = 20
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")