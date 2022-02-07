import collections

answer = []
graph = collections.defaultdict(list)
print(graph, graph[0])

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(tickets)

def dfs(s):
    print(s)
    while graph[s]:
        print('graph[s]:',graph[s], 'graph::', graph)
        dfs(graph[s].pop(0))
        print('poped')

    if not graph[s]:
        print('111::',s)
        answer.append(s)
        return

def solution(tickets):
    
    for de,ar in tickets:
        print(de, ar)
        graph[de].append(ar)
    print('appended::',graph, 'items::', graph.items())
    for de, ar in graph.items():
        print('item', de, ar)
        graph[de].sort()
        
    print('sorted::',graph)
    dfs("ICN")

    print('answer::',answer, 'answer[::-1]',answer[::-1])
    return answer[::-1]

solution(tickets)