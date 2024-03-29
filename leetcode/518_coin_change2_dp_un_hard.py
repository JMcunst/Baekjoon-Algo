# Input : amount = 5, coins = [1,2,5]
# Output : 4

# DP Unbounded Knapsack (hard)

# Memoization Code
def solution1(amount, coins):
    cache = {}

    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i,a) in cache:
            return cache[(i,a)]

        cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i,a)]

    return dfs(0,0)

# O(n*m) Space DP
def solution2(amount, coins):
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i+1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]

# O(n) Space DP
def solution3(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]]
        dp = nextDP
    return dp[amount]

amount = 5
coins = [1,2,5]
res = solution3(amount, coins)

print(res)

