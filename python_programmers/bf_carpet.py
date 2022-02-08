brown = 10
yellow = 2

def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    print(total)
    for b in range(1,total+1):
        print('b::', b)
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            print('total::',total, 'b::',b, 'a::', a)
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
                    print([int(a),b])
                    return [int(a),b]
            
    print(answer)
    return answer

solution(brown, yellow)