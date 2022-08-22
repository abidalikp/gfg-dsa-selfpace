def TOH(n, a, b, c):
    if n == 0: return
    TOH(n-1, a, c, b)
    print("Move Disc {} from {} to {}".format(n, a, c))
    TOH(n-1, b, a, c)

#main:

n = 3

TOH(n, "A", "B", "C")