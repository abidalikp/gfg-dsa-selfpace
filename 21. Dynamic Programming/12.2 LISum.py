def LISum(arr):
    n = len(arr)
    dp = arr[:]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]: dp[i] = max(dp[i], arr[i]+dp[j])
    return max(dp)

#main:

arr = [1, 20, 2, 3, 4, 5]
res = LISum(arr)
print(res)