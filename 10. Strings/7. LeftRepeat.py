def getLeftRepeat(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]: return i
    return -1

def getCount(s):
    d = dict()
    for char in s:
        if char in d: d[char] += 1
        else: d[char] = 1
    return d

def getLeftRepeat2(s):
    d = getCount(s)
    for i, char in enumerate(s):
        if d[char] > 1: return i
    return -1

def getLeftRepeat3(s):
    d = dict()
    res = -1
    for i, char in enumerate(s):
        if char in d:
            if res == -1: res = d[char]
            elif d[char] < res: res = d[char]
        else: d[char] = i
    return res

def getLeftRepeatOptim(s):
    n = len(s)
    d = dict()
    res = -1
    for i in range(n-1, -1, -1):
        if s[i] in d: res = i
        else: d[s[i]] = 1
    return res

#main:

# s = input()

s = 'geeksforgeeks'
# s = 'abbcc'
# s = 'abcd'

# ans = getLeftRepeat(s)
# ans = getLeftRepeat2(s)
# ans = getLeftRepeat3(s)
ans = getLeftRepeatOptim(s)

print(ans)