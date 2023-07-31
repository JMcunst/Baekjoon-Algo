import sys

N, M = list(map(int, input().split()))

standard_list = [0] * 101

now = 1

for _ in range(N):
    sec, sec_val = list(map(int, input().split()))
    for i in range(now, now+sec):
        standard_list[i] = sec_val

    now = now+sec
    
now = 1
for _ in range(M):
    sec, sec_val = list(map(int, input().split()))
    for i in range(now, now+sec):
        standard_list[i] = sec_val - standard_list[i]

    now = now+sec

print(max(standard_list))