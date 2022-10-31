def consecutiveOnes(arr):
    n = len(arr)

    ans = 0
    freq = 0
    for v in arr:
        if v == 1: 
            freq += 1
            ans = max(ans, freq)
        else: freq = 0
    return ans

#main:

l = [0, 1, 1, 0, 1, 0]
# l = [1, 0, 1, 1, 1, 1, 0, 1, 1]
# l = [1, 1, 1, 1]
# l = [0, 0, 0]

ans = consecutiveOnes(l)

print(ans)