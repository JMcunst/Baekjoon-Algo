prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0]*len(prices)
    print(answer)
    stack = []

    for i, price in enumerate(prices):
        #stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer

solution(prices)