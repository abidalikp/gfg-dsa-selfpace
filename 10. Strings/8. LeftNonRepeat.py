def getNonRepeatLeft(s):
    n = len(s)
    ans = -1
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]: break
        else: 
            ans = i
            break
    return ans

def getCount(s):
    d = dict()
    for char in s:
        if char in d: d[char] += 1
        else: d[char] = 1
    return d

def getNonRepeatLeft2(s):
    
    d = getCount(s)
    for i, char in enumerate(s):
        if d[char] == 1: return i
    return -1

def getNonRepeatLeftOptim(s):
    pass


#main:

s = 'geeksforgeeks'
# s = 'abbcc'
# s = 'abcd'

ans = getNonRepeatLeftOptim(s)

print(ans)