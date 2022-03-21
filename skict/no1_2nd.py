# 당신은 쇼핑몰에서 상품을 검색할 수 있습니다. 검색어를 입력하면 검색어를 부분 문자열로 갖는 모든 상품들이 검색됩니다.
# 부분 문자열이란, 문자열의 연속된 일부를 의미합니다. 예를 들어 abcde의 부분 문자열로 abc나 bcde 등이 있고, ac나 ea는 부분 문자열이 아닙니다.

# 특정 단어로 검색해서 검색된 상품의 개수가 하나일 때, 해당 단어를 상품의 고유 검색어라고 합니다. 당신은 상품마다 고유 검색어 중 가장 짧은 고유 검색어 목록을 구하려 합니다.

# 검색어 목록은 사전 순서대로 빠른 순으로 정렬되고, 중복되지 않아야 합니다. 검색어 목록은 공백 하나로 검색어들을 구분하는 형태입니다. 만약 고유 검색어가 없다면 None을 목록에 담습니다.

# 예를 들어, 쇼핑몰에 pencil, cilicon, contrabase, picturelist 네 가지 상품이 있다면, 각 상품의 가장 짧은 고유 검색어 목록은 다음과 같습니다.

# pencil : en nc pe 
# cilicon : ico ili lic 
# contrabase : a b 
# picturelist : u 
# pencil의 고유 검색어를 예시로 들어보겠습니다.

# pencil의 고유 검색어 중 길이가 1인 검색어는 존재하지 않습니다.
# p를 검색어로 검색하면 pencil과 picturelist 두 가지 상품이 검색되므로 p는 pencil의 고유 검색어가 아닙니다.
# e,n,c,i,l도 마찬가지로, pencil과 다른 상품이 함께 검색되므로 pencil의 고유 검색어가 아닙니다.
# en,nc,pe중 하나를 검색했을 때 pencil 하나만 검색됩니다. 따라서 pencil의 가장 짧은 고유 검색어는 en,nc,pe 3가지입니다.
# enc, nci, pencil 등도 고유 검색어지만, 더 짧은 고유 검색어가 존재하므로 가장 짧은 고유 검색어에서 제외됩니다.
# 쇼핑몰에 등록된 상품의 이름을 담은 문자열 배열 goods가 매개변수로 주어졌을 때, 가장 짧은 고유 검색어 목록을 순서대로 문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

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