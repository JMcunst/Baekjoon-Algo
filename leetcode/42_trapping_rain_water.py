# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6

# Google Interview Question
# O(1)

def solution(height):
    if not height: return 0

    left, right = 0, len(height) - 1
    lmax, rmax = height[left], height[right]
    res = 0

    while left < right:
        if lmax < rmax:
            left += 1
            lmax = max(lmax, height[left])
            res += lmax - height[left]
        else:
            right -= 1
            rmax = max(rmax, height[right])
            res += rmax - height[right]

    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = solution(height)

print(res)