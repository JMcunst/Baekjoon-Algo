n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    print('froutes::', routes)
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            print(routes)
            if cost[0] in routes and cost[1] in routes:
                print('cost[0]::', cost[0], 'cost[1]::', cost[1])
                continue
            if cost[0] in routes or cost[1] in routes:
                print('cost[0]::', cost[0], 'cost[1]::', cost[1])
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                print(ans)
                costs[i] = [-1, -1, -1]
                print('i::',i,'costs[i]::',costs[i])
                print('costs::',costs)
                break

    print(ans)
    return ans

solution(n, costs)