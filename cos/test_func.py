import itertools

def func_b(s):
	isnt = True
	# s의 길이
	length = len(s)
	# s의 앞의 절반만큼
	for i in range(length // 2):
		print(s[i], s[length - i - 1])
		if s[i] != s[length - i - 1]:
			# return False
			isnt = False
	return isnt
	

def func_arr(s):
	# print(s[:2:-1])
	# print(s[:2:-1])
	for i in range(len(s)):
		print(s[-i-1::-1])
	# for i in range(len(s1)):
	# 	print(s1[0:i], '===', s2[-i:])
	# 	if s1[0:i] == s2[-i:]:
	# 		answer = i
	# 		break
			
	# for i in range(len(s2)):
	# 	if s2[0:i] == s1[-i:]:
	# 		if answer < i:
	# 			answer = i
	# 			break
	return 'GOOD'

# arr = 'asdfqwer1234'
# print(arr[::-1])
# print(arr[-3:])

arr2 = ['1', '2', '3', '4']
num = list(map(''.join, arr2))
# print(num)

# ad = func_arr(arr)


def func_a(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
		print(a, b, mod)
	print('res:',b)
	return b

func_a(120, 33)