def ceilIndex(x, arr):
    left = 0
    right = len(arr)-1
    while left<right:
        mid = (left+right)//2
        if x == arr[mid]: return mid
        elif x < arr[mid]: right = mid - 1
        else: left = mid + 1
    return right

def optimalLIS(nums):
    tail = [nums[0]]
    for x in nums:
        if x > tail[-1]: tail.append(x)
        else:
            idx = ceilIndex(x, tail)
            tail[idx] = x
    return len(tail)

def LIST(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)
    

def LISM(nums, i, curr, memo):
    if memo[i] == -1:
        if i == len(nums): memo[i] = 0
        elif nums[i] > curr: memo[i] = max(1 + LIS(nums, i+1, nums[i]),
                                            LIS(nums, i+1, curr)) 
        else: memo[i] = LIS(nums, i+1, curr)
    return memo[i]

def LIS(nums, i, curr):
    if i == len(nums): return 0
    if nums[i] > curr: return max(1 + LIS(nums, i+1, nums[i]),
                                    LIS(nums, i+1, curr)) 
    return LIS(nums, i+1, curr)

#main:

nums = [1, 2, 5, 3, 6, 3]
n = len(nums)
memo = [-1] * (n+1)

res = LIS(nums, 0, 0)
res1 = LISM(nums, 0, 0, memo)
res2 = LIST(nums)
res3 = optimalLIS(nums)

print(res,res1,res2,res3)