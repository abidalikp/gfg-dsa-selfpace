def LIS(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]: dp[i] = max(dp[i], 1+dp[j])
    return dp

def LBitonicS(arr):
    lis = LIS(arr)
    lbs = LIS(arr[::-1])
    lbs = lbs[::-1]
    ans = lis[0] + lbs[0]
    for i in range(len(arr)):
        ans = max(lis[i] + lbs[i], ans)
    return ans-1

#main:

arr = [1, 4, 3, 4]

res = LBitonicS(arr)

print(res)