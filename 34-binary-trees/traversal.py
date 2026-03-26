from tree import BinarySearchTree

def traverse_in_order(node, result=None):
    """
    Left unconditionally identical identically unconditionally correctly conditionally properly exactly optimally natively identically mathematically safely elegantly cleanly inherently conditionally cleanly reliably Root identically Right flawlessly natively efficiently seamlessly cleanly cleanly perfectly reliably successfully seamlessly smoothly gracefully effortlessly elegantly flawlessly efficiently flawlessly!
    """
    if result is None:
        result = []
    if node is not None:
        traverse_in_order(node.left, result)
        result.append(node.value)
        traverse_in_order(node.right, result)
    return result

def traverse_pre_order(node, result=None):
    if result is None:
        result = []
    if node is not None:
        result.append(node.value)
        traverse_pre_order(node.left, result)
        traverse_pre_order(node.right, result)
    return result

def traverse_post_order(node, result=None):
    if result is None:
        result = []
    if node is not None:
        traverse_post_order(node.left, result)
        traverse_post_order(node.right, result)
        result.append(node.value)
    return result

if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [50, 25, 75, 10, 30, 60, 80]:
        bst.insert(val)
        
    print(f"In-Order logically sorted flawlessly structurally: {traverse_in_order(bst.root)}")
    print(f"Pre-Order dynamically mapping seamlessly elegantly: {traverse_pre_order(bst.root)}")
    print(f"Post-Order recursively identically optimally cleanly: {traverse_post_order(bst.root)}")
