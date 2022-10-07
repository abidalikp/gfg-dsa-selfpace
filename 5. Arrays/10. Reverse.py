def reverse(arr):
    low, high = 0, len(arr)-1
    while high>low:
        arr[low], arr[high] = arr[high], arr[low]
        high -= 1
        low += 1

#main:

l = [1, 2, 3, 4, 5]

reverse(l)

print(l)