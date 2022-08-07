def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def helper(G, v, visited):
    visited[v] = True
    print(v)
    for x in G[v]:
        if not visited[x]:
            helper(G, x, visited)

def dfs(G, V):
    visited = [False] * V
    helper(G, 3, visited)

#main:

V = 6
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 2, 1)
addEdge(adjG, 3, 1)
addEdge(adjG, 3, 4)
addEdge(adjG, 3, 5)

dfs(adjG, V)