import time
start = time.time() 

# 1
# 5 1
# 9 3 2 3 2
# 6 3 1 7 5
# 3 4 8 9 9
# 2 3 7 7 7
# 7 6 5 5 8
# test_input = int('1 \
#     5 1 \
#     9 3 2 3 2 \
#     6 3 1 7 5 \
#     3 4 8 9 9 \
#     2 3 7 7 7 \
#     7 6 5 5 8')
# ---------------------------------
# T = int(input())

# print(T, type(T))

# for i in range(T):
#     N, K = map(int, input().split())
#     print(N, type(N), K, type(K))

#     mp = [ list(map(int, input().split())) for _ in range(N)]

#     print(mp)


######################################
# ------------ answer 1 ------------ #
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,path,isConst):
	global ans
	if ans < path: # 최장 등산로 갱신하기
		ans = path
	# 사방 탐색 : 등산로 탐색
	for k in range(4):
		nr = r + dr[k]
		nc = c + dc[k]
		if nr < 0 or nr >= N or nc < 0 or nc >= N:
			continue
		if visited[nr][nc] == 1:
			continue
		# 이동가능하면 이동
		if m[r][c] > m[nr][nc]:
			visited[nr][nc] = 1
			dfs(nr, nc, path+1, isConst)
			visited[nr][nc] = 0
		# 이동이 불가능하고 공사를 아직 안했으면 (1~K만큼 공사 가능 -> 모든경우)
		elif m[r][c] <= m[nr][nc] and not isConst:
			for i in range(1,K+1):
				m[nr][nc] -= i # 공사하기
				isConst = True
				if m[r][c] > m[nr][nc]:
					visited[nr][nc] = 1
					dfs(nr,nc,path+1, isConst)
					visited[nr][nc] = 0
				# 공사 취소하기 -> 다른 경우를 체크하기 위해
				isConst = False
				m[nr][nc] += i

T = int(input())
for tc in range(1, T+1):
	N, K = map(int, input().split())
	m = [ list(map(int, input().split())) for _ in range(N)]
	# 가장 높은 봉우리 찾기
	maxH = 0
	for i in range(N):
		for j in range(N):
			if maxH < m[i][j]:
				maxH = m[i][j]

	ans = 0
	for i in range(N):
		for j in range(N):
			if m[i][j] == maxH:
				visited = [[0]*N for _ in range(N)]
				visited[i][j] = 1
				dfs(i,j,1,False)

	print("#{} {}".format(tc, ans))
######################################
# ------------ answer 2 ------------ #
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# def dfs(y,x,cnt,k,n):
#     global res
#     if(res < cnt+1):
#         res = cnt+1
#     visited[y][x] = 1
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if(ny>=0 and ny<n and nx>=0 and nx<n):
#             if(visited[ny][nx] == 0):
#                 # 안깎고 이동이 가능할 때
#                 if(arr[ny][nx] < arr[y][x]):
#                     dfs(ny,nx,cnt+1,k,n)
#                 # 깎고 이동할 때
#                 elif(arr[ny][nx]-k < arr[y][x]):
#                     # 값 저장
#                     pre = arr[ny][nx]
#                     # 깎고
#                     arr[ny][nx] = arr[y][x] -1
#                     dfs(ny,nx,cnt+1,0,n)
#                     # 값 복귀
#                     arr[ny][nx] = pre
#     visited[y][x] = 0

# T = int(input())

# # T = test_input
# for tc in range(T):
#     n, k = map(int, input().split())

#     arr = []
#     for i in range(n):
#         arr.append(list(map(int, input().split())))
    
#     res = 0
#     maxV = 0
#     visited = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if(maxV < arr[i][j]):
#                 maxV  = max(maxV, arr[i][j])
#     v = []
#     for i in range(n):
#         for j in range(n):
#             if(arr[i][j] == maxV):
#                 v.append([i,j])
#     for i in range(len(v)):
#         dfs(v[i][0], v[i][1], 0, k, n)
    
#     print("#{} {}".format(tc+1, res))




print("time :", time.time() - start)