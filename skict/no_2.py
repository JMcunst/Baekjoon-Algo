# 2번 문제
# 소용돌이수 4개가 시계 방향, 반시계 방향으로 중앙으로 들어감.

import math

def solution(n, clockwise):
    answer = [[1] * n for i in range(n)]

    cnt = math.ceil(n/2)

    num = 1

    for i in range(cnt):
        start, end = i, n-i-1

        if start == end:
            answer[start][end] = num
        else:
            if clockwise:
                # answer[start][] top, right
                val = num
                for i in range(start, end):
                    answer[start][i] = val
                    answer[i][end] = val
                    val += 1
                # answer[end][] bottom, left
                val = num
                for i in range(end,start,-1):
                    answer[end][i] = val
                    answer[i][start] = val
                    val += 1
            else:
                # answer[start][] top, right
                val = num
                for i in range(end,start,-1):
                    answer[start][i] = val
                    answer[i][end] = val
                    val += 1
                # answer[end][] bottom, left
                val = num
                for i in range(start, end):
                    answer[end][i] = val
                    answer[i][start] = val
                    val += 1

            diff = end - start
            num += diff

    return answer