def isPalindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]: return False
    return True

def minCutsMyWay(s):
    n = len(s)
    if isPalindrome(s): return 0
    res = 100
    for i in range(1, n):
        res = min(res, 1 + minCutsMyWay(s[:i]) + minCutsMyWay(s[i:]))
    return res
    # return min([1 + minCuts(s[:i]) + minCuts(s[i:]) for i in range(1, n)])

def minCutsR(s, i, j):
    if isPalindrome(s[i:j+1]): return 0
    return min([1 + minCutsR(s, i, k) + minCutsR(s, k+1, j) for k in range(i, j)])

def minCutsDP(s):
    n = len(s)
    dp = [[1e3 for _ in range(n)] for _ in range(n)]
    for gap in range(n):
        for i in range(n-gap):
            j = i+gap
            if i == j: dp[i][j] = 0
            elif isPalindrome(s[i:j+1]): dp[i][j] = 0
            else: dp[i][j] = min([1 + dp[i][k] + dp[k+1][j] for k in range(i, j)])
    return dp[0][n-1]

#main:

s = 'geek'

res = minCutsMyWay(s)
res1 = minCutsR(s, 0, len(s)-1)
res2 = minCutsDP(s)

print(res)
print(res1)
print(res2)