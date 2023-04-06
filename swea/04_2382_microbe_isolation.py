
#-------------answer1----------------#
# dy = [0, -1, 1, 0, 0]
# dx = [0, 0, 0, -1, 1]
# rev = [0, 2, 1, 4, 3]

# def move(virus):
#     for t in range(M):
#         new = {}
#         for pos, val in virus.items():
#             k, d, _ = val
#             ny, nx = pos[0] + dy[d], pos[1] + dx[d]
#             if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
#                 k = k//2
#                 if k == 0:
#                     continue
#                 d = rev[d]
#             if (ny, nx) not in new:
#                 new[(ny, nx)] = [k, d, k]
#             else:
#                 if new[(ny, nx)][2] < k:
#                     new[(ny, nx)][1] = d
#                     new[(ny, nx)][2] = k
#                 new[(ny, nx)][0] += k
#         virus = new
#     k_tot = 0
#     for val in virus.values():
#         k_tot += val[0]
#     return k_tot

# test_case = int(input())
# for tc in range(1, test_case+1):
#     N, M, K = map(int, input().split())
#     virus = {}
#     for _ in range(K):
#         y, x, k, d = list(map(int, input().split()))
#         virus[(y, x)] = [k, d, k]
#     print(f"#{tc} {move(virus)}")

#----------answer 2-----------#
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = []
    for _ in range(K):
        A.append(list(map(int, input().split())))

    print('AAAA:',A)
    for _ in range(M):
        info = dict()
        for row in range(K):
            r, c, k, d = A[row]
            print('R,C,K,D:',r,c,k,d)
            if not k:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            print('A[row][0]::', A[row][0])
            print('A[row][1]::', A[row][1])
            A[row][0], A[row][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                A[row][2] //= 2
                A[row][3] = rev[d]
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [row, k]
            else:
                num, size = info[(nr, nc)]
                if A[row][2] > size:
                    info[(nr, nc)] = [row, A[row][2]]
                    A[row][2] += A[num][2]
                    A[num][2] = 0
                else:
                    A[num][2] += A[row][2]
                    A[row][2] = 0
    microbe = 0
    for m in A:
        microbe += m[2]
    print("#{} {}".format(tc+1, microbe))
