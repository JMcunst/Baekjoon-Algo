def solution(customer, K):
    answer = []

    reserved = []
    ready = []

    for cus, resv in customer:
        print(cus, resv)
        if resv == 1: 
            if len(reserved) < K:
                print('예약 성공')
                reserved.append(cus)
            else:
                print('예약 FULL 대기룸')
                ready.append(cus)
        else:
            if cus in reserved:
                print('예약 ON -> 취소')
                reserved.remove(cus)
                if ready:
                    rcus = ready[0]
                    reserved.append(rcus)
                    ready.remove(rcus)
            else:
                print('대기 ON -> 취소')
                ready.remove(cus)
        print('중간 reserved', reserved, '중간 ready', ready)
    print('최종 reserved', reserved, '최종 ready', ready)

    reserved.sort()
    return reserved