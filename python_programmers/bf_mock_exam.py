def solution(answers):
    answer = []
    answer_temp = [] 
    count01 = 0 
    count02 = 0 
    count03 = 0 

    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)): 
        if answers[i] == one[i%len(one)]: 
            count01+=1 
        if answers[i] == two[i%len(two)]: 
            count02+=1 
        if answers[i] == three[i%len(three)]: 
            count03+=1 
    
    answer_temp = [count01, count02, count03] 
                    
    for person, score in enumerate(answer_temp): 
        if score == max(answer_temp): 
            answer.append(person+1) 
            
    return answer

