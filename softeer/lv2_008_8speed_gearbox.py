import sys

geers = list(map(int, input().split()))

st = geers[0]
asc = 0
dsc = 0
exp = []

for i in range(1, len(geers)):
    tmp = geers[i]
    if tmp - st > 0:
        asc = 1
        dsc = 0
        exp.append('ASC')
    else: 
        dsc = 1
        asc = 0
        exp.append('DSC')
    st = geers[i]
    
exp = list(set(exp))

if len(exp) >= 2:
    print('mixed')
else:
    if asc == 1 and dsc == 0:
        print('ascending')
    else:
        print('descending')