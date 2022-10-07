def isSorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]: return False
    return True


#main:

l1 = [1, 2, 13, 4, 5]
l = [1, 2, 3, 4, 5]

ans = isSorted(l)

print(ans)