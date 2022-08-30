def maxBridge(arr):
    n = len(arr)
    arr.sort(key = lambda k: (k[0], k[1]))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i][1] > arr[j][1]: dp[i] = max(dp[i], 1+dp[j])
    return max(dp)

#main:

arr = [(6,2), (2,6), (1,5), (4,3)]
arr2 = [(8,1), (1,2), (4,3), (3,4), (2,6), (6,7), (7,8), (5,5)]

res = maxBridge(arr2)

print(res)