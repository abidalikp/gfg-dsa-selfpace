#Catalan Number = (1/n) * (2n)C(n)

def countBSTR(n):
    if n == 0: return 1
    res = 0
    for i in range(n):
        left = countBSTR(i)
        right = countBSTR(n-i-1)
        res += left*right
    return res
    
def countBSTDP(n):
    dp = [1] + [0] * n
    for k in range(1, n+1):
        for i in range(k):
            dp[k] += dp[i] * dp[k-i-1]
    return dp[n]

#main:

n = 6
res = countBSTR(n)
res1 = countBSTDP(n)
print(res)
print(res1)