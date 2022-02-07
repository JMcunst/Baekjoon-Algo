
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(commands, commands[0], commands[0][1], len(commands))

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        list = []
        for j in range(commands[i][1]):
            if j >= commands[i][0]-1:
                print('i::', i, 'j::', j)
                list.append(array[j])
        list.sort()
        print('list::',list)
        answer.append(list[commands[i][2]-1])

    print('answer::', answer)
    return answer

solution(array, commands)


# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))