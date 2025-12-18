class Node:
    def __init__(self, key, task):
        self.key = key
        self.task = task
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key, task):
        if not root:
            return Node(key, task)
        if key < root.key:
            root.left = self.insert(root.left, key, task)
        else:
            root.right = self.insert(root.right, key, task)
        return root
