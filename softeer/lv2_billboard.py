import sys

num_list = [
[1,1,1,0,1,1,1],
[0,0,1,0,0,1,0],
[1,0,1,1,1,0,1],
[1,0,1,1,0,1,1],
[0,1,1,1,0,1,0],
[1,1,0,1,0,1,1],
[1,1,0,1,1,1,1],
[1,1,1,0,0,1,0],
[1,1,1,1,1,1,1],
[1,1,1,1,0,1,1],
[0,0,0,0,0,0,0] ]

T = int(input())

for _ in range(T):
    difference_count = 0

    n1, n2 = list(map(int, input().split()))
    n1_len, n2_len = len(str(n1)), len(str(n2))
    max_len = max([n1_len, n2_len])
    
    n1_list = []
    n2_list = []

    if n1_len == n2_len:
        n1_list = [int(digit) for digit in str(n1)]
        n2_list = [int(digit) for digit in str(n2)]
    elif n1_len > n2_len:
        n1_list = [int(digit) for digit in str(n1)]
        n2_list = [10]*(n1_len - n2_len) + [int(digit) for digit in str(n2)]
    else:
        n1_list = [10]*(n2_len - n1_len) + [int(digit) for digit in str(n1)]
        n2_list = [int(digit) for digit in str(n2)]

    for i in range(max_len):
        for j in range(7):
            if num_list[n1_list[i]][j] != num_list[n2_list[i]][j]:
                difference_count += 1

    print(difference_count)