from collections import deque


def addEdge(adjG, u, v):
    adjG[u].append(v)
    adjG[v].append(u)

def bfs(G, V, s):
    q = deque()
    visited = [False] * V
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

V = 6
adjG = [[] for _ in range(V)]

addEdge(adjG, 0, 1)
addEdge(adjG, 0, 2)
addEdge(adjG, 2, 1)
addEdge(adjG, 3, 1)
addEdge(adjG, 3, 4)
addEdge(adjG, 3, 5)

bfs(adjG, V, 3)