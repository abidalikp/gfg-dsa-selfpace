from collections import deque


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def spu(G, V, s):
    q = deque()
    visited = [False] * V
    dist = [-1] * V

    q.append(s)
    visited[s] = True
    dist[s] = 0

    while q:
        f = q.popleft()
        for nbr in G[f]:
            if not visited[nbr]:
                visited[nbr] = True
                dist[nbr] = dist[f] + 1
                q.append(nbr)

    return dist
        

#main:

V = 6
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 2, 1)
addEdge(adjG, 3, 1)
addEdge(adjG, 3, 4)
addEdge(adjG, 3, 5)

a = spu(adjG, V, 0)

print(a)