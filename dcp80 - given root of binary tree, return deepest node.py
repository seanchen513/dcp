"""
dcp#80

This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

"""


class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# Assume root is not None
def deepest(root, deepest_nodes = [], max_depth = 0, depth = 0):
    depth += 1

    if depth > max_depth:
        max_depth = depth
        deepest_nodes = [root]
    elif depth == max_depth:
        deepest_nodes.append(root)

    if root.left is not None:
        deepest_nodes, max_depth = deepest(root.left, deepest_nodes, max_depth, depth)

    if root.right is not None:
        deepest_nodes, max_depth = deepest(root.right, deepest_nodes, max_depth, depth)

    return deepest_nodes, max_depth


# max_depth = 1
tree = Node('a') 

# max_depth = 2
tree = Node('a', 
    Node('b'),
    Node('c'))

# max_depth = 3
tree = Node('a', 
    Node('b',
        Node('d')),
    Node('c'))

# max_depth = 3
tree = Node('a', 
    Node('b',
        Node('d')),
    Node('c',
        Node('e')))

# max_depth = 3
tree = Node('a', 
    Node('b',
        Node('d'), Node('e')),
    Node('c',
        Node('f'), Node('g')))

# max_depth = 5
tree = Node('a', 
    Node('b',
        Node('c',
            Node('d',
                Node('e')))))


deepest_nodes, max_depth = deepest(tree)

print("Max depth = {}".format(max_depth))
print("\nDeepest nodes = ")

for node in deepest_nodes:
    print(node.val)

