from sys import stdin


var_T = int(stdin.readline())
for _ in range(var_T):
    var_n, var_m, var_t = map(int, stdin.readline().split()) # n:교차로, m:도로, t:목적지후보
    var_s, var_g, var_h = map(int, stdin.readline().split()) # s:예술가출발, g:지점1 h:지점2
    for _ in range(var_m):
        var_a, var_b, var_d = map(int, stdin.readline().split()) # a와 b사이에 길이 d의 양방향 도로
    for _ in range(var_t):
        var_x = int(stdin.readline()) # t개의 목적지 후보들, 서로 다른 위치며, 모두 s가 아니다.