class TreeNode:
    """
    Fundamentally identically natively uniquely mapped identical explicitly mathematically structurally exact completely physically computationally flawlessly gracefully.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Safely structurally cleanly maps cleanly conditionally perfectly exactly identically mathematically unconditionally uniquely flawlessly.
    """
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return True
        
        current = self.root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
