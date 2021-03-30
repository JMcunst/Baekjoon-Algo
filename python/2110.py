from sys import stdin

def count_router(distance,home_list):       #router의 개수를 count하는 함수
    count = 1
    now_router = home_list[0]

    for x in range(1,var_H):                # key algorithm, 기준이 되는 now_router와 home[x]의 거리가 mid_d 보다 크거나 같다면 count++
        if (distance <= home_list[x] - now_router):
            count += 1
            now_router = home_list[x]
    
    return count

def binary_router(var_T,home_list):
   
    max_d, min_d = home_list[-1]-home_list[0], 1       # 최대 거리, 최소 거리(1)

    while min_d <= max_d :                 
        mid_h = (max_d + min_d)//2         # 중간 값
        count_r = count_router(mid_h,home_list)     # router 개수 count 함수의 매개변수로 mid_d,와 home_list를 넘김.
        
        if count_r < var_T:                         # Target router 개수를 못채운 경우
            max_d = mid_h - 1
        elif count_r >= var_T:                      # Target router 개수 채우거나 넘긴경우 (충족)
            min_d = mid_h + 1
            rtn = mid_h                             # 최종 결과값 저장

    return rtn

var_H, var_T = map(int,stdin.readline().split())
home_list = list(map(int,stdin.readlines()))
home_list.sort()

print(binary_router(var_T,home_list))