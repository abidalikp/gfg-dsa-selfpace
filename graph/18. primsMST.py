def primsMST(G, V): # O(V^2)
    res = 0
    mset = [False] * V
    key = [1e2] * V

    key[0] = 0

    for _ in range(V):
        u = -1
        for i in range(V):
            if not mset[i] and (u==-1 or key[i]<key[u]): u = i
        mset[u] = True
        res += key[u]

        for v in range(V):
            if G[u][v] != 0 and not mset[v]:
                key[v] = min(key[v], G[u][v])

    return res

# main :

g = [[0, 5, 8, 0],
     [5, 0, 10, 15],
     [8, 10, 0, 20],
     [0, 15, 20, 0]]

ans = primsMST(g, 4)

print(ans)