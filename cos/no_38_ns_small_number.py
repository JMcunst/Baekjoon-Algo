# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import itertools

def solution(card, n):
	answer = -1
	
	card = list(map(str, card))
	print('CARD:',card)
	nums = list(map(''.join, itertools.permutations(card)))
	print('PNUMS:',nums)
	nums = list(set(map(int, nums)))
	print('NUMS:',nums)
	nums.sort()
	print('SORTED:',nums)
	
	for i in range(len(nums)):
		if n == nums[i]:
			answer = i+1
			
	return answer

card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

# card2 = [1, 1, 1, 2]
# n2 = 1122
# ret2 = solution(card2, n2)

# print("solution 함수의 반환 값은", ret2, "입니다.")