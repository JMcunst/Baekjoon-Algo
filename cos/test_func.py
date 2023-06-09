import itertools
import string
from collections import deque 
import math

tmp = string.digits+string.ascii_lowercase

def convert(num, base):
	print('NUM:',num, ' BASE:',base)
	q, r = divmod(num, base)
	if q == 0:
		return tmp[r]
	else:
		return convert(q,base) + tmp[r]

def convert2(num, base):
	q, r = divmod(num, base)
	if q == 0:
		return tmp[r]
	else:
		return convert2(q, base) + tmp[r]

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

# func_a(120, 33)

s1 = 'ff'
# print(convert(1410,16))




def find(parent, nd):
	if nd == parent[nd]:
		return nd
	parent[nd] = find(parent, parent[nd])
	return parent[nd]

def merge(parent, nd, nf):
	nd = find(parent, nd)
	nf = find(parent,nf)
	if nd == nf:
		return True
	parent[nd] = nf
	return False

def sol(n, connection):
	parent = [i for i in range(n+1)]
	for i, connection in enumerate(connection):
		if merge(parent, connection[0], connection[1]):
			answer = i + 1
			break
	return answer
	


parent = [i for i in range(10+1)]
# print(parent)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

def bfs(n, arr2):
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if arr2[nx][ny] == 0:
					arr2[nx][ny] = arr2[x][y] + 1
					queue.append([nx, ny])


print(math.gcd(21, 14, 7, 3))