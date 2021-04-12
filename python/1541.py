from sys import stdin

list_minus = stdin.readline().split('-')
num = []

for i in list_minus:
    cnt = 0
    list_add = i.split('+')
    for j in list_add:
        cnt += int(j)
    num.append(cnt)
rtn = num[0]          

for i in range(1, len(num)):
    rtn -= num[i]

print(rtn)