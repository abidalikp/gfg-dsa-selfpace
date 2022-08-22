class Graph:
    def __init__(self, V):
        self.alist = [[] for _ in range(V)]
        self.V = V

    def addEdge(self, u, v, w):
        self.alist[u].append((w, v))

    def bellmanFord(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        for _ in range(self.V -1):
            for u in range(self.V):
                for w, v in self.alist[u]:
                    if dist[v] > dist[u] + w: dist[v] = dist[u] + w
        return dist

#main:

g = Graph(4)

g.addEdge(0, 1, 1)
g.addEdge(0, 2, 4)
g.addEdge(1, 3, 2)
g.addEdge(1, 2, -3)
g.addEdge(2, 3, 3)

ans = g.bellmanFord(0)

print(*ans)