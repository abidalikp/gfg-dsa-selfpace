def maxActivity(arr):
    arr.sort(key = lambda k: k[1])
    ans = 0
    end = 0
    for x in arr:
        if x[0] >= end:
            ans += 1
            end = x[1]
    return ans    

#main:

arr = [(1,3), (2,4), (3,8), (10,11)]

res = maxActivity(arr)

print(res)