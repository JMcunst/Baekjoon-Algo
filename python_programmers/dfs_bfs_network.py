def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for now_node in range(n):
        if visited[now_node] == False:
            dfs(n, computers, now_node, visited)
            answer += 1 
    return answer

def dfs(n, computers, now_node, visited):
    visited[now_node] = True
    for inj_node in range(n):
        if inj_node != now_node and computers[now_node][inj_node] == 1:
            if visited[inj_node] == False:
                dfs(n, computers, inj_node, visited)