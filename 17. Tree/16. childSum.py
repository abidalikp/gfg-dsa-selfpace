class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def childSum(node):
    if node is None: return True
    if not node.left and not node.right: return True
    summ = 0
    if node.left: summ += node.left.data
    if node.right: summ += node.right.data
    return (summ == node.data) and childSum(node.left) and childSum(node.right)


#main:

root = Node(20)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

ans = childSum(root)

print(ans)