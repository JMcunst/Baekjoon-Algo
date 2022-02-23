# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def get_prime(n): # very very special
    primes = [2]
    for i in range (3, n + 1, 2) :
        is_prime = True
        for j in range(2, i) :
            if i % j == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(i)
    return primes

def solution(a, b):
    answer = 0

    primes = get_prime(b)

    #제곱
    for i in primes:
        now = pow(i, 2)
        if a < now < b:
            answer += 1
    #세제곱
    for i in primes:
        now = pow(i, 3)
        if a < now < b:
            answer += 1

    return answer

a =  6
b =  30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")