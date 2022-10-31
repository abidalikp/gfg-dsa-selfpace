def printSnake(mat):
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        if i % 2:
            for j in range(c-1, -1, -1):
                print(mat[i][j], end=' ')
        else:
            for j in range(c):
                print(mat[i][j], end=' ')
    print()

#main:

t = []

m1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

t.append(m1)
t.append(m2)

for i in range(2):
    printSnake(t[i])