from sys import stdin

var_N = int(stdin.readline())
list_waiting_time = list(map(int, stdin.readline().split()))

list_waiting_time.sort()

rtn = var_wait = 0
for x in list_waiting_time:
    var_wait += x
    rtn += var_wait

print(rtn) 