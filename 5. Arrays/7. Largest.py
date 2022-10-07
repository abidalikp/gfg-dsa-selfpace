def indexOfLargest(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] > arr[index]: index = i
    return index


#main:

l1 = [1,42,23,4,15,56,17,38,9]
l = [11]

ans = indexOfLargest(l)

print(ans)