def solution(n):
    answer = 0
    ori = 0
    for i in range(n):
        # 오른쪽 위 꼭지점 양 옆 변 부분과 왼쪽 아래 꼭지점 양 옆 변 부분을 반복하며
        # 점점 중간으로 나아가는 for 문입니다.
        start, end = ori + 1, ori + 2 * (n - i) - 1  # hit
        print('i::', i, 'ori::', ori, 'start::', start, 'end::', end)
        if i % 2 == 0:
            # 대각선 성분이 존재하는 곳은 i가 0, 2, 4, ...로 짝수일 때 입니다.
            if end < n ** 2: 
                answer = answer + start + end
            elif start == end: 
                answer = answer + start
        ori = end
        # 오른쪽 위와 왼쪽 아래 꼭지점이 바뀔 때마다 시작지점인 ori를 업데이트합니다.
    return answer

n1 = 4
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")