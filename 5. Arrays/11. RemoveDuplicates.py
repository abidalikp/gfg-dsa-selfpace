def removeDuplicates(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != res[-1]: res.append(arr[i])
    return res

def removeDupicatesInplace(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]


#main:

l = [10, 10, 20, 20, 30, 40, 40, 40]

ans = removeDuplicates(l)
removeDupicatesInplace(l)

print(l)