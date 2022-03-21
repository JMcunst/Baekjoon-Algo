def solution(day, k):
    DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fdays = [-1] * 12
    
    days = DAYS[0]
    fdays[0] = 0 if (k + day - 1)%7 < 5 else 1
    
    for i in range(1, 12):
        dt = (days + k + day - 1)%7
        if dt < 5:
            fdays[i] = 0
        else:
            fdays[i] = 1
        days += DAYS[i]

    return fdays