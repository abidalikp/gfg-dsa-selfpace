def helper(arr, s, n):
    if n == 0: return 1 if s == 0 else 0
    return helper(arr, s, n-1) + helper(arr, s-arr[n-1], n-1)

def subsetSum(arr, s):
    return helper(arr, s, len(arr))


#main:

arr = [10, 5, 2, 3, 6]
s = 0
res = subsetSum(arr, s)
print(res)