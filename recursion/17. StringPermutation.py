def helper(s, i):
    if i == len(s)-1:
        print("".join(s))
        return
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        helper(s, i+1)
        s[i], s[j] = s[j], s[i]

def permute(s):
    helper(list(s), 0)

#main:

s = "abc"

permute(s)