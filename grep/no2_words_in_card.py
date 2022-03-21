from collections import Counter

def solution(card, word):
    CARD_ROWS = 3
    answer = []

    counter = []
    for i in range(CARD_ROWS):
        sc = list(card[i])
        counter += sc

    for st in word:
        cnt = Counter(counter)
        inw = [-1]*CARD_ROWS

        no_exist = False
        is_over = False

        for i in range(len(st)):
            ncnt = 0
            for j in range(CARD_ROWS):         
                if st[i] in card[j]:
                    if cnt[st[i]] > 0:
                        inw[j] = 1
                        cnt[st[i]] -= 1
                    else:
                        is_over = True
                else:
                    ncnt += 1
            if ncnt == CARD_ROWS:
                no_exist = True
        if no_exist or is_over:
            inw = [-1 for i in range(CARD_ROWS)]

        if sum(inw) == CARD_ROWS:
            answer.append(st)
    
    if not answer:
        answer.append('-1')

    return answer