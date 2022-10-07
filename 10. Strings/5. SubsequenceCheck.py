def getSubs(s, sub, i):
    if i == len(s): return [sub]
    return getSubs(s, sub+s[i], i+1) + getSubs(s, sub, i+1)

def isSubsequence(s, sub):
    sublist = []
    sublist += getSubs(s, '', 0)
    if sub in sublist: return True
    return False 

def isSubsequenceOptim(s, sub):
    n = len(sub)
    i = 0
    for c in s:
        if i < n and c == sub[i]: i += 1
    return i == n


#main:

s = 'ABCD'
sub = 'AD'

# s = 'ABCDE'
# sub = 'AED'

ans = isSubsequenceOptim(s, sub)

print(ans)