def getLeaders(arr):
    n = len(arr)
    lsf = arr[-1]
    ans = [lsf]
    for i in range(n-1, -1, -1):
        if arr[i] > lsf:
            ans.append(arr[i])
            lsf = arr[i]
    return ans[::-1]

#main:

arr = [7, 10, 4, 3, 6, 5, 2]

ans = getLeaders(arr)

print(ans)