class Graph:
    def __init__(self, V):
        self.alist = [[] for _ in range(V)]
        self.time = 0
        self.V = V

    def addEdge(self, u, v):
        self.alist[u].append(v)

    def tHelper(self, u, visited, low, discovery, stack):
        low[u] = self.time
        discovery[u] = self.time
        self.time += 1
        visited[u] = True
        stack.append(u)

        for v in self.alist[u]:
            if discovery[v] == -1:
                self.tHelper(v, visited, low, discovery, stack)

                low[u] = min(low[u], low[v])

            elif visited[v]: low[u] = min(low[u], discovery[v])

        w = -1
        if low[u] == discovery[u]:
            while w != u:
                w = stack.pop()
                print(w, end=" ")
                visited[w] = False
            print()
        
    def SCC(self):
        visited = [False] * self.V
        low = [-1] * self.V
        discovery = [-1] * self.V
        stack = []

        for i in range(self.V):
            if discovery[i] == -1 : self.tHelper(i, visited, low, discovery, stack)


# main :

# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print ("SSC in first graph ")
g1.SCC()
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("SSC in second graph ")
g2.SCC()
 
  
g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("SSC in third graph ")
g3.SCC()
 
g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print ("SSC in fourth graph ")
g4.SCC()
 
 
g5 = Graph (5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print ("SSC in fifth graph ")
g5.SCC()