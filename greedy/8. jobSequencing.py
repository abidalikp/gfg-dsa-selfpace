def maxProfit(arr, m):
    slot = [False] * m
    arr.sort(key = lambda k: k[1], reverse = True)
    ans = 0
    for d, p in arr:
        cd = d -1
        while cd >=0 and slot[cd]:
            cd -= 1
        if cd >=0:
            slot[cd] = True
            ans += p
    return ans

#main:

deadline = [4, 1, 1, 5, 5]
profit = [50, 5, 20, 10, 80]

arr = []
for d, p in zip(deadline, profit):
    arr.append((d, p))

res = maxProfit(arr, max(deadline))

print(res)