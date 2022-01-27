from sys import stdin

DOC_GRD = 0     # 서류심사 상수
INV_GRD = 1     # 면접심사 상수

var_T = int(stdin.readline())  # 1 <= T <= 20

for _ in range(var_T):
    applicants = []
    available_count = 1
    var_N = int(stdin.readline())  # 1 <= N <= 100,000
    for _ in range(var_N):
        applicant = list(map(int, stdin.readline().split()))
        applicants.append(applicant)

    applicants.sort(key=lambda x : x[DOC_GRD])  # 서류심사 기준으로 정렬, 오름차순
    inv_max = applicants[0][INV_GRD]

    for i in range(var_N):
        if  inv_max > applicants[i][INV_GRD]:
            available_count += 1
            inv_max = applicants[i][INV_GRD]

    print(available_count)
