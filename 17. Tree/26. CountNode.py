class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesNaive(root):       # O(n)
    if not root: return 0
    return 1 + countNodesNaive(root.left) + countNodesNaive(root.right)

def countNodesEfficient(root):
    lh = rh = 0
    curr = root
    while curr:
        lh += 1
        curr = curr.left
    curr = root
    while curr:
        rh += 1
        curr = curr.right
    if lh == rh: return pow(2, lh) - 1
    return 1 + countNodesEfficient(root.left) + countNodesEfficient(root.right)

#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)


ans1 = countNodesNaive(root)
ans2 = countNodesEfficient(root)

print(ans1)
print(ans2)