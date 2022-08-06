class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def countBT(node):
    if node is None: return 0
    return 1 + countBT(node.left) + countBT(node.right)

# main

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.left.left = Node(90)


c = countBT(root)

print(c)