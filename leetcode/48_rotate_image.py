# Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output : [[7,4,1],[8,5,2],[9,6,3]]

# Matrix

def solution(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right):
            top, bottom = left, right

            # save the topleft value
            topLeft = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = topLeft

        right -= 1
        left += 1
    
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = solution(matrix)

print(res)