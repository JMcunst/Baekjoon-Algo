from sys import stdin

def binaryTree(T,list_K):

    high_h, low_h = max(list_K), 0       # Key point 

    while low_h <= high_h :                 # 로우 <= 하이
        mid_h = (high_h + low_h)//2         # 중간 값
        count = 0
        for x in list_K:
            if x > mid_h:
              count += x-mid_h
        if count  < T:                         # N을 못채운 경우
            high_h = mid_h - 1
        elif count >= T:                      # N을 채우거나 넘긴경우 (합격)
            low_h = mid_h + 1
            rtn = mid_h

    return rtn

K, T = map(int,stdin.readline().split())
list_K = list(map(int,stdin.readline().split()))

print(binaryTree(T,list_K))
