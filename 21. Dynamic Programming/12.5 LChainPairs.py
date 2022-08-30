def longChain(arr):
    n = len(arr)
    arr.sort()
    dp = [1] * n
    for i in range(n):
        for j in range(n):
            if arr[i][0] > arr[j][1]: dp[i] = max(dp[i], 1+dp[j])
    return max(dp)

#main:

arr = [(5,24), (39,60), (15,28), (27,40), (50,90)]

res = longChain(arr)

print(res)