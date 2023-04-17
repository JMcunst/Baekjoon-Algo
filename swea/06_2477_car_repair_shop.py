# #-----------------answer1---------------------#
T = int(input())

for tc in range(1, 1+T):
    # N: 접수 창구 개수
    # M: 정비 창구 개수
    # K: 방문 고객 수
    # A, B: 지갑 두고 간 사람이 방문한 창구 번호
    # a: 각 접수 창구 걸리는 시간 list
    # b: 각 정비 창구 걸리는 시간 list
    # t: 각 고객이 정비소를 방문한 시간 list
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t_idx = 0
    len_t = len(t)

    # 방문 기록 저장 배열
    visitor_info = [[-1, -1] for _ in range(K)]

    reception_desks = [-1] * N
    repair_desks = [-1] * M
    TEST_desks = [-1] * 4
    print('REPAIR_INIT:',TEST_desks)
    reception_waiting_line = []
    repair_waiting_line = []

    time = 0

    flag = True
    while flag:
        # 0. 정비 창구에서 볼일 다 본 사람 out
        print('REPAIR_DESK:',repair_desks)
        for i in range(M):
            if repair_desks[i] != -1 and repair_desks[i][1] == 0:
                print('repair_desks[i][1]',repair_desks[i][1])
                repair_desks[i] = -1
        # 1. 접수 창구에서 볼일 다 본 사람 '정비 창구 대기열'로 옮기기
        for i in range(N):
            if reception_desks[i] != -1 and reception_desks[i][1] == 0:
                repair_waiting_line.append(reception_desks[i][0])
                reception_desks[i] = -1
        # 2. 이번 시간에 들어온 사람 '접수 창구 대기열'로 옮기기
        for i in range(t_idx, len_t):
            if t[i] == time:
                reception_waiting_line.append(i)
            else:
                t_idx = i
                break
        # 3. 정비 창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(M):
            if repair_desks[i] == -1 and repair_waiting_line:
                visitor_idx = repair_waiting_line.pop(0)
                repair_desks[i] = [visitor_idx, b[i]-1]
                # 몇번 정비 창구 방문했는지 기록하기
                visitor_info[visitor_idx][1] = i
            elif repair_desks[i] != -1:
                repair_desks[i][1] -= 1
        # 4. 접수 창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(N):
            if reception_desks[i] == -1 and reception_waiting_line:
                visitor_idx = reception_waiting_line.pop(0)
                reception_desks[i] = [visitor_idx, a[i]-1]
                # 몇번 접수 창구 방문했는지 기록하기
                visitor_info[visitor_idx][0] = i
            elif reception_desks[i] != -1:
                reception_desks[i][1] -= 1
        # 5. 모든 창구 사람 남은 시간 -1 해주기, 위 3, 4에서 함께 처리 해줌

        time += 1
        if time > K:
            for i in range(K):
                if visitor_info[i][1] == -1:
                    break
            else:
                flag = False

    answer = 0
    for i in range(K):
        if visitor_info[i][0] == A-1 and visitor_info[i][1] == B-1:
            answer += i+1

    if answer == 0:
        answer = -1

    print(f'#{tc} {answer}')
# #-----------------answer2-----------------#
# T = int(input())

# for tc in range(1, 1+T):
#     # N: 접수 창구 개수
#     # M: 정비 창구 개수
#     # K: 방문 고객 수
#     # A, B: 지갑 두고 간 사람이 방문한 창구 번호
#     # recpt: 각 접수 창구 걸리는 시간 list
#     # repair: 각 정비 창구 걸리는 시간 list
#     # customer: 각 고객이 정비소를 방문한 시간 list
#     N, M, K, A, B = map(int, input().split())
#     recept = list(map(int, input().split()))
#     repair = list(map(int, input().split()))
#     customer = list(map(int, input().split()))

#     new = []
#     answer = 0
#     recenum = []
#     repairnum = [0] * K
#     receptime = [-1] * N
#     repairtime = [-1] * M

#     for c in range(K):
#         flag = 0
#         for num in range(N):
#             if receptime[num] < customer[c]:
#                 receptime[num] = customer[c] + recept[num] - 1
#                 recenum.append(num)
#                 flag = 1
#                 new.append([receptime[num] + 1, c])
#                 break
#         if flag == 0:
#             idx = receptime.index(min(receptime))
#             recenum.append(idx)
#             receptime[idx] += recept[idx]
#             new.append([receptime[idx] + 1, idx, c])
#     print('NEW::', new)
#     new.sort()
#     for i in new:
#         flag = 0
#         for num in range(M):
#             if repairtime[num] < i[0]:
#                 repairtime[num] = i[0] + repair[num] - 1
#                 repairnum[i[2]] = num
#                 flag = 1
#                 break
#         if flag == 0:
#             idx = repairtime.index(min(repairtime))
#             repairnum[i[2]] = idx
#             repairtime[idx] += repair[idx]
#     for k1 in range(K):
#         if recenum[k1] + 1 == A and repairnum[k1] + 1 == B:
#             answer += (k1 + 1)
#     if answer == 0:
#         answer = -1

#     print('#{} {}'.format(tc, answer))
# -------------------answer 3----------------------#
# T = int(input())
# for tc in range(1, T+1):
#     # N : 접수창구갯수, M : 정비창구갯수, K : 방문자수
#     # A : 지갑 놓고간 접수창구, B : 지갑 놓고간 정비창구
#     N, M, K, A, B = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     customers = list(map(int, input().split()))
#     used_counter = []
#     visit_a = [0] * N
#     visit_b = [0] * M
#     result = 0
#     for i, t in enumerate(customers):
#         w = 0
#         w_idx = 0
#         while w < N:
#             if visit_a[w] <= t:
#                 w_idx = w
#                 break
#             if visit_a[w] < visit_a[w_idx]:
#                 w_idx = w
#             w += 1

#         visit_a[w_idx] = max(t, visit_a[w_idx]) + a[w_idx]
#         customers[i] = [i, visit_a[w_idx], w_idx]
#         if w_idx == A-1:
#             used_counter.append(i)
#     customers = sorted(customers, key=lambda x: (x[1], x[2]))
#     for customer in customers:
#         num, t, _ = customer
#         w = 0
#         w_idx = 0
#         while w < M:
#             if visit_b[w] <= t:
#                 w_idx = w
#                 break
#             if visit_b[w] < visit_b[w_idx]:
#                 w_idx = w
#             w += 1

#         visit_b[w_idx] = max(t, visit_b[w_idx]) + b[w_idx]
#         if w_idx == B-1 and num in used_counter:
#             result += num + 1

#     if not result:
#         result = -1

#     print('#{} {}'.format(tc, result))
