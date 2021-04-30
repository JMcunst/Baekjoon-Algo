from sys import stdin
from collections import deque

queue = deque()

queue.append([6, 1])

print(queue)
print(queue[0])
print(queue[0][1])

queue.popleft()

print(queue)

queue.append([5, 3])

print(queue)

queue.extend([2, 2])

print(queue)