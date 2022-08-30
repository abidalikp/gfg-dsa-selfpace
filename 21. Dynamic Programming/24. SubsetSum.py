def count(arr, s, i):
    if i == 0: return 1 if s == 0 else 0
    return count(arr, s, i-1) + count(arr, s-arr[i-1], i-1)

def countDP(arr, s):
    n = len(arr)
    dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j == 0: dp[i][j] = 1
            elif i == 0: dp[i][j] = 0
            else: dp[i][j] = dp[i-1][j] + (dp[i-1][j-arr[i-1]] if j >= arr[i-1] else 0) 
    return dp[n][s]

#main:

arr = [10, 5, 2, 3, 4, 6] #2
arr1 = [1, 2, 3, 4] 
arr2 = [10, 20, 15]
s = 8

res = count(arr, s, len(arr))
res2 = countDP(arr, s)

print(res)
print(res2)