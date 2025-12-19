class AVLNode:
    def __init__(self, key, task):
        self.key = key
        self.task = task
        self.left = None
        self.right = None
        self.height = 1

def h(n):
    return n.height if n else 0

def rotate_right(y):
    if not y or not y.left:
        return y
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(h(y.left), h(y.right))
    x.height = 1 + max(h(x.left), h(x.right))
    return x

def rotate_left(x):
    if not x or not x.right:
        return x
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(h(x.left), h(x.right))
    y.height = 1 + max(h(y.left), h(y.right))
    return y

def balance(n):
    return h(n.left) - h(n.right) if n else 0

def insert(root, key, task):
    if not root:
        return AVLNode(key, task)

    if key < root.key:
        root.left = insert(root.left, key, task)
    else:
        root.right = insert(root.right, key, task)

    root.height = 1 + max(h(root.left), h(root.right))
    b = balance(root)

    # Left Left
    if b > 1 and root.left and key < root.left.key:
        return rotate_right(root)

    # Right Right
    if b < -1 and root.right and key > root.right.key:
        return rotate_left(root)

    # Left Right
    if b > 1 and root.left and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Left
    if b < -1 and root.right and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root