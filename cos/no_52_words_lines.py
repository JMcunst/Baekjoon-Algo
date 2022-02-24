# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(K, words):
	answer = 1
	rest_len = K
	is_first = True
	for word in words:
		if is_first:
			length = len(word)
		else:
			length = len(word) + 1
			
		if 0<= rest_len - length <= K:
			rest_len -= length
			is_first = False
		else:
			answer += 1
			rest_len = K-length
			is_first = True
	
	return answer

K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")