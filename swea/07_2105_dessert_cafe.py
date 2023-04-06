
dr = [1, -1, -1, 1]
dc = [1, -1, 1, -1]


def dfs(r, c path):
    global answer
    if ~:
        answer = path
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < N and 0 <= nc < N):


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

# ------------answer 2 --------------#
T = int(input())

di = [1, 1, -1, -1]                                           # 우하, 우상, 좌상, 좌하
dj = [1, -1, -1, 1]
'''
합이 한변(N)-1 길이 이하인 a,b 조합 -> 모양결정

시작점의 위치 결정
i : 1 ~ N-(x+y)
j : y ~ N-x
갯수는 그 2(x+y)
한변길이 -1 부터 시작해서 while로

구한 시작점으로 델타탐색으로 하나씩 찾아다님
우하 a 좌하 b 좌상 a 우상 b -> di += 1
'''
for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # x는 사각형의 우하/좌상 길이, y는 다른 하나 길이
    ans = -1
    # n : x+y고 답 나오면 바로 끝내도록 큰수부터 체크
    for n in range(N-1, 0, -1):
        for x in range(1, n):                                   # x 값 결정
            flag = False                                        # 답 결정되면 바로 종료
            y = n-x                                             # y 값
            for si in range(N-n):                               # 시작점 i는 밑에서 n까지 가능하며
                for sj in range(y, N-x):                        # j는 왼쪽에서는 y, 오른쪽에서 x까지 가능
                    i, j = si, sj
                    desert_list = []                            # 해당 디저트 리스트
                    d = 0
                    for a in range(2 * n):
                        if arr[i][j] in desert_list:            # 돌면서 같은 수 있으면 다음 경우로 넘어감
                            break
                        else:
                            desert_list.append(arr[i][j])       # 있으면 리스트에 넣어줌
                            if i == si+n or j in [sj-y, sj+x]:
                                d += 1
                            i, j = i + di[d], j + dj[d]
                    else:                                       # 같은수 만나서 종료되는 일 없으면
                        ans = 2 * n                             # 답 2*n으로 하고
                        flag = True                             # 답 구했으면 모든 반복문 종료
                        break                                   # 큰수에서부터 돌았기 때문에 자연스럽게 가장 큰 값이 답
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    print('#{} {}'.format(t, ans))
#-----------------answer3------------------------#
# n : 회전 횟수, (ci,cj) : 현재 위치, v : 방문한 곳 표시, cnt : 디저트 종류 수
def DFS(n,ci,cj,v):
    # (i,j) : 출발 위치
    global i,j,ans
    
    # 절반을 갔을 때 가지치기
    if n == 2 and ans>=len(v)*2:
        return

    if n > 3 : # 종료조건
        return
        
    # 정답 갱신
    # 회전 3번, 복귀, 디저트 종류 수 최대
    if n == 3 and ci == i and cj == j and ans < len(v):
        ans = len(v)
        return
        
    # 직진 or 방향 바꾸기
    for k in range(n,n+2):
        ni,nj = ci + di[k], cj + dj[k]
        # 범위 내, 중복 아니면
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k,ni,nj,v)
            v.pop()

# 4번째 방향 바꾸기 : 복귀 못하므로 실패
di,dj = (1,1,-1,-1,0),(-1,1,1,-1,0)

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 지역의 한 변의 길이
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

	# 방문한 디저트 종류 수
    ans = -1
    # 범위 확인!!
    for i in range(0,N-2):
        for j in range(1,N-1):
            DFS(0,i,j,[])

    print(f'#{tc} {ans}')
#--------------------answer4 dfs good memory--------------------#
T = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(num, x, y, d):
    global max_cafe
    global sx, sy
    if d == 3 and x == sx and y == sy:
        max_cafe = max(max_cafe, num)
        return
    elif not (0<=x<n and 0<=y<n):
        return
    elif board[x][y] in visited:
        return
    else:
        visited.append(board[x][y])
        if d in [0, 1]:
            dfs(num+1, x+dx[d], y+dy[d], d)
            dfs(num+1, x+dx[d+1], y+dy[d+1], d+1)
        elif d == 2:
            if x + y != sx + sy:
                dfs(num+1, x+dx[2], y+dy[2], 2)
            else:
                dfs(num+1, x+dx[3], y+dy[3], 3)
        else:
            dfs(num+1, x+dx[3], y+dy[3], 3)
        visited.remove(board[x][y])
    return


for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_cafe = -1
    visited = []
    for i in range(n):
        for j in range(n-1):
            sx, sy = i, j
            visited.append(board[i][j])
            dfs(1, i+1, j+1, 0)
            visited.remove(board[i][j])

    print(f'#{test_case} {max_cafe}')
#---------------answer5 simulation----------------------#
# 시작점과 왼쪽, 오른쪽 길이 인자로 들어오면 돌면서 카페 종류 검사
def checkDesserts(sr, sc, left, right):
    global MAX
    cafe = [0] * 101	# 카페 종류 검사용
    cnt = 0             # 들린 카페 갯수
    lr = sr + left      # 왼쪽 꼭지점
    lc = sc - left
    rr = sr + right     # 오른쪽 꼭지점
    rc = sc + right
    br = sr + left + right      # 아래 꼭지점
    bc = sc + right - left

    # 왼쪽 길이만큼 두 변 검사
    for dis in range(1, left+1):
        if cafe[A[sr+dis][sc-dis]]:
            return
        cafe[A[sr+dis][sc-dis]] = 1
        if cafe[A[br-dis][bc+dis]]:
            return
        cafe[A[br-dis][bc+dis]] = 1
        cnt += 2

    # 오른쪽 길이만큼 두 변 검사
    for dis in range(1, right+1):
        if cafe[A[lr+dis][lc+dis]]:
            return
        cafe[A[lr+dis][lc+dis]] = 1
        if cafe[A[rr-dis][rc-dis]]:
            return
        cafe[A[rr-dis][rc-dis]] = 1
        cnt += 2

    # print(cafe)
    MAX = max(MAX, cnt)     # 최댓값 갱신


# 시작점 기준으로 좌, 우 가능한 거리 경우의 수 구하기
def makeDistance(sr, sc):
    for left in range(1, sc+1):
        for right in range(1, N-sc):
            if sr+left+right > N-1:     # 반대편 꼭지점이 맵 넘어가면 continue
                continue
            checkDesserts(sr, sc, left, right)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    MAX = -1
    for sr in range(N-2):
        for sc in range(1, N-1):
            makeDistance(sr, sc)

    print("#{} {}".format(tc+1, MAX))