import sys

N, M = list(map(int,input().split()))

rooms = {}
for _ in range(N):
    room = input()
    rooms[room] = [0]*9

for _ in range(M):
    input_line = input()
    room, st, en = input_line.split()
    st = int(st) -9
    en = int(en) -9

    for i in range(st, en):
        rooms[room][i] = 1

sorted_keys = sorted(rooms.keys())  
for k, key in enumerate(sorted_keys):
    print('Room', key,':')
    
    cnt = 0
    time_list = []

    st = None

    for i, sch in enumerate(rooms[key]):
        if sch == 0 and st is None:
            st = i
        elif sch == 1 and st is not None:
            en = i
            time_list.append(f"{st+9:02d}-{en+9:02d}")
            st = None
    if st is not None:
        en = len(rooms[key])
        time_list.append(f"{st+9:02d}-{en+9:02d}")

    cnt = len(time_list)

    if cnt == 0:
        print('Not available')
    elif cnt == 9:
        print('1 available:')
        print('09-18')
    else: 
        print(cnt, 'available:')
        for i in range(cnt):
            print(time_list[i])
    if k < N -1:
        print('-----')