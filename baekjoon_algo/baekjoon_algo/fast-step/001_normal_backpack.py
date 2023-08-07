N, K = list(map(int, input().split()))

values = [[0]*(K+1) for _ in range(N+1)]
items = [(0,0)]
for _ in range(N):
    W, V = list(map(int, input().split()))
    items.append((W,V))
    
for i in range(1, N+1):
    for sw in range(1, K+1):
        iw = items[i][0]
        iv = items[i][1]

        if iw > sw:
            values[i][sw] = values[i-1][sw]
        else:
            values[i][sw] = max(values[i-1][sw], iv + values[i-1][sw - iw])

print(values[N][K])




