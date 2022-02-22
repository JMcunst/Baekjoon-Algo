# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

var_N = 8
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def solution(pos):
    answer = 0
    start_row = int(pos[1])
    start_col = ord(pos[0])-65

    for i in range(var_N):
        now_row = start_row + dx[i]
        now_col = start_col + dy[i]

        if now_row in range(0,9) and now_col in range(0,9):
            answer += 1

    return answer

pos = 'A7'
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")
