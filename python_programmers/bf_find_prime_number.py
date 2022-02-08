from itertools import permutations

numbers = "011"

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    nums = [n for n in numbers]
    print('nums::', nums)
    pernum = []
    for i in range(1, len(numbers)+1):
        pernum += list(permutations(nums, i)) 
    print('pernum::', pernum)
    new_nums = [int(("").join(p)) for p in pernum]
    print('new_nums::', new_nums)
    my_nums = list(set(new_nums))
    print('my_nums::', my_nums)

    for n in my_nums:
        if is_prime_number(n) == True:
            answer += 1
    print(answer)
    return answer

solution(numbers)