def searchPattern(txt, pat):
    n = len(txt)
    m = len(pat)
    ans = []
    for i in range(n-m+1):
        for j in range(m):
            if pat[j] != txt[i+j]: break
        else: ans.append(i)
    return ans

#main:

txts = ['GEEKSFORGEEKS', 'ABCABCD', 'AAAAA']
pats = ['EKS', 'ABD', 'AAA']

for i in range(3):
    ans = searchPattern(txts[i], pats[i])
    print(*ans)