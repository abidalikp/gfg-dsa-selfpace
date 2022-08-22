from collections import deque

class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

#main:

def lineByLine(node):
    q = deque()
    q.append(node)
    q.append(-1)
    print(node.data)
    while len(q)>1:
        p = q.popleft()
        if p == -1:
            print(q[0].data)
            q.append(-1)
        else:

            if p.left:  q.append(p.left)
            if p.right:   q.append(p.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.left.right.left = Node(100)

lineByLine(root)