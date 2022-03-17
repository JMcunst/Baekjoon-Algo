# Input : nums = [1,3,-1,-3,5,3,6,7] k = 3
# Output : [3,3,5,5,6,7]

# Monotonic Queue (deque) # O(n)
from collections import deque

def solution(nums, k):
    output = []
    q = deque()
    left = right = 0
    
    while right < len(nums):
        # 큐 위쪽에 right값을 넣기 전에 right값 보다 작은 값들 빼기
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)

        # 왼쪽것 하나 빼기
        if left > q[0]:
            q.popleft()

        if (right+1) >= k: 
            output.append(nums[q[0]])
            left += 1
        right += 1

    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = solution(nums, k)

print(res)