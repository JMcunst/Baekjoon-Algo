# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(hour, minute):

	answer = 30*hour-5.5*minute # 공식: 30*(시침)-5.5*(분침)

	return "{:.1f}".format(answer)

hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")