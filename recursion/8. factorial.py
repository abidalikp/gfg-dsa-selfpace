def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

#main :

n = 6

res = factorial(n)

print(res)