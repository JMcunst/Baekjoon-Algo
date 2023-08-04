import sys

N, B = map(int, sys.stdin.readline().split())

coms = list(map(int, sys.stdin.readline().split()))

coms = sorted(coms, reverse=True)

left= coms[-1]
right = 2000000000

coms_dict = {}
for i in coms:
    if(i not in coms_dict.keys()):
        coms_dict[i]=1
    else:
        coms_dict[i]+=1

while (right-left >1):
    mid = (right + left) // 2

    cur = 0
    is_left = True

    for k,v in coms_dict.items():
        if k < mid:
            cur += ((mid - k)**2)*v
            if cur > B:
                right = mid
                is_left = False
                break

    if is_left:
        left = mid

print(left)

