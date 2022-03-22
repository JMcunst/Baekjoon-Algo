# 1번 문제
# 원가 대비 가격에 대한 그리디
from collections import Counter


def solution(money, costs):
    answer = 0
    counter = {}
    
    pr_list = [(1, costs[0]), (5,costs[1]), (10,costs[2]), (50,costs[3]),(100,costs[4]),(500,costs[5])]
    pr_list.sort(key=lambda x : x[0]/x[1], reverse=True)


    for value, cost in pr_list:
        share = money // value
        counter[cost] = share
        money %= value
        print(share, money)   


    for value, cnt in counter.items():
        cost = value * cnt
        answer += cost
    
    return answer