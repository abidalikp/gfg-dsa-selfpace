def isRotation(s1, s2):
    n = len(s1)
    if n != len(s2): return False
    for i in range(n):
        if s1[i:] == s2[:n-i] and s1[:i] == s2[n-i:]:
            return True
    return False

def isRotation2(s1, s2):
    return (s1 + s1).find(s2) != -1

#main:

l1 = ['ABCD', 'ABAAA', 'ABAB']
l2 = ['CDAB', 'BAAAA', 'ABBA']

t = len(l1)
for i in range(t):
    print(isRotation2(l1[i], l2[i]))