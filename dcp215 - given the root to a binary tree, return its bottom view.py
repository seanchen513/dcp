"""
dcp#215

This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
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


# Use dict with key = horizontal distance, and value = (max depth, node value).
# hdist = horizontal distance
# Returns dict.  Using pre-order traversal here.
# O(n) time for general binary tree.
def bottom_view_dict(root, d={}, depth=0, hdist=0):
    if root is None:
        return

    if hdist not in d:
        d[hdist] = (depth, root.val)
    else:
        if depth > d[hdist][0]:
            d[hdist] = (depth, root.val)

    bottom_view_dict(root.left, d, depth + 1, hdist - 1)
    bottom_view_dict(root.right, d, depth + 1, hdist + 1)

    return d


# Convert dict of (max depth, node value) to list of node values, sorted by horizontal distance.
# O(n log n) due to sorting.  (Worst case for general binary tree)
def bottom_view(root):
    d = bottom_view_dict(root)

    # l = []
    # for hdist in sorted(d):
    #     l.append(d[hdist][1])

    l = [d[key][1] for key in sorted(d)]

    return l


root = Node(5)
l = root.left = Node(3)
ll = l.left = Node(1)
lr = l.right = Node(4)
lll = ll.left = Node(0)
r = root.right = Node(7)
rl = r.left = Node(6)
rr = r.right = Node(9)
rrl = rr.left = Node(8)

print_tree(root)
view = bottom_view(root)
print("\nview: {}".format(view))

