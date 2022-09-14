class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

prev = None
def convert(root):
    global prev
    if not root: return root
    head = convert(root.left)
    if not prev: head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    convert(root.right)
    return head
    

#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

head = convert(root)
while(head):
    print(head.data)
    head = head.right