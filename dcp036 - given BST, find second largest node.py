"""
dcp#36

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node():
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
    

"""
Max node is all the way to the right.
Find second largest node in this order:
1. Go left of max node, then all the way to right if possible.
2. If max node is leaf, then look at parent of max node.
3. If parent has no left child, then parent is 2nd largest node.
4. Otherwise, look at left child of this parent, and go all the way to right if possible.
"""
def second_largest(root):
    max = root

    while max.right is not None:
        prev = max
        max = max.right

    if max.left is not None:
        second = max.left
        while second.right is not None:
            second = second.right

        return second

    if prev.left is None:
        return prev
    
    second = prev.left
    while second.right is not None:
        second = second.right
    
    return second


# Solution #2: 2nd largest element is 2nd element in reverse in-order traversal.
# Pass in "count" and "second" as lists in order to pass them by reference.
def second_largest2(root, count, second):
    if (root is None) or (count[0] >= 2):
         return None

    second_largest2(root.right, count, second)

    count[0] += 1
    if count[0] == 2:
        #second = [root] # this doesn't work
        second.append(root)
        return

    second_largest2(root.left, count, second)
    

root = Node(8)
l = root.left = Node(3)
ll = l.left = Node(1)
lr = l.right = Node(6)
lrl = lr.left = Node(4)
lrr = lr.right = Node(7)
r = root.right = Node(10)
rr = r.right = Node(14)
rrl = rr.left = Node(13)

print_tree(root)

second = second_largest(root)

second2 = []
count = [0]
second_largest2(root, count, second2)
print("\nsecond largest value = {}".format(second.val))
print("\nsecond largest value2 = {}".format(second2[0].val))

