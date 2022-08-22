class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def height(node):
    if node is None: return 0
    return 1 + max(height(node.left), height(node.right))

def isBalanced(node):
    if node is None: return True
    return ((height(node.left) - height(node.right) in [-1, 0, 1]) 
        and isBalanced(node.left) 
        and isBalanced(node.right))

def recursive(node):
    if node is None: return 0
    L = recursive(node.left)
    if L == -1: return -1
    R = recursive(node.right)
    if R == -1: return -1
    if abs(R-L) > 1: return -1
    else: return 1 + max(R, L)

def isBalancedN(node):
    if recursive(node) == -1: return False
    return True

#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.right.right.right = Node(80)
root.right.right.right.right = Node(90)

ans = isBalancedN(root)

print(ans)