import sys

M, N, K = list(map(int, input().split()))

secret_num = list(map(int, input().split()))
secret_num = ''.join(str(x) for x in secret_num)    

control_num = list(map(int, input().split()))
control_num = ''.join(str(x) for x in control_num)  

conut = 0
count = control_num.count(secret_num)

if count == 0:
    print('normal')
else:
    print('secret')