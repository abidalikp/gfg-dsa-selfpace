def maxWater(arr):
    n = len(arr)

    left = [arr[0]]
    for i in range(1, n):
        left.append(max(left[-1], arr[i]))

    right = [arr[-1]]
    for i in range(1, n):
        right.append(max(right[-1], arr[i]))
    right.reverse()

    water = 0
    for i in range(1, n-1):
        water += min(left[i], right[i]) - arr[i]

    return water

#main:

l = [3, 0, 1, 2, 5]
l = [2, 0, 2]
# l = [1, 2, 3]
# l = [3, 2, 1]

ans = maxWater(l)

print(ans)