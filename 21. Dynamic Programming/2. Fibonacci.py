def rFib(n):
    if n == 0 or n == 1: return n
    return rFib(n-1) + rFib(n-2)

def mFib(n):
    if memo[n] == -1:
        if n == 0 or n == 1: memo[n] = n
        else: memo[n] = mFib(n-1) + mFib(n-2)
    return memo[n]

def tFib(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


#main:

n = 7
memo = [-1] * (n+1)

print(rFib(n))
print(mFib(n))
print(tFib(n))