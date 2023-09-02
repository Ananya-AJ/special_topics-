class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror_tree(node):
    if node is None:
        return
    else:
        temp = node
        mirror_tree(node.left)
        mirror_tree(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.data, end=" ")
    print_tree(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Original tree:")
    print_tree(root)
    mirror_tree(root)
    print("\nMirrored tree:")
    print_tree(root)