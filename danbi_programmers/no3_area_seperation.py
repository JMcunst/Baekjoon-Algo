def solution(v):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    area = []

    for i, val_i in enumerate(v):
        for j, val_j in enumerate(val_i):
            if v[i][j] == 1:
                tarea = 1
                cnt += 1
                v[i][j] = 0
                queue = [[i,j]]
                while queue:
                    x,y = queue[0][0], queue[0][1]
                    del queue[0]
                    for k in range(4):
                        x1 = x + dx[k]
                        y1 = y + dy[k]
                        if 0 <= x1 < len(v) and 0 <= y1 < len(val_i) and v[x1][y1] == 1:
                            v[x1][y1] = 0
                            tarea += 1
                            queue.append([x1, y1])
                area.append(tarea)

    answer = [cnt, max(area)]
    return answer