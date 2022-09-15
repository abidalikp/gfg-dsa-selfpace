class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if not root: return 0
    d1 = height(root.left) + height(root.right)
    d2 = diameter(root.left)    
    d3 = diameter(root.right)
    return max(d1, d2, d3)    

ans = 0
def ht(root):
    global ans
    if not root: return 0
    lh = ht(root.left)
    rh = ht(root.right)
    ans = max(res, lh, rh)
    return 1 + max(lh, rh)

#main:

head = Node(10)
head.left = Node(20)
head.right = Node(30)
head.right.left = Node(40)
head.right.right = Node(50)
head.right.right.right = Node(60)
head.right.right.right.right = Node(70)

res = diameter(head)
ht(head)
print(ans)
print(res)