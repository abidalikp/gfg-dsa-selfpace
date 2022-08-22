def sumofDigits(n):
    if n == 0: return 0
    return n%10 + sumofDigits(n//10)

#main:

n = 255423
res = sumofDigits(n)
print(res)