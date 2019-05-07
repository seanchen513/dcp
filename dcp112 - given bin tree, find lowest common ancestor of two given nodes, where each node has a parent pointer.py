"""
dcp#112

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

class Node():
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


# Because parent pointer is available, it's easy to find the path from a given node
# to the root of tree.  We traverse this path for the first node, putting each node in a set.
# Then we traverse the second path, checking if each node is in the set.
# The first node along the traversal of the path that is in the set is the LCA.
# O(n) time.  O(log n) if we used a self-balancing binary tree.
def lca(x, y):
    if x == y:
        return x

    # create set of nodes along path from x to root
    path = {x}

    while x is not None:
        path.add(x)
        x = x.parent

    while y is not None:
        if y in path:
            return y
        y = y.parent

    return None # shouldn't happen


def print_tree(root, d=0):
    if root is None:
        return

    print_tree(root.right, d+1)
    print("  "*d + str(root.val))
    print_tree(root.left, d+1)


root  = root = Node(1)
l  = root.left = Node(2, root)
ll = root.left.left = Node(4, l)
lr = root.left.right = Node(5, l)
r  = root.right = Node(3, root)
rl = root.right.left = Node(6, r)
rr = root.right.right = Node(7, r)

print_tree(root)


nodes = {root, l, ll, lr, r, rl, rr}
#nodes = {root, r}

print("\n### Test LCA of node with itself:\n")
for node in nodes:
    a = lca(node, node)
    print("lca({}, {}) = {}".format(node.val, node.val, a.val))


print("\n### Other tests:\n")
for node1 in nodes:
    for node2 in nodes:
        if node1 != node2:
            a = lca(node1, node2)
            print("lca({}, {}) = {}".format(node1.val, node2.val, a.val))


