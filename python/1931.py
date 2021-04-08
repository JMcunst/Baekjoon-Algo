from sys import stdin

var_N = int(stdin.readline())
list_meeting = []

for _ in range(var_N):
    var_start, var_end = map(int, stdin.readline().split())
    list_meeting.append([var_start,var_end])

list_meeting = sorted(list_meeting, key = lambda x : (x[1], x[0]))

rtn = end = 0
for i,j in list_meeting:
    if i >= end:
        rtn += 1
        end = j

print(rtn)