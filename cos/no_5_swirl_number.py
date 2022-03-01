def solution(n):
    answer = 0
    ori = 0
    for i in range(n):
        start, end = ori + 1, ori + 2 * (n - i) - 1  # hit
        print('i::', i, 'ori::', ori, 'start::', start, 'end::', end)
        if i % 2 == 0:
            if end < n ** 2: 
                answer = answer + start + end
            elif start == end: 
                answer = answer + start
        ori = end
    return answer

n1 = 4
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")