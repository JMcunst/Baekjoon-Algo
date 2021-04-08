from sys import stdin

n, k = map(int, stdin.readline().split())
m = []
num = 0

for i in range(n):
    m.append(int(stdin.readline()))

for i in range(n - 1, -1, -1): #range(시작,종료,얼만큼)
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]

print(num)