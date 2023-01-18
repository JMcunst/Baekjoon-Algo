# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import string

tmp = string.digits+string.ascii_lowercase
tmp1 = string.digits
tmp2 = string.digits+string.ascii_lowercase
tmp3 = string.ascii_uppercase
tmp4 = string.ascii_letters

def convert(num, base):
	print('NUM:',num, ' BASE:',base)
	q, r = divmod(num, base)
	print('q:',q,' ,r:',r)
	if q == 0:
		return tmp[r]
	else:
		return convert(q,base) + tmp[r]
	
def solution(s1, s2, p, q):
	print('S1:',int(s1,p), ' S3:',int(s2,p))
	sum_num = int(s1,p) + int(s2,p)
	print('SUM_NUM:',sum_num)
	
	return convert(sum_num, q)

s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")

test = int('1010',2)
print('TEST:',test)