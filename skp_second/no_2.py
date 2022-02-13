deposit = [500, 1000, -300, 200, -400, 100, -100]
deposit2 = [500, 1000, 2000, -1000, -1500, 500]

def solution(deposit):
    stack = []

    for price in deposit:
        if price > 0 :
            stack.append(price)
        elif price < 0:
            total = 0
            need = -1*price
            while need > total:
                now = stack.pop()
                total += now
            if total-need != 0:
                stack.append(total-need)

    print(stack)
    return stack

solution(deposit2)