def squareRoot(x):
    if x == 1: return 0
    return 1 + squareRoot(x//2)

def cubeRoot(x):
    if x < 3: return 0
    return 1 + cubeRoot(x//3)

#main:

x = 10

res = squareRoot(x)
print(res)
res = cubeRoot(x)
print(res)