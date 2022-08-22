def isSafe(row, col, sol):
    for j in range(col):
        if sol[row][j]: return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if sol[i][j]: return False

    for i, j in zip(range(row, len(sol), -1), range(col, -1, -1)):
        if sol[i][j]: return False
        
    return True
        

def solve(col, sol):
    if col == len(sol): return True
    for i in range(len(sol)):
        if isSafe(i, col, sol):
            sol[i][col] = 1
            if solve(col+1, sol): return True
            sol[i][col] = 0
    return False

def nQueen(N):
    sol = [[0 for _ in range(N)] for _ in range(N)]
    if solve(0, sol): return sol
    else: return "Not Possible"

#main:

N = 4

res = nQueen(N)

print(res)