def minTrailsR(f, e):
    if e == 1 or f == 1 or f == 0: return f
    return min([(1+max(minTrailsR(x-1, e-1), minTrailsR(f-x, e))) for x in range(1, f+1)])
    # res = 100
    # for x in range(1, f+1):
    #     res = min(res, 1+max(minTrailsR(x-1, e-1), minTrailsR(f-x, e)))
    # return res

def minTrailsDP(f, e):
    dp = [[100 for _ in range(e+1)] for _ in range(f+1)]
    for i in range(f+1):
        for j in range(1, e+1):
            if i == 1 or j == 1 or i == 0: dp[i][j] = i
            else:
                for x in range(1, i+1):
                    dp[i][j] = min(dp[i][j], 1+max(dp[x-1][j-1], dp[i-x][j]))
    return dp[f][e]
#main:

e = 10
f = 10

res = minTrailsDP(f, e)
res2 = minTrailsR(f, e)

print(res)
print(res2)