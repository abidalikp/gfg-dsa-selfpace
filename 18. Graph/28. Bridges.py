class Graph:
    def __init__(self, V):
        self.V = V
        self.time = 0
        self.alist = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.alist[u].append(v)
        self.alist[v].append(u)

    def bHelper(self, u, visited, parent, low, discovery, bridges):
        visited[u] = True
        low[u] = self.time
        discovery[u] = self.time
        self.time += 1
        for v in self.alist[u]:
            if not visited[v]:
                parent[v] = u
                self.bHelper(v, visited, parent, low, discovery, bridges)

                low[u] = min(low[u], low[v])

                if low[v] > discovery[u]: bridges.append((u, v))

            elif v != parent[u]: low[u] = min(low[u], discovery[v])

    def bridge(self):
        bridges = []
        visited = [False] * self.V
        low = [1e2] * self.V
        discovery = [1e2] * self.V
        parent = [-1] *self.V

        for i in range(self.V):
            if not visited[i]: self.bHelper(i, visited, parent, low, discovery, bridges)

        print(*bridges)


#main:

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
 
  
print ("Bridges in first graph ")
g1.bridge()
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()
 
  
g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nBridges in third graph ")
g3.bridge()