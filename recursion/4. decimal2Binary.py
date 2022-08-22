def decimalToBinary(n):
    if not n: return
    decimalToBinary(n//2)
    print(n%2)

#main:

n = 7

decimalToBinary(n)