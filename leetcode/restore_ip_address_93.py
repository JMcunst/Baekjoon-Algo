# Input : s = "25525511135"
# Output : ["255.255.11.135","255.255.111.35"]

# BruteForce , BackTracking(DFS기반 트리탐색 알고리즘)

def solution(s):
    answer = []

    if len(s) > 12 or len(s) < 4:
        print('ERR: Length Over')
        return answer


    def backtrack(i, dots, curIP):
        print(i, dots)
        if dots == 5 and i == len(s):
            print('GOOD: Find IP')
            answer.append(curIP[:-1])
            return
        if dots > 4:
            print('ERR: Dots Over')
            return

        for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) < 255 and (i == j or s[i] != '0'):
                backtrack(j+1, dots+1, curIP + s[i:j+1] + '.')
    backtrack(0,0,'')

    return answer


s = '25525511135'
res = solution(s)

print(res)