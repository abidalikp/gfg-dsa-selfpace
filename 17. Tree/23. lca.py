class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find(root, x, path):
    if not root: return False
    path.append(root.data)
    if root.data == x: return True
    if find(root.left, x, path) or find(root.right, x, path): return True
    path.pop()
    return False

def LCA(root, n1, n2):
    p1 = []
    p2 = []
    if find(root, n1, p1) and find(root, n2, p2):
        l = min(len(p1), len(p2))
        for i in range(l-1):
            if p1[i+1] != p2[i+1]: return p1[i]
    else: return None

def LCA2(root, n1, n2):
    if not root: return None
    if root.data == n1 or root.data == n2: return root
    lca1 = LCA2(root.left, n1, n2)
    lca2 = LCA2(root.right, n1, n2)
    if lca1 and lca2: return root
    return lca1 if lca1 else lca2 

#main:

head = Node(10)
head.left = Node(20)
head.right = Node(30)
head.right.left = Node(40)
head.right.right = Node(50)

res = LCA(head, 20, 30)
res2 = LCA2(head, 20, 30)

print(res)
print(res2.data)