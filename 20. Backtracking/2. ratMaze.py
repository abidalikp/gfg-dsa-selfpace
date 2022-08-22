def solve(maze, i, j, sol):
    if i+1 == len(maze) and j+1 == len(maze[0]):
        sol[i][j] = 1
        return True
    if i < len(maze) and j < len(maze[0]) and maze[i][j]:
        sol[i][j] = 1
        if solve(maze, i, j+1, sol): return True
        if solve(maze, i+1, j, sol): return True
        sol[i][j] = 0
    return False

def ratMaze(maze):
    sol = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    if solve(maze, 0, 0, sol):
        return sol
    else: return "Not possible"

#main:

maze = [[1,0,1],
        [1,1,0],
        [1,1,1]]

res = ratMaze(maze)

print(res)