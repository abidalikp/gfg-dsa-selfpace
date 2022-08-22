#Topological Sorting
from collections import deque


def addEdge(adj, u, v):
    adj[u].append(v)

def topoSort(G, V):
    indegree = [0] * V
    for x in G:
        for y in x:
            indegree[y] += 1
    
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    while q:
        f = q.popleft()
        print(f)
        for x in G[f]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
                

#main:

V = 5
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 2)
addEdge(adjG, 0, 3)
addEdge(adjG, 2, 3)
addEdge(adjG, 1, 3)
addEdge(adjG, 1, 4)

topoSort(adjG, V)