citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for idx , citation in enumerate(citations):
        print('idx::',idx,'citation::',citation)
        if idx >= citation:
            print('fidx::',idx,'fcitation::',citation)
            return idx
    return len(citations)

# def solution(citations):
#     citations.sort(reverse=True)
#     # 
#     obj1 = enumerate(citations, start=1)
#     # [(1, 3),(2, 0),(3, 6),(4, 1),(5, 5)]
#     print(obj1)
#     print(map(min, enumerate(citations, start=1)))
#     answer = max(map(min, enumerate(citations, start=1)))
#     print(answer)
#     return answer

solution(citations)


