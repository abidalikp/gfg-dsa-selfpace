from collections import deque
from queue import Queue


class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

def maxWidth(node):
    q = deque()
    q.append(node)
    maxm = 0
    q.append(-1)
    while len(q)>1:
        p = q.popleft()
        if p == -1:
            maxm = max(len(q), maxm)
            q.append(-1)
        else:
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
    return maxm

def maxWidth2(node):
    q = deque()
    q.append(node)
    maxm = 0
    while q:
        n = len(q)
        maxm = max(maxm, n)
        for _ in range(n):
            p = q.popleft()
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
    return maxm

#main:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(50)
root.left.right.right = Node(50)
root.left.right.right.right = Node(50)

ans = maxWidth2(root)

print(ans)