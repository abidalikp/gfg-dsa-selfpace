def rLCS(s1, s2, i, j):
    if i == 0 or j == 0: return 0
    if s1[i-1] == s2[j-1]: return 1 + rLCS(s1, s2, i-1, j-1)
    return max(rLCS(s1, s2, i-1, j), rLCS(s1, s2, i, j-1))

def mLCS(s1, s2, i, j):
    if memo[i][j] == -1:
        if i == 0 or j == 0: memo[i][j] = 0
        elif s1[i-1] == s2[j-1]: memo[i][j] = 1 + rLCS(s1, s2, i-1, j-1)
        else: memo[i][j] = max(rLCS(s1, s2, i-1, j), rLCS(s1, s2, i, j-1))
    return memo[i][j]

def tLCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = 0
    for j in range(n2+1):
        dp[0][j] = 0
    for i in range(n1+1):
        for j in range(n2+1):
            if i == 0 or j == 0: dp[i][j] = 0
            elif s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp
#main:

s1 = 'axyz'
n1 = len(s1)
s2 = 'baz'
n2 = len(s2)

memo = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

res1 = rLCS(s1, s2, len(s1), len(s2))
res2 = mLCS(s1, s2, len(s1), len(s2))
res3 = tLCS(s1, s2)
print(res3, res1, res2)