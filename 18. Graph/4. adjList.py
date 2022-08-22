def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

#main:

V = 6
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 2, 1)
addEdge(adjG, 3, 1)
addEdge(adjG, 3, 4)
addEdge(adjG, 3, 5)

print(adjG)