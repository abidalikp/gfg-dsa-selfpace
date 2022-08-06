class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def lca(root, n1, n2):
    if not root: return None
    if root.data == n1 or root.data == n2: return root
    L = lca(root.left, n1, n2)
    R = lca(root.right, n1, n2)
    if L and R:
        return root
    if L:
        return L
    else:
        return R
    
#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.left.left = Node(90)

n1, n2 = 80, 90

ans = lca(root, n1, n2)

print(ans.data)