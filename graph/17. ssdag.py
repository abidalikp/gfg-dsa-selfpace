class Graph:
    def __init__(self, n):
        self.alist = [[] for _ in range(n)]
        self.n = n

    def addEdge(self, u, v, w):
        self.alist[u].append((v, w))

    def topoHelper(self, node, visited, stack):
        visited[node] = True
        for x, _ in self.alist[node]:
            if not visited[x]: self.topoHelper(x, visited, stack)
        stack.append(node)

    def topoSort(self):
        visited = [False] * self.n
        stack = []
        for i in range(self.n):
            if not visited[i]: self.topoHelper(i, visited, stack)
        return stack[::-1]

    def shortestPath(self, source):
        dist = [1e2] * self.n
        dist[source] = 0

        topo = self.topoSort()

        for u in topo:
            for v, w in self.alist[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        return dist

#main :

g = Graph(6)

g.addEdge(0, 1, 2)
g.addEdge(0, 4, 1)
g.addEdge(1, 2, 3)
g.addEdge(2, 3, 6)
g.addEdge(4, 5, 4)
g.addEdge(4, 2, 2)
g.addEdge(5, 3, 1)

print(g.shortestPath(0))

