from sys import stdin

var_N = list(input())  # 0 < N <= 10^5
sorted_var_N = sorted(var_N, reverse=True)
sum = 0

for i in sorted_var_N:
    sum += int(i)

if sum %3 != 0 or '0' not in sorted_var_N:
    print(-1)
else:
    print(''.join(sorted_var_N))