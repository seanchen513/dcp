"""
dcp#160

This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
 
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
"""

# Clarify: How to represent? Are weights all positive?
# If weights can be <= 0, we would have to worry about whether paths have to
# go all the way to leaves.


# "weight" is for edge connecting current node to its parent
class Node():
    # use default [] to make iterable since None is not iterable
    def __init__(self, val, weight=0, children=[]): 
        self.val = val
        self.weight = weight
        self.children = children


# not bothering to implement
def print_tree():
    pass 


"""
Idea: 
For each node, keep track of max weights of one-way paths going down starting from that node.
[If a node has no children (ie, is a leaf), we can ignore it.]
[If a node has only 1 child (and a parent), we can ignore it since the path including its parent
will have bigger weight.]
The max weight turning at the node is the sum of the two biggest of these one-way paths.

Keep track of the max of these max weights throughout the tree.
[For these nodes, suffices to consider only nodes with at least 2 children.]
[If no nodes have at least two children, then tree is linear and the max path is the entire linear path.]

[Notes in square bracket can be done by hand and maybe implemented, but that's
not what the code here does.]

Example:
    a
 3/ |5 \8
 b  c   d
      2/ \4
      e   f
    1/ \1
    g   h

Numbers are max weights of one-way paths going down starting from node:

   a:3,5,12
  /|\
 b c d:3,4
    /     \
   e:1,1   f
  / \
 g   h

2-way max weights:
a: 5 + 12 = 17
d: 3 + 4 = 7
e: 2 + 2 = 4

weight of longest path = max(17, 7, 4) = 17
"""

# max_weight is max weight of all 2-way paths found so far
def max_weight_path(root, max_weight=0):
    if root is None:
        return 0

    max1 = 0 # largest weight among 1-way paths down from node
    max2 = 0 # 2nd largest weight among 1-way paths down from node

    print("\n*** Starting processing for node {}".format(root.val))

    for ch in root.children:
        max_1way, max_2way = max_weight_path(ch, max_weight)
        ch_weight = max_1way + ch.weight

        if ch_weight >= max1:
            max2 = max1
            max1 = ch_weight

        print("\nFor node {}, evaluated up to child {}:".format(root.val, ch.val))
        print("    max1, max2 (1-way paths) = {}, {}".format(max1, max2))

    print("\n--- finished processing node {}".format(root.val))
    print("    max1 (1-way), max_weight (2-way) = {}, {}".format(max1, max(max1 + max2, max_weight)))

    # 1st arg: max weight of 1-way paths down from this node
    # 2nd arg: max weight of all 2-way paths found so far
    return max1, max(max1 + max2, max_weight)


"""
    a
 3/ |5 \8
 b  c   d
      2/ \4
      e   f
    1/ \1
    g   h

a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1

The longest (2-way) path: c -> a -> d -> f, with length 5 + 8 + 4 = 17.
The longest (1-way) path: a -> d -> f, with length 8 + 4 = 12.
"""

### Tree given by problem statement.
root = Node('a')
b = Node('b', 3)
c = Node('c', 5)
d = Node('d', 8)
e = Node('e', 2)
f = Node('f', 4)
g = Node('g', 1)
h = Node('h', 1) 
root.children = [b, c, d]
d.children = [e, f]
e.children = [g, h]

### Same tree pruned down to be linear.
# root = Node('a')
# d = Node('d', 8)
# e = Node('e', 2)
# g = Node('g', 1)
# root.children = [d]
# d.children = [e]
# e.children = [g]


#print_tree(root)

max_1way, max_2way = max_weight_path(root)

print("\nmax weight of all 1-way paths = {}".format(max_1way))
print("\nmax weight of all 2-way paths = {}".format(max_2way))

