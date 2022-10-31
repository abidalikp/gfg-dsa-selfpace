def minFlips(arr):
    n = len(arr)
    
    flip = 0
    if arr[0] == arr[-1] and arr[0] == 0: flip = 1

    count = 0
    for i in range(n):
        if arr[i] == flip: count += 1
        elif count:
            print('From ', i-count, ' to ', i-1)
            count = 0
    if count: print('From ', n-count, ' to ', n-1)

def minFlips2(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print('From', i, end=' ')
            else: print('to', i-1)
    if arr[-1] != arr[0]: print('to', n-1)

#main:

l = [1, 1, 0, 0, 0, 1]
# l = [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
# l = [1, 1, 1]
# l = [1, 0]

minFlips2(l)