def getCount(s):
    d = dict()
    for char in s:
        if char in d: d[char] += 1
        else: d[char] = 1
    return d

def isAnagram(s1, s2):
    return list(s1).sort() == list(s2).sort()

def isAnagramOptim(s1, s2):
    # 1. Get count of each unique characters in s1
    d1 = getCount(s1)
    # 2. Get count of each unique characters in s2
    d2 = getCount(s2)
    # 3. Compare count of each element in both s1 and s2
    if len(d1) != len(d2): return False
    for char in d1.keys():
        if d1[char] != d2[char]: return False
    return True

#main:

s1 = 'listen'
s2 = 'silent'

# s1 = 'aaabc'
# s2 = 'cabaa'

# s1 = 'aaa'
# s2 = 'bab'

ans = isAnagram(s1, s2)

print(ans)