def minPagesMyWay(arr, k, i, j):
    if k == 1: return sum(arr[i:j+1])
    res = 1e3
    for l in range(i, j):
        res = min(res, max(minPagesMyWay(arr, k-1, i, l), 
                            minPagesMyWay(arr, k-1, l+1, j)))
    return res

def minPagesRec(arr, k, n):
    if k == 1: return sum(arr[:n])
    if n == 1: return arr[0]
    return min([max(minPagesRec(arr, k-1, i), sum(arr[i:n])) for i in range(1, n)])

def minPagesDP(arr, k):
    n = len(arr)
    dp = [[1e3 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            if i == 1: dp[i][j] = sum(arr[:j])
            elif j == 1: dp[i][j] = arr[0]
            else: dp[i][j] = min([max(dp[i-1][p], sum(arr[p:j])) for p in range(1, j)])
    return dp[k][n]

#main:

# arr = [10, 5, 30, 1, 2, 5, 10, 10]
arr = [10, 20, 30, 40]
k = 2

res = minPagesMyWay(arr, k, 0, len(arr)-1)
res1 = minPagesRec(arr, k, len(arr))
res2 = minPagesDP(arr, k)

print(res)
print(res1)
print(res2)