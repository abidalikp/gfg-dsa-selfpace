def dijkstras(G, V, s):
    dist = [1e2] * V
    dist[s] = 0

    visited = [False] * V
    
    for _ in range(V):
        u = -1
        for i in range(V):
            if not visited[i] and (u == -1 or dist[i]<dist[u]): u = i
        visited[u] = True
        for v in range(V):
            if G[u][v] != 0 and not visited[v]:
                dist[v] = min(dist[v], dist[u]+G[u][v])

    return dist




#main:

g = [[0, 5, 10, 0],
     [5, 0, 3, 20],
     [10, 3, 0, 2],
     [0, 20, 2, 0]]

v = len(g)

ans = dijkstras(g, v, 0)

print(ans)
