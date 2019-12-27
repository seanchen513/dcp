"""
dcp#394

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, depth=0):
    if root is None:
        return

    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)


# Finds the first leaf that gives the target sum along the path from root to leaf
def path_target_sum(root, target_sum, sum=0):
    if root is None:
        return None

    sum += root.val

    if (root.left is None) and (root.right is None): # leaf
        if sum == target_sum:
            return root
        else:
            return None
    
    leaf = path_target_sum(root.left, target_sum, sum)
    if leaf:
        return leaf

    leaf = path_target_sum(root.right, target_sum, sum)
    if leaf:
        return leaf


def path_to_node(root, node, path=[]):
    if root is None:
        return None

    if (root == node) or path_to_node(root.left, node) or path_to_node(root.right, node):
        path.append(root.val)
        return path

    return None


###############################################################################

root = Node(8)
root.left = Node(4)
root.left.left = Node(2)
root.left.right = Node(6)
root.right = Node(13)
root.right.right = Node(19)

target_sum = 18

leaf = path_target_sum(root, target_sum)

print_tree(root)
print("\ntarget sum = {}".format(target_sum))

if leaf is None:
    print("\nNo path from root to leaf that sums to given number.")
else:
    print("\nleaf = {}".format(leaf.val))

path = path_to_node(root, leaf)
print("\npath = {}".format(path))

