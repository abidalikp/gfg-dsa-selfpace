
class Graph:
    def __init__(self, V):
        self.V = V
        self.G = []

    def addEdge(self, u, v, w):
        self.G.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i: return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        elif rank[yroot] > rank[xroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalsMST(self):

        self.G.sort(key = lambda x: x[2])

        parent = [i for i in range(self.V)]
        rank = [0 for i in range(self.V)]
        res = 0
        i = e =0
        while e < self.V-1:
            u, v, w = self.G[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                res += w
                self.union(parent, rank, x, y)

        return res

#main:
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
  

ans = g.kruskalsMST()

print(ans)