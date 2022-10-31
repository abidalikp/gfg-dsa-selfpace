def printBoundry(mat):
    r = len(mat)
    c = len(mat[0])
    if r == 1: print(*mat[0], end=' ')
    elif c == 1:
        for i in range(r): print(mat[i][0], end=" ")
    else:
        # Print first row
        for i in range(c-1):
            print(mat[0][i], end=" ")
        # Print last column
        for i in range(r-1):
            print(mat[i][c-1], end=" ")
        # Print last row reverse
        for i in range(c-1, 0, -1):
            print(mat[r-1][i], end=" ")
        # Print first column reverse
        for i in range(r-1, 0, -1):
            print(mat[i][0], end=" ")

    print()

#main:

t = []

m1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]

m3 = [[1, 2, 3, 4]]

m4 = [[1],
        [2],
        [3]]

t.append(m1)
t.append(m2)
t.append(m3)
t.append(m4)

for i in range(4):
    printBoundry(t[i])