def isPalindrome(s):
    n = len(s)

    for i in range(n//2):
        if s[i] != s[n-i-1]: return False
    return True

#main:

s = 'ABCDCBA'
# s = 'ABBA'
# s = 'geeks'

ans = isPalindrome(s)

print(ans)