def isAnagram(s, p, i, j):
    d = {}
    for c in s[i:j]:
        if c in d: d[c] += 1
        else: d[c] = 1
    for c in p:
        if c in d:
            d[c] -= 1
            if d[c] < 0: return False
        else: return False
    return True

def anagramSearch(s, p):
    n = len(s)
    m = len(p)
    if m > n: return False

    for i in range(m, n):
        if isAnagram(s, p, i-m, i): return True
    
    return False
    
def isSame(cp, cs):
    for i in range(128):
        if cp[i] != cs[i]: return False
    return True

def anagramSearch2(s, p):
    n = len(s)
    m = len(p)
    cs = [0] * 128
    cp = [0] * 128
    for i in range(m):
        cs[ord(s[i])] += 1
        cp[ord(p[i])] += 1
    for i in range(m, n):
        if isSame(cp, cs): return True
        cs[ord(s[i])] += 1
        cs[ord(s[i-m])] -= 1
        
    return False

#main:

l1 = ['geeksforgeeks', 'geeksforgeeks']
l2 = ['frog', 'rseek']

t = len(l1)
for i in range(t):
    print('1->', anagramSearch(l1[i], l2[i]))
    print('2->',anagramSearch2(l1[i], l2[i]))