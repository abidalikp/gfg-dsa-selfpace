def search(mat, x): # O(log(R)*log(C))
    R, C = len(mat), len(mat[0])

    # Find row
    start, end = 0, R-1
    while start <= end:
        mid = (start + end)//2
        if mat[mid][0] < x:
            start = mid + 1
        elif mat[mid][0] > x:
            end = mid - 1
        else:
            print('Found at', mid, 0)
            return
    row = end
    #Find column
    start, end = 0, C-1
    while start <= end:
        mid = (start + end)//2
        if mat[row][mid] < x:
            start = mid + 1
        elif mat[row][mid] > x:
            end = mid - 1
        else:
            print('Found at', row, mid)
            return
    print('Not Found')

def search2(mat, x):
    R, C = len(mat), len(mat[0])
    r, c = 0, C-1
    while r < R and c >= 0:
        if mat[r][c] == x:
            print('Found at', r, c)
            return
        elif x < mat[r][c]:
            c -= 1
        else:
            r += 1
    print('Not Found')

#main:

m1 =    [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

m2 =    [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

t = [m1, m2]
x = 16

for i in range(len(t)):
    search(t[i], x)
    search2(t[i], x)
    print()