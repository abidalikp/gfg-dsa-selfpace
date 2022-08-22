def printNto1(n):
    if n == 0: return
    print(n)
    printNto1(n-1)

#main:

n = 5

printNto1(n)