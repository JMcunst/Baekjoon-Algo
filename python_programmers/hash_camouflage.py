cloths = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        print(c, t)
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    print(clothes_type)

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

solution(cloths)


# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer