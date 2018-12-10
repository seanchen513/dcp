'''
DCP#8

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

'''

 

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1

    if root.left is not None and root.right is None:
        return (root.val == root.left.val) + count_unival_subtrees(root.left)
    
    if root.left is None and root.right is not None:
        return (root.val == root.right.val) + count_unival_subtrees(root.right)
    
    # root.left is not None and root.right is not None
    return (root.val == root.left.val == root.right.val) + count_unival_subtrees(root.left) + count_unival_subtrees(root.right)



root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
root = Node(False, Node(True), Node(False, Node(True, Node(True), Node(True)), Node(False)))

count = count_unival_subtrees(root)

print("count: {0}".format(count))
print(f'count: {count}')



