import heapq


def addEdge(adj, u, v, w):
    adj[u].append((w, v))
    adj[v].append((w, u))

def dijkstras(G, V, src):
    dist = [1e7] * V
    dist[src] = 0

    d = {src: 0}

    while d:
        root = min(d, key = lambda k: d[k])
        del d[root]
        for edge, nbr in G[root]:
            if dist[root] + edge < dist[nbr]:
                dist[nbr] = dist[root] + edge
                d[nbr] = dist[nbr]
    
    return dist



#main:

V = 4
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1, 2)
addEdge(adjG, 1, 2, 10)
addEdge(adjG, 1, 3, 3)
addEdge(adjG, 3, 2, 2)

ans = dijkstras(adjG, V, 0)

print(ans)