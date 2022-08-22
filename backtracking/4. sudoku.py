from math import sqrt

def isSafe(grid, i, j, l):
    n = len(grid)
    for k in range(n):
        if grid[i][k] == l or grid[k][j] == l: return False
    r = int(sqrt(n))
    ri = i-i%r
    rj = j-j%r
    for id in range(ri):
        for jd in range(rj):
            if grid[id+ri][jd+rj] == l: return False
    return True

def solve(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0: break
        else: continue
        break
    else: return True
    for l in range(1, n+1):
        if isSafe(grid, i, j, l):
            grid[i][j] = l
            if solve(grid): return True
            grid[i][j] = 0
    return False



def sudoku(grid):
    if solve(grid): return grid
    else: return "Not Possible"

#main:

grid = [[1, 0, 3, 0],
        [0, 0, 2, 1],
        [0, 1, 0, 2],
        [2, 4, 0, 0]]

res = sudoku(grid)

print(res)