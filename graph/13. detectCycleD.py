def addEdge(adj, u, v):
    adj[u].append(v)


def dfsHelper(G, node, visited, recSet):
    visited[node] = True
    recSet[node] = True
    for x in G[node]:
        if not visited[x]:
            if dfsHelper(G, x, visited, recSet):
                return True
        elif recSet[x] == True:
            return True
    recSet[node] = False
    return False


def detectCycle(G, V):
    visited = [False] * V
    recSet = [False] * V
    for x in range(V):
        if not visited[x]:
            if dfsHelper(G, x, visited, recSet):
                return True
    return False


#main:

V = 4
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 1, 2)
addEdge(adjG, 2, 3)
addEdge(adjG, 3, 1)

ans = detectCycle(adjG, V)

print(ans)