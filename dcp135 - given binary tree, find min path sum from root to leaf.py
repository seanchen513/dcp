"""
dcp#135

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1

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


# O(n) time for general binary tree.
def min_path_sum(root, sum=0, min_sum=None):
    if root is None:
        if min_sum is None:
            min_sum = sum
        else:
            min_sum = min(min_sum, sum)

        return min_sum

    sum += root.val

    min_sum = min_path_sum(root.left, sum, min_sum)
    min_sum = min_path_sum(root.right, sum, min_sum)

    return min_sum


# slightly different version
def min_path_sum2(root, sum=0, min_sum=None):
    if root is None:
        return None

    sum += root.val

    if (root.left is None) and (root.right is None): # leaf node
        if min_sum is None:
            min_sum = sum
        else:
            min_sum = min(min_sum, sum)

        return min_sum

    min_sum = min_path_sum2(root.left, sum, min_sum)
    min_sum = min_path_sum2(root.right, sum, min_sum)

    return min_sum


def min_sum_leaf(root, leaf=None, sum=0, min_sum=None):
    if root is None:
        return min_sum, leaf

    sum += root.val

    if (root.left is None) and (root.right is None): # leaf node
        if min_sum is None:
            min_sum = sum
            leaf = root
        else:
            if sum < min_sum:
                min_sum = sum
                leaf = root

        return min_sum, leaf

    min_sum, leaf = min_sum_leaf(root.left, leaf, sum, min_sum)
    min_sum, leaf = min_sum_leaf(root.right, leaf, sum, min_sum)

    return min_sum, leaf


def path_leaf_to_root(root, leaf, path=[]):
    if root is None:
        return None

    if (root == leaf) or path_leaf_to_root(root.left, leaf) or path_leaf_to_root(root.right, leaf):
        path.append(root.val)
        return path

    return None


# root = Node(5)
# l = root.left = Node(3)
# ll = l.left = Node(1)
# lr = l.right = Node(4)
# lll = ll.left = Node(0)
# r = root.right = Node(7)
# rl = r.left = Node(6)
# rr = r.right = Node(9)
# rrl = rr.left = Node(8)

root = Node(10)
l = root.left = Node(5)
lr = l.right = Node(2)
r = root.right = Node(5)
rr = r.right = Node(1)
rrl = rr.left = Node(-1)

print_tree(root)

min = min_path_sum(root)
print("\nmin path sum = {}".format(min))

min_sum, leaf = min_sum_leaf(root)
print("\nmin sum leaf = {}".format(leaf.val))

path = path_leaf_to_root(root, leaf)
print("\nmin sum path = {}".format(path))

