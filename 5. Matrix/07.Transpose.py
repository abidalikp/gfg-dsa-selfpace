def printTranspose(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    print(mat)

#main:

t = []

m1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 = [[1, 2, 3],
        [5, 6, 7],
        [9, 10, 11]]

t.append(m1)
t.append(m2)

for i in range(2):
    printTranspose(t[i])