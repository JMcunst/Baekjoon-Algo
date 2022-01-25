from sys import stdin

var_N = int(stdin.readline())  # 0 <= N < 50
list_a = list(map(int, stdin.readline().split()))
list_b = list(map(int, stdin.readline().split()))

rtn_min = 0

sorted_list_a = sorted(list_a)
sorted_list_b = sorted(list_b, reverse=True)

for i in range(var_N):
    rtn_min += sorted_list_a[i] * sorted_list_b[i]

print(rtn_min)
