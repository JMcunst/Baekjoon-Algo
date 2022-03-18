# Input : matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output : [[1,0,1],[0,0,0],[1,0,1]]

# In-place

def solution(matrix):
    # O(1)
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == 0:
                matrix[0][col] = 0

                if row > 0:
                    matrix[row][0] = 0
                else:
                    print('row:',row,',col:',col)
                    rowZero = True

    print('matrix1:',matrix)

    for row in range(1, ROWS):
        for col in range(1, COLS):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    print('matrix2:',matrix)

    if matrix[0][0] == 0:
        for row in range(ROWS):
            matrix[row][0] = 0

    print('matrix3:',matrix)

    if rowZero:
        for col in range(COLS):
            matrix[0][col] = 0

    print('matrix4:',matrix)

    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
res = solution(matrix)

print(res)