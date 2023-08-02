import sys
from collections import deque

dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
direct = ['^', 'v', '>', '<']
rotate = {
    "L": [['^','<'],['v','>'],['>','^'],['<','v']],
    "R": [['^','>'],['v','<'],['>','v'],['<','^']],
    "Rev": [['^','v'],['v','^'],['>','<'],['<','>']]
}

def find_rotation_direction(arr):
    for direction, rotations in rotate.items():
        if arr in rotations:
            return direction
    return None

def bfs(h, w, fwd):
    path = []
    q = deque()
    q.append([h, w])
    visited[h][w] = True

    while q:
        lh, lw = q.popleft()
        for k in range(4):
            mh = lh + dh[k]
            mw = lw + dw[k]
            if maps[mh][mw] == 1:
                if fwd == direct[k]:
                    path.append('A')
                    if k < 2:
                        q.append([mh + dh[k], mw])
                    else:
                        q.append([mh, mw + dw[k]])
                    continue
                else:
                    rot = find_rotation_direction([fwd, direct[k]])
                    if rot == "Rev":
                        break
                    else:
                        path.append(rot)
                        fwd = direct[k]
                        q.append([lh, lw])
                        continue
    return path


H, W = list(map(int, input().split()))

maps = []
for i in range(H):
    row = input()
    row = [1 if cell == '#' else 0 for cell in row]
    maps.append(row)

sw = -1
sh = -1
fw = ''

visited = [[False] * W for _ in range(H)] 
trace = []
for i in range(H):
    for j in range(W):
        cnt = 0
        if maps[i][j] == 1:
            for k in range(4):
                mh = i + dh[k]
                mw = j + dw[k]
                if 0 <= mh < H and 0 <= mw < W:
                    if maps[mh][mw] == 1:
                        cnt += 1
                        fw = direct[k]
        if cnt == 1:
            sw = j
            sh = i
            trace = bfs(sh, sw, fw)
            break;
        
print(sh+1, sw+1)
print(fw)
print(''.join(trace))