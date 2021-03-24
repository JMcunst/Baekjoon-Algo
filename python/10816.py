from sys import stdin, stdout

_ = stdin.readline()        # Discard empty line
N = sorted(map(int,stdin.readline().split()))   # N[-10 -10 2 3 3 6 7 10 10 10]
_ = stdin.readline()        # Discard empty line
M = map(int,stdin.readline().split())           # M[10 9 -5 2 3 4 5 -10]

def binarySearch(num, N, start, end):       # 이분탐색 함수
    if start > end:         # start가 end보다 큰 경우
        return 0
    m = (start+end)//2      # mid
    if num == N[m]:
        i, j = 1, 1
        while m-i >= start: # mid기준 왼쪽
            if N[m-i] != N[m]:
                break
            else: i += 1
        while m+j <= end:   # mid기준 오른쪽
            if N[m+j] != N[m]:
                break
            else: j += 1
        return i + j - 1
    elif num < N[m]:
        return binarySearch(num, N, start, m-1)
    else:
        return binarySearch(num, N, m+1, end)

n_dict = {}             # 딕셔너리 자료형 선언
for n in N:
    start = 0           # 0
    end = len(N) - 1    # 9
    if n not in n_dict:  #
        n_dict[n] = binarySearch(n, N, start, end)

print(' '.join(str(n_dict[x]) if x in n_dict else '0' for x in M ))