def rotateAnti(mat):
    n = len(mat)
    # 1. Reverse each row
    for i in range(n):
        for j in range(n//2):
            mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j]
    # 2. Transpose
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    print(mat)

#main:

m1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

t = [m1, m2]

for i in range(2):
    rotateAnti(t[i])