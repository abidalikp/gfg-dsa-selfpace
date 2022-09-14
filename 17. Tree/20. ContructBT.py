class Node:
    def __init__(self, data):
        self.data = data
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

preidx = 0
def construct(preO, inO, start, end):
    global preidx
    if start > end: return None
    root = Node(preO[preidx])
    preidx += 1

    for i in range(start, end+1):
        if inO[i] == root.data:
            inidx = i
            break
    
    root.left = construct(preO, inO, start, inidx-1)
    root.right = construct(preO, inO, inidx+1, end)

    return root

# main:

inO = [20, 10, 40, 30, 50]
preO = [10, 20, 30, 40, 50]


root = construct(preO, inO, 0, len(inO)-1)

inorder(root)
print()
preorder(root)
