from sys import stdin
from collections import deque

def bfs(var_vtx):           # 1 2 3
    mat_visit[var_vtx] = 1    # vertex 방문 인증
    queue = deque()
    queue.append(var_vtx)
    while queue:  
        vtx = queue.popleft()     # vtx            : 1       3                    2     |    1           2                       3
        for i in mat_table[vtx]:  # mat_table[vtx] :[3]    [1,2]      [1,2]      [3]    |   [2]       [1,3,4]     [1,3,4]     [1,3,4]      [2,4]       [2,4]
            if mat_visit[i] == 0: # i              : 3       1          2         3     |    2           1           3           4           2           4
                                  # mat_visit :  [,1,0,0] [,1,0,-1] [,1,0,-1] [,1,1,-1] | [,1,0,0,0] [,1,-1,0,0] [,1,-1,0,0] [,1,-1,1,0] [,1,-1,1,1] [,1,-1,1,1] 
                mat_visit[i] = -mat_visit[vtx]
                queue.append(i)
            else:
                if mat_visit[i] == mat_visit[vtx]:
                    return False
            print('visit2=',mat_visit)
    return True         # 이분 그래프 O

var_T = int(stdin.readline())

for _ in range(var_T):
    var_V,var_E = map(int, stdin.readline().split())
    bool_isBG = True
    mat_table = [[] for i in range(var_V+1)]    # [[], [], [], []]
    mat_visit = [0 for i in range(var_V+1)]     # [0, 0, 0, 0]
    for _ in range(var_E):
        var_a,var_b = map(int, stdin.readline().split())
        mat_table[var_a].append(var_b)
        mat_table[var_b].append(var_a)
    for i in range(1,var_V+1):
        if mat_visit[i] == 0:   # 방문하지 않은 vertex라면, bfs(v)
            if not bfs(i):
                bool_isBG = False
                break

# mat_table : [[], [3], [3], [1, 2]]  |  [[], [2], [1, 3, 4], [2, 4], [3, 2]]
# mat_visit : [0, 1, 1, -1]           |  [0, 1, -1, 1, 1]

    print("YES"if bool_isBG else "NO")