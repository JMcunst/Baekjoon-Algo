from collections import deque

def solution(arr, processes):
    answer = []

    on_heap = deque()
    wait_heap = deque()

    t = 0
    while t >= 0 and t < 8:
        if on_heap and str(t) == on_heap[0][2]:
            on_heap.popleft()
            # print(on_heap)
        if len(on_heap) == 0 and len(wait_heap) > 0:
            on_heap.append(wait_heap.popleft())
        # if str(t) == on_heap[0][2]:
        #     on_heap.popleft()
        print(len(processes))
        for proc in processes:
            list_pro = proc.split(' ')
            end_time = list_pro[1] + list_pro[2]

            if str(t) == list_pro[1]:
                if wait_heap and wait_heap[0][0].startswith('w'): # 대기중인 쓰기작업
                    if list_pro[0].startswith('w'):
                        st_w = []
                        while wait_heap[0][0] == 'write':
                            st_w.append(wait_heap.popleft())
                        wait_heap.append(list_pro)
                        while st_w:
                            wait_heap.appendleft(st_w.pop())
                    else:
                        wait_heap.append(list_pro)
                elif on_heap: 
                    if str(on_heap[0]).startswith('w'): # 쓰기작업중이면 전부 대기큐
                        if list_pro[0].startswith('w'):
                            st_w = []
                            while wait_heap[0][0] == 'write':
                                st_w.append(wait_heap.popleft())
                            wait_heap.append(list_pro)
                            while st_w:
                                wait_heap.appendleft(st_w.pop())
                        else:
                            wait_heap.append(list_pro)
                    else:                               # 읽기 작업중이면 
                        if list_pro[0].startswith('r'):  # 다음 읽기 작업이면 같이 넣기
                            on_heap.append(list_pro)
                        else:
                            wait_heap.append(list_pro)
                else: 
                    on_heap.append(list_pro)


        # print('t:',t)
        # print('on_heap:', on_heap)
        # print('wait_heap:', wait_heap)
        # print('------------------')

        
        t += 1

    return answer


# arr = spot 지점, process = 스케줄
input_arr1 = ["1","2","4","3","3","4","1","5"]
input_pros1 = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]
# result1 = ["24","3415","4922","12492215","13"]

input_arr2 = ["1","1","1","1","1","1","1"]
input_pros2 = ["write 1 12 1 5 8", "read 2 3 0 2", "read 5 5 1 2", "read 7 5 2 5", "write 13 4 0 1 3", "write 19 3 3 5 5", "read 30 4 0 6", "read 32 3 1 5"]
# result2 = ["338","38","8888","3385551","38555","29"]

res = solution(input_arr1, input_pros1)
print('res::',res)

