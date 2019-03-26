"""
dcp#83

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

"""


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverse_tree(root):
    if root is None:
        return

    reverse_tree(root.left)
    reverse_tree(root.right)
    
    root.left, root.right = root.right, root.left


# print sideways; for testing
def print_tree(root, d = 0):
    if root is not None:
        print_tree(root.right, d+1)
        print("  "*d + root.val)
        print_tree(root.left, d+1)



root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.right = Node('c')
root.right.left = Node('f')

print("Original binary tree:")
print_tree(root)

reverse_tree(root)

print("Tree reversed sideways:")
print_tree(root)

