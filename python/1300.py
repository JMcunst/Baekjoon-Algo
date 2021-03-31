from sys import stdin

var_N = int(stdin.readline())
var_k = int(stdin.readline())

def count_value(mid, N):       #해당 mid값의 번째를 count하는 함수
    temp_count = 0

    for x in range(1, N+1):                # key algorithm
       temp_count += min(N, mid//x)
    
    return temp_count

def binary_k(var_N, var_k):
    high, low = var_k, 1

    while low <= high:
        mid = (high + low)//2

        count = count_value(mid, var_N)

        if count < var_k:
            low = mid + 1
        elif count >= var_k:
            rtn = mid
            high = mid - 1 

    return rtn

print(binary_k(var_N,var_k))