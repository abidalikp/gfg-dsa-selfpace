def maxDifference(arr): # O(n2)
    largest = arr[-1]-arr[0]
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j]-arr[i] > largest: largest = arr[j]-arr[i]
    return largest

def maxDifferenceOptim(arr):
    n = len(arr)
    smallest = arr[0]
    largest = arr[-1]-arr[0]
    for i in range(1, n):
        largest = max(largest, arr[i]-smallest)
        smallest = min(smallest, arr[i])
    return largest


#main:

#input
arr = [2, 3, 10, 6, 4, 8, 1]

#output -> 8
ans1 = maxDifference(arr)
ans2 = maxDifferenceOptim(arr)

print(ans1)
print(ans2)


