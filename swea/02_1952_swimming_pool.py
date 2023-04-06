import time

start = time.time()

#-------------------answer 1------------------#
def dfs(exp, idx):
    global min_val
    if idx >= 12:
    #11월과 12월이 세달 이용권을 할 때가 있을 것이기 때문에, 12일때가 아닌 12보다 클 때라고 설정해줌
    #사실 12월은 무조건 세 달이 아닌 한 달혹은 일 이용권을 하는 것이 이득이겠지만 그에 따른 처리를 해주는 것보다
    #이렇게 처리를 해주는 편이 훨씬 간편합니다.
        if min_val > exp:
            min_val = exp
        return
    if month[idx]*ticket[0] < ticket[1]: #한 달을 모두 일 이용권으로 사용하는게 한 달이용권보다 쌀 때
        dfs(exp+month[idx]*ticket[0], idx+1)
    else: # 한달 이용권이 더 쌀 때 
        dfs(exp+ticket[1], idx+1)
    if month[idx]: #만약 그 달에 0일이면 세 달 이용권을 시작하지 않아도 되니까 솎아주기
        dfs(exp+ticket[2], idx+3) #세 달 이용권일 때 idx 처리 주의!


T = int(input())

for test_case in range(1, T+1):
    ticket = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_val = ticket[3] #일년 이용권을 최소값으로 설정해주기
    dfs(0,0)
    print('#{} {}'.format(test_case, min_val))
#-------------------answer 2-----------------#
T = int(input())
for t in range(1, T+1):
    #일, 1달, 3달, 1년 이용권
    price_list = list(map(int, input().split()))
    #월별 이용날
    month_list = list(map(int, input().split()))
    #결과 저장 변수 그 달의 최저값을 저장한다.
    result_list = [0] * 13
    for n in range(1, 13):
        #가격을 저장할 임시변수
        a = [0, 0, 987654321, 987654321]
        #일권으로 계산했을때, 전달비용 + 참여일수 * 일비
        a[0] = result_list[n-1] + month_list[n-1] * price_list[0]
        #1달권으로 계산했을때, 전달비용 + 1달권 비용
        a[1] = result_list[n-1] + price_list[1]
        #3달권으로 계산했을때, 3달 전비용 + 3달권비용
        if n >= 3:   a[2] = result_list[n-3] + price_list[2]
        #1년권으로 계산했을때, 1년비용
        if n >= 12:   a[3] = price_list[3]
        #현시점에서 제일 적은 비용의 값을 넣는다.
        result_list[n] = min(a)
    print('#{} {}'.format(t, result_list[12]))


print("time :", time.time() - start)