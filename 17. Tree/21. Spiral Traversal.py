from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    s1 = [root]
    s2 = []
    while s1 or s2:
        while s1:
            node = s1.pop()
            print(node.data, end=', ')
            if node.left: s2.append(node.left)
            if node.right: s2.append(node.right)
        print()
        while s2:
            node = s2.pop()
            print(node.data, end=', ')
            if node.right: s1.append(node.right)
            if node.left: s1.append(node.left)
        print()
        

#main:

head = Node(10)
head.left = Node(20)
head.right = Node(30)
head.left.left = Node(40)
head.left.right = Node(50)
head.right.left = Node(60)
head.right.right = Node(70)
head.left.left.left = Node(80)
head.left.left.right = Node(90)

levelOrder(head)