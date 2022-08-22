def cutRope(n, a, b, c):
    if n < 0: return -1
    if n == 0: return 0
    res = max(cutRope(n-a, a, b, c), cutRope(n-b, a, b, c), cutRope(n-c, a, b, c))
    if res == -1: return -1
    return 1+res
#main:

n = 9
a = 2
b = 2
c = 2

res = cutRope(n, a, b, c)

print(res)