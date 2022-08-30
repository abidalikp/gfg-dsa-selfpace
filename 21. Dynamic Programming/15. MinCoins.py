def minCoinsT(coins, val):
    dp = [0] + [1e7] * val
    for i in range(1, val+1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], 1+dp[i-c])
    return dp[val]


def minCoinsR(coins, val):
    if val == 0: return 0
    res = 1e7
    for i in range(len(coins)):
        if coins[i] <= val:
            res = min(res, 1+minCoinsR(coins, val-coins[i]))
    return res

#main:

coins = [3, 4, 1]
val = 5

res = minCoinsT(coins, val)
res2 = minCoinsR(coins, val)

print(res)
print(res2)