def LIS(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]: dp[i] = max(dp[i], 1+dp[j])
    return max(dp)

def minDelete(arr):
    return len(arr)-LIS(arr)

#main:

arr = [4, 2, 5]
res = minDelete(arr)
print(res)