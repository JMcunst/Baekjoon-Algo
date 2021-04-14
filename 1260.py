from sys import stdin

def dfs(V):
    print(V, end=' ')               # 방문한 노드 출력
    list_visit[V] = 1               # 방문한 노드 1체크(나 방문했다!)
    for i in range(1, var_N + 1):   
        if list_visit[i] == 0 and inj_matrix[V][i] == 1:    # 방문하지 않고, 현재 노드에 인접한 노드 방문시 재귀
            dfs(i)      # 재귀

def bfs(V):
    queue = [V]                     # queue에 현재 노드 세팅
    list_visit[V] = 0               # dfs를 돌았기 때문에, 초기화
    while(queue):
        V = queue[0]                # 현재 큐의 노드 세팅
        print(V, end=' ')
        del queue[0]                # queue[0] 삭제
        for i in range(1, var_N + 1):
            if list_visit[i] == 1 and inj_matrix[V][i] == 1: # 방문했고 인접노드 방문했으면 큐에 노드 추가하고 방문 초기화
                queue.append(i)
                list_visit[i] = 0

var_N, var_M, var_V = map(int, stdin.readline().split())
inj_matrix = [[0] * (var_N + 1) for i in range(var_N + 1)]  # 인접행렬 생성 (var_N +1 사이즈 만큼 행과 열)
list_visit = [0 for i in range(var_N + 1)]                  # 방문 정보 리스트 생성 (var_N +1 사이즈 만큼)

for i in range(var_M):  # 인접행렬 세팅   
    x, y = map(int, stdin.readline().split())    # 0 1 1 0 
    inj_matrix[x][y] = 1                # 1 0 0 1
    inj_matrix[y][x] = 1                # 1 0 0 1
                                        # 0 1 1 0
dfs(var_V)
print()
bfs(var_V)