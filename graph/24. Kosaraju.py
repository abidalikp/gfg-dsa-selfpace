# Strongly Connected Components

class Graph:
    def __init__(self, V):
        self.alist = [[] for _ in range(V)]
        self.V = V

    def addEdge(self, u, v):
        self.alist[u].append(v)

    def topoHelper(self, u, visited, stack):
        visited[u] = True
        for v in self.alist[u]:
            if not visited[v]: self.topoHelper(v, visited, stack)
        stack.append(u)

    def topoSort(self):
        stack = []
        visited = [False] * self.V
        for u in range(self.V):
            if not visited[u]: self.topoHelper(u, visited, stack)
        return stack[::-1]

    def transpose(self):
        g = [[] for _ in range(self.V)]
        for u in range(self.V):
            for v in self.alist[u]:
                g[v].append(u)
        return g

    def dfs(self, g, u, visited, stack):
        visited[u] = True
        for v in g[u]:
            if not visited[v]: self.dfs(g, v, visited, stack)
        stack.append(u)

    def kosaraju(self):
        #topo
        topo = self.topoSort()
        #transpose
        t = self.transpose()
        #dfs
        visited = [False] * self.V
        for u in topo:
            if not visited[u]:
                stack = []
                self.dfs(t, u, visited, stack)
                print(*stack)


#main

g = Graph(5)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(1, 3)
g.addEdge(3, 4)

g.kosaraju()