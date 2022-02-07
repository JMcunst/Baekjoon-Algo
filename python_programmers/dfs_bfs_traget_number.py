from collections import deque

numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    print('orgin queue::',queue)
    while queue:
        print('next queue::',queue)
        temp, idx = queue.popleft()
        print('temp::',temp,'idx::', idx)
        idx += 1
        if idx < len(numbers):
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

solution(numbers, target)