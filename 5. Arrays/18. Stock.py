def maxProfit(arr):
    n = len(arr)
    profit = 0
    for i in range(1, n):
        if arr[i]>arr[i-1]: profit += arr[i]-arr[i-1]
    return profit

#main:

l = [1, 5, 3, 8, 12]
l1 = [30, 20, 10]
l2 = [10, 20, 30]
l3 = [1, 5, 3, 1, 2, 8]

ans = maxProfit(l)

print(ans)