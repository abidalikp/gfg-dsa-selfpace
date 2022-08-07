from collections import deque


def addEdge(adjG, u, v):
    adjG[u].append(v)
    adjG[v].append(u)

def bfsD(G, V):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            bfs(G, i, visited)

def bfs(G, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        front = q.popleft()
        print(front)

        for nbr in G[front]:
            if not visited[nbr]:
                visited[nbr] = True
                q.append(nbr)


#main:

V = 7
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 2, 1)
addEdge(adjG, 3, 1)
addEdge(adjG, 4, 5)
addEdge(adjG, 6, 5)
addEdge(adjG, 6, 4)


bfsD(adjG, V)