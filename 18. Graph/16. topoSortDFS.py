def addEdge(adj, u, v):
    adj[u].append(v)

def dfsHelper(G, v, visited, stack):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            dfsHelper(G, i, visited, stack)
    stack.append(v)

def topoSort(G, V):
    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            dfsHelper(G, i, visited, stack)
    print(stack[::-1])


#main:

V = 5
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 2)
addEdge(adjG, 0, 3)
addEdge(adjG, 2, 3)
addEdge(adjG, 1, 3)
addEdge(adjG, 1, 4)

topoSort(adjG, V)