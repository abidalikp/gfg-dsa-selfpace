def maxSum(arr, k):
    n = len(arr)
    res = sum(arr[:k])
    for i in range(1, n-k):
        currsum = sum(arr[i:i+k])
        if currsum > res: res = currsum
    return res

def maxSumOptim(arr, k):
    n = len(arr)
    currsum = res = sum(arr[:k])
    for i in range(k, n):
        currsum += arr[i] - arr[i-k]
        if currsum > res: res = currsum
    return res

def givenSum(arr, s):
    n = len(arr)

    for i in range(n):
        currsum = 0
        for j in range(i, n):
            currsum += arr[j]
            if currsum == s: return 'yes'
    return 'no'

def givenSumOptim(arr, s):
    n = len(arr)
    currsum = arr[0]
    i = 0
    j = 1
    while j<n:
        if currsum == s: return 'yes'
        elif currsum > s:
            currsum -= arr[i]
            i += 1
        else:
            currsum += arr[j]
            j += 1
    return 'no'



#main:

# l = [1, 8, 30, -5, 20, 7]
# l = [5, -10, 6, 90, 3]
# k = 2

# ans = maxSum(l, k)
# ans2 = maxSumOptim(l, k)

# print(ans)
# print(ans2)

l = [1, 4, 20, 3, 10, 5]
# l = [1, 4, 0, 0, 3, 10, 5]
# l = [2, 4]
s = 33

ans = givenSumOptim(l, s)

print(ans)