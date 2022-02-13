from sys import stdin

n, k = map(int, stdin.readline().split())
m = []
num = 0

for i in range(n):
    m.append(int(stdin.readline()))

for i in range(n - 1, -1, -1): #range(시작,종료,얼만큼)
    if k == 0:
        break
                        # 4200//50000 4200//10000 4200//5000 4200//1000 200//500 200//100 
    num += k // m[i]    #    0           0           0          4          4         6
    k %= m[i]           #    4200        4200        4200       200        200       0

print(num)