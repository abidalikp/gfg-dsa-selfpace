class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def inorder(node):
    curr = node
    s = []
    while curr or s:
        while curr:
            s.append(curr)
            curr = curr.left
        x = s.pop()
        print(x.data, end=", ")
        curr = x.right

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

inorder(root)