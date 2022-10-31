def leftRotate(arr, d): # O(n) + O(n)
    ans = []
    for i in range(d, len(arr)):
        ans.append(arr[i])
    for i in range(d):
        ans.append(arr[i])
    return ans

def leftRotateInplace(arr, d): # O(n) + O(d) 
    n = len(arr)
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d, n):
        arr[i-d] = arr[i]
    for i in range(d):
        arr[n-d+i] = temp[i]

def reverse(arr, low, high):
    while high > low:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

def leftRotateOptim(arr, d): # O(n) + O(1)
    n = len(arr)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

#main:

l = [1, 2, 3, 4, 5]
d = 2

ans = leftRotate(l, d)
# leftRotateInplace(l, d)
leftRotateOptim(l, d)

print(ans)
print(l)