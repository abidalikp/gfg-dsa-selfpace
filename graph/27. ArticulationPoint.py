class Graph:
    def __init__(self, V):
        self.alist = [[] for _ in range(V)]
        self.V = V
        self.time = 0

    def addEdge(self, u, v):
        self.alist[u].append(v)
        self.alist[v].append(u)

    def helperAP(self, u, ap, visited, parent, discovery, low):
        visited[u] = True
        children = 0
        
        discovery[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.alist[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.helperAP(v, ap, visited, parent, discovery, low)
                
                low[u] = min(low[u], low[v])
                
                if parent[u] == -1 and children > 1: ap[u] = True

                if parent[u] != -1 and low[v] >= discovery[u]:  ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])


    def articulationPoint(self):
        ap = [False] * self.V
        visited = [False] * self.V
        parent = [-1] * self.V
        discovery = [1e2] * self.V
        low = [1e2] * self.V

        for i in range(self.V):
            if not visited[i]: self.helperAP(i, ap, visited, parent, discovery, low)

        for i, x in enumerate(ap):
            if x: print(i, end=" ")

# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
  
print ("\nArticulation points in first graph ")
g1.articulationPoint()
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nArticulation points in second graph ")
g2.articulationPoint()
 
  
g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nArticulation points in third graph ")
g3.articulationPoint()