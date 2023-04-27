def inside(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    return True
def square(sx,sy):
    global answer
    for k in range(N+1,0,-1):

        cost=k*k+(k-1)*(k-1)
        cnt=0
        do=0
        for x in range(sx-k+1,sx+1):
            for y in range(sy-do,sy+do+1):

                if inside(x,y):
                    if room[x][y]==1:
                        cnt+=1
            do+=1
        do-=2
        for x in range(sx+1,sx+k):
            for y in range(sy-do,sy+do+1):

                if inside(x,y):

                    if room[x][y]==1:
                        cnt+=1

            do-=1


        if M*cnt-cost>=0:
            #print(k,cnt,cost,M*cnt)
            #print(sx,sy,k,M,M*cnt,cost)
            return cnt

    return 0

T=int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    room=[list(map(int,input().split())) for _ in range(N)]
    answer=1


    for x in range(N):
        for y in range(N):
            answer=max(answer,square(x,y))
            #print(x,y,answer)
    print("#%d %d"%(t,answer))