from collections import Counter

def solution(goods):
    answer = []
    primary_dict = {}
    answer_dict = {}
    part_list = []

    for good in goods:
        primary_dict[good] = []
        my_list = []
        
        for i in range(len(good)):
            k = i+1
            while k <= len(good):
                if good[i:k] not in my_list:
                    my_list.append(good[i:k])
                primary_dict[good].append(good[i:k])
                k += 1
        part_list += my_list

    counter = Counter(part_list)

    for good, value in primary_dict.items():
        answer_dict[good] = []
        flag = True
        length = -1
        value.sort(key=len)
        for i in range(len(value)):
            if flag:
                if counter[value[i]] == 1:
                    length = len(value[i])
                    flag = False
                    answer_dict[good].append(value[i])
            else:
                if counter[value[i]] == 1 and len(value[i]) == length:
                    answer_dict[good].append(value[i])
            
    for good, words in answer_dict.items():
        if words:
            fw = list(set(words))
            fw.sort()
            for i, word in enumerate(fw):
                if i == 0:
                    st = word
                else:
                    st += ' '+word
            answer.append(st)
        else:
            answer.append('None')
            continue
    return answer



# goods
input = ["pencil","cilicon"]
input1 = ["pencil","cilicon","contrabase","picturelist"]
input2 = ["abcdeabcd","cdabe","abce","bcdeab"]
res = solution(input2)
print('res::',res)
# result = ["en nc pe","ico ili lic","a b","u"]