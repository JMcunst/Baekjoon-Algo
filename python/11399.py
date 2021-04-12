from sys import stdin

var_N = int(stdin.readline())
list_waiting_time = list(map(int, stdin.readline().split()))
# [3, 1, 4, 3, 2]
list_waiting_time.sort()
# [1, 2, 3, 3, 4]

rtn = var_wait = 0                    # 1
for x in list_waiting_time:           # 1 2
    var_wait += x                     # 1 2 3
    rtn += var_wait                   # 1 2 3 3
                                      # 1 2 3 3 4 
print(rtn) 
