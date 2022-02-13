# t = [3,5,2,9,8]
# m = 3
t = [4,2,3,1]
m = 2
# result = 13

def solution(t, m):
    t.sort()
    print(t)
    answer = 0

    for i in range(m):
        need = t[i]+1
        answer+= need

    print(answer)
    return answer



solution(t, m)