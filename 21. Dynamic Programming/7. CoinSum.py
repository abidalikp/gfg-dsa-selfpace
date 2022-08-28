def rCount(coins, s, i):
    if i == 0 or s < 0: return 0
    if s == 0: return 1
    return rCount(coins, s, i-1) + rCount(coins, s-coins[i-1], i)

def mCount(coins, s, i):
    if memo[i][s] == -1:
        if s == 0: memo[i][s] = 1
        elif i == 0: memo[i][s] = 0
        else:
            res = mCount(coins, s, i-1)
            if coins[i-1] <= s:
                res += mCount(coins, s-coins[i-1], i)
            memo[i][s] = res
    return memo[i][s]

def tCount(coins, s):
    n = len(coins)
    dp = [[-1 for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j == 0: dp[i][j] = 1
            elif i == 0: dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]
                if coins[i-1] <= j:
                    dp[i][j] += dp[i][j-coins[i-1]]
    return dp[n][s]

#main:

coins = [2, 5, 3, 6]
n = len(coins)
s = 10
memo = [[-1 for _ in range(s+1)] for _ in range(n+1)]
res1 = rCount(coins, s, n)
res2 = mCount(coins, s, n)
res3 = tCount(coins, s)

print(res1, res2, res3)