def longSeq(arr):
    n = len(arr)

    longest = 1
    currlong = 1
    for i in range(1, n):
        if arr[i-1]%2 != arr[i]%2: currlong += 1
        else: currlong = 1
        longest = max(longest, currlong)
    return longest 

#main:

# l = list(map(int, input().strip().split()))

l = [10, 12, 14, 7, 8]
# l = [7, 10, 13, 14]
# l = [10, 12, 8, 4]

ans = longSeq(l)

print(ans)