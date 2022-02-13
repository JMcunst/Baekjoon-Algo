from sys import stdin

def dfs(V):
    list_visit[V] = 1               # 방문한 노드 1체크(나 방문했다!)
    for i in range(1, var_com + 1):   
        if list_visit[i] == 0 and inj_matrix[V][i] == 1:    # 방문하지 않고, 현재 노드에 인접한 노드 방문시 재귀
            dfs(i)      # 재귀

var_com = int(stdin.readline())
var_net = int(stdin.readline())
inj_matrix = [[0] * (var_com + 1) for i in range(var_com + 1)]  # 인접행렬 생성 (var_N +1 사이즈 만큼 행과 열)
list_visit = [0 for i in range(var_com + 1)]                  # 방문 정보 리스트 생성 (var_N +1 사이즈 만큼)

for i in range(var_net):  # 인접행렬 세팅         # 0 1 0 0 1 0 0
    x, y = map(int, stdin.readline().split())    # 1 0 1 0 1 0 0
    inj_matrix[x][y] = 1                         # 0 1 0 0 0 0 0
    inj_matrix[y][x] = 1                         # 0 0 0 0 0 0 1
                                                 # 1 1 0 0 0 1 0
dfs(1)                                           # 0 0 0 0 1 0 0
rtn = -1                                         # 0 0 0 1 0 0 0
for i in range(1,var_com+1):                    
    if list_visit[i] == 1:
        rtn += 1
print(rtn)
