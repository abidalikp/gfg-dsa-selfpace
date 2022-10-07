def maxSumOptim(arr):
    n = len(arr)

    if max(arr) < 0: return max(arr)

    maxsum = 0
    currsum = 0
    for i in range(n):
        currsum = max(arr[i]+currsum, arr[i])
        maxsum = max(maxsum, currsum) 
    return maxsum

def minSum(arr):
    n = len(arr)
    minsum = arr[0]
    currmin = arr[0]
    for i in range(1, n):
        currmin = min(currmin+arr[i], arr[i])
        minsum = min(minsum, currmin)
    return minsum

#Circular Subarray
def maxSumCir(arr): # O(n2)
    n = len(arr)
    maxsum = arr[0]
    for i in range(n):
        maxsum = max(maxsum, maxSumOptim(arr[i:]+arr[:i]))
    return maxsum

def maxSumCirOptim(arr):
    n = len(arr)

    normal = maxSumOptim(arr)
    
    if normal < 0: return normal
    
    circular = sum(arr)-minSum(arr)

    return max(normal, circular)

#main:

l = [5, -2, 3, 4] # => 12
# l = [2, 3, -4] # => 5
# l = [8, -4, 3, -5, 4] # => 12
# l = [-8, 7, 6] # => 13
# l = [3, -4, 5, 6, -8, 7] # => 17
# l = [-1, -2, -3]

ans = maxSumCir(l)
ans1 = maxSumCirOptim(l)

print(ans)
print(ans1)