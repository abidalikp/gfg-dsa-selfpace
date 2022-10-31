def maxSum(arr):
    n = len(arr)

    maxsum = arr[0]
    for i in range(n):
        currsum = 0
        for j in range(i, n):
            currsum += arr[j]
            maxsum = max(maxsum, currsum)
    return maxsum

def maxSumOptim(arr):
    n = len(arr)

    if max(arr) < 0: return max(arr)

    maxsum = 0
    currsum = 0
    for i in range(n):
        currsum = max(arr[i]+currsum, arr[i])
        maxsum = max(maxsum, currsum) 
    return maxsum        

#main:

# l = list(map(int, input().strip().split()))

l = [2, 3, -8, 7, -1, 2, 3]
# l = [5, 8, 3]
# l = [-6, -1, -8]
# l = [-5, 1, -2, 3, -1, 2, -2]

ans = maxSum(l)
ans2 = maxSumOptim(l)

print(ans)
print(ans2)