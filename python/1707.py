from sys import stdin
from collections import deque

def bfs(var_vtx):
    mat_visit[var_vtx] = 1    
    queue = deque()
    queue.append(var_vtx)
    while queue:
        vtx = queue.popleft()
        for i in mat_table[vtx]:
            if mat_visit[i] == 0:
                mat_visit[i] = -mat_visit[vtx]
                queue.append(i)
            else:
                if mat_visit[i] == mat_visit[vtx]:
                    return False
    return True

var_T = int(stdin.readline())

for _ in range(var_T):
    var_V,var_E = map(int, stdin.readline().split())
    bool_isBi = True
    mat_table = [[] for i in range(var_V+1)]
    mat_visit = [0 for i in range(var_V+1)]
    for _ in range(var_E):
        var_a,var_b = map(int, stdin.readline().split())
        mat_table[var_a].append(var_b)
        mat_table[var_b].append(var_a)
    for i in range(1,var_V+1):
        if mat_visit[i] == 0:
            if not bfs(i):
                bool_isBi = False
                break
    print(mat_table)
    print(mat_visit)
    print("YES"if bool_isBi else "NO")