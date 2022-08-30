def minJumps(arr):
    n = len(arr)
    dp = [100] * n
    dp[-1] = 0
    for i in range(n-2, -1, -1):
        for j in range(arr[i]):
            if i+j+1 < n: dp[i] = min(dp[i], 1+dp[i+j+1])
    return dp[0]

def minJumps2(arr):
    n = len(arr)
    dp = [100] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if arr[j]+j >= i: dp[i] = min(dp[i], 1+dp[j])
    return dp[n-1] 

#main:

arr = [3, 4, 2, 1, 2, 1]
arr2 = [4, 1, 5, 3, 1, 3, 2, 1, 8]
res = minJumps2(arr)
print(res)