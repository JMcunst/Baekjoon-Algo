from sys import stdin


var_T = int(stdin.readline())
for _ in range(var_T):
    var_n, var_m, var_t = map(int, stdin.readline().split()) # n:교차로, m:도로, t:목적지후보
    var_s, var_g, var_h = map(int, stdin.readline().split()) # s:예술가출발, g:지점1 h:지점2
    for _ in range(var_m):
        var_a, var_b, var_d = map(int, stdin.readline().split())
    for _ in range(var_t):
        var_x = int(stdin.readline())