import heapq

numbers = [5, 9, 7, 11]

def find_max_sum(numbers):
    numbers.sort(reverse=True)
    
    heapq.heapify(numbers)

    max_fst = heapq.heappopright(numbers) 
    max_sec = heapq.heappopright(numbers) 

    return max_fst+max_sec

max = find_max_sum(numbers)
