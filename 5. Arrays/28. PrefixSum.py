def prefixSum(arr):
    presum = [0]
    for v in arr:
        presum.append(presum[-1] + v)
    return presum

# ---------- 1 --------------

def getSum(arr, i, j):
    return arr[j+1] - arr[i]

# l = [2, 8, 3, 9, 6, 5, 4]

# presum = prefixSum(l)

# ans = []
# queries = [(0, 2), (1, 3), (2, 6)]
# for query in queries:
#     ans.append(getSum(presum, query[0], query[1]))

# print(*ans)

# ---------- 2 --------------

def hasEquilibrium(arr):
    total_sum = sum(arr)
    curr_sum = 0
    for curr_element in arr:
        if curr_sum == total_sum - curr_element: return True
        curr_sum += curr_element
    return False


l = [3, 4, 8, -9, 20, 6]
# l = [4, 2, -2]
# l = [4, -4, 2]

ans = hasEquilibrium(l)

print(ans)