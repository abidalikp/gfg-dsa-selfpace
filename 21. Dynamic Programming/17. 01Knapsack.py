def maxValueR(v, w, W, n):
    if n == 0 or w == 0: return 0
    if w[n-1] <= W: 
        return max(v[n-1] + maxValueR(v, w, W-w[n-1], n-1), 
                    maxValueR(v, w, W, n-1))
    else: return maxValueR(v, w, W, n-1)

def maxValueT(v, w, W):
    n = len(v)
    dp = [[-100 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or  w == 0: dp[i][j] = 0
            elif w[i-1] <= j: 
                dp[i][j] = max(dp[i-1][j], 
                                v[i-1] + dp[i-1][j-w[i-1]])
            else: dp[i][j] = dp[i-1][j] 
    return dp[n][W]

#main:

v = [10, 40, 30, 50]
w = [5, 4, 6, 3]
W = 10

res = maxValueR(v, w, W, len(v))
res2 = maxValueT(v, w, W)

print(res)
print(res2)