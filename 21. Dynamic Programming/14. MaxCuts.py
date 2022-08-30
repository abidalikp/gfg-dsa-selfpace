def maxCuts(n, a, b, c): # T-> O(n) & S-> O(n)
    dp = [0] + [-1] * n
    for i in range(1, n+1):
        if i-a >= 0: dp[i] = max(dp[i], dp[i-a])
        if i-b >= 0: dp[i] = max(dp[i], dp[i-b])
        if i-c >= 0: dp[i] = max(dp[i], dp[i-c])
        if dp[i] != -1: dp[i] += 1
    return dp[n]

def maxCutsR(n, a, b, c):
    if n == 0: return 0
    if n < 0: return -1
    res = max(maxCutsR(n-a, a, b, c),
                maxCutsR(n-b, a, b, c),
                maxCutsR(n-c, a, b, c))
    return res if res == -1 else res + 1

#main:

res = maxCuts(10, 2, 3, 3)

print(res)