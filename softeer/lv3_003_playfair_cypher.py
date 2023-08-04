import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

msg = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

answer = ''

board = []
for k in key:
    if k not in board:
        board.append(k)

for alp in alphabet:
    if alp not in board:
        board.append(alp)

nboard = []
st = 0
for _ in range(5):
    arr = []

    for i in range(st, st+5):
        arr.append(board[i])
    nboard.append(arr)
    st += 5

encript_msg = []
is_remaining = True
while is_remaining:
    if len(msg) < 2:
        print('END',msg)
        tm = msg[0] + 'X' 
        encript_msg.append(tm)
        is_remaining = False
    else:
        print('ING',msg)
        tmsg = msg[:2]

        if tmsg[0] == tmsg[1]:
            if tmsg[0] == 'X':
                tm = tmsg[0] + 'Q'
                encript_msg.append(tm)
            else:
                tm = tmsg[0] + 'X'
                encript_msg.append(tm)
            msg = msg[1:]
        else:
            encript_msg.append(tmsg)
            if len(msg) == 2:
                is_remaining = False
            else:
                msg = msg[2:]

for em in encript_msg:
    fw, sw = em[0], em[1]
    fw_x, fw_y = -1,-1
    sw_x, sw_y = -1,-1
    ans_fw = ''
    ans_sw = ''


    for i in range(5):
        for j in range(5):
            if nboard[i][j] == fw: 
                fw_x, fw_y = i, j
            if nboard[i][j] == sw:
                sw_x, sw_y = i, j

    if fw_x == sw_x:
        ans_fw = nboard[fw_x][(fw_y+1)%5]
        ans_sw = nboard[sw_x][(sw_y+1)%5]
    elif fw_y == sw_y:
        ans_fw = nboard[(fw_x+1)%5][fw_y]
        ans_sw = nboard[(sw_x+1)%5][sw_y]
    else:
        ans_fw = nboard[fw_x][sw_y]
        ans_sw = nboard[sw_x][fw_y]

    ans_w = ans_fw + ans_sw
    answer += ans_w

print(answer)