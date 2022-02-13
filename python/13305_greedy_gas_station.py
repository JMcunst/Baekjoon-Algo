from sys import stdin

var_N = int(stdin.readline())
list_dist = list(map(int,stdin.readline().split()))
list_cost = list(map(int,stdin.readline().split()))

rtn = list_dist[0]*list_cost[0]
var_min_cost = list_cost[0]

for i in range(1,len(list_dist)):
    if var_min_cost > list_cost[i]:
        var_min_cost = list_cost[i]
    var_temp_expen = var_min_cost * list_dist[i]
    rtn += var_temp_expen

print(rtn)