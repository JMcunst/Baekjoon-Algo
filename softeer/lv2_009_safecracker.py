import sys

W, N = list(map(int, input().split()))

metals = [list(map(int, input().split())) for _ in range(N)]

metals.sort(key=lambda x : x[1], reverse=True)

result = 0 

for mw, mp in metals:
    if W > mw:
        result += mw * mp
        W -= mw
    else:
        result += W * mp
        break

print(result)