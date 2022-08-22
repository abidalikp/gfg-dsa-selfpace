from queue import Queue

class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def levelOrder(node):
    q = Queue()
    q.put(node)
    while not q.empty():
        p = q.get()
        print(p.data)

        if p.left:  q.put(p.left)
        if p.right:   q.put(p.right)

def lineByLine(node):
    q = Queue()
    q.put(node)
    q.put(-1)
    while q.qsize()>1:
        p = q.get()
        if p == -1:
            print()
            q.put(-1)
        else:
            print(p.data, end=" ")

            if p.left:  q.put(p.left)
            if p.right:   q.put(p.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.left.left = Node(90)

lineByLine(root)