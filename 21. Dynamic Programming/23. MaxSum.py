def maxSumR(arr, i):
    if i < 0: return 0
    return max(maxSumR(arr, i-1), arr[i] + maxSumR(arr, i-2))

def maxSumDP(arr):
    n = len(arr)
    if n == 1: return arr[0]
    dp = [arr[0], max(arr[0], arr[1])]
    for i in range(2, n):
        dp.append(max(dp[i-1], arr[i]+dp[i-2]))
    return dp[n-1]

def maxSum(arr):
    n = len(arr)
    if n == 1: return arr[0]
    prev = arr[0]
    curr = max(arr[0], arr[1])
    for i in range(2, n):
        prev, curr = curr, max(curr, prev+arr[i])
    return curr

#main:

arr = [10, 5, 15, 20, 2, 30]

res = maxSumR(arr, len(arr)-1)
res1 = maxSumDP(arr)
res2 = maxSum(arr)

print(res)
print(res1)
print(res2)