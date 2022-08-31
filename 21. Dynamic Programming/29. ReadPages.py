def minPagesMyWay(arr, k, i, j):
    if k == 1: return sum(arr[i:j+1])
    res = 1e3
    for l in range(i, j):
        res = min(res, max(minPagesMyWay(arr, k-1, i, l), 
                            minPagesMyWay(arr, k-1, l+1, j)))
    return res



#main:

arr = [10, 5, 30, 1, 2, 5, 10, 10]
k = 3

res = minPagesMyWay(arr, k, 0, len(arr)-1)

print(res)