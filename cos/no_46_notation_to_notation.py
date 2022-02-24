# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import string

tmp = string.digits+string.ascii_lowercase

def convert(num, base):
	q, r = divmod(num, base)
	if q == 0:
		return tmp[r]
	else:
		return convert(q,base) + tmp[r]
	
def solution(s1, s2, p, q):
	sum_num = int(s1,p) + int(s2,p)
	
	return convert(sum_num, q)

s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")