def majorityElement(arr): # Morris counting principle
    n = len(arr)
    res = 0
    count = 0
    for i in range(n):
        if arr[i] == arr[res]: count += 1
        else: count -= 1
        if count == 0: 
            res = i
            count = 1
    count = 0
    for val in arr:
        if val == arr[res]: count += 1
    
    if count > n//2: return res
    return -1

#main:

l = [8, 3, 4, 8, 8]
# l = [3, 7, 4, 7, 7, 5]
# l = [20, 30, 40, 50, 50, 50, 50]

ans = majorityElement(l)

print(ans)