# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 2차 5번

def solution(arr):
    answer = 0
    idx = 0

    tmp = [0 for i in range(len(arr)-1)]

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            tmp[idx] += 1
        else:
            idx += 1

    answer = max(tmp)+1

    print(arr)
    print(tmp)
    print(answer)

    if answer < 2:
        return 1
        
    return answer


arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")