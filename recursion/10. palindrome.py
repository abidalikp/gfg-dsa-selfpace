def helper(s, low, high):
    if low >= high: return True
    if s[low] != s[high]: return False
    return helper(s, low+1, high-1)

def isPalindrome(s):
    return helper(s, 0, len(s)-1)


#main:

s = "axcxa"

res = isPalindrome(s)

print(res)