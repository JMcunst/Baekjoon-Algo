# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import itertools

def solution(arr, K):
	answer = 10001
	list_a = list(itertools.combinations(arr, 4))
	
	for nums in list_a:
		list_nums = list(set(nums))
		max_n, min_n = max(list_nums), min(list_nums)
		rtn = max_n - min_n
		if rtn < answer:
			answer = rtn
	return answer

arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")