# R = Rock(바위)
# S = Scissor(가위)
# P = Paper(보)
rsp3 = ["SPR","PPR","PSS","RSS","RRR"]
rsp32 = ["RRR", "SPS"]

FST_P = 0
SCD_P = 1
THD_P = 2

def find_co_winner(match, key, answer):
    list_two = []

    for i in range(3):
        if match[i] == key:
            list_two.append(i)

    if answer[list_two[0]] == answer[list_two[1]]:
        answer[list_two[0]] += 1
        answer[list_two[1]] += 1
    else:
        if answer[list_two[0]] > answer[list_two[1]]:
            answer[list_two[1]] += 2
        else:
            answer[list_two[0]] += 2
    
    return answer

def solution(rsp3):
    answer = [0, 0, 0]

    for match in rsp3:
        print(match)
        if 'S' in match and 'P' in match and 'R' in match:
            print('yesyes')
            continue
        elif match[FST_P] == match[SCD_P] and match[SCD_P] == match[THD_P] and match[THD_P] == match[FST_P]:
            print('yyyyyyyyy')
            continue
        elif match.count('P') == 2:
            if 'S' in match:
                answer[match.index('S')] += 2
            else:
                answer = find_co_winner(match, 'P', answer)
        elif match.count('S') == 2:
            if 'R' in match:
                answer[match.index('R')] += 2
            else:
                answer = find_co_winner(match, 'S', answer)
        elif match.count('R') == 2:
            if 'P' in match:
                answer[match.index('P')] += 2
            else:
                answer = find_co_winner(match, 'R', answer)
        
    print(answer)
    return answer

solution(rsp32)