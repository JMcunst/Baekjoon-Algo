# Input : Grid, m = 3, n = 7
# Output : 28

# DP
import math

def solution(m, n):
    row = [1] * n

    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow

    return row[0]

def solution2(m, n):
    a = m -1
    b = n-1

    return int(math.factorial(a + b) /math.factorial(a) /math.factorial(b))

# m x n grid
m = 3
n = 7
res = solution2(m, n)

print(res)


