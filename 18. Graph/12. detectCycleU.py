def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def dfs(G, node, visited, parent):
    visited[node] = True
    for x in G[node]:
        if not visited[x]:
            if dfs(G, x, visited, node):
                return True
        elif x != parent:
            return True
    return False

def detectCycle(G, V):
    visited = [False] * V
    return dfs(G, 0, visited, -1)

#main:

V = 6
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 3, 1)
addEdge(adjG, 3, 4)
addEdge(adjG, 3, 5)

ans = detectCycle(adjG, V)

print(ans)