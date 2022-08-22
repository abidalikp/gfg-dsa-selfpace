def kill(n, k):
    if n == 1: return 0
    return (kill(n-1, k) + k) % n

#main:

n = 7
k = 3
res = kill(n, k)
print(res)