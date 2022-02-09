p = [70, 50, 80, 50]
limit = 100

def solution(p, limit):
    p.sort()
    print('people::', p)
    cnt = 0
    
    i = 0
    j = len(p)-1
    while i<=j:
        print('i::',i,'j::',j,'p[i]::',p[i],'p[j]::',p[j])
        cnt+=1
        if p[j]+p[i]<=limit:
            i+=1
        j-=1
    return cnt

solution(p, limit)