def editDistanceT(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def editDistanceM(s1, s2, m, n, memo):
    if memo[m][n] == -1:
        if m == 0: memo[m][n] = n
        elif n == 0: memo[m][n] = m
        elif s1[m-1] == s2[n-1]: memo[m][n] = editDistance(s1, s2, m-1, n-1)
        else: memo[m][n] = 1 + min(editDistance(s1, s2, m-1, n),
                            editDistance(s1, s2, m, n-1),
                            editDistance(s1, s2, m-1, n-1))
    return memo[m][n]

def editDistance(s1, s2, m, n):
    if m == 0: return n
    if n == 0: return m
    if s1[m-1] == s2[n-1]: return editDistance(s1, s2, m-1, n-1)
    else: return 1 + min(editDistance(s1, s2, m-1, n),
                        editDistance(s1, s2, m, n-1),
                        editDistance(s1, s2, m-1, n-1))

#main:

s1 = 'saturday'
m = len(s1)
s2 = 'sunday'
n = len(s2)

memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
res1 = editDistance(s1, s2, m, n)
res2 = editDistanceM(s1, s2, m, n, memo)
res3 = editDistanceT(s1, s2)

print(res1, res2, res3)