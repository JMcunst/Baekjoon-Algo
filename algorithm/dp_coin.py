# dp coin 문제
k = 2000

coins = [1, 5, 10, 50, 100]

dp = [0] * (k+1)


for i in range(1, k+1):
    dp[i] = -1
    
    for j in range(len(coins)):
        if coins[j] <= i:  # 만들려는 금액  i coins[j] 기준코인(1,10,15...)
            if dp[i-coins[j]] < 0: continue  # 기준코인으로는 i를 만들 수 없음.
            if dp[i] < 0:
                dp[i] = dp[i - coins[j]] + 1
            elif dp[i - coins[j]] + 1 < dp[i]:
                dp[i] = dp[i - coins[j]] + 1

print(dp[k])