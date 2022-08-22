def print1toN(n):
    if n == 0: return
    print1toN(n-1)
    print(n)

#main:

n = 5

print1toN(n)