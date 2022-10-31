def traverseSpiral(mat):
    r = len(mat)
    c = len(mat[0])
    if r == 1:
        for i in range(c):
            print(mat[0][i], end=' ')
    elif c == 1:
        for i in range(r):
            print(mat[i][0], end=' ')
    else:
        top, right, bottom, left = 0, c-1, r-1, 0
        while left <= right and top <= bottom:
            # Top row
            for i in range(left, right+1):
                print(mat[top][i], end=' ')
            top += 1
            # Right column
            for i in range(top, bottom+1):
                print(mat[i][right], end=' ')
            right -= 1
            # Bottom row
            if top <= bottom:
                for i in range(right, left-1, -1):
                    print(mat[bottom][i], end=' ')
                bottom -= 1
            # Left column
            if left <= right:
                for i in range(bottom, top-1, -1):
                    print(mat[i][left], end=' ')
                left += 1
    print()

#main:

m1 =    [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 =    [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

m3 =    [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]

m4 =    [[1, 2, 3, 4]]

m5 =    [[1],
        [2],
        [3]]

t = [m1, m2, m3, m4, m5]

for i in range(len(t)):
    traverseSpiral(t[i])