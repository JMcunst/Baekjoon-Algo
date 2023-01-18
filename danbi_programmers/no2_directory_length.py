def solution(N, relation, dirname):
    answer = 0
    fname = 'root'
    direc = {}
    mxalen = -1

    relation.sort(key=lambda x : x[0])
    
    for s,e in relation:
        if s not in direc:
            direc[s] = []
            direc[s].append(e)
        else:
            direc[s].append(e)
    
    for val in direc:
        if val != 1:
            fname += dirname[val]
        for vaj in direc[val]:


    return answer