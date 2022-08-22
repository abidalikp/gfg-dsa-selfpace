# Recursive calling only at the end.
# Tail Recursive is faster since modern compilers donot save instances.

# print 1 to N

def notTR(n): #not tail
    if n == 0: return
    notTR(n-1)
    print(n)

def tailR(n, k):
    if n == 0: return
    print(k)
    tailR(n-1, k+1)

#main

n = 5

#notTR(n)
tailR(n, 1)