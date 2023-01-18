# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 4차 1번

words = []

def create_words(lev, s):
	print('LEV:',lev,'S:',s,'WORDS:',words)
	# global words
	# VOWELS = ['A', 'E', 'I', 'O', 'U']
	VOWELS = ['A', 'E', 'I']
	words.append(s)
	for i in range(0, 3):
		if lev < 3:
			create_words(lev+1, s + VOWELS[i])

def solution(word):
	global words
	words = []
	answer = 0
	create_words(0, '')
	for idx, i in enumerate(words):
		if word == i:
			answer = idx
			break
	return answer

word1 = "AAAAE"
ret1 = solution(word1)

print("solution 함수의 반환 값은", ret1, "입니다.")

# word2 = "AAAE"
# ret2 = solution(word2)

# print("solution 함수의 반환 값은", ret2, "입니다.")