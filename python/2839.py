from sys import stdin

var_N = int(stdin.readline())  # 3 <= N <= 5000
rtn_bag = 0

while var_N >= 0:
    if var_N % 5 == 0:
        rtn_bag += var_N // 5
        print(rtn_bag)
        break
    var_N -= 3
    rtn_bag += 1
else:
    print(-1)