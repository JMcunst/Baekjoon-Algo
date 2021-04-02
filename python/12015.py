from sys import stdin

var_N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
nlist = [0]
                                # A = [10,20,10,30,20,50]
for a in range(var_N):          # a = 0    1         2       3            4 5
    low = 0                     # l = 0 1  0 1 2     0 0 1   0 1 2 3      ...
    high = len(nlist) - 1       # h = 0 0  1 1 1     2 0 0   2 2 2 2      ...
    while low <= high:          # m = 0    0 1       1 0     1 1 2        ...
        mid = (low +high)//2
        if nlist[mid] < A[a]:
            low = mid + 1
        elif nlist[mid] >= A[a]:
            high = mid - 1
    if low >= len(nlist):       # 1>=1     2>=2              3>=3         ...
        nlist.append(A[a])      # [0,10]   [0,10,20]         [0,10,20,30] ...
    elif low < len(nlist):      #                    1<3                  ...
        nlist[low] = A[a]       #                    10=10                ...

print(len(nlist) - 1)
# from sys import stdin
# from bisect import bisect_left

# var_N = int(stdin.readline())
# A = list(map(int, stdin.readline().split()))
# nlist = [0]

# for a in A:
#     if nlist[-1] < a:
#         nlist.append(a)
#     else:
#         nlist[bisect_left(nlist,a)] = a

# print(len(nlist)-1)

