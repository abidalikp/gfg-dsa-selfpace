def secondLargest(arr):
    largest = max(arr)
    index = -1
    for i in range(len(arr)):
        if largest != arr[i]:
            if index == -1 or arr[i] > arr[index]: index = i
    return index        

#main:

l = [1,42,23,4,15,56,17,38,9]

ans = secondLargest(l)

print(ans)