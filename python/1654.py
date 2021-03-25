from sys import stdin

K, N = map(int,stdin.readline().split())
list_K = list(map(int,stdin.readlines()))
high_l, low_l = sum(list_K)//N, 1       # Key point 

while low_l <= high_l :                 # 로우 <= 하이
    mid_l = (high_l + low_l)//2         # 중간 값
    count = sum([x//mid_l for x in list_K])   # list_K를 mid값으로 나눈 몫 (예제1 -> 4+3+2+2)
    if count  < N:                         # N을 못채운 경우
        high_l = mid_l - 1
    elif count >= N:                      # N을 채우거나 넘긴경우 (합격)
        low_l = mid_l + 1
        rtn = mid_l

print(rtn)