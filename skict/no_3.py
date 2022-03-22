def solution(width, height, diagonals):
    answer = 0

    for x,y in diagonals:
        visited = [[0]*(width) for _ in range(height)]
        visited[0][0] = 1

        vp = [x-1, y-1]
        rp = [x-1, y]

        print('vp:',vp, 'rp:',rp)

        for i in range(0, vp[1]): 
            for j in range(0, vp[0]): 
                if i==0 and j == 0: 
                    continue
                else: 
                    visited[i][j] += (visited[i-1][j] + visited[i][j-1])
        print(visited)

        route = [[0]*(width) for _ in range(height)]
        route[rp[0]][rp[1]] = 1

        for i in range(rp[1], height): 
            for j in range(rp[0], width): 
                if i==rp[1] and j == rp[0]: 
                    continue
                else: 
                    route[i][j] += (route[i-1][j] + route[i][j-1])
        print(route)

        if vp[0] != 0 and vp[1] != 0:
            summ = visited[vp[0]][vp[1]] * route[width][height] * 2
            answer += summ
        else:
            summ = route[width][height] * 2
            answer += summ

    return answer

solution(2,2, [[1,1],[2,2]])

