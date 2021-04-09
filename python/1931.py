from sys import stdin

var_N = int(stdin.readline())
list_meeting = []

for _ in range(var_N):
    var_start, var_end = map(int, stdin.readline().split())
    list_meeting.append([var_start,var_end])

list_meeting = sorted(list_meeting, key = lambda x : (x[1], x[0]))
# x[0] : 0 3 0 5 3 5 6  8  8  2  12
# x[1] : 4 5 6 7 8 9 10 11 12 13 14

rtn = end = 0               # i  0 3 0 5 3 5 6  8  8  2  12
for i,j in list_meeting:    # j  4 5 6 7 8 9 10 11 12 13 14
    if i >= end:            #    1>=0 3>=4 0>=4 5>=4 6>=7 8>=7 8>=11 2>=11 12>=11   
        rtn += 1            #rtn   1              2         3                4
        end = j             #end   4              7         11               14

print(rtn)