M=1000000
P=1500000

N = int(input())

def fibo3(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b%M, (a+b)%M
        print(a, b)
    return a

print(fibo3(N%P))