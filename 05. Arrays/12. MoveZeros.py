def moveZerosEnd(arr):
    count = 0
    ans = []
    for x in arr:
        if x != 0: ans.append(x)
        else: count += 1
    while count:
        ans.append(0)
        count -= 1
    return ans 

def moveZerosEndInplace(arr):
    n = len(arr)
    index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

#main:

l = [10 , 20, 0, 9, 0, 0, 10, 11, 0]


# ans = moveZerosEnd(l)
moveZerosEndInplace(l)

print(l)