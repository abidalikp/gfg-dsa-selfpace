def addEdge(mat, u, v):
    mat[u][v] = 1
    mat[v][u] = 1

#main:

V = 4
mat = [[0] * V for _ in range(V)]

addEdge(mat, 0, 1)
addEdge(mat, 0, 2)
addEdge(mat, 2, 1)
addEdge(mat, 3, 1)

print(mat)