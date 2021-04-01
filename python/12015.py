# from sys import stdin

# var_N = int(stdin.readline())
# A = list(map(int, stdin.readline().split()))
# nlist = [0]

# for a in range(var_N):
#     low = 0
#     high = len(nlist) - 1
#     while low <= high:
#         mid = (low +high)//2
#         if nlist[mid] < A[a]:
#             low = mid + 1
#         elif nlist[mid] >= A[a]:
#             high = mid - 1
#     if low >= len(nlist):
#         nlist.append(A[a])
#     elif low < len(nlist):
#         nlist[low] = A[a]

# print(len(nlist) - 1)
from sys import stdin
from bisect import bisect_left

var_N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
nlist = [0]

for a in A:
    if nlist[-1] < a:
        nlist.append(a)
    else:
        nlist[bisect_left(nlist,a)] = a

print(len(nlist)-1)

