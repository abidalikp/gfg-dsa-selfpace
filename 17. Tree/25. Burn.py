class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

res = 0
def burnTime(root, leaf, dist):
    if not root: return 0
    if root.data == leaf:
        dist[0] = 0
        return 1
    ldist = [-1]
    rdist = [-1]
    lh = burnTime(root.left, leaf, ldist)
    rh = burnTime(root.right, leaf, rdist)
    global res
    if ldist[0] != -1:
        dist[0] = ldist[0] + 1
        res = max(res, rh + dist[0])
    elif rdist[0] != -1:
        dist[0] = rdist[0] + 1
        res = max(res, lh + dist[0])
    return max(lh, rh) + 1

#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

leaf = 50
dist = [-1]
ans = burnTime(root, leaf, dist)

print(res)