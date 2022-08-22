def isSafe(s, l, r):
    if l>0 and s[l-1] == 'A' and s[l] == 'B': return False
    elif l+1==r and s[l] == 'A' and s[l+1] == 'B': return False
    return True

def permute(s, l, r):

    if l == r:
        print("".join(s))
        return
    else:
        for i in range(l, r+1):
            s[i], s[l] = s[l], s[i]
            if isSafe(s, l, r): permute(s, l+1, r)
            s[i], s[l] = s[l], s[i]

#main:

string = "ABC"

permute(list(string), 0, len(string)-1)