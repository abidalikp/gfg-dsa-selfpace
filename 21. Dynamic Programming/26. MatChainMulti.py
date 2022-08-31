def minMatrix(arr):
    n = len(arr)
    if n < 3: return 0
    if n == 3: return arr[0]*arr[1]*arr[2]
    res = 100
    for i in range(1, n-1):
        res = min(res, arr[i-1]*arr[i]*arr[i+1] +
                        minMatrix(arr[:i]+arr[i+1:]))
    return res

def mChainR(arr, i, j):
    if i+1 == j: return 0
    if i+2 == j: return arr[i]*arr[i+1]*arr[j]
    # res = 100
    # for k in range(i+1, j):
    #     res = min(res, arr[i]*arr[k]*arr[j] + 
    #                       mChain(arr, i, k) + mChain(arr, k, j))
    # return res
    return min([(arr[i]*arr[k]*arr[j] + mChainR(arr, i, k) +
                        mChainR(arr, k, j)) for k in range(i+1, j)])

def mChainDP(arr):
    n = len(arr)
    dp = [[1e3 for _ in range(n)] for _ in range(n)]
    for gap in range(1, n):
        for i in range(n-gap):
            j = i+gap
            if i+1 == j: dp[i][j] = 0
            elif i+2 == j: dp[i][j] = arr[i]*arr[i+1]*arr[j]
            else: dp[i][j] = min([(arr[i]*arr[k]*arr[j] + dp[i][k] +
                                    dp[k][j]) for k in range(i+1, j)])
    return dp[0][n-1]

#main:

arr = [2, 1, 3, 4] #20

res = minMatrix(arr)
res1 = mChainR(arr, 0, len(arr)-1)
res2 = mChainDP(arr)

print(res)
print(res1)
print(res2)