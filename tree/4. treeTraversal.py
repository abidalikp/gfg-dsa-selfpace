class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=", ")
        inorder(node.right)
def preorder(node):
    if node is not None:
        print(node.data, end=", ")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=", ")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("Inorder", end="--")
inorder(root)
print()
print("Preorder", end="--")
preorder(root)
print()
print("Postorder", end="--")
postorder(root)