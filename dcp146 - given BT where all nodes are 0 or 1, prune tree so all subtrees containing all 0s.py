"""
dcp#146

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print tree sideways, with right side first
def print_tree(root, space=0):
    if root is not None:
        #space += 2
        print_tree(root.right, space+4)
        
        print(" "*space + str(root.val))
        
        print_tree(root.left, space+4)

# depth-first; recursively look for leaf nodes to prune
def prune_tree(root, left, parent=None):
    if root is None:
        return

    prune_tree(root.left, True, root)
    prune_tree(root.right, False, root)

    if root.left is None and root.right is None: # leaf node
        if root.val == 0: # then remove this node
            if parent is None:
                root = None
            else:
                if left:
                    parent.left = None
                else:
                    parent.right = None
        
        return


def test(root):
    print("original tree:")
    print_tree(root)

    prune_tree(root, None)

    print("pruned tree:")
    print_tree(root)


# root = Node(0)    # test case
# root = None       # test case

root = Node(0)
root.left = Node(1)
subroot = Node(1, Node(0), Node(0))
root.right = Node(0, subroot, Node(0))

test(root)

