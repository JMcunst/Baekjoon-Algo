from sys import stdin

var_N = int(stdin.readline())  # 1 <= N <= 100000
list_rope = []
list_max_w = []

for i in range(var_N):
    list_rope.append(int(stdin.readline()))

list_rope.sort(reverse=True)

for i in range(var_N):
    list_max_w.append(list_rope[i]*(i+1))

print(max(list_max_w))